# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Authenticate.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Authenticate(object):
    def setupUi(self, Authenticate):
        if not Authenticate.objectName():
            Authenticate.setObjectName(u"Authenticate")
        Authenticate.resize(432, 467)
        self.horizontalLayout = QHBoxLayout(Authenticate)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bgLayer = QFrame(Authenticate)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setAutoFillBackground(True)
        self.bgLayer.setFrameShape(QFrame.StyledPanel)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.bgLayer)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.bgframe = QFrame(self.bgLayer)
        self.bgframe.setObjectName(u"bgframe")
        self.bgframe.setFrameShape(QFrame.StyledPanel)
        self.bgframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.bgframe)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.bgframe)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(4)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(3)
        self.frame_2.setMidLineWidth(1)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(2)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.imgView = QLabel(self.frame_3)
        self.imgView.setObjectName(u"imgView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.imgView.sizePolicy().hasHeightForWidth())
        self.imgView.setSizePolicy(sizePolicy2)
        self.imgView.setFrameShape(QFrame.Box)
        self.imgView.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.imgView, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.contactBtn = QPushButton(self.frame)
        self.contactBtn.setObjectName(u"contactBtn")

        self.horizontalLayout_2.addWidget(self.contactBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.line = QFrame(self.bgframe)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(4)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line)

        self.stackedWidget = QStackedWidget(self.bgframe)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_6 = QSpacerItem(20, 29, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_7)

        self.regStatus = QLabel(self.page)
        self.regStatus.setObjectName(u"regStatus")
        font1 = QFont()
        font1.setPointSize(6)
        self.regStatus.setFont(font1)
        self.regStatus.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.regStatus)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.label_21 = QLabel(self.page)
        self.label_21.setObjectName(u"label_21")
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.label_21.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_21)

        self.frame_7 = QFrame(self.page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.firstname = QLineEdit(self.frame_7)
        self.firstname.setObjectName(u"firstname")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.firstname)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_12)

        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_13)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_14)

        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_15)

        self.surname = QLineEdit(self.frame_7)
        self.surname.setObjectName(u"surname")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.surname)

        self.gender = QComboBox(self.frame_7)
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.setObjectName(u"gender")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.gender)

        self.dept = QComboBox(self.frame_7)
        self.dept.addItem("")
        self.dept.addItem("")
        self.dept.addItem("")
        self.dept.addItem("")
        self.dept.addItem("")
        self.dept.addItem("")
        self.dept.setObjectName(u"dept")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.dept)

        self.jobtitle = QComboBox(self.frame_7)
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.setObjectName(u"jobtitle")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.jobtitle)

        self.employeeID = QLineEdit(self.frame_7)
        self.employeeID.setObjectName(u"employeeID")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.employeeID)

        self.rank = QComboBox(self.frame_7)
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.setObjectName(u"rank")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.rank)

        self.phone = QLineEdit(self.frame_7)
        self.phone.setObjectName(u"phone")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.phone)

        self.email = QLineEdit(self.frame_7)
        self.email.setObjectName(u"email")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.email)


        self.gridLayout_5.addLayout(self.formLayout_2, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.label_16 = QLabel(self.page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_16)

        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_17)

        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_18)

        self.regUserid = QLineEdit(self.frame_6)
        self.regUserid.setObjectName(u"regUserid")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.regUserid)

        self.regPaswd = QLineEdit(self.frame_6)
        self.regPaswd.setObjectName(u"regPaswd")
        self.regPaswd.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.regPaswd)


        self.gridLayout_4.addLayout(self.formLayout_3, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.label_19 = QLabel(self.page)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_19)

        self.frame_8 = QFrame(self.page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_20 = QLabel(self.frame_8)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_20)

        self.authID = QLineEdit(self.frame_8)
        self.authID.setObjectName(u"authID")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.authID)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.regCancelBtn = QPushButton(self.frame_8)
        self.regCancelBtn.setObjectName(u"regCancelBtn")

        self.horizontalLayout_5.addWidget(self.regCancelBtn)

        self.registerBtn = QPushButton(self.frame_8)
        self.registerBtn.setObjectName(u"registerBtn")

        self.horizontalLayout_5.addWidget(self.registerBtn)


        self.formLayout_4.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_5)


        self.gridLayout_6.addLayout(self.formLayout_4, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_7)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_33 = QLabel(self.page_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_33)

        self.updateStatus = QLabel(self.page_3)
        self.updateStatus.setObjectName(u"updateStatus")
        self.updateStatus.setFont(font1)
        self.updateStatus.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.updateStatus)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.label_38 = QLabel(self.page_3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_38)

        self.frame_9 = QFrame(self.page_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_9)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_26 = QLabel(self.frame_9)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_26)

        self.upJob = QComboBox(self.frame_9)
        self.upJob.addItem("")
        self.upJob.addItem("")
        self.upJob.addItem("")
        self.upJob.addItem("")
        self.upJob.addItem("")
        self.upJob.setObjectName(u"upJob")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.upJob)

        self.label_27 = QLabel(self.frame_9)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_27)

        self.upDept = QComboBox(self.frame_9)
        self.upDept.addItem("")
        self.upDept.addItem("")
        self.upDept.addItem("")
        self.upDept.addItem("")
        self.upDept.addItem("")
        self.upDept.addItem("")
        self.upDept.setObjectName(u"upDept")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.upDept)

        self.label_28 = QLabel(self.frame_9)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_28)

        self.upID = QLineEdit(self.frame_9)
        self.upID.setObjectName(u"upID")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.upID)

        self.label_29 = QLabel(self.frame_9)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_29)

        self.upRank = QComboBox(self.frame_9)
        self.upRank.addItem("")
        self.upRank.addItem("")
        self.upRank.addItem("")
        self.upRank.addItem("")
        self.upRank.addItem("")
        self.upRank.addItem("")
        self.upRank.addItem("")
        self.upRank.addItem("")
        self.upRank.addItem("")
        self.upRank.addItem("")
        self.upRank.setObjectName(u"upRank")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.upRank)

        self.label_30 = QLabel(self.frame_9)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_30)

        self.upMobile = QLineEdit(self.frame_9)
        self.upMobile.setObjectName(u"upMobile")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.upMobile)

        self.label_31 = QLabel(self.frame_9)
        self.label_31.setObjectName(u"label_31")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_31)

        self.upEmail = QLineEdit(self.frame_9)
        self.upEmail.setObjectName(u"upEmail")

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.upEmail)


        self.gridLayout_7.addLayout(self.formLayout_5, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.label_22 = QLabel(self.page_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_22)

        self.frame_10 = QFrame(self.page_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_35 = QLabel(self.frame_10)
        self.label_35.setObjectName(u"label_35")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_35)

        self.label_36 = QLabel(self.frame_10)
        self.label_36.setObjectName(u"label_36")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_36)

        self.upUser = QLineEdit(self.frame_10)
        self.upUser.setObjectName(u"upUser")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.upUser)

        self.upPaswd = QLineEdit(self.frame_10)
        self.upPaswd.setObjectName(u"upPaswd")
        self.upPaswd.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.upPaswd)


        self.gridLayout_8.addLayout(self.formLayout_6, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_10)

        self.label_32 = QLabel(self.page_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_32)

        self.frame_11 = QFrame(self.page_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_37 = QLabel(self.frame_11)
        self.label_37.setObjectName(u"label_37")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_37)

        self.upAuthID = QLineEdit(self.frame_11)
        self.upAuthID.setObjectName(u"upAuthID")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.upAuthID)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.updateCancelBtn = QPushButton(self.frame_11)
        self.updateCancelBtn.setObjectName(u"updateCancelBtn")

        self.horizontalLayout_6.addWidget(self.updateCancelBtn)

        self.updateBtn = QPushButton(self.frame_11)
        self.updateBtn.setObjectName(u"updateBtn")

        self.horizontalLayout_6.addWidget(self.updateBtn)


        self.formLayout_7.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_6)


        self.gridLayout_9.addLayout(self.formLayout_7, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_11)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)

        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 127, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.frame_4 = QFrame(self.page_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(2)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.loginStatus = QLabel(self.frame_5)
        self.loginStatus.setObjectName(u"loginStatus")
        self.loginStatus.setFont(font1)
        self.loginStatus.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.loginStatus)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.userid = QLineEdit(self.frame_5)
        self.userid.setObjectName(u"userid")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.userid)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.password = QLineEdit(self.frame_5)
        self.password.setObjectName(u"password")
        self.password.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.password)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.loginBtn = QPushButton(self.frame_5)
        self.loginBtn.setObjectName(u"loginBtn")

        self.horizontalLayout_3.addWidget(self.loginBtn)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_3)


        self.verticalLayout_4.addLayout(self.formLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.reglinkBtn = QPushButton(self.frame_5)
        self.reglinkBtn.setObjectName(u"reglinkBtn")

        self.horizontalLayout_4.addWidget(self.reglinkBtn)

        self.updatelinkBtn = QPushButton(self.frame_5)
        self.updatelinkBtn.setObjectName(u"updatelinkBtn")

        self.horizontalLayout_4.addWidget(self.updatelinkBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addWidget(self.frame_5, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.verticalSpacer_3 = QSpacerItem(20, 127, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_7.addWidget(self.stackedWidget)


        self.gridLayout_10.addWidget(self.bgframe, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.bgLayer)


        self.retranslateUi(Authenticate)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Authenticate)
    # setupUi

    def retranslateUi(self, Authenticate):
        Authenticate.setWindowTitle(QCoreApplication.translate("Authenticate", u"Authenticate", None))
        self.imgView.setText(QCoreApplication.translate("Authenticate", u"TextLabel", None))
        self.contactBtn.setText(QCoreApplication.translate("Authenticate", u"Contact Author", None))
        self.label_7.setText(QCoreApplication.translate("Authenticate", u"Employee's Registration Form", None))
        self.regStatus.setText(QCoreApplication.translate("Authenticate", u"popup message", None))
        self.label_21.setText(QCoreApplication.translate("Authenticate", u"Employee's Details:", None))
        self.label_5.setText(QCoreApplication.translate("Authenticate", u"Firstname:", None))
        self.label_8.setText(QCoreApplication.translate("Authenticate", u"Lastname:", None))
        self.label_9.setText(QCoreApplication.translate("Authenticate", u"Gender:", None))
        self.label_10.setText(QCoreApplication.translate("Authenticate", u"Job Title:", None))
        self.label_11.setText(QCoreApplication.translate("Authenticate", u"Department:", None))
        self.label_12.setText(QCoreApplication.translate("Authenticate", u"Employment ID:", None))
        self.label_13.setText(QCoreApplication.translate("Authenticate", u"Rank:", None))
        self.label_14.setText(QCoreApplication.translate("Authenticate", u"Phone Number:", None))
        self.label_15.setText(QCoreApplication.translate("Authenticate", u"Email:", None))
        self.gender.setItemText(0, QCoreApplication.translate("Authenticate", u"Male", None))
        self.gender.setItemText(1, QCoreApplication.translate("Authenticate", u"Female", None))
        self.gender.setItemText(2, QCoreApplication.translate("Authenticate", u"Other", None))

        self.dept.setItemText(0, QCoreApplication.translate("Authenticate", u"Medical", None))
        self.dept.setItemText(1, QCoreApplication.translate("Authenticate", u"Reception", None))
        self.dept.setItemText(2, QCoreApplication.translate("Authenticate", u"Human Resource", None))
        self.dept.setItemText(3, QCoreApplication.translate("Authenticate", u"Pharmacy", None))
        self.dept.setItemText(4, QCoreApplication.translate("Authenticate", u"Laboratory", None))
        self.dept.setItemText(5, QCoreApplication.translate("Authenticate", u"Admin", None))

        self.jobtitle.setItemText(0, QCoreApplication.translate("Authenticate", u"Medical Doctor", None))
        self.jobtitle.setItemText(1, QCoreApplication.translate("Authenticate", u"Nurse", None))
        self.jobtitle.setItemText(2, QCoreApplication.translate("Authenticate", u"Receptionist", None))
        self.jobtitle.setItemText(3, QCoreApplication.translate("Authenticate", u"Pharmacist", None))
        self.jobtitle.setItemText(4, QCoreApplication.translate("Authenticate", u"Lab Scientist", None))

        self.rank.setItemText(0, QCoreApplication.translate("Authenticate", u"0", None))
        self.rank.setItemText(1, QCoreApplication.translate("Authenticate", u"1", None))
        self.rank.setItemText(2, QCoreApplication.translate("Authenticate", u"2", None))
        self.rank.setItemText(3, QCoreApplication.translate("Authenticate", u"3", None))
        self.rank.setItemText(4, QCoreApplication.translate("Authenticate", u"4", None))
        self.rank.setItemText(5, QCoreApplication.translate("Authenticate", u"5", None))
        self.rank.setItemText(6, QCoreApplication.translate("Authenticate", u"6", None))
        self.rank.setItemText(7, QCoreApplication.translate("Authenticate", u"7", None))
        self.rank.setItemText(8, QCoreApplication.translate("Authenticate", u"8", None))
        self.rank.setItemText(9, QCoreApplication.translate("Authenticate", u"9", None))

        self.label_16.setText(QCoreApplication.translate("Authenticate", u"Login Details:", None))
        self.label_17.setText(QCoreApplication.translate("Authenticate", u"Usersname:", None))
        self.label_18.setText(QCoreApplication.translate("Authenticate", u"Password:", None))
        self.label_19.setText(QCoreApplication.translate("Authenticate", u"Authorization:", None))
        self.label_20.setText(QCoreApplication.translate("Authenticate", u"Authorized ID:", None))
        self.regCancelBtn.setText(QCoreApplication.translate("Authenticate", u"Cancel", None))
        self.registerBtn.setText(QCoreApplication.translate("Authenticate", u"Register", None))
        self.label_33.setText(QCoreApplication.translate("Authenticate", u"Employee's Update Form", None))
        self.updateStatus.setText(QCoreApplication.translate("Authenticate", u"flashmsg", None))
        self.label_38.setText(QCoreApplication.translate("Authenticate", u"Employee's Details:", None))
        self.label_26.setText(QCoreApplication.translate("Authenticate", u"Job Title:", None))
        self.upJob.setItemText(0, QCoreApplication.translate("Authenticate", u"Medical Doctor", None))
        self.upJob.setItemText(1, QCoreApplication.translate("Authenticate", u"Nurse", None))
        self.upJob.setItemText(2, QCoreApplication.translate("Authenticate", u"Receptionist", None))
        self.upJob.setItemText(3, QCoreApplication.translate("Authenticate", u"Pharmacist", None))
        self.upJob.setItemText(4, QCoreApplication.translate("Authenticate", u"Lab Scientist", None))

        self.label_27.setText(QCoreApplication.translate("Authenticate", u"Department:", None))
        self.upDept.setItemText(0, QCoreApplication.translate("Authenticate", u"Medical", None))
        self.upDept.setItemText(1, QCoreApplication.translate("Authenticate", u"Reception", None))
        self.upDept.setItemText(2, QCoreApplication.translate("Authenticate", u"Human Resource", None))
        self.upDept.setItemText(3, QCoreApplication.translate("Authenticate", u"Pharmacy", None))
        self.upDept.setItemText(4, QCoreApplication.translate("Authenticate", u"Laboratory", None))
        self.upDept.setItemText(5, QCoreApplication.translate("Authenticate", u"Admin", None))

        self.label_28.setText(QCoreApplication.translate("Authenticate", u"Employment ID:", None))
        self.label_29.setText(QCoreApplication.translate("Authenticate", u"Rank:", None))
        self.upRank.setItemText(0, QCoreApplication.translate("Authenticate", u"0", None))
        self.upRank.setItemText(1, QCoreApplication.translate("Authenticate", u"1", None))
        self.upRank.setItemText(2, QCoreApplication.translate("Authenticate", u"2", None))
        self.upRank.setItemText(3, QCoreApplication.translate("Authenticate", u"3", None))
        self.upRank.setItemText(4, QCoreApplication.translate("Authenticate", u"4", None))
        self.upRank.setItemText(5, QCoreApplication.translate("Authenticate", u"5", None))
        self.upRank.setItemText(6, QCoreApplication.translate("Authenticate", u"6", None))
        self.upRank.setItemText(7, QCoreApplication.translate("Authenticate", u"7", None))
        self.upRank.setItemText(8, QCoreApplication.translate("Authenticate", u"8", None))
        self.upRank.setItemText(9, QCoreApplication.translate("Authenticate", u"9", None))

        self.label_30.setText(QCoreApplication.translate("Authenticate", u"Phone Number:", None))
        self.label_31.setText(QCoreApplication.translate("Authenticate", u"Email:", None))
        self.label_22.setText(QCoreApplication.translate("Authenticate", u"Login Details:", None))
        self.label_35.setText(QCoreApplication.translate("Authenticate", u"Usersname:", None))
        self.label_36.setText(QCoreApplication.translate("Authenticate", u"Password:", None))
        self.label_32.setText(QCoreApplication.translate("Authenticate", u"Authorization:", None))
        self.label_37.setText(QCoreApplication.translate("Authenticate", u"Authorized ID:", None))
        self.updateCancelBtn.setText(QCoreApplication.translate("Authenticate", u"Cancel", None))
        self.updateBtn.setText(QCoreApplication.translate("Authenticate", u"Update", None))
        self.label_2.setText(QCoreApplication.translate("Authenticate", u"Login", None))
        self.loginStatus.setText(QCoreApplication.translate("Authenticate", u"popup message", None))
        self.label_3.setText(QCoreApplication.translate("Authenticate", u"Username:", None))
        self.userid.setPlaceholderText(QCoreApplication.translate("Authenticate", u"Usersname", None))
        self.label_4.setText(QCoreApplication.translate("Authenticate", u"Password:", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Authenticate", u"Password", None))
        self.loginBtn.setText(QCoreApplication.translate("Authenticate", u"Login", None))
        self.reglinkBtn.setText(QCoreApplication.translate("Authenticate", u"Register", None))
        self.updatelinkBtn.setText(QCoreApplication.translate("Authenticate", u"Forgot Password", None))
    # retranslateUi

