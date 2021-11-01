# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1121, 684)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 150, 1041, 271))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("#textEdit {\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"background: white;\n"
"}")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setLineWidth(3)
        self.textEdit.setMidLineWidth(6)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setDocumentTitle("")
        self.textEdit.setUndoRedoEnabled(True)
        self.textEdit.setObjectName("textEdit")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(480, 570, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("#playButton {\n"
"color: black;\n"
"background-color: yellow;\n"
"border-radius: 5;\n"
"border: 1px solid gray;\n"
"}")
        self.playButton.setObjectName("playButton")
        self.selectLang = QtWidgets.QComboBox(self.centralwidget)
        self.selectLang.setGeometry(QtCore.QRect(270, 570, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.selectLang.setFont(font)
        self.selectLang.setObjectName("selectLang")
        self.selectLang.addItem("")
        self.selectLang.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 90, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 10, 471, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 0, 71, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Downloads/nh.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 40, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("#label_4{\n"
"color:red;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(700, 570, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pauseButton.setFont(font)
        self.pauseButton.setStyleSheet("#play {\n"
"color: black;\n"
"background-color: white;\n"
"border-radius: 15;\n"
"border: 2px solid gray;\n"
"}")
        self.pauseButton.setObjectName("pauseButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 0, 61, 91))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_5.setObjectName("label_5")
        self.chooseFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseFileButton.setGeometry(QtCore.QRect(40, 460, 1041, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.chooseFileButton.setFont(font)
        self.chooseFileButton.setStyleSheet("#play {\n"
"color: black;\n"
"background-color: white;\n"
"border-radius: 15;\n"
"border: 5px solid gray;\n"
"}")
        self.chooseFileButton.setObjectName("chooseFileButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 530, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(530, 430, 51, 21))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Nhập văn bản vào ô dưới này, sau đó lựa chọn ngôn ngữ và giọng đọc để bắt đầu cho công cụ đọc văn bản Tiếng Việt."))
        self.playButton.setText(_translate("MainWindow", "ĐỌC NGAY"))
        self.selectLang.setItemText(0, _translate("MainWindow", "Tiếng Việt"))
        self.selectLang.setItemText(1, _translate("MainWindow", "Tiếng Anh"))
        self.label.setText(_translate("MainWindow", "Chuyển văn bản thành giọng nói"))
        self.label_2.setText(_translate("MainWindow", "HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG "))
        self.label_4.setText(_translate("MainWindow", "Posts and Telecommunications Institute of Technology"))
        self.pauseButton.setText(_translate("MainWindow", "Dừng"))
        self.chooseFileButton.setText(_translate("MainWindow", "Chọn file từ hệ thống (*.txt *.doc *.docx *.mp3)"))
        self.label_6.setText(_translate("MainWindow", "Chọn ngôn ngữ"))
        self.label_7.setText(_translate("MainWindow", "Hoặc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())