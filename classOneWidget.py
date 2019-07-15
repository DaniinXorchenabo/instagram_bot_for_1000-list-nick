# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\программы\1000ListNik\instagramm\design\classOneWidgetUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def __init__(self, form, postfix):
        self.form = form
        self.postfix = postfix
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(688, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(13, 80, 641, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_button.sizePolicy().hasHeightForWidth())
        self.img_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.img_button.setFont(font)
        self.img_button.setText("")
        self.img_button.setObjectName("img_button")
        self.horizontalLayout.addWidget(self.img_button)
        self.username_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.username_button.setFont(font)
        self.username_button.setText("")
        self.username_button.setObjectName("username_button")
        self.horizontalLayout.addWidget(self.username_button)
        self.prisebutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prisebutton.sizePolicy().hasHeightForWidth())
        self.prisebutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.prisebutton.setFont(font)
        self.prisebutton.setText("")
        self.prisebutton.setObjectName("prisebutton")
        self.horizontalLayout.addWidget(self.prisebutton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

