# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\программы\1000ListNik\instagramm\design\2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 965)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(-1, 0, 600, 931))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 601, 931))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(50, 60, 50, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_insta_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.input_insta_text.setEnabled(True)
        self.input_insta_text.setMinimumSize(QtCore.QSize(101, 120))
        self.input_insta_text.setText("")
        self.input_insta_text.setPixmap(QtGui.QPixmap("C:/Users/Acer/.designer/backup/fire.png"))
        self.input_insta_text.setObjectName("input_insta_text")
        self.verticalLayout.addWidget(self.input_insta_text)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(101, 50))
        self.label.setSizeIncrement(QtCore.QSize(0, 50))
        self.label.setBaseSize(QtCore.QSize(0, 50))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Acer/.designer/backup/fire.png"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.input_instagramm = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.input_instagramm.setFont(font)
        self.input_instagramm.setInputMask("")
        self.input_instagramm.setObjectName("input_instagramm")
        self.verticalLayout.addWidget(self.input_instagramm)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.check_login_insta_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(151)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.check_login_insta_button.sizePolicy().hasHeightForWidth())
        self.check_login_insta_button.setSizePolicy(sizePolicy)
        self.check_login_insta_button.setMinimumSize(QtCore.QSize(200, 70))
        self.check_login_insta_button.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.check_login_insta_button.setFont(font)
        self.check_login_insta_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.check_login_insta_button.setStyleSheet("")
        self.check_login_insta_button.setText("")
        self.check_login_insta_button.setShortcut("")
        self.check_login_insta_button.setObjectName("check_login_insta_button")
        self.horizontalLayout.addWidget(self.check_login_insta_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(101, 250))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 50))
        self.label_2.setBaseSize(QtCore.QSize(0, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/Acer/.designer/backup/fire.png"))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.error_akk = QtWidgets.QLabel(self.centralwidget)
        self.error_akk.setGeometry(QtCore.QRect(56, 472, 501, 91))
        self.error_akk.setObjectName("error_akk")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 21))
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
        self.error_akk.setText(_translate("MainWindow", "Такого аккаунта нет"))
