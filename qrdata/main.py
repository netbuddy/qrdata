import os
import sys
import tempfile
from PIL import Image
from PySide6.QtCore import Qt, QMetaObject, QTranslator
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QToolBar

from chardet.universaldetector import UniversalDetector

from qrdata.enums import QrCodeMode
from qrdata.qrdata_ui import Ui_MainWindow  # 导入从.ui文件生成的UI类
from qrdata.qrcode_data import QRData
from qrdata.inputdata import InputData
from qrdata.qrcode_generator import QRCodeGenerator
from qrdata.logger import GUILogger, Logger
from qrdata.data_check import DataChecker

class MainWindow(QMainWindow):
    def __init__(self, qrdata, input_data):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        toolbar = QToolBar("qrdata toolbar")
        self.addToolBar(toolbar)
        button_action = QAction(QIcon(os.path.join(os.path.dirname(__file__), "data/images/locale.jpg")), "Your button", self)
        button_action.setStatusTip("This is your button")
        # button_action.triggered.connect(self.onLocaleButtonClick)
        toolbar.addAction(button_action)

        self.qrdata = qrdata
        self.input_data = input_data
        self.selected_file = None
        self.logger = GUILogger(self.ui.logTextEdit)
        self.data_encoding = 'unknown'

        self.ui.versionSlider.valueChanged.connect(self.updateVersionLabel)
        self.ui.versionSlider.valueChanged.connect(lambda x: self.qrdata.set_version(self.ui.versionSlider.value()))
        self.ui.inputFilePushButton.clicked.connect(self.openFileDialog)
        self.ui.outputDirPushButton.clicked.connect(self.selectOutputDirectory)
        self.ui.inputTextTextEdit.textChanged.connect(self.inputTextTextEdit_textChanged)
        self.ui.runPushButton.clicked.connect(self.runPushButton_clicked)

        QMetaObject.connectSlotsByName(self)
        self.show()

    def updateVersionLabel(self):
        version_value = self.ui.versionSlider.value()
        self.ui.versionLabel.setText(str(version_value))

    def openFileDialog(self):
        self.selected_file, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*)")
        if self.selected_file:
            file_encoding, confidence = self.detcect_encoding(self.selected_file)
            self.data_encoding = file_encoding
            log_str = "文件编码格式为：{}， 置信度为：{}".format(file_encoding, confidence)
            self.logger.log(log_str)
            if file_encoding != 'unknown' and confidence > 0.75:
                #TODO 根据不同的编码格式，进行不同的处理
                with open(self.selected_file, 'r', encoding=file_encoding) as file:
                    content = file.read()
                self.ui.inputTextTextEdit.appendPlainText(content)
            else:
                self.ui.inputTextTextEdit.appendPlainText(f"<span style='color:red;'>该文件为二进制文件</span>")
            self.ui.inputFileLineEdit.setText(self.selected_file)
    def selectOutputDirectory(self):
        selected_directory = QFileDialog.getExistingDirectory(self, "选择目录")
        if selected_directory:
            self.ui.outputDirLineEdit.setText(selected_directory)

    def detcect_encoding(self, filepath):
        """检测文件编码
        Args:
            detector: UniversalDetector 对象
            filepath: 文件路径
        Return:
            file_encoding: 文件编码
            confidence: 检测结果的置信度，百分比
        """
        detector = UniversalDetector()
        detector.reset()
        for each in open(filepath, 'rb'):
            detector.feed(each)
            if detector.done:
                break
        detector.close()
        file_encoding = detector.result['encoding']
        confidence = detector.result['confidence']
        if file_encoding is None:
            file_encoding = 'unknown'
            confidence = 0.99
        return file_encoding, confidence
    
    def inputTextTextEdit_textChanged(self):
        text = self.ui.inputTextTextEdit.toPlainText()
        self.input_data.load_data(text, "utf-8")

    def runPushButton_clicked(self):
        version = int(self.ui.versionSlider.value())
        #判断errCorrGroupBox中哪一个radiobox被选中
        if self.ui.errCorrHRadioButton.isChecked():
            error_correction = "H"
        elif self.ui.errCorrQRadioButton.isChecked():
            error_correction = "Q"
        elif self.ui.errCorrMRadioButton.isChecked():
            error_correction = "M"
        elif self.ui.errCorrLRadioButton.isChecked():
            error_correction = "L"
        #判断modeGroupBox中哪一个radiobox被选中
        if self.ui.numericRadioButton.isChecked():
            mode = QrCodeMode.Numeric
        elif self.ui.alphanumericRadioButton.isChecked():
            mode = QrCodeMode.Alphanumeric
        elif self.ui.byteRadioButton.isChecked():
            mode = QrCodeMode.Byte
        elif self.ui.kanjiRadioButton.isChecked():
            mode = QrCodeMode.Kanji
        with open(self.selected_file, 'rb') as file:
            data = file.read()
        output_dir = self.ui.outputDirLineEdit.text()
        
        if self.ui.pdfRadioButton.isChecked():
            #创建临时目录（mkdtemp）
            images_output_dir = tempfile.mkdtemp()
        else:
            images_output_dir = output_dir
        generator = QRCodeGenerator(self.logger)
        generator.generate_qrcodes(version, error_correction, mode, data, self.data_encoding, images_output_dir)

        checker = DataChecker(data, self.data_encoding, images_output_dir, self.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')

        if self.ui.pngRadioButton.isChecked():
            if self.ui.previewCheckBox.isChecked():
                image_path = os.path.join(output_dir, 'qrcode_0.png')
                self.open_file(image_path)
        elif self.ui.pdfRadioButton.isChecked():
            self.merge_images_to_pdf(images_output_dir, output_dir)
            if self.ui.previewCheckBox.isChecked():
                pdf_path = os.path.join(output_dir, 'qrcode.pdf')
                self.open_file(pdf_path)
        

    def open_file(self, file_path):
        #打开系统默认的图片工具并显示指定的图片
        if os.name == 'nt':
            os.system('start ' + file_path)
        elif os.name == 'posix':
            os.system('xdg-open ' + file_path)
        else:
            print('unsupported platform')
    
    #将多个png图片合并为一个pdf文件
    def merge_images_to_pdf(self, images_dir, output_dir):
        output_path = os.path.join(output_dir, 'qrcode.pdf')
        images = []
        file_names = os.listdir(images_dir)
        file_names.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))
        for file_name in file_names:
            file_path = os.path.join(images_dir, file_name)
            images.append(Image.open(file_path))
        images[0].save(output_path, save_all=True, append_images=images[1:])
        self.logger.log("QR codes pdf saved to: " + output_dir + "\n")
def main():
    app = QApplication(sys.argv)

    #TODO 将界面由ui改为qml，实现多语言运行时切换
    #https://github.com/AndreAugustoDev/Python-QML-Dynamic-Language-Switch
    # current_dir = os.path.dirname(__file__)
    # translator = QTranslator()
    # if translator.load('zh_cn.qm', directory=os.path.join(current_dir, 'data/i18n')):
    #     app.installTranslator(translator)
        
    qr_data = QRData()
    input_data = InputData()
    window = MainWindow(qr_data, input_data)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()