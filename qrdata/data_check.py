#对二维码承载的数据进行校验

import os

from qrdata.parse_qrcode import zxingParseQRCode


class DataChecker:
    def __init__(self, raw_data, images_dir, logger):
        self.raw_data = raw_data
        #raw_data为数据，保存为文件，保存在/tmp目录下
        with open(os.path.join('/tmp', 'raw_data'), 'w') as f:
            f.write(raw_data)
        self.raw_file = os.path.join('/tmp', 'raw_data')
        self.images_dir = images_dir
        self.logger = logger

    def check_data(self):
        #images_dir的文件名称为"xxx_0.ong,xxx_1.png,xxx_2.png"的格式，按顺序加载文件
        file_names = os.listdir(self.images_dir)
        file_names.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))
        #将解析出的数据进行拼接，保存为文件
        with open(os.path.join('/tmp', 'qrdata'), 'w') as f:
            for file_name in file_names:
                file_path = os.path.join(self.images_dir, file_name)
                if os.path.isfile(file_path):
                    print(file_path)
                    #解析二维码
                    qrcode_data = zxingParseQRCode(file_path)
                    if qrcode_data is None:
                        print("解析二维码失败")
                        break
                    #将数据追加到文件中
                    f.write(qrcode_data)
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
            else:
                self.logger.log("数据校验失败")

