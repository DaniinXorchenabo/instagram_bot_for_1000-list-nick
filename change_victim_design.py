# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\программы\1000ListNik\instagramm\design\3.ui'
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
        self.groupBox.setGeometry(QtCore.QRect(60, 0, 600, 1024))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 601, 981))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(50, 60, 50, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.change_task = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.change_task.setEnabled(True)
        self.change_task.setMinimumSize(QtCore.QSize(101, 120))
        self.change_task.setText("")
        self.change_task.setPixmap(QtGui.QPixmap("C:/Users/Acer/.designer/backup/fire.png"))
        self.change_task.setObjectName("change_task")
        self.verticalLayout.addWidget(self.change_task)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.all_selector = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.all_selector.setFont(font)
        self.all_selector.setText("")
        self.all_selector.setObjectName("all_selector")
        self.horizontalLayout_2.addWidget(self.all_selector)
        self.like_sellector = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.like_sellector.setFont(font)
        self.like_sellector.setText("")
        self.like_sellector.setObjectName("like_sellector")
        self.horizontalLayout_2.addWidget(self.like_sellector)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.subscription_sellector = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.subscription_sellector.setFont(font)
        self.subscription_sellector.setText("")
        self.subscription_sellector.setObjectName("subscription_sellector")
        self.horizontalLayout_3.addWidget(self.subscription_sellector)
        self.comments_sellector = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comments_sellector.setFont(font)
        self.comments_sellector.setText("")
        self.comments_sellector.setObjectName("comments_sellector")
        self.horizontalLayout_3.addWidget(self.comments_sellector)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 499, 312))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(-1, -1, 501, 499))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.task_from_list1 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        self.task_from_list1.setObjectName("task_from_list1")
        self.task_1 = QtWidgets.QHBoxLayout(self.task_from_list1)
        self.task_1.setObjectName("task_1")
        self.list_for_button1_img = QtWidgets.QPushButton(self.task_from_list1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.list_for_button1_img.sizePolicy().hasHeightForWidth())
        self.list_for_button1_img.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.list_for_button1_img.setFont(font)
        self.list_for_button1_img.setText("")
        self.list_for_button1_img.setObjectName("list_for_button1_img")
        self.task_1.addWidget(self.list_for_button1_img)
        self.list_for_button_username = QtWidgets.QPushButton(self.task_from_list1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.list_for_button_username.sizePolicy().hasHeightForWidth())
        self.list_for_button_username.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.list_for_button_username.setFont(font)
        self.list_for_button_username.setText("")
        self.list_for_button_username.setObjectName("list_for_button_username")
        self.task_1.addWidget(self.list_for_button_username)
        self.list_for_button1_prise = QtWidgets.QPushButton(self.task_from_list1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(90)
        sizePolicy.setHeightForWidth(self.list_for_button1_prise.sizePolicy().hasHeightForWidth())
        self.list_for_button1_prise.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.list_for_button1_prise.setFont(font)
        self.list_for_button1_prise.setText("")
        self.list_for_button1_prise.setObjectName("list_for_button1_prise")
        self.task_1.addWidget(self.list_for_button1_prise)
        self.list_for_button1_prise.raise_()
        self.list_for_button1_img.raise_()
        self.list_for_button_username.raise_()
        self.verticalLayout_2.addWidget(self.task_from_list1)
        self.task_from_list1_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        self.task_from_list1_2.setObjectName("task_from_list1_2")
        self.task_2 = QtWidgets.QHBoxLayout(self.task_from_list1_2)
        self.task_2.setObjectName("task_2")
        self.list_for_button1_2_ing = QtWidgets.QPushButton(self.task_from_list1_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.list_for_button1_2_ing.sizePolicy().hasHeightForWidth())
        self.list_for_button1_2_ing.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.list_for_button1_2_ing.setFont(font)
        self.list_for_button1_2_ing.setText("")
        self.list_for_button1_2_ing.setObjectName("list_for_button1_2_ing")
        self.task_2.addWidget(self.list_for_button1_2_ing)
        self.list_for_button1_username = QtWidgets.QPushButton(self.task_from_list1_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.list_for_button1_username.sizePolicy().hasHeightForWidth())
        self.list_for_button1_username.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.list_for_button1_username.setFont(font)
        self.list_for_button1_username.setText("")
        self.list_for_button1_username.setObjectName("list_for_button1_username")
        self.task_2.addWidget(self.list_for_button1_username)
        self.list_for_button1_prise_2 = QtWidgets.QPushButton(self.task_from_list1_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(90)
        sizePolicy.setHeightForWidth(self.list_for_button1_prise_2.sizePolicy().hasHeightForWidth())
        self.list_for_button1_prise_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.list_for_button1_prise_2.setFont(font)
        self.list_for_button1_prise_2.setText("")
        self.list_for_button1_prise_2.setObjectName("list_for_button1_prise_2")
        self.task_2.addWidget(self.list_for_button1_prise_2)
        self.verticalLayout_2.addWidget(self.task_from_list1_2)
        self.task_from_list1_3 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        self.task_from_list1_3.setObjectName("task_from_list1_3")
        self.task_3 = QtWidgets.QHBoxLayout(self.task_from_list1_3)
        self.task_3.setObjectName("task_3")
        self.list_for_button1_3_img = QtWidgets.QPushButton(self.task_from_list1_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.list_for_button1_3_img.sizePolicy().hasHeightForWidth())
        self.list_for_button1_3_img.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.list_for_button1_3_img.setFont(font)
        self.list_for_button1_3_img.setText("")
        self.list_for_button1_3_img.setObjectName("list_for_button1_3_img")
        self.task_3.addWidget(self.list_for_button1_3_img)
        self.list_for_button1_username_2 = QtWidgets.QPushButton(self.task_from_list1_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.list_for_button1_username_2.sizePolicy().hasHeightForWidth())
        self.list_for_button1_username_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.list_for_button1_username_2.setFont(font)
        self.list_for_button1_username_2.setText("")
        self.list_for_button1_username_2.setObjectName("list_for_button1_username_2")
        self.task_3.addWidget(self.list_for_button1_username_2)
        self.list_for_button1_prise_3 = QtWidgets.QPushButton(self.task_from_list1_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(90)
        sizePolicy.setHeightForWidth(self.list_for_button1_prise_3.sizePolicy().hasHeightForWidth())
        self.list_for_button1_prise_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.list_for_button1_prise_3.setFont(font)
        self.list_for_button1_prise_3.setText("")
        self.list_for_button1_prise_3.setObjectName("list_for_button1_prise_3")
        self.task_3.addWidget(self.list_for_button1_prise_3)
        self.verticalLayout_2.addWidget(self.task_from_list1_3)
        self.task_from_list1_4 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        self.task_from_list1_4.setObjectName("task_from_list1_4")
        self.task_5 = QtWidgets.QHBoxLayout(self.task_from_list1_4)
        self.task_5.setObjectName("task_5")
        self.list_for_button1_4_img = QtWidgets.QPushButton(self.task_from_list1_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.list_for_button1_4_img.sizePolicy().hasHeightForWidth())
        self.list_for_button1_4_img.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.list_for_button1_4_img.setFont(font)
        self.list_for_button1_4_img.setText("")
        self.list_for_button1_4_img.setObjectName("list_for_button1_4_img")
        self.task_5.addWidget(self.list_for_button1_4_img)
        self.list_for_button1_username_3 = QtWidgets.QPushButton(self.task_from_list1_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.list_for_button1_username_3.sizePolicy().hasHeightForWidth())
        self.list_for_button1_username_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.list_for_button1_username_3.setFont(font)
        self.list_for_button1_username_3.setText("")
        self.list_for_button1_username_3.setObjectName("list_for_button1_username_3")
        self.task_5.addWidget(self.list_for_button1_username_3)
        self.list_for_button1_prise_4 = QtWidgets.QPushButton(self.task_from_list1_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(90)
        sizePolicy.setHeightForWidth(self.list_for_button1_prise_4.sizePolicy().hasHeightForWidth())
        self.list_for_button1_prise_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.list_for_button1_prise_4.setFont(font)
        self.list_for_button1_prise_4.setText("")
        self.list_for_button1_prise_4.setObjectName("list_for_button1_prise_4")
        self.task_5.addWidget(self.list_for_button1_prise_4)
        self.verticalLayout_2.addWidget(self.task_from_list1_4)
        self.task_from_list1_5 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        self.task_from_list1_5.setObjectName("task_from_list1_5")
        self.task_4 = QtWidgets.QHBoxLayout(self.task_from_list1_5)
        self.task_4.setObjectName("task_4")
        self.list_for_button1_4 = QtWidgets.QPushButton(self.task_from_list1_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.list_for_button1_4.sizePolicy().hasHeightForWidth())
        self.list_for_button1_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.list_for_button1_4.setFont(font)
        self.list_for_button1_4.setText("")
        self.list_for_button1_4.setObjectName("list_for_button1_4")
        self.task_4.addWidget(self.list_for_button1_4)
        self.subscription_sellector_9 = QtWidgets.QPushButton(self.task_from_list1_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.subscription_sellector_9.sizePolicy().hasHeightForWidth())
        self.subscription_sellector_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.subscription_sellector_9.setFont(font)
        self.subscription_sellector_9.setText("")
        self.subscription_sellector_9.setObjectName("subscription_sellector_9")
        self.task_4.addWidget(self.subscription_sellector_9)
        self.subscription_sellector_10 = QtWidgets.QPushButton(self.task_from_list1_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(90)
        sizePolicy.setHeightForWidth(self.subscription_sellector_10.sizePolicy().hasHeightForWidth())
        self.subscription_sellector_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.subscription_sellector_10.setFont(font)
        self.subscription_sellector_10.setText("")
        self.subscription_sellector_10.setObjectName("subscription_sellector_10")
        self.task_4.addWidget(self.subscription_sellector_10)
        self.verticalLayout_2.addWidget(self.task_from_list1_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.horizontalLayoutWidget_4)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout_6.addWidget(self.verticalScrollBar, 0, QtCore.Qt.AlignRight)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.end_change_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_change_button.sizePolicy().hasHeightForWidth())
        self.end_change_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.end_change_button.setFont(font)
        self.end_change_button.setText("")
        self.end_change_button.setObjectName("end_change_button")
        self.horizontalLayout_4.addWidget(self.end_change_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.change_task_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.change_task_3.setEnabled(True)
        self.change_task_3.setMinimumSize(QtCore.QSize(101, 170))
        self.change_task_3.setText("")
        self.change_task_3.setPixmap(QtGui.QPixmap("C:/Users/Acer/.designer/backup/fire.png"))
        self.change_task_3.setObjectName("change_task_3")
        self.verticalLayout.addWidget(self.change_task_3)
        self.change_task_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.change_task_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.change_task_2.sizePolicy().hasHeightForWidth())
        self.change_task_2.setSizePolicy(sizePolicy)
        self.change_task_2.setMinimumSize(QtCore.QSize(101, 120))
        self.change_task_2.setText("")
        self.change_task_2.setPixmap(QtGui.QPixmap("C:/Users/Acer/.designer/backup/fire.png"))
        self.change_task_2.setObjectName("change_task_2")
        self.verticalLayout.addWidget(self.change_task_2)
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
