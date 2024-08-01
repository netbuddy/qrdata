import os#系统库，判断是本地二维码文件还是网络二维码
import sys
import cv2 as cv#读取图片的库
from pyzbar.pyzbar import decode#解析二维码的库
import zxing#解析二维码的库
# 解析方法一:借助pyzbar
def pyzbarParseQRCode(filePath):
    if os.path.isfile(filePath):# 判断是否是本地文件
        img = cv.imread(filePath)#读取二维码图片
        texts = decode(img)#解码验证码图片
        qrInfo=""
        for text in texts:#遍历解码数据
          data = text.data
          qrInfo += data.decode("utf-8")#将内容解码成指定格式
          #print(qrInfo)#打印
        # with open("qr_code_text_v1.txt", "w") as file:
        #     file.write(qrInfo)
        return qrInfo

#解析方法二:借助zxing识别
def zxingParseQRCode(filePath):
    reader = zxing.BarCodeReader()
    if os.path.isfile(filePath):
        barcode = reader.decode(filePath)
        #print(barcode.parsed)
        text = barcode.parsed
        # with open("qr_code_text_v2.txt", "w") as file:
        #     file.write(text)
        return text

if __name__ == '__main__':
    # 选择文件名并写入文件
    filePath = input("请输入文件名 (包括扩展名): ")
    pyzbarParseQRCode(filePath)
    zxingParseQRCode(filePath)