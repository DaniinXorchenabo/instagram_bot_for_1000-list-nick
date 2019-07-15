# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\программы\1000ListNik\instagramm\design\4.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setStyleSheet("background: #ffffff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gone_session_button = QtWidgets.QPushButton(self.centralwidget)
        self.gone_session_button.setGeometry(QtCore.QRect(20, 150, 351, 91))
        self.gone_session_button.setStyleSheet("background: rdba(0,0,0,0);")
        self.gone_session_button.setText("")
        self.gone_session_button.setObjectName("gone_session_button")
        self.done_session = QtWidgets.QLabel(self.centralwidget)
        self.done_session.setEnabled(True)
        self.done_session.setGeometry(QtCore.QRect(30, 160, 332, 72))
        self.done_session.setMinimumSize(QtCore.QSize(101, 72))
        self.done_session.setText("")
        self.done_session.setPixmap(QtGui.QPixmap("C:/Users/Acer/.designer/backup/fire.png"))
        self.done_session.setObjectName("done_session")
        self.done_session.raise_()
        self.gone_session_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
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

