# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Profile.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Profile(object):
    def setupUi(self, Profile):
        if not Profile.objectName():
            Profile.setObjectName(u"Profile")
        Profile.resize(610, 844)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Profile.sizePolicy().hasHeightForWidth())
        Profile.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Profile)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.bgflayer = QFrame(Profile)
        self.bgflayer.setObjectName(u"bgflayer")
        self.bgflayer.setFrameShape(QFrame.StyledPanel)
        self.bgflayer.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.bgflayer)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.bgLayer = QFrame(self.bgflayer)
        self.bgLayer.setObjectName(u"bgLayer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bgLayer.sizePolicy().hasHeightForWidth())
        self.bgLayer.setSizePolicy(sizePolicy1)
        self.bgLayer.setFocusPolicy(Qt.StrongFocus)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.bgLayer)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.bgLayer)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.editBtn = QPushButton(self.bgLayer)
        self.editBtn.setObjectName(u"editBtn")
        self.editBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.editBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.frame_3 = QFrame(self.bgLayer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 13, -1)
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamily(u"Georgia")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_23.setMargin(10)

        self.horizontalLayout_3.addWidget(self.label_23)

        self.address = QLineEdit(self.frame_3)
        self.address.setObjectName(u"address")
        font1 = QFont()
        font1.setFamily(u"Georgia")
        font1.setPointSize(7)
        self.address.setFont(font1)
        self.address.setCursorPosition(0)

        self.horizontalLayout_3.addWidget(self.address)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout_4.addLayout(self.verticalLayout, 2, 0, 1, 3)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.formLayout_3 = QFormLayout(self.frame)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gender = QLabel(self.frame)
        self.gender.setObjectName(u"gender")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.gender.sizePolicy().hasHeightForWidth())
        self.gender.setSizePolicy(sizePolicy3)
        self.gender.setAutoFillBackground(True)
        self.gender.setFrameShape(QFrame.StyledPanel)
        self.gender.setMargin(2)

        self.horizontalLayout.addWidget(self.gender)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setFamily(u"Georgia")
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setMargin(0)

        self.horizontalLayout.addWidget(self.label_10)

        self.age = QLabel(self.frame)
        self.age.setObjectName(u"age")
        sizePolicy3.setHeightForWidth(self.age.sizePolicy().hasHeightForWidth())
        self.age.setSizePolicy(sizePolicy3)
        self.age.setAutoFillBackground(True)
        self.age.setFrameShape(QFrame.StyledPanel)
        self.age.setMargin(2)

        self.horizontalLayout.addWidget(self.age)


        self.formLayout_3.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_12)

        self.mname = QLabel(self.frame)
        self.mname.setObjectName(u"mname")
        self.mname.setAutoFillBackground(True)
        self.mname.setFrameShape(QFrame.StyledPanel)
        self.mname.setMargin(2)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.mname)

        self.fname = QLabel(self.frame)
        self.fname.setObjectName(u"fname")
        sizePolicy3.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy3)
        self.fname.setFocusPolicy(Qt.ClickFocus)
        self.fname.setAutoFillBackground(True)
        self.fname.setFrameShape(QFrame.StyledPanel)
        self.fname.setMargin(2)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.lname = QLabel(self.frame)
        self.lname.setObjectName(u"lname")
        self.lname.setAutoFillBackground(True)
        self.lname.setFrameShape(QFrame.StyledPanel)
        self.lname.setMargin(2)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lname)

        self.pclass = QLabel(self.frame)
        self.pclass.setObjectName(u"pclass")
        self.pclass.setAutoFillBackground(True)
        self.pclass.setFrameShape(QFrame.StyledPanel)
        self.pclass.setWordWrap(True)
        self.pclass.setMargin(2)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.pclass)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 2, 1)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.formLayout_4 = QFormLayout(self.frame_2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_19)

        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_21)

        self.mobile = QLineEdit(self.frame_2)
        self.mobile.setObjectName(u"mobile")
        self.mobile.setFont(font1)
        self.mobile.setCursorPosition(0)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.mobile)

        self.email = QLineEdit(self.frame_2)
        self.email.setObjectName(u"email")
        self.email.setFont(font1)
        self.email.setCursorPosition(0)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.email)

        self.origin = QLabel(self.frame_2)
        self.origin.setObjectName(u"origin")
        self.origin.setAutoFillBackground(True)
        self.origin.setFrameShape(QFrame.StyledPanel)
        self.origin.setMargin(2)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.origin)

        self.nationality = QLabel(self.frame_2)
        self.nationality.setObjectName(u"nationality")
        self.nationality.setAutoFillBackground(True)
        self.nationality.setFrameShape(QFrame.StyledPanel)
        self.nationality.setMargin(2)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.nationality)


        self.gridLayout_4.addWidget(self.frame_2, 0, 1, 2, 2)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.groupBox_3 = QGroupBox(self.bgLayer)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFlat(True)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setVerticalSpacing(9)
        self.formLayout_5.setContentsMargins(-1, 13, 13, 13)
        self.label_33 = QLabel(self.groupBox_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)
        self.label_33.setAlignment(Qt.AlignCenter)
        self.label_33.setMargin(2)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_33)

        self.label_35 = QLabel(self.groupBox_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)
        self.label_35.setAlignment(Qt.AlignCenter)
        self.label_35.setMargin(2)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_35)

        self.status = QLabel(self.groupBox_3)
        self.status.setObjectName(u"status")
        self.status.setAutoFillBackground(True)
        self.status.setFrameShape(QFrame.StyledPanel)
        self.status.setWordWrap(True)
        self.status.setMargin(2)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.status)

        self.id = QLabel(self.groupBox_3)
        self.id.setObjectName(u"id")
        self.id.setAutoFillBackground(True)
        self.id.setFrameShape(QFrame.StyledPanel)
        self.id.setMargin(2)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.id)


        self.horizontalLayout_5.addLayout(self.formLayout_5)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setVerticalSpacing(9)
        self.formLayout_6.setContentsMargins(0, 13, 13, 13)
        self.label_37 = QLabel(self.groupBox_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)
        self.label_37.setAlignment(Qt.AlignCenter)
        self.label_37.setMargin(2)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_37)

        self.label_39 = QLabel(self.groupBox_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font)
        self.label_39.setAlignment(Qt.AlignCenter)
        self.label_39.setMargin(2)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_39)

        self.regdate = QLabel(self.groupBox_3)
        self.regdate.setObjectName(u"regdate")
        self.regdate.setMinimumSize(QSize(0, 20))
        self.regdate.setAutoFillBackground(True)
        self.regdate.setFrameShape(QFrame.StyledPanel)
        self.regdate.setMargin(2)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.regdate)

        self.admdate = QLabel(self.groupBox_3)
        self.admdate.setObjectName(u"admdate")
        self.admdate.setAutoFillBackground(True)
        self.admdate.setFrameShape(QFrame.StyledPanel)
        self.admdate.setMargin(2)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.admdate)


        self.horizontalLayout_5.addLayout(self.formLayout_6)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.bgLayer)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFlat(True)
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 13, 14, -1)
        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_17.setMargin(10)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_17)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setMargin(10)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.kfname = QLineEdit(self.groupBox_4)
        self.kfname.setObjectName(u"kfname")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.kfname)

        self.klname = QLineEdit(self.groupBox_4)
        self.klname.setObjectName(u"klname")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.klname)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_7.setContentsMargins(-1, 13, 14, -1)
        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy5)
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setMargin(10)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.label_26 = QLabel(self.groupBox_4)
        self.label_26.setObjectName(u"label_26")
        sizePolicy5.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy5)
        self.label_26.setFont(font)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setMargin(10)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_26)

        self.kmobile = QLineEdit(self.groupBox_4)
        self.kmobile.setObjectName(u"kmobile")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.kmobile)

        self.krelation = QLineEdit(self.groupBox_4)
        self.krelation.setObjectName(u"krelation")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.krelation)


        self.gridLayout_2.addLayout(self.formLayout_7, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 13, -1)
        self.label_28 = QLabel(self.groupBox_4)
        self.label_28.setObjectName(u"label_28")
        sizePolicy2.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy2)
        self.label_28.setFont(font)
        self.label_28.setAlignment(Qt.AlignCenter)
        self.label_28.setMargin(10)

        self.horizontalLayout_6.addWidget(self.label_28)

        self.kaddress = QLineEdit(self.groupBox_4)
        self.kaddress.setObjectName(u"kaddress")

        self.horizontalLayout_6.addWidget(self.kaddress)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.updateBtn = QPushButton(self.bgLayer)
        self.updateBtn.setObjectName(u"updateBtn")
        self.updateBtn.setMinimumSize(QSize(100, 0))
        self.updateBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.updateBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.closeBtn = QPushButton(self.bgLayer)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(100, 0))
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.closeBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.gridLayout_3.addWidget(self.bgLayer, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, -1, 1, -1)
        self.logo = QLabel(self.bgflayer)
        self.logo.setObjectName(u"logo")
        self.logo.setPixmap(QPixmap(u"_ui/Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo)

        self.bgflbl = QLabel(self.bgflayer)
        self.bgflbl.setObjectName(u"bgflbl")
        sizePolicy3.setHeightForWidth(self.bgflbl.sizePolicy().hasHeightForWidth())
        self.bgflbl.setSizePolicy(sizePolicy3)
        self.bgflbl.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setUnderline(False)
        font3.setWeight(50)
        self.bgflbl.setFont(font3)
        self.bgflbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.bgflbl)

        self.miniBtn = QPushButton(self.bgflayer)
        self.miniBtn.setObjectName(u"miniBtn")
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(12)
        self.miniBtn.setFont(font4)
        self.miniBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.miniBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(self.bgflayer)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamily(u"Tahoma")
        font5.setPointSize(11)
        self.exitBtn.setFont(font5)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setMouseTracking(True)
        self.exitBtn.setTabletTracking(True)
        self.exitBtn.setLayoutDirection(Qt.LeftToRight)
        self.exitBtn.setAutoFillBackground(False)
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.exitBtn)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.bgflayer, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 0, 3, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 3, 1)


        self.retranslateUi(Profile)

        QMetaObject.connectSlotsByName(Profile)
    # setupUi

    def retranslateUi(self, Profile):
        Profile.setWindowTitle(QCoreApplication.translate("Profile", u"Patient's Profile", None))
        self.label_7.setText(QCoreApplication.translate("Profile", u"Patient's Personal Details", None))
        self.editBtn.setText(QCoreApplication.translate("Profile", u"Edit", None))
        self.label_23.setText(QCoreApplication.translate("Profile", u"Address:", None))
        self.label_2.setText(QCoreApplication.translate("Profile", u"First Name", None))
        self.label_4.setText(QCoreApplication.translate("Profile", u"Middle Name:", None))
        self.label_5.setText(QCoreApplication.translate("Profile", u"Last Name: ", None))
        self.label_8.setText(QCoreApplication.translate("Profile", u"Gender:", None))
        self.gender.setText("")
        self.label_10.setText(QCoreApplication.translate("Profile", u"Age:", None))
        self.age.setText("")
        self.label_12.setText(QCoreApplication.translate("Profile", u"Class:", None))
        self.mname.setText("")
        self.fname.setText("")
        self.lname.setText("")
        self.pclass.setText("")
        self.label_13.setText(QCoreApplication.translate("Profile", u"Mobile:", None))
        self.label_15.setText(QCoreApplication.translate("Profile", u"Email: ", None))
        self.label_19.setText(QCoreApplication.translate("Profile", u"State of Origin:", None))
        self.label_21.setText(QCoreApplication.translate("Profile", u"Nationality:", None))
        self.origin.setText("")
        self.nationality.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("Profile", u"Hospital Details:", None))
        self.label_33.setText(QCoreApplication.translate("Profile", u"Patient's Number:", None))
        self.label_35.setText(QCoreApplication.translate("Profile", u"Patient Status:", None))
        self.status.setText("")
        self.id.setText("")
        self.label_37.setText(QCoreApplication.translate("Profile", u"Date of Registration:", None))
        self.label_39.setText(QCoreApplication.translate("Profile", u"Date of Admission:", None))
        self.regdate.setText("")
        self.admdate.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("Profile", u"Next of Kin Details", None))
        self.label_17.setText(QCoreApplication.translate("Profile", u"First Name:", None))
        self.label_9.setText(QCoreApplication.translate("Profile", u"Last Name:", None))
        self.label_18.setText(QCoreApplication.translate("Profile", u"Phone:", None))
        self.label_26.setText(QCoreApplication.translate("Profile", u"Relationship:", None))
        self.label_28.setText(QCoreApplication.translate("Profile", u"Address:", None))
        self.updateBtn.setText(QCoreApplication.translate("Profile", u"Update", None))
        self.closeBtn.setText(QCoreApplication.translate("Profile", u"Close", None))
        self.logo.setText("")
        self.bgflbl.setText(QCoreApplication.translate("Profile", u"Patient's Profile", None))
        self.miniBtn.setText(QCoreApplication.translate("Profile", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("Profile", u"X", None))
    # retranslateUi

