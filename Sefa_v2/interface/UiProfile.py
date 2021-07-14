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
        Profile.resize(553, 824)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Profile.sizePolicy().hasHeightForWidth())
        Profile.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Profile)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, -1, 6, -1)
        self.logo = QLabel(Profile)
        self.logo.setObjectName(u"logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
        self.logo.setMinimumSize(QSize(40, 40))
        self.logo.setPixmap(QPixmap(u"_ui/Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo)

        self.label = QLabel(Profile)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.miniBtn = QPushButton(Profile)
        self.miniBtn.setObjectName(u"miniBtn")
        sizePolicy.setHeightForWidth(self.miniBtn.sizePolicy().hasHeightForWidth())
        self.miniBtn.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(12)
        self.miniBtn.setFont(font1)
        self.miniBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(Profile)
        self.exitBtn.setObjectName(u"exitBtn")
        sizePolicy.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy)
        self.exitBtn.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(11)
        self.exitBtn.setFont(font2)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setMouseTracking(True)
        self.exitBtn.setTabletTracking(True)
        self.exitBtn.setLayoutDirection(Qt.LeftToRight)
        self.exitBtn.setAutoFillBackground(False)
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.exitBtn)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.bgLayer = QFrame(Profile)
        self.bgLayer.setObjectName(u"bgLayer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bgLayer.sizePolicy().hasHeightForWidth())
        self.bgLayer.setSizePolicy(sizePolicy3)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.bgLayer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.bgLayer)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamily(u"Georgia")
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_2.setFont(font3)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.fname = QLabel(self.frame)
        self.fname.setObjectName(u"fname")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy5)
        font4 = QFont()
        font4.setFamily(u"Georgia")
        font4.setPointSize(7)
        self.fname.setFont(font4)
        self.fname.setAutoFillBackground(True)
        self.fname.setFrameShape(QFrame.StyledPanel)
        self.fname.setMargin(2)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.mname = QLabel(self.frame)
        self.mname.setObjectName(u"mname")
        sizePolicy5.setHeightForWidth(self.mname.sizePolicy().hasHeightForWidth())
        self.mname.setSizePolicy(sizePolicy5)
        self.mname.setFont(font4)
        self.mname.setAutoFillBackground(True)
        self.mname.setFrameShape(QFrame.StyledPanel)
        self.mname.setMargin(2)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.mname)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.lname = QLabel(self.frame)
        self.lname.setObjectName(u"lname")
        sizePolicy5.setHeightForWidth(self.lname.sizePolicy().hasHeightForWidth())
        self.lname.setSizePolicy(sizePolicy5)
        self.lname.setFont(font4)
        self.lname.setAutoFillBackground(True)
        self.lname.setFrameShape(QFrame.StyledPanel)
        self.lname.setMargin(2)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lname)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.age = QLabel(self.frame)
        self.age.setObjectName(u"age")
        sizePolicy5.setHeightForWidth(self.age.sizePolicy().hasHeightForWidth())
        self.age.setSizePolicy(sizePolicy5)
        self.age.setFont(font4)
        self.age.setAutoFillBackground(True)
        self.age.setFrameShape(QFrame.StyledPanel)
        self.age.setMargin(2)

        self.horizontalLayout.addWidget(self.age)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setMargin(0)

        self.horizontalLayout.addWidget(self.label_10)

        self.gender = QLabel(self.frame)
        self.gender.setObjectName(u"gender")
        sizePolicy5.setHeightForWidth(self.gender.sizePolicy().hasHeightForWidth())
        self.gender.setSizePolicy(sizePolicy5)
        self.gender.setFont(font4)
        self.gender.setAutoFillBackground(True)
        self.gender.setFrameShape(QFrame.StyledPanel)
        self.gender.setMargin(2)

        self.horizontalLayout.addWidget(self.gender)


        self.formLayout_3.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_12)

        self.class_2 = QLabel(self.frame)
        self.class_2.setObjectName(u"class_2")
        sizePolicy5.setHeightForWidth(self.class_2.sizePolicy().hasHeightForWidth())
        self.class_2.setSizePolicy(sizePolicy5)
        self.class_2.setAutoFillBackground(True)
        self.class_2.setFrameShape(QFrame.StyledPanel)
        self.class_2.setMargin(2)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.class_2)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.phone = QLabel(self.frame_2)
        self.phone.setObjectName(u"phone")
        sizePolicy5.setHeightForWidth(self.phone.sizePolicy().hasHeightForWidth())
        self.phone.setSizePolicy(sizePolicy5)
        self.phone.setFont(font4)
        self.phone.setAutoFillBackground(True)
        self.phone.setFrameShape(QFrame.StyledPanel)
        self.phone.setMargin(2)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.phone)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.email = QLabel(self.frame_2)
        self.email.setObjectName(u"email")
        sizePolicy5.setHeightForWidth(self.email.sizePolicy().hasHeightForWidth())
        self.email.setSizePolicy(sizePolicy5)
        self.email.setFont(font4)
        self.email.setAutoFillBackground(True)
        self.email.setFrameShape(QFrame.StyledPanel)
        self.email.setMargin(2)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.email)

        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_19)

        self.origin = QLabel(self.frame_2)
        self.origin.setObjectName(u"origin")
        sizePolicy5.setHeightForWidth(self.origin.sizePolicy().hasHeightForWidth())
        self.origin.setSizePolicy(sizePolicy5)
        self.origin.setFont(font4)
        self.origin.setAutoFillBackground(True)
        self.origin.setFrameShape(QFrame.StyledPanel)
        self.origin.setMargin(2)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.origin)

        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_21)

        self.nationality = QLabel(self.frame_2)
        self.nationality.setObjectName(u"nationality")
        sizePolicy5.setHeightForWidth(self.nationality.sizePolicy().hasHeightForWidth())
        self.nationality.setSizePolicy(sizePolicy5)
        self.nationality.setFont(font4)
        self.nationality.setAutoFillBackground(True)
        self.nationality.setFrameShape(QFrame.StyledPanel)
        self.nationality.setMargin(2)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.nationality)


        self.gridLayout_3.addWidget(self.frame_2, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 13, -1)
        self.label_23 = QLabel(self.groupBox)
        self.label_23.setObjectName(u"label_23")
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)
        self.label_23.setFont(font3)
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_23.setMargin(10)

        self.horizontalLayout_3.addWidget(self.label_23)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        sizePolicy5.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy5)
        self.label_11.setAutoFillBackground(True)
        self.label_11.setFrameShape(QFrame.StyledPanel)
        self.label_11.setMargin(2)

        self.horizontalLayout_3.addWidget(self.label_11)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 13, -1)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(10)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.addressL2 = QLabel(self.groupBox)
        self.addressL2.setObjectName(u"addressL2")
        sizePolicy5.setHeightForWidth(self.addressL2.sizePolicy().hasHeightForWidth())
        self.addressL2.setSizePolicy(sizePolicy5)
        self.addressL2.setFont(font4)
        self.addressL2.setAutoFillBackground(True)
        self.addressL2.setFrameShape(QFrame.StyledPanel)
        self.addressL2.setMargin(2)

        self.horizontalLayout_4.addWidget(self.addressL2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addLayout(self.verticalLayout, 1, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.bgLayer)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy5.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy5)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 22, -1, -1)
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setVerticalSpacing(9)
        self.formLayout_5.setContentsMargins(-1, 13, 13, 13)
        self.label_33 = QLabel(self.groupBox_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)
        self.label_33.setAlignment(Qt.AlignCenter)
        self.label_33.setMargin(2)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_33)

        self.cardNum = QLabel(self.groupBox_3)
        self.cardNum.setObjectName(u"cardNum")
        sizePolicy5.setHeightForWidth(self.cardNum.sizePolicy().hasHeightForWidth())
        self.cardNum.setSizePolicy(sizePolicy5)
        self.cardNum.setFont(font4)
        self.cardNum.setAutoFillBackground(True)
        self.cardNum.setFrameShape(QFrame.StyledPanel)
        self.cardNum.setMargin(2)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.cardNum)

        self.label_35 = QLabel(self.groupBox_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font3)
        self.label_35.setAlignment(Qt.AlignCenter)
        self.label_35.setMargin(2)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_35)

        self.patientsStat = QLabel(self.groupBox_3)
        self.patientsStat.setObjectName(u"patientsStat")
        sizePolicy5.setHeightForWidth(self.patientsStat.sizePolicy().hasHeightForWidth())
        self.patientsStat.setSizePolicy(sizePolicy5)
        self.patientsStat.setFont(font4)
        self.patientsStat.setAutoFillBackground(True)
        self.patientsStat.setFrameShape(QFrame.StyledPanel)
        self.patientsStat.setMargin(2)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.patientsStat)


        self.horizontalLayout_5.addLayout(self.formLayout_5)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setVerticalSpacing(9)
        self.formLayout_6.setContentsMargins(0, 13, 13, 13)
        self.label_37 = QLabel(self.groupBox_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font3)
        self.label_37.setAlignment(Qt.AlignCenter)
        self.label_37.setMargin(2)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_37)

        self.regdate = QLabel(self.groupBox_3)
        self.regdate.setObjectName(u"regdate")
        sizePolicy5.setHeightForWidth(self.regdate.sizePolicy().hasHeightForWidth())
        self.regdate.setSizePolicy(sizePolicy5)
        self.regdate.setFont(font4)
        self.regdate.setAutoFillBackground(True)
        self.regdate.setFrameShape(QFrame.StyledPanel)
        self.regdate.setMargin(2)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.regdate)

        self.label_39 = QLabel(self.groupBox_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font3)
        self.label_39.setAlignment(Qt.AlignCenter)
        self.label_39.setMargin(2)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_39)

        self.admissiondate = QLabel(self.groupBox_3)
        self.admissiondate.setObjectName(u"admissiondate")
        sizePolicy5.setHeightForWidth(self.admissiondate.sizePolicy().hasHeightForWidth())
        self.admissiondate.setSizePolicy(sizePolicy5)
        self.admissiondate.setFont(font4)
        self.admissiondate.setAutoFillBackground(True)
        self.admissiondate.setFrameShape(QFrame.StyledPanel)
        self.admissiondate.setMargin(2)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.admissiondate)


        self.horizontalLayout_5.addLayout(self.formLayout_6)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.bgLayer)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy5.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy5)
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 27, -1, -1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 13, 14, -1)
        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_17.setMargin(10)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_17)

        self.kFname = QLabel(self.groupBox_4)
        self.kFname.setObjectName(u"kFname")
        sizePolicy5.setHeightForWidth(self.kFname.sizePolicy().hasHeightForWidth())
        self.kFname.setSizePolicy(sizePolicy5)
        self.kFname.setFont(font4)
        self.kFname.setAutoFillBackground(True)
        self.kFname.setFrameShape(QFrame.StyledPanel)
        self.kFname.setMargin(2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.kFname)

        self.klname = QLabel(self.groupBox_4)
        self.klname.setObjectName(u"klname")
        sizePolicy5.setHeightForWidth(self.klname.sizePolicy().hasHeightForWidth())
        self.klname.setSizePolicy(sizePolicy5)
        self.klname.setAutoFillBackground(True)
        self.klname.setFrameShape(QFrame.StyledPanel)
        self.klname.setMargin(2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.klname)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setMargin(10)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_9)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_7.setContentsMargins(-1, 13, 14, -1)
        self.kphone = QLabel(self.groupBox_4)
        self.kphone.setObjectName(u"kphone")
        sizePolicy5.setHeightForWidth(self.kphone.sizePolicy().hasHeightForWidth())
        self.kphone.setSizePolicy(sizePolicy5)
        self.kphone.setFont(font4)
        self.kphone.setAutoFillBackground(True)
        self.kphone.setFrameShape(QFrame.StyledPanel)
        self.kphone.setMargin(2)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.kphone)

        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy6)
        self.label_18.setFont(font3)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setMargin(10)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.label_26 = QLabel(self.groupBox_4)
        self.label_26.setObjectName(u"label_26")
        sizePolicy6.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy6)
        self.label_26.setFont(font3)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setMargin(10)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_26)

        self.krelationship = QLabel(self.groupBox_4)
        self.krelationship.setObjectName(u"krelationship")
        sizePolicy5.setHeightForWidth(self.krelationship.sizePolicy().hasHeightForWidth())
        self.krelationship.setSizePolicy(sizePolicy5)
        self.krelationship.setFont(font4)
        self.krelationship.setAutoFillBackground(True)
        self.krelationship.setFrameShape(QFrame.StyledPanel)
        self.krelationship.setMargin(2)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.krelationship)


        self.gridLayout_2.addLayout(self.formLayout_7, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 13, -1)
        self.label_28 = QLabel(self.groupBox_4)
        self.label_28.setObjectName(u"label_28")
        sizePolicy1.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy1)
        self.label_28.setFont(font3)
        self.label_28.setAlignment(Qt.AlignCenter)
        self.label_28.setMargin(10)

        self.horizontalLayout_6.addWidget(self.label_28)

        self.kaddressL1 = QLabel(self.groupBox_4)
        self.kaddressL1.setObjectName(u"kaddressL1")
        sizePolicy5.setHeightForWidth(self.kaddressL1.sizePolicy().hasHeightForWidth())
        self.kaddressL1.setSizePolicy(sizePolicy5)
        self.kaddressL1.setFont(font4)
        self.kaddressL1.setAutoFillBackground(True)
        self.kaddressL1.setFrameShape(QFrame.StyledPanel)
        self.kaddressL1.setMargin(2)

        self.horizontalLayout_6.addWidget(self.kaddressL1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, 13, -1)
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setMargin(10)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.kaddressL2 = QLabel(self.groupBox_4)
        self.kaddressL2.setObjectName(u"kaddressL2")
        sizePolicy5.setHeightForWidth(self.kaddressL2.sizePolicy().hasHeightForWidth())
        self.kaddressL2.setSizePolicy(sizePolicy5)
        self.kaddressL2.setFont(font4)
        self.kaddressL2.setAutoFillBackground(True)
        self.kaddressL2.setFrameShape(QFrame.StyledPanel)
        self.kaddressL2.setMargin(2)

        self.horizontalLayout_7.addWidget(self.kaddressL2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.closeBtn = QPushButton(self.bgLayer)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy7)

        self.horizontalLayout_8.addWidget(self.closeBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.gridLayout.addWidget(self.bgLayer, 1, 0, 1, 1)


        self.retranslateUi(Profile)

        QMetaObject.connectSlotsByName(Profile)
    # setupUi

    def retranslateUi(self, Profile):
        Profile.setWindowTitle(QCoreApplication.translate("Profile", u"Dialog", None))
        self.logo.setText("")
        self.label.setText(QCoreApplication.translate("Profile", u"Patient's Profile", None))
        self.miniBtn.setText(QCoreApplication.translate("Profile", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("Profile", u"X", None))
        self.groupBox.setTitle(QCoreApplication.translate("Profile", u"Patient's Personal Details", None))
        self.label_2.setText(QCoreApplication.translate("Profile", u"First Name", None))
        self.fname.setText("")
        self.label_4.setText(QCoreApplication.translate("Profile", u"Middle Name:", None))
        self.mname.setText("")
        self.label_5.setText(QCoreApplication.translate("Profile", u"Last Name: ", None))
        self.lname.setText("")
        self.label_8.setText(QCoreApplication.translate("Profile", u"Gender:", None))
        self.age.setText("")
        self.label_10.setText(QCoreApplication.translate("Profile", u"Age:", None))
        self.gender.setText("")
        self.label_12.setText(QCoreApplication.translate("Profile", u"Class:", None))
        self.class_2.setText("")
        self.label_13.setText(QCoreApplication.translate("Profile", u"Mobile:", None))
        self.phone.setText("")
        self.label_15.setText(QCoreApplication.translate("Profile", u"Email: ", None))
        self.email.setText("")
        self.label_19.setText(QCoreApplication.translate("Profile", u"State of Origin:", None))
        self.origin.setText("")
        self.label_21.setText(QCoreApplication.translate("Profile", u"Nationality:", None))
        self.nationality.setText("")
        self.label_23.setText(QCoreApplication.translate("Profile", u"Address Line 1:", None))
        self.label_11.setText("")
        self.label_3.setText(QCoreApplication.translate("Profile", u"Address Line 2", None))
        self.addressL2.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("Profile", u"Hospital Details:", None))
        self.label_33.setText(QCoreApplication.translate("Profile", u"Patient's Number:", None))
        self.cardNum.setText("")
        self.label_35.setText(QCoreApplication.translate("Profile", u"Patient Status:", None))
        self.patientsStat.setText("")
        self.label_37.setText(QCoreApplication.translate("Profile", u"Date of Registration:", None))
        self.regdate.setText("")
        self.label_39.setText(QCoreApplication.translate("Profile", u"Date of Admission:", None))
        self.admissiondate.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("Profile", u"Next of Kin Details", None))
        self.label_17.setText(QCoreApplication.translate("Profile", u"First Name:", None))
        self.kFname.setText("")
        self.klname.setText("")
        self.label_9.setText(QCoreApplication.translate("Profile", u"Last Name:", None))
        self.kphone.setText("")
        self.label_18.setText(QCoreApplication.translate("Profile", u"Phone:", None))
        self.label_26.setText(QCoreApplication.translate("Profile", u"Relationship:", None))
        self.krelationship.setText("")
        self.label_28.setText(QCoreApplication.translate("Profile", u"Address Line 1:", None))
        self.kaddressL1.setText("")
        self.label_6.setText(QCoreApplication.translate("Profile", u"Address Line 2:", None))
        self.kaddressL2.setText("")
        self.closeBtn.setText(QCoreApplication.translate("Profile", u"Close", None))
    # retranslateUi

