# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\программы\1000ListNik\instagramm\design\1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(882, 1073)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(-1, 0, 600, 1024))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 601, 981))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(50, 60, 50, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hellow_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hellow_text.setEnabled(True)
        self.hellow_text.setMinimumSize(QtCore.QSize(101, 120))
        self.hellow_text.setText("")
        self.hellow_text.setPixmap(QtGui.QPixmap("C:/Users/Acer/.designer/backup/fire.png"))
        self.hellow_text.setObjectName("hellow_text")
        self.verticalLayout.addWidget(self.hellow_text)
        self.hellow_text_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hellow_text_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hellow_text_2.sizePolicy().hasHeightForWidth())
        self.hellow_text_2.setSizePolicy(sizePolicy)
        self.hellow_text_2.setMinimumSize(QtCore.QSize(101, 50))
        self.hellow_text_2.setText("")
        self.hellow_text_2.setPixmap(QtGui.QPixmap("C:/Users/Acer/.designer/backup/fire.png"))
        self.hellow_text_2.setObjectName("hellow_text_2")
        self.verticalLayout.addWidget(self.hellow_text_2)
        self.get_coin = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.get_coin.setFont(font)
        self.get_coin.setText("")
        self.get_coin.setObjectName("get_coin")
        self.verticalLayout.addWidget(self.get_coin)
        self.hellow_text_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hellow_text_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hellow_text_3.sizePolicy().hasHeightForWidth())
        self.hellow_text_3.setSizePolicy(sizePolicy)
        self.hellow_text_3.setMinimumSize(QtCore.QSize(101, 50))
        self.hellow_text_3.setText("")
        self.hellow_text_3.setPixmap(QtGui.QPixmap("C:/Users/Acer/.designer/backup/fire.png"))
        self.hellow_text_3.setObjectName("hellow_text_3")
        self.verticalLayout.addWidget(self.hellow_text_3)
        self.PR_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.PR_button.setFont(font)
        self.PR_button.setText("")
        self.PR_button.setObjectName("PR_button")
        self.verticalLayout.addWidget(self.PR_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 21))
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

