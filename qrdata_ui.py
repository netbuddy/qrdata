# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/public/wp/gitee/qrdata/qrdata.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 606)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.create = QtWidgets.QWidget()
        self.create.setObjectName("create")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.create)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.create)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.parameter = QtWidgets.QGroupBox(self.frame)
        self.parameter.setObjectName("parameter")
        self.gridLayout = QtWidgets.QGridLayout(self.parameter)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.parameter)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout_3.addWidget(self.radioButton_8, 1, 1, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout_3.addWidget(self.radioButton_6, 0, 1, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_3.addWidget(self.radioButton_5, 0, 0, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout_3.addWidget(self.radioButton_7, 1, 0, 1, 1)
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_9.setObjectName("radioButton_9")
        self.gridLayout_3.addWidget(self.radioButton_9, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.parameter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.parameter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.errCorrGroupBox = QtWidgets.QGroupBox(self.parameter)
        self.errCorrGroupBox.setTitle("")
        self.errCorrGroupBox.setObjectName("errCorrGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.errCorrGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.errCorrHRadioButton = QtWidgets.QRadioButton(self.errCorrGroupBox)
        self.errCorrHRadioButton.setChecked(True)
        self.errCorrHRadioButton.setObjectName("errCorrHRadioButton")
        self.gridLayout_2.addWidget(self.errCorrHRadioButton, 1, 0, 1, 1)
        self.errCorrMRadioButton = QtWidgets.QRadioButton(self.errCorrGroupBox)
        self.errCorrMRadioButton.setObjectName("errCorrMRadioButton")
        self.gridLayout_2.addWidget(self.errCorrMRadioButton, 2, 0, 1, 1)
        self.errCorrQRadioButton = QtWidgets.QRadioButton(self.errCorrGroupBox)
        self.errCorrQRadioButton.setObjectName("errCorrQRadioButton")
        self.gridLayout_2.addWidget(self.errCorrQRadioButton, 1, 1, 1, 1)
        self.errCorrLRadioButton = QtWidgets.QRadioButton(self.errCorrGroupBox)
        self.errCorrLRadioButton.setObjectName("errCorrLRadioButton")
        self.gridLayout_2.addWidget(self.errCorrLRadioButton, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.errCorrGroupBox, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.parameter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.parameter)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 1, 0, 1, 1)
        self.versionSlider = QtWidgets.QSlider(self.frame_6)
        self.versionSlider.setMinimum(1)
        self.versionSlider.setMaximum(40)
        self.versionSlider.setOrientation(QtCore.Qt.Horizontal)
        self.versionSlider.setObjectName("versionSlider")
        self.gridLayout_8.addWidget(self.versionSlider, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 1, 2, 1, 1)
        self.versionLabel = QtWidgets.QLabel(self.frame_6)
        self.versionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.versionLabel.setObjectName("versionLabel")
        self.gridLayout_8.addWidget(self.versionLabel, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_6, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.parameter)
        self.input_output = QtWidgets.QGroupBox(self.frame)
        self.input_output.setObjectName("input_output")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.input_output)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.input_output)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.input_output)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.inputFilePushButton = QtWidgets.QPushButton(self.frame_5)
        self.inputFilePushButton.setEnabled(True)
        self.inputFilePushButton.setObjectName("inputFilePushButton")
        self.gridLayout_6.addWidget(self.inputFilePushButton, 0, 1, 1, 1)
        self.inputFileLineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.inputFileLineEdit.setEnabled(True)
        self.inputFileLineEdit.setReadOnly(False)
        self.inputFileLineEdit.setObjectName("inputFileLineEdit")
        self.gridLayout_6.addWidget(self.inputFileLineEdit, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_5, 1, 0, 1, 1)
        self.inputTextTextEdit = QtWidgets.QPlainTextEdit(self.frame_3)
        self.inputTextTextEdit.setObjectName("inputTextTextEdit")
        self.gridLayout_5.addWidget(self.inputTextTextEdit, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_3, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.input_output)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.input_output)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.outputDirLineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.outputDirLineEdit.setReadOnly(True)
        self.outputDirLineEdit.setObjectName("outputDirLineEdit")
        self.gridLayout_7.addWidget(self.outputDirLineEdit, 0, 0, 1, 1)
        self.radioButton_12 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_12.setChecked(True)
        self.radioButton_12.setObjectName("radioButton_12")
        self.gridLayout_7.addWidget(self.radioButton_12, 1, 0, 1, 1)
        self.outputDirPushButton = QtWidgets.QPushButton(self.frame_4)
        self.outputDirPushButton.setObjectName("outputDirPushButton")
        self.gridLayout_7.addWidget(self.outputDirPushButton, 0, 1, 1, 1)
        self.radioButton_13 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_13.setObjectName("radioButton_13")
        self.gridLayout_7.addWidget(self.radioButton_13, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_4, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.input_output)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.create)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.horizontalLayout_3.addWidget(self.plainTextEdit_2)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.tabWidget.addTab(self.create, "")
        self.parse = QtWidgets.QWidget()
        self.parse.setObjectName("parse")
        self.tabWidget.addTab(self.parse, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.parameter.setTitle(_translate("MainWindow", "二维码参数"))
        self.radioButton_8.setText(_translate("MainWindow", "字节"))
        self.radioButton_6.setText(_translate("MainWindow", "数字"))
        self.radioButton_5.setText(_translate("MainWindow", "自动"))
        self.radioButton_7.setText(_translate("MainWindow", "数字+字母"))
        self.radioButton_9.setText(_translate("MainWindow", "汉字"))
        self.label.setText(_translate("MainWindow", "尺寸："))
        self.label_3.setText(_translate("MainWindow", "编码格式："))
        self.errCorrHRadioButton.setText(_translate("MainWindow", "高（30%）"))
        self.errCorrMRadioButton.setText(_translate("MainWindow", "中等（15%）"))
        self.errCorrQRadioButton.setText(_translate("MainWindow", "较高（25%）"))
        self.errCorrLRadioButton.setText(_translate("MainWindow", "低（7%）"))
        self.label_2.setText(_translate("MainWindow", "纠错级别："))
        self.label_7.setText(_translate("MainWindow", "1"))
        self.label_8.setText(_translate("MainWindow", "40"))
        self.versionLabel.setText(_translate("MainWindow", "1"))
        self.input_output.setTitle(_translate("MainWindow", "输入输出"))
        self.label_4.setText(_translate("MainWindow", "输入数据："))
        self.inputFilePushButton.setText(_translate("MainWindow", "文件"))
        self.label_5.setText(_translate("MainWindow", "输出目录："))
        self.radioButton_12.setText(_translate("MainWindow", "png"))
        self.outputDirPushButton.setText(_translate("MainWindow", "目录"))
        self.radioButton_13.setText(_translate("MainWindow", "pdf"))
        self.groupBox_3.setTitle(_translate("MainWindow", "运行日志"))
        self.pushButton_3.setText(_translate("MainWindow", "运行"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.create), _translate("MainWindow", "生成"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parse), _translate("MainWindow", "解析"))
