# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FindPatient.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FindPatient(object):
    def setupUi(self, FindPatient):
        if not FindPatient.objectName():
            FindPatient.setObjectName(u"FindPatient")
        FindPatient.setWindowModality(Qt.ApplicationModal)
        FindPatient.resize(757, 532)
        FindPatient.setMouseTracking(True)
        FindPatient.setTabletTracking(True)
        FindPatient.setFocusPolicy(Qt.StrongFocus)
        FindPatient.setWindowOpacity(0.970000000000000)
        FindPatient.setAutoFillBackground(True)
        FindPatient.setModal(True)
        self.gridLayout = QGridLayout(FindPatient)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_2 = QFrame(FindPatient)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_10.setContentsMargins(3, 0, 8, 0)
        self.logo = QLabel(self.frame_2)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(45, 45))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(6)
        self.logo.setFont(font)
        self.logo.setMouseTracking(True)
        self.logo.setTabletTracking(True)
        self.logo.setAutoFillBackground(False)
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.logo)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, 1, -1)
        self.miniBtn = QPushButton(self.frame_2)
        self.miniBtn.setObjectName(u"miniBtn")
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(11)
        self.miniBtn.setFont(font1)
        self.miniBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.miniBtn.setMouseTracking(True)
        self.miniBtn.setTabletTracking(True)
        self.miniBtn.setAutoFillBackground(False)
        self.miniBtn.setAutoDefault(False)
        self.miniBtn.setFlat(False)

        self.horizontalLayout_11.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(self.frame_2)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMaximumSize(QSize(16777215, 16777215))
        self.exitBtn.setFont(font1)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setMouseTracking(True)
        self.exitBtn.setTabletTracking(True)
        self.exitBtn.setLayoutDirection(Qt.LeftToRight)
        self.exitBtn.setAutoFillBackground(False)
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setFlat(False)

        self.horizontalLayout_11.addWidget(self.exitBtn)


        self.gridLayout_13.addLayout(self.horizontalLayout_11, 0, 1, 1, 1)

        self.label_29 = QLabel(self.frame_2)
        self.label_29.setObjectName(u"label_29")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setAutoFillBackground(False)
        self.label_29.setWordWrap(True)
        self.label_29.setMargin(7)

        self.gridLayout_13.addWidget(self.label_29, 0, 0, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_13)


        self.horizontalLayout_7.addWidget(self.frame_2)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.bgLayer = QFrame(FindPatient)
        self.bgLayer.setObjectName(u"bgLayer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bgLayer.sizePolicy().hasHeightForWidth())
        self.bgLayer.setSizePolicy(sizePolicy1)
        self.bgLayer.setAutoFillBackground(False)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.searchLabel = QLabel(self.bgLayer)
        self.searchLabel.setObjectName(u"searchLabel")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Symbol")
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.searchLabel.setFont(font2)

        self.gridLayout_2.addWidget(self.searchLabel, 3, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.sendBtn = QPushButton(self.bgLayer)
        self.sendBtn.setObjectName(u"sendBtn")
        font3 = QFont()
        font3.setFamily(u"Comic Sans MS")
        font3.setPointSize(9)
        self.sendBtn.setFont(font3)
        self.sendBtn.setAutoFillBackground(False)
        self.sendBtn.setStyleSheet(u"background-color: rgb(103, 103, 12);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.sendBtn)

        self.horizontalSpacer_2 = QSpacerItem(400, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.closeBtn = QPushButton(self.bgLayer)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setFont(font3)
        self.closeBtn.setAutoFillBackground(False)
        self.closeBtn.setStyleSheet(u"background-color: rgb(69, 69, 69);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.closeBtn)

        self.logout = QPushButton(self.bgLayer)
        self.logout.setObjectName(u"logout")
        self.logout.setFont(font3)
        self.logout.setAutoFillBackground(False)
        self.logout.setStyleSheet(u"background-color: rgb(69, 69, 69);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.logout)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 5, 0, 1, 2)

        self.label = QLabel(self.bgLayer)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(10)
        font4.setUnderline(True)
        self.label.setFont(font4)
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.searchBtn = QPushButton(self.bgLayer)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setEnabled(True)
        self.searchBtn.setMaximumSize(QSize(100, 150))
        self.searchBtn.setStyleSheet(u"background-color: rgb(53, 0, 159);")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.searchBtn)

        self.input = QLineEdit(self.bgLayer)
        self.input.setObjectName(u"input")
        self.input.setAutoFillBackground(False)
        self.input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(6, 6, 6);")
        self.input.setAlignment(Qt.AlignCenter)
        self.input.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.input)


        self.gridLayout_2.addLayout(self.formLayout_2, 1, 0, 1, 2)

        self.frame_3 = QFrame(self.bgLayer)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result = QGroupBox(self.frame_3)
        self.result.setObjectName(u"result")
        self.horizontalLayout_14 = QHBoxLayout(self.result)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 22, -1, 13)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 7, -1, -1)
        self.label_2 = QLabel(self.result)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(5)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.fname = QLabel(self.result)
        self.fname.setObjectName(u"fname")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy2)
        self.fname.setAutoFillBackground(True)
        self.fname.setWordWrap(False)
        self.fname.setMargin(2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.label_4 = QLabel(self.result)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(5)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.pnumber = QLabel(self.result)
        self.pnumber.setObjectName(u"pnumber")
        sizePolicy2.setHeightForWidth(self.pnumber.sizePolicy().hasHeightForWidth())
        self.pnumber.setSizePolicy(sizePolicy2)
        self.pnumber.setAutoFillBackground(True)
        self.pnumber.setWordWrap(False)
        self.pnumber.setMargin(2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pnumber)

        self.label_7 = QLabel(self.result)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setMargin(5)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.plreview = QLabel(self.result)
        self.plreview.setObjectName(u"plreview")
        sizePolicy2.setHeightForWidth(self.plreview.sizePolicy().hasHeightForWidth())
        self.plreview.setSizePolicy(sizePolicy2)
        self.plreview.setAutoFillBackground(True)
        self.plreview.setWordWrap(False)
        self.plreview.setMargin(2)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.plreview)


        self.horizontalLayout_14.addLayout(self.formLayout)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(-1, 7, -1, -1)
        self.label_5 = QLabel(self.result)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setMargin(5)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.lname = QLabel(self.result)
        self.lname.setObjectName(u"lname")
        sizePolicy2.setHeightForWidth(self.lname.sizePolicy().hasHeightForWidth())
        self.lname.setSizePolicy(sizePolicy2)
        self.lname.setAutoFillBackground(True)
        self.lname.setWordWrap(False)
        self.lname.setMargin(2)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lname)

        self.label_8 = QLabel(self.result)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setMargin(5)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.pclass = QLabel(self.result)
        self.pclass.setObjectName(u"pclass")
        sizePolicy2.setHeightForWidth(self.pclass.sizePolicy().hasHeightForWidth())
        self.pclass.setSizePolicy(sizePolicy2)
        self.pclass.setAutoFillBackground(True)
        self.pclass.setWordWrap(False)
        self.pclass.setMargin(2)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.pclass)

        self.label_6 = QLabel(self.result)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setMargin(5)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lastdate_2 = QDateEdit(self.result)
        self.lastdate_2.setObjectName(u"lastdate_2")
        sizePolicy2.setHeightForWidth(self.lastdate_2.sizePolicy().hasHeightForWidth())
        self.lastdate_2.setSizePolicy(sizePolicy2)
        self.lastdate_2.setReadOnly(True)
        self.lastdate_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.lastdate_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.lastdate_2.setCalendarPopup(False)
        self.lastdate_2.setTimeSpec(Qt.LocalTime)
        self.lastdate_2.setDate(QDate(2021, 3, 19))

        self.horizontalLayout_2.addWidget(self.lastdate_2)

        self.label_3 = QLabel(self.result)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lastdate = QDateEdit(self.result)
        self.lastdate.setObjectName(u"lastdate")
        sizePolicy2.setHeightForWidth(self.lastdate.sizePolicy().hasHeightForWidth())
        self.lastdate.setSizePolicy(sizePolicy2)
        self.lastdate.setReadOnly(True)
        self.lastdate.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.lastdate.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.lastdate.setCalendarPopup(False)
        self.lastdate.setTimeSpec(Qt.LocalTime)
        self.lastdate.setDate(QDate(2021, 3, 19))

        self.horizontalLayout_2.addWidget(self.lastdate)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.horizontalLayout_14.addLayout(self.formLayout_3)


        self.verticalLayout.addWidget(self.result)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.patientBtn = QPushButton(self.frame_4)
        self.patientBtn.setObjectName(u"patientBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.patientBtn.sizePolicy().hasHeightForWidth())
        self.patientBtn.setSizePolicy(sizePolicy3)
        font5 = QFont()
        font5.setFamily(u"MS UI Gothic")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.patientBtn.setFont(font5)

        self.horizontalLayout.addWidget(self.patientBtn)

        self.newBtn = QPushButton(self.frame_4)
        self.newBtn.setObjectName(u"newBtn")
        sizePolicy3.setHeightForWidth(self.newBtn.sizePolicy().hasHeightForWidth())
        self.newBtn.setSizePolicy(sizePolicy3)
        self.newBtn.setFont(font5)

        self.horizontalLayout.addWidget(self.newBtn)

        self.bookBtn = QPushButton(self.frame_4)
        self.bookBtn.setObjectName(u"bookBtn")
        sizePolicy3.setHeightForWidth(self.bookBtn.sizePolicy().hasHeightForWidth())
        self.bookBtn.setSizePolicy(sizePolicy3)
        self.bookBtn.setFont(font5)

        self.horizontalLayout.addWidget(self.bookBtn)


        self.verticalLayout.addWidget(self.frame_4)


        self.gridLayout_2.addWidget(self.frame_3, 4, 0, 1, 2)

        self.progressBar = QProgressBar(self.bgLayer)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout_2.addWidget(self.progressBar, 6, 0, 1, 2)


        self.gridLayout.addWidget(self.bgLayer, 1, 0, 1, 1)


        self.retranslateUi(FindPatient)

        QMetaObject.connectSlotsByName(FindPatient)
    # setupUi

    def retranslateUi(self, FindPatient):
        FindPatient.setWindowTitle(QCoreApplication.translate("FindPatient", u"Find Patient", None))
        self.logo.setText("")
        self.miniBtn.setText(QCoreApplication.translate("FindPatient", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("FindPatient", u"X", None))
        self.label_29.setText(QCoreApplication.translate("FindPatient", u"Find Patient", None))
        self.searchLabel.setText("")
        self.sendBtn.setText(QCoreApplication.translate("FindPatient", u"Send File", None))
        self.closeBtn.setText(QCoreApplication.translate("FindPatient", u"Close", None))
        self.logout.setText(QCoreApplication.translate("FindPatient", u"Log Out", None))
        self.label.setText(QCoreApplication.translate("FindPatient", u"Find Patient's Record", None))
        self.searchBtn.setText(QCoreApplication.translate("FindPatient", u"SEARCH", None))
        self.input.setPlaceholderText(QCoreApplication.translate("FindPatient", u"Please insert name or card number of patient", None))
        self.result.setTitle(QCoreApplication.translate("FindPatient", u"Patient Details:", None))
        self.label_2.setText(QCoreApplication.translate("FindPatient", u"First Name:", None))
        self.fname.setText("")
        self.label_4.setText(QCoreApplication.translate("FindPatient", u"Patient Number:", None))
        self.pnumber.setText("")
        self.label_7.setText(QCoreApplication.translate("FindPatient", u"Last Clerked by:", None))
        self.plreview.setText("")
        self.label_5.setText(QCoreApplication.translate("FindPatient", u"Last Name:", None))
        self.lname.setText("")
        self.label_8.setText(QCoreApplication.translate("FindPatient", u"Patient Class: ", None))
        self.pclass.setText("")
        self.label_6.setText(QCoreApplication.translate("FindPatient", u"Reg Date:", None))
        self.lastdate_2.setDisplayFormat(QCoreApplication.translate("FindPatient", u"ddd, dd/MMM/yyyy", None))
        self.label_3.setText(QCoreApplication.translate("FindPatient", u"Date of Last Visit:", None))
        self.lastdate.setDisplayFormat(QCoreApplication.translate("FindPatient", u"ddd, dd/MMM/yyyy", None))
        self.patientBtn.setText(QCoreApplication.translate("FindPatient", u"View", None))
        self.newBtn.setText(QCoreApplication.translate("FindPatient", u"New Patient", None))
        self.bookBtn.setText(QCoreApplication.translate("FindPatient", u"Book Appointment", None))
    # retranslateUi

