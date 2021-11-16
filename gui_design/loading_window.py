# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadingWindow(object):
    def setupUi(self, LoadingWindow):
        LoadingWindow.setObjectName("LoadingWindow")
        LoadingWindow.resize(860, 396)
        self.centralwidget = QtWidgets.QWidget(LoadingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backgroundImg = QtWidgets.QLabel(self.centralwidget)
        self.backgroundImg.setGeometry(QtCore.QRect(0, 0, 860, 396))
        self.backgroundImg.setText("")
        self.backgroundImg.setPixmap(QtGui.QPixmap("../RESOURCES/background2.jpg"))
        self.backgroundImg.setScaledContents(True)
        self.backgroundImg.setObjectName("backgroundImg")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(30, 0, 800, 370))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
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
        font.setFamily("Sitka")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 20pt \"Sitka\";")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.loadinLabel = QtWidgets.QLabel(self.groupBox)
        self.loadinLabel.setGeometry(QtCore.QRect(280, 140, 240, 121))
        self.loadinLabel.setStyleSheet("border-width: 3px;\n"
"\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 0, 83);\n"
"\n"
"border-style: solid;\n"
"color: rgb(0, 0, 0);                                                      \n"
"background-color: rgb(255, 255, 255);")
        self.loadinLabel.setText("")
        self.loadinLabel.setPixmap(QtGui.QPixmap("../RESOURCES/please_wait3.gif"))
        self.loadinLabel.setScaledContents(False)
        self.loadinLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loadinLabel.setObjectName("loadinLabel")
        self.resultsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resultsBtn.setEnabled(True)
        self.resultsBtn.setGeometry(QtCore.QRect(570, 420, 240, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.resultsBtn.setFont(font)
        self.resultsBtn.setAcceptDrops(False)
        self.resultsBtn.setAutoFillBackground(False)
        self.resultsBtn.setStyleSheet("background-color: rgb(0, 111, 0);\n"
"\n"
"font: 75 16pt \"Sitka Small\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 3px;\n"
"border-radius: 30px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"\n"
"alternate-background-color: rgb(135, 135, 135);")
        self.resultsBtn.setCheckable(False)
        self.resultsBtn.setAutoDefault(False)
        self.resultsBtn.setDefault(False)
        self.resultsBtn.setFlat(False)
        self.resultsBtn.setObjectName("resultsBtn")
        LoadingWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoadingWindow)
        QtCore.QMetaObject.connectSlotsByName(LoadingWindow)

    def retranslateUi(self, LoadingWindow):
        _translate = QtCore.QCoreApplication.translate
        LoadingWindow.setWindowTitle(_translate("LoadingWindow", "Prediction in process"))
        self.groupBox.setTitle(_translate("LoadingWindow", "Prediction process running"))
        self.resultsBtn.setText(_translate("LoadingWindow", "results"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadingWindow = QtWidgets.QMainWindow()
    ui = Ui_LoadingWindow()
    ui.setupUi(LoadingWindow)
    LoadingWindow.show()
    sys.exit(app.exec_())
