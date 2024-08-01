#对二维码承载的数据进行校验

import base64
import os

from qrdata.parse_qrcode import pyzbarParseQRCode


class DataChecker:
    def __init__(self, raw_data, images_dir, logger):
        self.raw_data = raw_data
        #raw_data为数据，保存为文件，保存在/tmp目录下
        if isinstance(raw_data, str):
            with open(os.path.join('/tmp', 'raw_data'), 'w') as f:
                f.write(raw_data)
        #如果content是bytes类型
        elif isinstance(raw_data, bytes):
            with open(os.path.join('/tmp', 'raw_data'), 'wb') as f:
                f.write(raw_data)
        self.raw_file = os.path.join('/tmp', 'raw_data')
        self.images_dir = images_dir
        self.logger = logger

    def check_data(self):
        #images_dir的文件名称为"xxx_0.ong,xxx_1.png,xxx_2.png"的格式，按顺序加载文件
        file_names = os.listdir(self.images_dir)
        file_names.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

        qrcode_data = None
        for file_name in file_names:
            file_path = os.path.join(self.images_dir, file_name)
            if os.path.isfile(file_path):
                print(file_path)
                #解析二维码
                data = pyzbarParseQRCode(file_path)
                if data is None:
                    print("解析二维码失败")
                    break
                if qrcode_data is None:
                    qrcode_data = data
                else:
                    qrcode_data += data

        try:
            #中文文本
            if base64.b64encode(base64.b64decode(qrcode_data)).decode() == qrcode_data:
                qrcode_data = base64.b64decode(qrcode_data)
                with open(os.path.join('/tmp', 'qrdata'), 'wb') as f:
                    f.write(qrcode_data)
            #英文文本
            else:
                with open(os.path.join('/tmp', 'qrdata'), 'w') as f:
                    f.write(qrcode_data)
        except ValueError as e:
            #二进制数据
            result_bytes = self.bytesstr_to_bytes(qrcode_data)
            with open(os.path.join('/tmp', 'qrdata'), 'wb') as f:
                    f.write(result_bytes)
            
        #如果当前平台为linux，采用sha256sum工具分别计算raw_file和qrdata的校验值，比较是否相同
        if os.name == 'posix':
            os.system('sha256sum ' + self.raw_file + ' > ' + os.path.join('/tmp', 'raw_file_sha256'))
            os.system('sha256sum ' + os.path.join('/tmp', 'qrdata') + ' > ' + os.path.join('/tmp', 'qrdata_sha256'))
            with open(os.path.join('/tmp', 'raw_file_sha256'), 'r') as f:
                raw_file_sha256 = f.readline().split(' ')[0]
            with open(os.path.join('/tmp', 'qrdata_sha256'), 'r') as f:
                qrdata_sha256 = f.readline().split(' ')[0]
            if raw_file_sha256 ==qrdata_sha256:
                self.logger.log("数据校验成功")
                return True
            else:
                self.logger.log("数据校验失败")
                return False

    def bytesstr_to_bytes(self, bytes_str):
        # 创建一个空的字节列表
        byte_list = []

        # 遍历字符串中的每个字符
        for char in bytes_str:
            # 如果字符是十六进制转义序列的一部分，例如 '\x1a'
            if char == '\\':
                # 下一个字符应该是 'x'
                next_char = bytes_str[bytes_str.index(char) + 1]
                if next_char == 'x':
                    # 提取接下来的两个十六进制字符
                    hex_chars = bytes_str[bytes_str.index(char) + 2 : bytes_str.index(char) + 4]
                    # 转换成字节并添加到列表中
                    byte_list.append(bytes.fromhex(hex_chars))
            else:
                # 如果不是十六进制转义序列，直接将字符转换为字节
                byte_list.append(char.encode('utf-8'))

        # 将字节列表合并成一个字节串
        result_bytes = b''.join(byte_list)

        return result_bytes