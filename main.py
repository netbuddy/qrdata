import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from qrdata_ui import Ui_MainWindow  # 导入从.ui文件生成的UI类
from qrdata import QRData

class MainWindow(QMainWindow):
    def __init__(self, qrdata):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.qrdata = qrdata

        self.ui.versionSlider.valueChanged.connect(self.updateVersionLabel)
        self.ui.versionSlider.valueChanged.connect(lambda x: self.qrdata.set_version(self.ui.versionSlider.value()))
        self.ui.inputFilePushButton.clicked.connect(self.openFileDialog)
        self.ui.outputDirPushButton.clicked.connect(self.selectOutputDirectory)

        self.show()
    
    def updateVersionLabel(self):
        version_value = self.ui.versionSlider.value()
        self.ui.versionLabel.setText(str(version_value))

    def openFileDialog(self):
        selected_file, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*)")
        if selected_file:
            self.ui.inputFileLineEdit.setText(selected_file)
    def selectOutputDirectory(self):
        selected_directory = QFileDialog.getExistingDirectory(self, "选择目录")
        if selected_directory:
            self.ui.outputDirLineEdit.setText(selected_directory)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qr_data = QRData()
    window = MainWindow(qr_data)
    sys.exit(app.exec_())