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
        Register.resize(512, 546)
        self.gridLayout = QGridLayout(Register)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgLayer = QFrame(Register)
        self.bgLayer.setObjectName(u"bgLayer")
        font = QFont()
        font.setPointSize(8)
        self.bgLayer.setFont(font)
        self.bgLayer.setMouseTracking(True)
        self.bgLayer.setTabletTracking(True)
        self.bgLayer.setFrameShape(QFrame.StyledPanel)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.bgframe = QFrame(self.bgLayer)
        self.bgframe.setObjectName(u"bgframe")
        self.bgframe.setFont(font)
        self.bgframe.setMouseTracking(True)
        self.bgframe.setTabletTracking(True)
        self.bgframe.setFrameShape(QFrame.Box)
        self.bgframe.setFrameShadow(QFrame.Raised)
        self.bgframe.setLineWidth(2)
        self.bgframe.setMidLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.bgframe)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pinfo = QLabel(self.bgframe)
        self.pinfo.setObjectName(u"pinfo")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.pinfo.setFont(font1)
        self.pinfo.setMouseTracking(True)
        self.pinfo.setTabletTracking(True)
        self.pinfo.setAlignment(Qt.AlignCenter)
        self.pinfo.setMargin(0)

        self.verticalLayout.addWidget(self.pinfo)

        self.groupBox = QGroupBox(self.bgframe)
        self.groupBox.setObjectName(u"groupBox")
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.groupBox.setFont(font2)
        self.groupBox.setMouseTracking(True)
        self.groupBox.setTabletTracking(True)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.fname = QLineEdit(self.groupBox)
        self.fname.setObjectName(u"fname")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy)
        self.fname.setMinimumSize(QSize(150, 0))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setWeight(50)
        self.fname.setFont(font3)
        self.fname.setMouseTracking(True)
        self.fname.setTabletTracking(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(True)
        self.label_3.setTabletTracking(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(True)
        self.label_4.setTabletTracking(True)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(True)
        self.label_5.setTabletTracking(True)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setMouseTracking(True)
        self.label_6.setTabletTracking(True)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.lname = QLineEdit(self.groupBox)
        self.lname.setObjectName(u"lname")
        self.lname.setFont(font3)
        self.lname.setMouseTracking(True)
        self.lname.setTabletTracking(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lname)

        self.oname = QLineEdit(self.groupBox)
        self.oname.setObjectName(u"oname")
        self.oname.setFont(font3)
        self.oname.setMouseTracking(True)
        self.oname.setTabletTracking(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.oname)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gender = QComboBox(self.groupBox)
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.setObjectName(u"gender")
        self.gender.setFont(font3)
        self.gender.setCursor(QCursor(Qt.PointingHandCursor))
        self.gender.setMouseTracking(True)
        self.gender.setTabletTracking(True)

        self.horizontalLayout_4.addWidget(self.gender)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setMouseTracking(True)
        self.label_11.setTabletTracking(True)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.age = QLineEdit(self.groupBox)
        self.age.setObjectName(u"age")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.age.sizePolicy().hasHeightForWidth())
        self.age.setSizePolicy(sizePolicy1)
        self.age.setMinimumSize(QSize(30, 0))
        self.age.setFont(font3)
        self.age.setMouseTracking(True)
        self.age.setTabletTracking(True)

        self.horizontalLayout_4.addWidget(self.age)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.pclass = QComboBox(self.groupBox)
        self.pclass.addItem("")
        self.pclass.addItem("")
        self.pclass.addItem("")
        self.pclass.addItem("")
        self.pclass.addItem("")
        self.pclass.setObjectName(u"pclass")
        self.pclass.setFont(font3)
        self.pclass.setCursor(QCursor(Qt.PointingHandCursor))
        self.pclass.setMouseTracking(True)
        self.pclass.setTabletTracking(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pclass)


        self.horizontalLayout.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(True)
        self.label_2.setTabletTracking(True)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setMouseTracking(True)
        self.label_7.setTabletTracking(True)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.origin = QLineEdit(self.groupBox)
        self.origin.setObjectName(u"origin")
        self.origin.setFont(font3)
        self.origin.setMouseTracking(True)
        self.origin.setTabletTracking(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.origin)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setMouseTracking(True)
        self.label_9.setTabletTracking(True)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setMouseTracking(True)
        self.label_10.setTabletTracking(True)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_10)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setMouseTracking(True)
        self.label_8.setTabletTracking(True)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.nationality = QLineEdit(self.groupBox)
        self.nationality.setObjectName(u"nationality")
        self.nationality.setFont(font3)
        self.nationality.setMouseTracking(True)
        self.nationality.setTabletTracking(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.nationality)

        self.address = QLineEdit(self.groupBox)
        self.address.setObjectName(u"address")
        self.address.setFont(font3)
        self.address.setMouseTracking(True)
        self.address.setTabletTracking(True)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.address)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.state = QLineEdit(self.groupBox)
        self.state.setObjectName(u"state")
        sizePolicy.setHeightForWidth(self.state.sizePolicy().hasHeightForWidth())
        self.state.setSizePolicy(sizePolicy)
        self.state.setFont(font3)
        self.state.setMouseTracking(True)
        self.state.setTabletTracking(True)

        self.horizontalLayout_6.addWidget(self.state)

        self.label_22 = QLabel(self.groupBox)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_22)

        self.country = QLineEdit(self.groupBox)
        self.country.setObjectName(u"country")
        sizePolicy.setHeightForWidth(self.country.sizePolicy().hasHeightForWidth())
        self.country.setSizePolicy(sizePolicy)
        self.country.setFont(font3)

        self.horizontalLayout_6.addWidget(self.country)


        self.formLayout_2.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.phone = QLineEdit(self.groupBox)
        self.phone.setObjectName(u"phone")
        sizePolicy.setHeightForWidth(self.phone.sizePolicy().hasHeightForWidth())
        self.phone.setSizePolicy(sizePolicy)
        self.phone.setFont(font3)
        self.phone.setMouseTracking(True)
        self.phone.setTabletTracking(True)

        self.horizontalLayout_8.addWidget(self.phone)

        self.label_24 = QLabel(self.groupBox)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_24)

        self.email = QLineEdit(self.groupBox)
        self.email.setObjectName(u"email")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.email.sizePolicy().hasHeightForWidth())
        self.email.setSizePolicy(sizePolicy2)
        self.email.setFont(font3)

        self.horizontalLayout_8.addWidget(self.email)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_8)


        self.horizontalLayout.addLayout(self.formLayout_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.groupBox_2 = QGroupBox(self.bgframe)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.groupBox_2.setFont(font2)
        self.groupBox_2.setMouseTracking(True)
        self.groupBox_2.setTabletTracking(True)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setMouseTracking(True)
        self.label_12.setTabletTracking(True)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setMouseTracking(True)
        self.label_14.setTabletTracking(True)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setMouseTracking(True)
        self.label_20.setTabletTracking(True)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_20)

        self.kfname = QLineEdit(self.groupBox_2)
        self.kfname.setObjectName(u"kfname")
        sizePolicy.setHeightForWidth(self.kfname.sizePolicy().hasHeightForWidth())
        self.kfname.setSizePolicy(sizePolicy)
        self.kfname.setMinimumSize(QSize(150, 0))
        self.kfname.setFont(font3)
        self.kfname.setMouseTracking(True)
        self.kfname.setTabletTracking(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.kfname)

        self.kphone = QLineEdit(self.groupBox_2)
        self.kphone.setObjectName(u"kphone")
        self.kphone.setFont(font3)
        self.kphone.setMouseTracking(True)
        self.kphone.setTabletTracking(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.kphone)

        self.kaddress = QLineEdit(self.groupBox_2)
        self.kaddress.setObjectName(u"kaddress")
        self.kaddress.setFont(font3)
        self.kaddress.setMouseTracking(True)
        self.kaddress.setTabletTracking(True)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.kaddress)


        self.horizontalLayout_2.addLayout(self.formLayout_3)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setMouseTracking(True)
        self.label_13.setTabletTracking(True)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setMouseTracking(True)
        self.label_15.setTabletTracking(True)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setMouseTracking(True)
        self.label_21.setTabletTracking(True)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_21)

        self.klname = QLineEdit(self.groupBox_2)
        self.klname.setObjectName(u"klname")
        sizePolicy.setHeightForWidth(self.klname.sizePolicy().hasHeightForWidth())
        self.klname.setSizePolicy(sizePolicy)
        self.klname.setMinimumSize(QSize(100, 0))
        self.klname.setFont(font3)
        self.klname.setMouseTracking(True)
        self.klname.setTabletTracking(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.klname)

        self.krelationship = QComboBox(self.groupBox_2)
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.addItem("")
        self.krelationship.setObjectName(u"krelationship")
        self.krelationship.setFont(font3)
        self.krelationship.setCursor(QCursor(Qt.PointingHandCursor))
        self.krelationship.setMouseTracking(True)
        self.krelationship.setTabletTracking(True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.krelationship)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.kstate = QLineEdit(self.groupBox_2)
        self.kstate.setObjectName(u"kstate")
        sizePolicy.setHeightForWidth(self.kstate.sizePolicy().hasHeightForWidth())
        self.kstate.setSizePolicy(sizePolicy)
        self.kstate.setFont(font3)
        self.kstate.setMouseTracking(True)
        self.kstate.setTabletTracking(True)

        self.horizontalLayout_7.addWidget(self.kstate)

        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_23)

        self.kcountry = QLineEdit(self.groupBox_2)
        self.kcountry.setObjectName(u"kcountry")
        sizePolicy.setHeightForWidth(self.kcountry.sizePolicy().hasHeightForWidth())
        self.kcountry.setSizePolicy(sizePolicy)
        self.kcountry.setFont(font3)

        self.horizontalLayout_7.addWidget(self.kcountry)


        self.formLayout_4.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_7)


        self.horizontalLayout_2.addLayout(self.formLayout_4)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer_2 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.groupBox_3 = QGroupBox(self.bgframe)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font2)
        self.groupBox_3.setMouseTracking(True)
        self.groupBox_3.setTabletTracking(True)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setMouseTracking(True)
        self.label_16.setTabletTracking(True)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setMouseTracking(True)
        self.label_18.setTabletTracking(True)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_18)

        self.patientID = QLineEdit(self.groupBox_3)
        self.patientID.setObjectName(u"patientID")
        self.patientID.setFont(font3)
        self.patientID.setMouseTracking(True)
        self.patientID.setTabletTracking(True)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.patientID)

        self.status = QComboBox(self.groupBox_3)
        self.status.addItem("")
        self.status.addItem("")
        self.status.addItem("")
        self.status.setObjectName(u"status")
        self.status.setFont(font3)
        self.status.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.status)


        self.horizontalLayout_3.addLayout(self.formLayout_5)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setMouseTracking(True)
        self.label_17.setTabletTracking(True)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_17)

        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setMouseTracking(True)
        self.label_19.setTabletTracking(True)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_19)

        self.regDate = QDateTimeEdit(self.groupBox_3)
        self.regDate.setObjectName(u"regDate")
        self.regDate.setFont(font3)
        self.regDate.setCursor(QCursor(Qt.PointingHandCursor))
        self.regDate.setMouseTracking(True)
        self.regDate.setTabletTracking(True)
        self.regDate.setWrapping(True)
        self.regDate.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.regDate.setDateTime(QDateTime(QDate(2021, 4, 11), QTime(0, 0, 0)))
        self.regDate.setCalendarPopup(True)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.regDate)

        self.admissionDate = QDateTimeEdit(self.groupBox_3)
        self.admissionDate.setObjectName(u"admissionDate")
        self.admissionDate.setFont(font3)
        self.admissionDate.setCursor(QCursor(Qt.PointingHandCursor))
        self.admissionDate.setMouseTracking(True)
        self.admissionDate.setTabletTracking(True)
        self.admissionDate.setWrapping(True)
        self.admissionDate.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.admissionDate.setDateTime(QDateTime(QDate(2021, 4, 11), QTime(0, 0, 0)))
        self.admissionDate.setCalendarPopup(True)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.admissionDate)


        self.horizontalLayout_3.addLayout(self.formLayout_6)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(self.bgframe)
        self.cancelBtn.setObjectName(u"cancelBtn")
        font4 = QFont()
        font4.setFamily(u"Comic Sans MS")
        font4.setPointSize(8)
        self.cancelBtn.setFont(font4)
        self.cancelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelBtn.setMouseTracking(True)
        self.cancelBtn.setTabletTracking(True)

        self.horizontalLayout_5.addWidget(self.cancelBtn)

        self.regBtn = QPushButton(self.bgframe)
        self.regBtn.setObjectName(u"regBtn")
        self.regBtn.setFont(font4)
        self.regBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.regBtn.setMouseTracking(True)
        self.regBtn.setTabletTracking(True)

        self.horizontalLayout_5.addWidget(self.regBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.gridLayout_2.addWidget(self.bgframe, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 0, 0, 1, 1)


        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Registration Form", None))
        self.pinfo.setText(QCoreApplication.translate("Register", u"TextLabel", None))
        self.groupBox.setTitle(QCoreApplication.translate("Register", u"Patient's Details:", None))
        self.label.setText(QCoreApplication.translate("Register", u"First Name:", None))
        self.label_3.setText(QCoreApplication.translate("Register", u"Last Name:", None))
        self.label_4.setText(QCoreApplication.translate("Register", u"Other Name:", None))
        self.label_5.setText(QCoreApplication.translate("Register", u"Gender:", None))
        self.label_6.setText(QCoreApplication.translate("Register", u"Class:", None))
        self.gender.setItemText(0, QCoreApplication.translate("Register", u"Male", None))
        self.gender.setItemText(1, QCoreApplication.translate("Register", u"Female", None))
        self.gender.setItemText(2, QCoreApplication.translate("Register", u"Other", None))

        self.label_11.setText(QCoreApplication.translate("Register", u"Age", None))
        self.pclass.setItemText(0, QCoreApplication.translate("Register", u"Private", None))
        self.pclass.setItemText(1, QCoreApplication.translate("Register", u"Company", None))
        self.pclass.setItemText(2, QCoreApplication.translate("Register", u"Family", None))
        self.pclass.setItemText(3, QCoreApplication.translate("Register", u"HMO", None))
        self.pclass.setItemText(4, QCoreApplication.translate("Register", u"Other", None))

        self.label_2.setText(QCoreApplication.translate("Register", u"Phone Number:", None))
        self.label_7.setText(QCoreApplication.translate("Register", u"State of Origin:", None))
        self.label_9.setText(QCoreApplication.translate("Register", u"Address:", None))
        self.label_10.setText(QCoreApplication.translate("Register", u"State:", None))
        self.label_8.setText(QCoreApplication.translate("Register", u"Nationality:", None))
        self.label_22.setText(QCoreApplication.translate("Register", u"Country:", None))
        self.label_24.setText(QCoreApplication.translate("Register", u"Email:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Register", u"Next of Kin Detail:", None))
        self.label_12.setText(QCoreApplication.translate("Register", u"first Name:", None))
        self.label_14.setText(QCoreApplication.translate("Register", u"Phone Number:", None))
        self.label_20.setText(QCoreApplication.translate("Register", u"Address:", None))
        self.label_13.setText(QCoreApplication.translate("Register", u"Last Name:", None))
        self.label_15.setText(QCoreApplication.translate("Register", u"Relationship:", None))
        self.label_21.setText(QCoreApplication.translate("Register", u"State:", None))
        self.krelationship.setItemText(0, QCoreApplication.translate("Register", u"Father", None))
        self.krelationship.setItemText(1, QCoreApplication.translate("Register", u"Mother", None))
        self.krelationship.setItemText(2, QCoreApplication.translate("Register", u"Uncle", None))
        self.krelationship.setItemText(3, QCoreApplication.translate("Register", u"Aunt", None))
        self.krelationship.setItemText(4, QCoreApplication.translate("Register", u"Son", None))
        self.krelationship.setItemText(5, QCoreApplication.translate("Register", u"Daughter", None))
        self.krelationship.setItemText(6, QCoreApplication.translate("Register", u"Brother", None))
        self.krelationship.setItemText(7, QCoreApplication.translate("Register", u"Sister", None))
        self.krelationship.setItemText(8, QCoreApplication.translate("Register", u"Cousin", None))
        self.krelationship.setItemText(9, QCoreApplication.translate("Register", u"Relation", None))
        self.krelationship.setItemText(10, QCoreApplication.translate("Register", u"Friend", None))
        self.krelationship.setItemText(11, QCoreApplication.translate("Register", u"Husband", None))
        self.krelationship.setItemText(12, QCoreApplication.translate("Register", u"Wife", None))
        self.krelationship.setItemText(13, QCoreApplication.translate("Register", u"Fiance", None))

        self.label_23.setText(QCoreApplication.translate("Register", u"Country:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Register", u"Patient's Hospital Details:", None))
        self.label_16.setText(QCoreApplication.translate("Register", u"Patient's ID:", None))
        self.label_18.setText(QCoreApplication.translate("Register", u"Patient's Status:", None))
        self.status.setItemText(0, QCoreApplication.translate("Register", u"In-Patient", None))
        self.status.setItemText(1, QCoreApplication.translate("Register", u"Out-Patient", None))
        self.status.setItemText(2, QCoreApplication.translate("Register", u"Discharged", None))

        self.label_17.setText(QCoreApplication.translate("Register", u"Registration Date:", None))
        self.label_19.setText(QCoreApplication.translate("Register", u"Admission Date:", None))
#if QT_CONFIG(tooltip)
        self.cancelBtn.setToolTip(QCoreApplication.translate("Register", u"<html><head/><body><p>Click to cancel registration</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cancelBtn.setText(QCoreApplication.translate("Register", u"Cancel", None))
#if QT_CONFIG(tooltip)
        self.regBtn.setToolTip(QCoreApplication.translate("Register", u"<html><head/><body><p>Click to Register</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.regBtn.setText(QCoreApplication.translate("Register", u"Register", None))
    # retranslateUi

