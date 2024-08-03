import csv
import math
import qrcode
import os
import segno
import base64

from qrdata.enums import QrCodeMode

class QRCodeGenerator:
    def __init__(self, logger):
        self.qrcodes = []
        self.logger = logger

    def generate_qrcodes(self, version, error_correction, mode, bytes_data, data_encoding, output_dir):
        # if isinstance(in_data, bytes):
        #     data = self.binary_to_base64(in_data)
        # else:
        #     data = in_data
        if data_encoding == 'ascii':
            str_data = bytes_data.decode('ascii')
        elif data_encoding == 'utf-8':
            str_data = bytes_data.decode('utf-8')
        elif data_encoding == 'gbk':
            str_data = self.binary_to_base64(bytes_data)
        elif data_encoding == 'binary':
            str_data = self.binary_to_base64(bytes_data)
        bytes_data_len = len(bytes_data)    
        str_data_len = len(str_data)
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
                    break
        
        # #英文文本
        # if data_encoding == 'ascii':
        #     #全数字
        #     if mode == QrCodeMode.Numeric:
        #         max_chars = min(max_bytes, 7089)
        #     #数字+大写字母
        #     elif mode == QrCodeMode.Alphanumeric:
        #         max_chars = min(max_bytes, 4296)
        #     else:
        #         max_chars = min(max_bytes, 2953)
        # #非英文文本
        # elif data_encoding == 'utf-8':
        #     max_chars = min(max_bytes//3, 984)
        # #中文文本(gbk)
        # elif data_encoding == 'gbk':
        #     max_chars = max_bytes
        # elif data_encoding == 'binary':
        #     max_chars = max_bytes
        if data_encoding == 'utf-8':
            max_bytes = max_bytes//3

        for i in range(0, str_data_len, max_bytes):
            chunk = str_data[i:i + max_bytes]
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