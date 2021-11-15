# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detection_results_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DetectionResultsWindow(object):
    def setupUi(self, DetectionResultsWindow):
        DetectionResultsWindow.setObjectName("DetectionResultsWindow")
        DetectionResultsWindow.resize(1400, 930)
        self.centralwidget = QtWidgets.QWidget(DetectionResultsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backgroundImg = QtWidgets.QLabel(self.centralwidget)
        self.backgroundImg.setGeometry(QtCore.QRect(0, 0, 1400, 930))
        self.backgroundImg.setText("")
        self.backgroundImg.setPixmap(QtGui.QPixmap("../RESOURCES/background.jpg"))
        self.backgroundImg.setScaledContents(True)
        self.backgroundImg.setObjectName("backgroundImg")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(30, 0, 1340, 900))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.groupBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.backBtn = QtWidgets.QPushButton(self.groupBox)
        self.backBtn.setEnabled(True)
        self.backBtn.setGeometry(QtCore.QRect(30, 809, 240, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.backBtn.setFont(font)
        self.backBtn.setAcceptDrops(False)
        self.backBtn.setAutoFillBackground(False)
        self.backBtn.setStyleSheet("\n"
"                            background-color: rgb(159, 0, 0);\n"
"                            font: 75 16pt \"Sitka Small\";\n"
"                            color: rgb(255, 255, 255);\n"
"                            border-width: 3px;\n"
"                            border-radius: 30px;\n"
"                            border-color: rgb(255, 255, 255);\n"
"                            border-style: solid;\n"
"                        ")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../RESOURCES/left_arrow_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backBtn.setIcon(icon)
        self.backBtn.setIconSize(QtCore.QSize(24, 24))
        self.backBtn.setCheckable(False)
        self.backBtn.setAutoDefault(False)
        self.backBtn.setDefault(False)
        self.backBtn.setFlat(False)
        self.backBtn.setObjectName("backBtn")
        self.verticalGroupBox1 = QtWidgets.QGroupBox(self.groupBox)
        self.verticalGroupBox1.setGeometry(QtCore.QRect(300, 769, 1021, 111))
        self.verticalGroupBox1.setStyleSheet("border-width: 3px;\n"
"                            border-radius: 15px;\n"
"                            border-color: rgb(0, 0, 0);\n"
"                            border-style: solid;\n"
"                            font: 10pt \"Sitka Small\";\n"
"                            color: rgb(255, 255, 255);\n"
"                            background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
"                            rgba(0, 0, 32, 170));\n"
"                        ")
        self.verticalGroupBox1.setObjectName("verticalGroupBox1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalGroupBox1)
        self.verticalLayout_5.setContentsMargins(6, 24, 6, 6)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.detectionTextEdit = QtWidgets.QPlainTextEdit(self.verticalGroupBox1)
        self.detectionTextEdit.setStyleSheet("border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"background-color: rgb(188, 188, 188);\n"
"color: rgb(0, 0, 0);\n"
"                                                \n"
"\n"
"")
        self.detectionTextEdit.setObjectName("detectionTextEdit")
        self.verticalLayout_5.addWidget(self.detectionTextEdit)
        self.verticalGroupBox2 = QtWidgets.QGroupBox(self.groupBox)
        self.verticalGroupBox2.setGeometry(QtCore.QRect(20, 114, 640, 640))
        self.verticalGroupBox2.setStyleSheet("border-width: 3px;\n"
"                            border-radius: 15px;\n"
"                            border-color: rgb(0, 0, 0);\n"
"                            border-style: solid;\n"
"                            font: 10pt \"Sitka Small\";\n"
"                            color: rgb(255, 255, 255);\n"
"                            background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
"                            rgba(0, 0, 32, 170));\n"
"                        ")
        self.verticalGroupBox2.setObjectName("verticalGroupBox2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalGroupBox2)
        self.verticalLayout_6.setContentsMargins(6, 30, 6, 6)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.plotLabel1 = QtWidgets.QLabel(self.verticalGroupBox2)
        self.plotLabel1.setText("")
        self.plotLabel1.setObjectName("plotLabel1")
        self.verticalLayout_6.addWidget(self.plotLabel1)
        self.verticalGroupBox3 = QtWidgets.QGroupBox(self.groupBox)
        self.verticalGroupBox3.setGeometry(QtCore.QRect(680, 114, 640, 640))
        self.verticalGroupBox3.setStyleSheet("border-width: 3px;\n"
"                            border-radius: 15px;\n"
"                            border-color: rgb(0, 0, 0);\n"
"                            border-style: solid;\n"
"                            font: 10pt \"Sitka Small\";\n"
"                            color: rgb(255, 255, 255);\n"
"                            background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
"                            rgba(0, 0, 32, 170));\n"
"                        ")
        self.verticalGroupBox3.setObjectName("verticalGroupBox3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalGroupBox3)
        self.verticalLayout_7.setContentsMargins(6, 30, 6, 6)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.plotLabel2 = QtWidgets.QLabel(self.verticalGroupBox3)
        self.plotLabel2.setText("")
        self.plotLabel2.setObjectName("plotLabel2")
        self.verticalLayout_7.addWidget(self.plotLabel2)
        DetectionResultsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DetectionResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(DetectionResultsWindow)

    def retranslateUi(self, DetectionResultsWindow):
        _translate = QtCore.QCoreApplication.translate
        DetectionResultsWindow.setWindowTitle(_translate("DetectionResultsWindow", "Detection Results"))
        self.groupBox.setTitle(_translate("DetectionResultsWindow", "Detetion Results"))
        self.backBtn.setText(_translate("DetectionResultsWindow", "Back"))
        self.verticalGroupBox1.setTitle(_translate("DetectionResultsWindow", "Model detects that:"))
        self.verticalGroupBox2.setTitle(_translate("DetectionResultsWindow", "Probabilities graph:"))
        self.verticalGroupBox3.setTitle(_translate("DetectionResultsWindow", "Distebution graph:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DetectionResultsWindow = QtWidgets.QMainWindow()
    ui = Ui_DetectionResultsWindow()
    ui.setupUi(DetectionResultsWindow)
    DetectionResultsWindow.show()
    sys.exit(app.exec_())
