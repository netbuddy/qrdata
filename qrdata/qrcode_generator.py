import csv
import qrcode
import os
import segno
import base64

from qrdata.enums import QrCodeMode

class QRCodeGenerator:
    def __init__(self, logger):
        self.qrcodes = []
        self.logger = logger

    def generate_qrcodes(self, version, error_correction, mode, in_data, output_dir):
        if isinstance(in_data, bytes):
            data = self.binary_to_base64(in_data)
        else:
            data = in_data
        in_data_len = len(in_data)
        data_len = len(data)
        #读取qrcode.csv文件，基于version和error_correction的值从文件中筛选出特定的行
        max_bytes = 0
        #得到当前文件所在的目录
        current_dir = os.path.dirname(__file__)
        with open(os.path.join(current_dir, 'data/qrcode.csv'), 'r') as file:
            reader = csv.reader(file)
            #不读取header
            next(reader)
            for row in reader:
                if int(row[0]) == version and row[1] == error_correction:
                    max_bytes = int(row[mode.value])
                    #将max_bytes凑整为100的整数倍
                    # max_bytes = max_bytes - max_bytes % 100
                    break

        for i in range(0, len(data), max_bytes):
            chunk = data[i:i + max_bytes]
            if error_correction == "H":
                error_correction=qrcode.constants.ERROR_CORRECT_H
            elif error_correction == "M":
                error_correction=qrcode.constants.ERROR_CORRECT_M
            elif error_correction == "L":
                error_correction=qrcode.constants.ERROR_CORRECT_L
            elif error_correction == "Q":
                error_correction=qrcode.constants.ERROR_CORRECT_Q
            
            if mode == QrCodeMode.Numeric:
                mode_str = 'numeric'
            elif mode == QrCodeMode.Alphanumeric:
                mode_str = 'alphanumeric'
            elif mode == QrCodeMode.Byte:
                mode_str = 'byte'
            elif mode == QrCodeMode.Kanji:
                mode_str = 'kanji'
            elif mode ==QrCodeMode.Auto:
                mode_str = 'byte'
            # qr = qrcode.QRCode(
            #     version=version,
            #     error_correction=error_correction,
            #     box_size=10,
            #     border=4,
            # )
            # qr.add_data(chunk)
            # qr.make(fit=True)
            # img = qr.make_image(fill_color="black", back_color="white")
            qr_code = segno.make(chunk, error=error_correction, version=version, mode=mode_str)
            self.qrcodes.append(qr_code)
        self.save_qrcodes(output_dir)
            
    def save_qrcodes(self, output_dir):
        for i, qr_code in enumerate(self.qrcodes):
            filename = f"qrcode_{i}.png"
            filepath = output_dir + "/" + filename
            qr_code.save(filepath, scale=10)
            self.logger.log("Saved QR code to: " + filepath + "\n")
        self.logger.log("All QR codes saved to: " + output_dir + "\n")

    #将二进制数据转为base64编码
    def binary_to_base64(self, data):
        str_data = str(base64.b64encode(data), encoding='utf-8')
        return str_data