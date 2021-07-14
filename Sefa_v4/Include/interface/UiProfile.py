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
        Profile.resize(548, 577)
        self.gridLayout = QGridLayout(Profile)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgLayer = QFrame(Profile)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setFrameShape(QFrame.StyledPanel)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.bgLayer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.bgframe = QFrame(self.bgLayer)
        self.bgframe.setObjectName(u"bgframe")
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.bgframe.setFont(font)
        self.bgframe.setFrameShape(QFrame.Box)
        self.bgframe.setFrameShadow(QFrame.Raised)
        self.bgframe.setLineWidth(2)
        self.bgframe.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgframe)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.groupBox = QGroupBox(self.bgframe)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.groupBox.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.fname = QLabel(self.groupBox)
        self.fname.setObjectName(u"fname")
        self.fname.setMinimumSize(QSize(150, 0))
        self.fname.setFont(font)
        self.fname.setAutoFillBackground(True)
        self.fname.setFrameShape(QFrame.StyledPanel)
        self.fname.setMargin(3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.lname = QLabel(self.groupBox)
        self.lname.setObjectName(u"lname")
        self.lname.setFont(font)
        self.lname.setAutoFillBackground(True)
        self.lname.setFrameShape(QFrame.StyledPanel)
        self.lname.setMargin(3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lname)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.oname = QLabel(self.groupBox)
        self.oname.setObjectName(u"oname")
        self.oname.setFont(font)
        self.oname.setAutoFillBackground(True)
        self.oname.setFrameShape(QFrame.StyledPanel)
        self.oname.setMargin(3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.oname)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.gender = QLabel(self.groupBox)
        self.gender.setObjectName(u"gender")
        self.gender.setFont(font)
        self.gender.setAutoFillBackground(True)
        self.gender.setFrameShape(QFrame.StyledPanel)
        self.gender.setMargin(3)

        self.horizontalLayout_5.addWidget(self.gender)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_19)

        self.age = QLabel(self.groupBox)
        self.age.setObjectName(u"age")
        self.age.setFont(font)
        self.age.setAutoFillBackground(True)
        self.age.setFrameShape(QFrame.StyledPanel)
        self.age.setMargin(3)

        self.horizontalLayout_5.addWidget(self.age)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.label_24 = QLabel(self.groupBox)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_24)

        self.pclass = QLabel(self.groupBox)
        self.pclass.setObjectName(u"pclass")
        self.pclass.setFont(font)
        self.pclass.setAutoFillBackground(True)
        self.pclass.setFrameShape(QFrame.StyledPanel)
        self.pclass.setMargin(3)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pclass)


        self.horizontalLayout.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.phone = QLabel(self.groupBox)
        self.phone.setObjectName(u"phone")
        self.phone.setMinimumSize(QSize(150, 0))
        self.phone.setFont(font)
        self.phone.setAutoFillBackground(True)
        self.phone.setFrameShape(QFrame.StyledPanel)
        self.phone.setMargin(3)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.phone)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_12)

        self.label_25 = QLabel(self.groupBox)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_25)

        self.label_26 = QLabel(self.groupBox)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_26)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.state = QLabel(self.groupBox)
        self.state.setObjectName(u"state")
        self.state.setFont(font)
        self.state.setAutoFillBackground(True)
        self.state.setFrameShape(QFrame.StyledPanel)
        self.state.setMargin(3)

        self.horizontalLayout_6.addWidget(self.state)

        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_28)

        self.country = QLabel(self.groupBox)
        self.country.setObjectName(u"country")
        self.country.setFont(font)
        self.country.setAutoFillBackground(True)
        self.country.setFrameShape(QFrame.StyledPanel)
        self.country.setMargin(3)

        self.horizontalLayout_6.addWidget(self.country)


        self.formLayout_2.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.email = QLabel(self.groupBox)
        self.email.setObjectName(u"email")
        self.email.setFont(font)
        self.email.setAutoFillBackground(True)
        self.email.setFrameShape(QFrame.StyledPanel)
        self.email.setMargin(3)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.email)

        self.origin = QLabel(self.groupBox)
        self.origin.setObjectName(u"origin")
        self.origin.setFont(font)
        self.origin.setAutoFillBackground(True)
        self.origin.setFrameShape(QFrame.StyledPanel)
        self.origin.setMargin(3)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.origin)

        self.nationality = QLabel(self.groupBox)
        self.nationality.setObjectName(u"nationality")
        self.nationality.setFont(font)
        self.nationality.setAutoFillBackground(True)
        self.nationality.setFrameShape(QFrame.StyledPanel)
        self.nationality.setMargin(3)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.nationality)

        self.address = QLabel(self.groupBox)
        self.address.setObjectName(u"address")
        self.address.setFont(font)
        self.address.setAutoFillBackground(True)
        self.address.setFrameShape(QFrame.StyledPanel)
        self.address.setMargin(3)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.address)


        self.horizontalLayout.addLayout(self.formLayout_2)


        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.bgframe)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setFont(font1)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.patientID = QLabel(self.groupBox_3)
        self.patientID.setObjectName(u"patientID")
        self.patientID.setFont(font)
        self.patientID.setAutoFillBackground(True)
        self.patientID.setFrameShape(QFrame.StyledPanel)
        self.patientID.setMargin(3)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.patientID)

        self.status = QLabel(self.groupBox_3)
        self.status.setObjectName(u"status")
        self.status.setFont(font)
        self.status.setAutoFillBackground(True)
        self.status.setFrameShape(QFrame.StyledPanel)
        self.status.setMargin(3)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.status)


        self.horizontalLayout_3.addLayout(self.formLayout_5)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.regDate = QLabel(self.groupBox_3)
        self.regDate.setObjectName(u"regDate")
        self.regDate.setFont(font)
        self.regDate.setAutoFillBackground(True)
        self.regDate.setFrameShape(QFrame.StyledPanel)
        self.regDate.setMargin(3)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.regDate)

        self.admissionDate = QLabel(self.groupBox_3)
        self.admissionDate.setObjectName(u"admissionDate")
        self.admissionDate.setFont(font)
        self.admissionDate.setAutoFillBackground(True)
        self.admissionDate.setFrameShape(QFrame.StyledPanel)
        self.admissionDate.setMargin(3)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.admissionDate)


        self.horizontalLayout_3.addLayout(self.formLayout_6)


        self.gridLayout_2.addWidget(self.groupBox_3, 5, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.bgframe)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setFont(font1)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.label_34 = QLabel(self.groupBox_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font1)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_34)

        self.kfname = QLabel(self.groupBox_2)
        self.kfname.setObjectName(u"kfname")
        self.kfname.setMinimumSize(QSize(150, 0))
        self.kfname.setFont(font)
        self.kfname.setAutoFillBackground(True)
        self.kfname.setFrameShape(QFrame.StyledPanel)
        self.kfname.setMargin(3)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.kfname)

        self.klname = QLabel(self.groupBox_2)
        self.klname.setObjectName(u"klname")
        self.klname.setFont(font)
        self.klname.setAutoFillBackground(True)
        self.klname.setFrameShape(QFrame.StyledPanel)
        self.klname.setMargin(3)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.klname)

        self.krelationship = QLabel(self.groupBox_2)
        self.krelationship.setObjectName(u"krelationship")
        self.krelationship.setFont(font)
        self.krelationship.setAutoFillBackground(True)
        self.krelationship.setFrameShape(QFrame.StyledPanel)
        self.krelationship.setMargin(3)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.krelationship)


        self.horizontalLayout_2.addLayout(self.formLayout_3)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.kstate = QLabel(self.groupBox_2)
        self.kstate.setObjectName(u"kstate")
        self.kstate.setFont(font)
        self.kstate.setAutoFillBackground(True)
        self.kstate.setFrameShape(QFrame.StyledPanel)
        self.kstate.setMargin(3)

        self.horizontalLayout_7.addWidget(self.kstate)

        self.label_31 = QLabel(self.groupBox_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_31)

        self.kcountry = QLabel(self.groupBox_2)
        self.kcountry.setObjectName(u"kcountry")
        self.kcountry.setFont(font)
        self.kcountry.setAutoFillBackground(True)
        self.kcountry.setFrameShape(QFrame.StyledPanel)
        self.kcountry.setMargin(3)

        self.horizontalLayout_7.addWidget(self.kcountry)


        self.formLayout_4.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.label_33 = QLabel(self.groupBox_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font1)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_33)

        self.kphone = QLabel(self.groupBox_2)
        self.kphone.setObjectName(u"kphone")
        self.kphone.setMinimumSize(QSize(150, 0))
        self.kphone.setFont(font)
        self.kphone.setAutoFillBackground(True)
        self.kphone.setFrameShape(QFrame.StyledPanel)
        self.kphone.setMargin(3)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.kphone)

        self.kaddress = QLabel(self.groupBox_2)
        self.kaddress.setObjectName(u"kaddress")
        self.kaddress.setFont(font)
        self.kaddress.setAutoFillBackground(True)
        self.kaddress.setFrameShape(QFrame.StyledPanel)
        self.kaddress.setMargin(3)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.kaddress)


        self.horizontalLayout_2.addLayout(self.formLayout_4)


        self.gridLayout_2.addWidget(self.groupBox_2, 3, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.closeBtn = QPushButton(self.bgframe)
        self.closeBtn.setObjectName(u"closeBtn")

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 6, 0, 1, 1)


        self.gridLayout_3.addWidget(self.bgframe, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 0, 0, 1, 1)


        self.retranslateUi(Profile)

        QMetaObject.connectSlotsByName(Profile)
    # setupUi

    def retranslateUi(self, Profile):
        Profile.setWindowTitle(QCoreApplication.translate("Profile", u"Patient's Profile", None))
        self.groupBox.setTitle(QCoreApplication.translate("Profile", u"Patient's Personal Info:", None))
        self.label.setText(QCoreApplication.translate("Profile", u"First Name:", None))
        self.fname.setText("")
        self.label_7.setText(QCoreApplication.translate("Profile", u"Last Name:", None))
        self.lname.setText("")
        self.label_8.setText(QCoreApplication.translate("Profile", u"Other Name:", None))
        self.oname.setText("")
        self.label_9.setText(QCoreApplication.translate("Profile", u"Gender:", None))
        self.gender.setText("")
        self.label_19.setText(QCoreApplication.translate("Profile", u"Age:", None))
        self.age.setText("")
        self.label_24.setText(QCoreApplication.translate("Profile", u"Class:", None))
        self.pclass.setText("")
        self.label_2.setText(QCoreApplication.translate("Profile", u"Phone Number:", None))
        self.phone.setText("")
        self.label_10.setText(QCoreApplication.translate("Profile", u"Email:", None))
        self.label_11.setText(QCoreApplication.translate("Profile", u"State Of Origin:", None))
        self.label_12.setText(QCoreApplication.translate("Profile", u"Nationality:", None))
        self.label_25.setText(QCoreApplication.translate("Profile", u"Address:", None))
        self.label_26.setText(QCoreApplication.translate("Profile", u"Resident State:", None))
        self.state.setText("")
        self.label_28.setText(QCoreApplication.translate("Profile", u"Country:", None))
        self.country.setText("")
        self.email.setText("")
        self.origin.setText("")
        self.nationality.setText("")
        self.address.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("Profile", u"Patient's Hospital Info:", None))
        self.label_5.setText(QCoreApplication.translate("Profile", u"Patient's ID:", None))
        self.label_15.setText(QCoreApplication.translate("Profile", u"Patient's Status:", None))
        self.patientID.setText("")
        self.status.setText("")
        self.label_6.setText(QCoreApplication.translate("Profile", u"Registration Date:", None))
        self.label_16.setText(QCoreApplication.translate("Profile", u"Admission Date:", None))
        self.regDate.setText("")
        self.admissionDate.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Profile", u"Patient's Next of Kin Info:", None))
        self.label_3.setText(QCoreApplication.translate("Profile", u"First Name:", None))
        self.label_13.setText(QCoreApplication.translate("Profile", u"Last Name:", None))
        self.label_34.setText(QCoreApplication.translate("Profile", u"Relationship:", None))
        self.kfname.setText("")
        self.klname.setText("")
        self.krelationship.setText("")
        self.label_4.setText(QCoreApplication.translate("Profile", u"Address:", None))
        self.label_14.setText(QCoreApplication.translate("Profile", u"State:", None))
        self.kstate.setText("")
        self.label_31.setText(QCoreApplication.translate("Profile", u"Country:", None))
        self.kcountry.setText("")
        self.label_33.setText(QCoreApplication.translate("Profile", u"Phone Number:", None))
        self.kphone.setText("")
        self.kaddress.setText("")
        self.closeBtn.setText(QCoreApplication.translate("Profile", u"Close", None))
    # retranslateUi

