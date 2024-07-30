# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qrdata.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QStatusBar, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1169, 815)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.create = QWidget()
        self.create.setObjectName(u"create")
        self.verticalLayout_2 = QVBoxLayout(self.create)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.create)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.parameter = QGroupBox(self.frame)
        self.parameter.setObjectName(u"parameter")
        self.gridLayout = QGridLayout(self.parameter)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(self.parameter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radioButton_8 = QRadioButton(self.groupBox_2)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.gridLayout_3.addWidget(self.radioButton_8, 1, 1, 1, 1)

        self.radioButton_6 = QRadioButton(self.groupBox_2)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout_3.addWidget(self.radioButton_6, 0, 1, 1, 1)

        self.radioButton_5 = QRadioButton(self.groupBox_2)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setChecked(True)

        self.gridLayout_3.addWidget(self.radioButton_5, 0, 0, 1, 1)

        self.radioButton_7 = QRadioButton(self.groupBox_2)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.gridLayout_3.addWidget(self.radioButton_7, 1, 0, 1, 1)

        self.radioButton_9 = QRadioButton(self.groupBox_2)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.gridLayout_3.addWidget(self.radioButton_9, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 2, 1, 1, 1)

        self.label = QLabel(self.parameter)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.parameter)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.errCorrGroupBox = QGroupBox(self.parameter)
        self.errCorrGroupBox.setObjectName(u"errCorrGroupBox")
        self.gridLayout_2 = QGridLayout(self.errCorrGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.errCorrHRadioButton = QRadioButton(self.errCorrGroupBox)
        self.errCorrHRadioButton.setObjectName(u"errCorrHRadioButton")
        self.errCorrHRadioButton.setChecked(True)

        self.gridLayout_2.addWidget(self.errCorrHRadioButton, 1, 0, 1, 1)

        self.errCorrMRadioButton = QRadioButton(self.errCorrGroupBox)
        self.errCorrMRadioButton.setObjectName(u"errCorrMRadioButton")

        self.gridLayout_2.addWidget(self.errCorrMRadioButton, 2, 0, 1, 1)

        self.errCorrQRadioButton = QRadioButton(self.errCorrGroupBox)
        self.errCorrQRadioButton.setObjectName(u"errCorrQRadioButton")

        self.gridLayout_2.addWidget(self.errCorrQRadioButton, 1, 1, 1, 1)

        self.errCorrLRadioButton = QRadioButton(self.errCorrGroupBox)
        self.errCorrLRadioButton.setObjectName(u"errCorrLRadioButton")

        self.gridLayout_2.addWidget(self.errCorrLRadioButton, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.errCorrGroupBox, 1, 1, 1, 1)

        self.label_2 = QLabel(self.parameter)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.parameter)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_8.addWidget(self.label_7, 1, 0, 1, 1)

        self.versionSlider = QSlider(self.frame_6)
        self.versionSlider.setObjectName(u"versionSlider")
        self.versionSlider.setMinimum(1)
        self.versionSlider.setMaximum(40)
        self.versionSlider.setValue(40)
        self.versionSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_8.addWidget(self.versionSlider, 1, 1, 1, 1)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_8.addWidget(self.label_8, 1, 2, 1, 1)

        self.versionLabel = QLabel(self.frame_6)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.versionLabel, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_6, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.parameter)

        self.input_output = QGroupBox(self.frame)
        self.input_output.setObjectName(u"input_output")
        self.gridLayout_4 = QGridLayout(self.input_output)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_4 = QLabel(self.input_output)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.input_output)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.inputFilePushButton = QPushButton(self.frame_5)
        self.inputFilePushButton.setObjectName(u"inputFilePushButton")
        self.inputFilePushButton.setEnabled(True)

        self.gridLayout_6.addWidget(self.inputFilePushButton, 0, 1, 1, 1)

        self.inputFileLineEdit = QLineEdit(self.frame_5)
        self.inputFileLineEdit.setObjectName(u"inputFileLineEdit")
        self.inputFileLineEdit.setEnabled(True)
        self.inputFileLineEdit.setReadOnly(False)

        self.gridLayout_6.addWidget(self.inputFileLineEdit, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_5, 1, 0, 1, 1)

        self.inputTextTextEdit = QPlainTextEdit(self.frame_3)
        self.inputTextTextEdit.setObjectName(u"inputTextTextEdit")

        self.gridLayout_5.addWidget(self.inputTextTextEdit, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 0, 1, 1, 1)

        self.label_5 = QLabel(self.input_output)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.input_output)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.outputDirLineEdit = QLineEdit(self.frame_4)
        self.outputDirLineEdit.setObjectName(u"outputDirLineEdit")
        self.outputDirLineEdit.setReadOnly(True)

        self.gridLayout_7.addWidget(self.outputDirLineEdit, 0, 0, 1, 1)

        self.radioButton_12 = QRadioButton(self.frame_4)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setChecked(True)

        self.gridLayout_7.addWidget(self.radioButton_12, 1, 0, 1, 1)

        self.outputDirPushButton = QPushButton(self.frame_4)
        self.outputDirPushButton.setObjectName(u"outputDirPushButton")

        self.gridLayout_7.addWidget(self.outputDirPushButton, 0, 1, 1, 1)

        self.radioButton_13 = QRadioButton(self.frame_4)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.gridLayout_7.addWidget(self.radioButton_13, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_4, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.input_output)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.create)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.logTextEdit = QTextEdit(self.groupBox_3)
        self.logTextEdit.setObjectName(u"logTextEdit")

        self.horizontalLayout_3.addWidget(self.logTextEdit)


        self.horizontalLayout_2.addWidget(self.groupBox_3)

        self.runPushButton = QPushButton(self.frame_2)
        self.runPushButton.setObjectName(u"runPushButton")

        self.horizontalLayout_2.addWidget(self.runPushButton)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.tabWidget.addTab(self.create, "")
        self.parse = QWidget()
        self.parse.setObjectName(u"parse")
        self.tabWidget.addTab(self.parse, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1169, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.parameter.setTitle(QCoreApplication.translate("MainWindow", u"QRCode parameters", None))
        self.groupBox_2.setTitle("")
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"Byte", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"Numeric", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"Alphanumeric", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"Kanji", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Version:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MOde:", None))
        self.errCorrGroupBox.setTitle("")
        self.errCorrHRadioButton.setText(QCoreApplication.translate("MainWindow", u"High(30%)", None))
        self.errCorrMRadioButton.setText(QCoreApplication.translate("MainWindow", u"Medium(15%)", None))
        self.errCorrQRadioButton.setText(QCoreApplication.translate("MainWindow", u"Quarter(25%)", None))
        self.errCorrLRadioButton.setText(QCoreApplication.translate("MainWindow", u"Low(7%)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Error Correction Level:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.input_output.setTitle(QCoreApplication.translate("MainWindow", u"Input/Output", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Input Data:", None))
        self.inputFilePushButton.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Output Dir:", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"png", None))
        self.outputDirPushButton.setText(QCoreApplication.translate("MainWindow", u"Dir", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"pdf", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))
        self.runPushButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.create), QCoreApplication.translate("MainWindow", u"Generate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parse), QCoreApplication.translate("MainWindow", u"Parse", None))
    # retranslateUi

