# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(640, 714)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Register.sizePolicy().hasHeightForWidth())
        Register.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Register)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_5 = QFrame(Register)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_10.setContentsMargins(3, 0, 8, 0)
        self.logo = QLabel(self.frame_5)
        self.logo.setObjectName(u"logo")
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(45, 45))
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.logo)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.miniBtn = QPushButton(self.frame_5)
        self.miniBtn.setObjectName(u"miniBtn")
        sizePolicy.setHeightForWidth(self.miniBtn.sizePolicy().hasHeightForWidth())
        self.miniBtn.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(11)
        self.miniBtn.setFont(font)
        self.miniBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.miniBtn.setMouseTracking(True)
        self.miniBtn.setTabletTracking(True)
        self.miniBtn.setAutoFillBackground(False)
        self.miniBtn.setAutoDefault(False)
        self.miniBtn.setFlat(False)

        self.gridLayout_13.addWidget(self.miniBtn, 0, 1, 1, 1)

        self.label_29 = QLabel(self.frame_5)
        self.label_29.setObjectName(u"label_29")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy2)

        self.gridLayout_13.addWidget(self.label_29, 0, 0, 1, 1)

        self.exitBtn = QPushButton(self.frame_5)
        self.exitBtn.setObjectName(u"exitBtn")
        sizePolicy.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy)
        self.exitBtn.setMaximumSize(QSize(16777215, 16777215))
        self.exitBtn.setFont(font)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setMouseTracking(True)
        self.exitBtn.setTabletTracking(True)
        self.exitBtn.setLayoutDirection(Qt.LeftToRight)
        self.exitBtn.setAutoFillBackground(False)
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setFlat(False)

        self.gridLayout_13.addWidget(self.exitBtn, 0, 2, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_13)


        self.horizontalLayout_9.addWidget(self.frame_5)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.bgLayer = QFrame(Register)
        self.bgLayer.setObjectName(u"bgLayer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bgLayer.sizePolicy().hasHeightForWidth())
        self.bgLayer.setSizePolicy(sizePolicy3)
        self.bgLayer.setAutoFillBackground(True)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, -1, 6, -1)
        self.bookBtn = QPushButton(self.bgLayer)
        self.bookBtn.setObjectName(u"bookBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(3)
        sizePolicy4.setHeightForWidth(self.bookBtn.sizePolicy().hasHeightForWidth())
        self.bookBtn.setSizePolicy(sizePolicy4)
        self.bookBtn.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(8)
        self.bookBtn.setFont(font1)
        self.bookBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bookBtn.setAutoFillBackground(False)
        self.bookBtn.setStyleSheet(u"background-color: rgb(118, 118, 118);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.bookBtn)

        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(self.bgLayer)
        self.cancelBtn.setObjectName(u"cancelBtn")
        sizePolicy4.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy4)
        self.cancelBtn.setMinimumSize(QSize(0, 30))
        self.cancelBtn.setFont(font1)
        self.cancelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelBtn.setAutoFillBackground(False)
        self.cancelBtn.setStyleSheet(u"background-color: rgb(118, 118, 118);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.regBtn = QPushButton(self.bgLayer)
        self.regBtn.setObjectName(u"regBtn")
        sizePolicy4.setHeightForWidth(self.regBtn.sizePolicy().hasHeightForWidth())
        self.regBtn.setSizePolicy(sizePolicy4)
        self.regBtn.setMinimumSize(QSize(0, 30))
        self.regBtn.setFont(font1)
        self.regBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.regBtn.setAutoFillBackground(False)
        self.regBtn.setStyleSheet(u"background-color: rgb(118, 118, 118);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.regBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.bgLayer)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.groupBox_3.setFlat(True)
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.groupBox_3)
        self.frame.setObjectName(u"frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy5)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, -1, -1, 4)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setMargin(5)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.fname = QLineEdit(self.frame)
        self.fname.setObjectName(u"fname")
        self.fname.setMinimumSize(QSize(0, 0))
        self.fname.setFont(font1)
        self.fname.setAutoFillBackground(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setMargin(5)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.lname = QLineEdit(self.frame)
        self.lname.setObjectName(u"lname")
        self.lname.setFont(font1)
        self.lname.setAutoFillBackground(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lname)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.setWordWrap(True)
        self.label_16.setMargin(5)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_16)

        self.lname_2 = QLineEdit(self.frame)
        self.lname_2.setObjectName(u"lname_2")
        self.lname_2.setFont(font1)
        self.lname_2.setAutoFillBackground(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lname_2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setMargin(5)
        self.label_5.setIndent(2)
        self.label_5.setOpenExternalLinks(False)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy6)

        self.horizontalLayout_14.addWidget(self.comboBox)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setMargin(6)

        self.horizontalLayout_14.addWidget(self.label_6)

        self.age = QLineEdit(self.frame)
        self.age.setObjectName(u"age")
        self.age.setFont(font1)
        self.age.setAutoFillBackground(True)

        self.horizontalLayout_14.addWidget(self.age)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_14)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setMargin(5)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.class_2 = QComboBox(self.frame)
        self.class_2.addItem("")
        self.class_2.addItem("")
        self.class_2.addItem("")
        self.class_2.addItem("")
        self.class_2.setObjectName(u"class_2")
        sizePolicy6.setHeightForWidth(self.class_2.sizePolicy().hasHeightForWidth())
        self.class_2.setSizePolicy(sizePolicy6)
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(8)
        self.class_2.setFont(font2)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.class_2)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.groupBox_3)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy5.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy5)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.formLayout_2 = QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(-1, -1, -1, 5)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(5)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.phone = QLineEdit(self.frame_2)
        self.phone.setObjectName(u"phone")
        self.phone.setFont(font1)
        self.phone.setAutoFillBackground(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.phone)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(5)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.email = QLineEdit(self.frame_2)
        self.email.setObjectName(u"email")
        self.email.setFont(font1)
        self.email.setAutoFillBackground(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.email)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(5)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.origin = QLineEdit(self.frame_2)
        self.origin.setObjectName(u"origin")
        self.origin.setFont(font1)
        self.origin.setAutoFillBackground(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.origin)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setMargin(5)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.nationality = QLineEdit(self.frame_2)
        self.nationality.setObjectName(u"nationality")
        self.nationality.setMinimumSize(QSize(0, 30))
        self.nationality.setFont(font1)
        self.nationality.setAutoFillBackground(True)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.nationality)


        self.gridLayout_3.addWidget(self.frame_2, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy7)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.addressL1 = QLineEdit(self.groupBox_3)
        self.addressL1.setObjectName(u"addressL1")
        self.addressL1.setFont(font1)
        self.addressL1.setAutoFillBackground(True)

        self.horizontalLayout_3.addWidget(self.addressL1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        sizePolicy7.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy7)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setMargin(5)

        self.horizontalLayout_4.addWidget(self.label_12)

        self.addressL2 = QLineEdit(self.groupBox_3)
        self.addressL2.setObjectName(u"addressL2")
        self.addressL2.setFont(font1)
        self.addressL2.setAutoFillBackground(True)

        self.horizontalLayout_4.addWidget(self.addressL2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.bgLayer)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.groupBox_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy5.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy5)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.formLayout_3 = QFormLayout(self.frame_4)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_17 = QLabel(self.frame_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_17.setWordWrap(True)
        self.label_17.setMargin(5)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_17)

        self.kfname = QLineEdit(self.frame_4)
        self.kfname.setObjectName(u"kfname")
        self.kfname.setMinimumSize(QSize(0, 0))
        self.kfname.setFont(font1)
        self.kfname.setAutoFillBackground(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.kfname)

        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setWordWrap(True)
        self.label_19.setMargin(5)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_19)

        self.klname = QLineEdit(self.frame_4)
        self.klname.setObjectName(u"klname")
        self.klname.setFont(font1)
        self.klname.setAutoFillBackground(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.klname)


        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.groupBox_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy5.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy5)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.formLayout_4 = QFormLayout(self.frame_6)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setWordWrap(True)
        self.label_20.setMargin(5)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_20)

        self.krelationship = QComboBox(self.frame_6)
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.setObjectName(u"krelationship")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.krelationship)

        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_23.setWordWrap(True)
        self.label_23.setMargin(5)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_23)

        self.kphone = QLineEdit(self.frame_6)
        self.kphone.setObjectName(u"kphone")
        self.kphone.setFont(font1)
        self.kphone.setAutoFillBackground(True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.kphone)


        self.gridLayout.addWidget(self.frame_6, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy7.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy7)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setMargin(5)

        self.horizontalLayout_5.addWidget(self.label_13)

        self.kaddressL1 = QLineEdit(self.groupBox_2)
        self.kaddressL1.setObjectName(u"kaddressL1")
        self.kaddressL1.setFont(font1)
        self.kaddressL1.setAutoFillBackground(True)

        self.horizontalLayout_5.addWidget(self.kaddressL1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy7.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy7)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setMargin(5)

        self.horizontalLayout_6.addWidget(self.label_14)

        self.kaddressL2 = QLineEdit(self.groupBox_2)
        self.kaddressL2.setObjectName(u"kaddressL2")
        self.kaddressL2.setFont(font1)
        self.kaddressL2.setAutoFillBackground(True)

        self.horizontalLayout_6.addWidget(self.kaddressL2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.bgLayer)
        self.label.setObjectName(u"label")
        sizePolicy6.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy6)
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(16)
        font3.setUnderline(True)
        self.label.setFont(font3)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(6)

        self.horizontalLayout_2.addWidget(self.label)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.bgLayer)


        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Dialog", None))
        self.logo.setText("")
        self.miniBtn.setText(QCoreApplication.translate("Register", u"__", None))
        self.label_29.setText(QCoreApplication.translate("Register", u"Register New Patient", None))
        self.exitBtn.setText(QCoreApplication.translate("Register", u"X", None))
        self.bookBtn.setText(QCoreApplication.translate("Register", u"Book Appointment", None))
        self.cancelBtn.setText(QCoreApplication.translate("Register", u"Cancel", None))
        self.regBtn.setText(QCoreApplication.translate("Register", u"Register", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Register", u"Patient's Details", None))
        self.label_8.setText(QCoreApplication.translate("Register", u"First Name:", None))
        self.label_9.setText(QCoreApplication.translate("Register", u"Last Name:", None))
        self.label_16.setText(QCoreApplication.translate("Register", u"Other Name:", None))
        self.label_5.setText(QCoreApplication.translate("Register", u"Gender:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Register", u"Male", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Register", u"Female", None))

        self.label_6.setText(QCoreApplication.translate("Register", u"Age:", None))
        self.label_7.setText(QCoreApplication.translate("Register", u"Class:", None))
        self.class_2.setItemText(0, QCoreApplication.translate("Register", u"Private", None))
        self.class_2.setItemText(1, QCoreApplication.translate("Register", u"Company", None))
        self.class_2.setItemText(2, QCoreApplication.translate("Register", u"HMO", None))
        self.class_2.setItemText(3, QCoreApplication.translate("Register", u"Family", None))

        self.label_2.setText(QCoreApplication.translate("Register", u"Mobile:", None))
        self.label_3.setText(QCoreApplication.translate("Register", u"Email: ", None))
        self.label_4.setText(QCoreApplication.translate("Register", u"State of Origin:", None))
        self.label_10.setText(QCoreApplication.translate("Register", u"Nationality:", None))
        self.label_11.setText(QCoreApplication.translate("Register", u"Address Line1: ", None))
        self.label_12.setText(QCoreApplication.translate("Register", u"Address Line2:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Register", u"Next of Kin Details:", None))
        self.label_17.setText(QCoreApplication.translate("Register", u"First Name:", None))
        self.label_19.setText(QCoreApplication.translate("Register", u"Last Name:", None))
        self.label_20.setText(QCoreApplication.translate("Register", u"Relationship:", None))
        self.krelationship.setItemText(0, QCoreApplication.translate("Register", u"Father", None))
        self.krelationship.setItemText(1, QCoreApplication.translate("Register", u"Mother", None))
        self.krelationship.setItemText(2, QCoreApplication.translate("Register", u"Husband", None))
        self.krelationship.setItemText(3, QCoreApplication.translate("Register", u"Wife", None))
        self.krelationship.setItemText(4, QCoreApplication.translate("Register", u"Brother", None))
        self.krelationship.setItemText(5, QCoreApplication.translate("Register", u"Sister", None))
        self.krelationship.setItemText(6, QCoreApplication.translate("Register", u"Friend", None))

        self.label_23.setText(QCoreApplication.translate("Register", u"Mobile:", None))
        self.label_13.setText(QCoreApplication.translate("Register", u"Address Line1: ", None))
        self.label_14.setText(QCoreApplication.translate("Register", u"Address Line2:", None))
        self.label.setText(QCoreApplication.translate("Register", u"Patient's Registraion Form", None))
    # retranslateUi

