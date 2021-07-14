# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Patient.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Patient(object):
    def setupUi(self, Patient):
        if not Patient.objectName():
            Patient.setObjectName(u"Patient")
        Patient.setWindowModality(Qt.ApplicationModal)
        Patient.resize(827, 684)
        Patient.setMouseTracking(True)
        Patient.setTabletTracking(True)
        Patient.setFocusPolicy(Qt.StrongFocus)
        Patient.setWindowOpacity(0.970000000000000)
        Patient.setAutoFillBackground(True)
        Patient.setModal(True)
        self.gridLayout = QGridLayout(Patient)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_2 = QFrame(Patient)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_10.setContentsMargins(3, 0, 8, 0)
        self.logo = QLabel(self.frame_2)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 45))
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
        self.label_29 = QLabel(self.frame_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAutoFillBackground(False)
        self.label_29.setWordWrap(True)
        self.label_29.setMargin(7)

        self.gridLayout_13.addWidget(self.label_29, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, 1, -1)
        self.minBtn = QPushButton(self.frame_2)
        self.minBtn.setObjectName(u"minBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minBtn.sizePolicy().hasHeightForWidth())
        self.minBtn.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(11)
        self.minBtn.setFont(font1)
        self.minBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minBtn.setMouseTracking(True)
        self.minBtn.setTabletTracking(True)
        self.minBtn.setAutoFillBackground(False)
        self.minBtn.setAutoDefault(False)
        self.minBtn.setFlat(False)

        self.horizontalLayout_11.addWidget(self.minBtn)

        self.exitBtn = QPushButton(self.frame_2)
        self.exitBtn.setObjectName(u"exitBtn")
        sizePolicy1.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy1)
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


        self.gridLayout_13.addLayout(self.horizontalLayout_11, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(405, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_13)


        self.horizontalLayout_7.addWidget(self.frame_2)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.bgLayer = QFrame(Patient)
        self.bgLayer.setObjectName(u"bgLayer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.bgLayer.sizePolicy().hasHeightForWidth())
        self.bgLayer.setSizePolicy(sizePolicy2)
        self.bgLayer.setAutoFillBackground(False)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.bgLayer)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(16)
        font2.setUnderline(True)
        self.label.setFont(font2)
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.psearchBtn = QPushButton(self.bgLayer)
        self.psearchBtn.setObjectName(u"psearchBtn")
        self.psearchBtn.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(100)
        sizePolicy4.setVerticalStretch(150)
        sizePolicy4.setHeightForWidth(self.psearchBtn.sizePolicy().hasHeightForWidth())
        self.psearchBtn.setSizePolicy(sizePolicy4)
        self.psearchBtn.setMaximumSize(QSize(100, 150))
        self.psearchBtn.setStyleSheet(u"background-color: rgb(53, 0, 159);")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.psearchBtn)

        self.input = QLineEdit(self.bgLayer)
        self.input.setObjectName(u"input")
        sizePolicy3.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy3)
        self.input.setMinimumSize(QSize(0, 30))
        self.input.setAutoFillBackground(False)
        self.input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(6, 6, 6);")
        self.input.setAlignment(Qt.AlignCenter)
        self.input.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.input)


        self.gridLayout_2.addLayout(self.formLayout_2, 1, 0, 1, 2)

        self.frame_3 = QFrame(self.bgLayer)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy5)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy5.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy5)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 22, -1, 13)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(5)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.fname = QLabel(self.groupBox)
        self.fname.setObjectName(u"fname")
        sizePolicy.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy)
        self.fname.setMinimumSize(QSize(0, 0))
        self.fname.setAutoFillBackground(True)
        self.fname.setWordWrap(False)
        self.fname.setMargin(6)

        self.horizontalLayout_6.addWidget(self.fname)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy6.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy6)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setMargin(5)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lname = QLabel(self.groupBox)
        self.lname.setObjectName(u"lname")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.lname.sizePolicy().hasHeightForWidth())
        self.lname.setSizePolicy(sizePolicy7)
        self.lname.setMinimumSize(QSize(0, 0))
        self.lname.setAutoFillBackground(True)
        self.lname.setWordWrap(False)
        self.lname.setMargin(6)

        self.horizontalLayout_8.addWidget(self.lname)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pnumber = QLabel(self.groupBox)
        self.pnumber.setObjectName(u"pnumber")
        self.pnumber.setMinimumSize(QSize(0, 25))
        self.pnumber.setAutoFillBackground(True)
        self.pnumber.setWordWrap(False)
        self.pnumber.setMargin(6)

        self.horizontalLayout_9.addWidget(self.pnumber)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_9)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        sizePolicy6.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy6)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pclass = QLabel(self.groupBox)
        self.pclass.setObjectName(u"pclass")
        self.pclass.setMinimumSize(QSize(0, 25))
        self.pclass.setAutoFillBackground(True)
        self.pclass.setWordWrap(False)
        self.pclass.setMargin(6)

        self.horizontalLayout_12.addWidget(self.pclass)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_12)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy6.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy6)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setMargin(5)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.plreview = QLabel(self.groupBox)
        self.plreview.setObjectName(u"plreview")
        sizePolicy7.setHeightForWidth(self.plreview.sizePolicy().hasHeightForWidth())
        self.plreview.setSizePolicy(sizePolicy7)
        self.plreview.setMinimumSize(QSize(0, 25))
        self.plreview.setAutoFillBackground(True)
        self.plreview.setWordWrap(False)
        self.plreview.setMargin(6)

        self.horizontalLayout_13.addWidget(self.plreview)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_13)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy6.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy6)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setMargin(5)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.lastdate = QDateEdit(self.groupBox)
        self.lastdate.setObjectName(u"lastdate")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.lastdate.sizePolicy().hasHeightForWidth())
        self.lastdate.setSizePolicy(sizePolicy8)
        self.lastdate.setMinimumSize(QSize(0, 25))
        self.lastdate.setReadOnly(True)
        self.lastdate.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.lastdate.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.lastdate.setCalendarPopup(False)
        self.lastdate.setTimeSpec(Qt.LocalTime)
        self.lastdate.setDate(QDate(2021, 3, 19))

        self.horizontalLayout_4.addWidget(self.lastdate)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.recordBtn = QPushButton(self.frame_4)
        self.recordBtn.setObjectName(u"recordBtn")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.recordBtn.sizePolicy().hasHeightForWidth())
        self.recordBtn.setSizePolicy(sizePolicy9)
        font3 = QFont()
        font3.setFamily(u"MS UI Gothic")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.recordBtn.setFont(font3)

        self.horizontalLayout.addWidget(self.recordBtn)

        self.pnewBtn = QPushButton(self.frame_4)
        self.pnewBtn.setObjectName(u"pnewBtn")
        sizePolicy9.setHeightForWidth(self.pnewBtn.sizePolicy().hasHeightForWidth())
        self.pnewBtn.setSizePolicy(sizePolicy9)
        self.pnewBtn.setFont(font3)

        self.horizontalLayout.addWidget(self.pnewBtn)

        self.bookBtn = QPushButton(self.frame_4)
        self.bookBtn.setObjectName(u"bookBtn")
        sizePolicy9.setHeightForWidth(self.bookBtn.sizePolicy().hasHeightForWidth())
        self.bookBtn.setSizePolicy(sizePolicy9)
        self.bookBtn.setFont(font3)

        self.horizontalLayout.addWidget(self.bookBtn)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.gridLayout_2.addWidget(self.frame_3, 4, 0, 1, 2)

        self.searchLabel = QLabel(self.bgLayer)
        self.searchLabel.setObjectName(u"searchLabel")
        self.searchLabel.setMinimumSize(QSize(0, 18))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Symbol")
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setItalic(True)
        font4.setWeight(75)
        self.searchLabel.setFont(font4)

        self.gridLayout_2.addWidget(self.searchLabel, 3, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pclose = QPushButton(self.bgLayer)
        self.pclose.setObjectName(u"pclose")
        self.pclose.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setFamily(u"Comic Sans MS")
        font5.setPointSize(9)
        self.pclose.setFont(font5)
        self.pclose.setAutoFillBackground(False)
        self.pclose.setStyleSheet(u"background-color: rgb(69, 69, 69);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.pclose)

        self.send = QPushButton(self.bgLayer)
        self.send.setObjectName(u"send")
        self.send.setMinimumSize(QSize(0, 30))
        self.send.setFont(font5)
        self.send.setAutoFillBackground(False)
        self.send.setStyleSheet(u"background-color: rgb(103, 103, 12);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.send)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 5, 0, 1, 2)


        self.gridLayout.addWidget(self.bgLayer, 1, 0, 1, 1)


        self.retranslateUi(Patient)
        self.pclose.clicked.connect(Patient.hide)

        QMetaObject.connectSlotsByName(Patient)
    # setupUi

    def retranslateUi(self, Patient):
        Patient.setWindowTitle(QCoreApplication.translate("Patient", u"Find Patient", None))
        self.logo.setText("")
        self.label_29.setText(QCoreApplication.translate("Patient", u"Patient", None))
        self.minBtn.setText(QCoreApplication.translate("Patient", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("Patient", u"X", None))
        self.label.setText(QCoreApplication.translate("Patient", u"Find Patient's Record", None))
        self.psearchBtn.setText(QCoreApplication.translate("Patient", u"SEARCH", None))
        self.input.setPlaceholderText(QCoreApplication.translate("Patient", u"Please insert name or card number of patient", None))
        self.groupBox.setTitle(QCoreApplication.translate("Patient", u"Patient Details:", None))
        self.label_2.setText(QCoreApplication.translate("Patient", u"First Name:", None))
        self.fname.setText("")
        self.label_5.setText(QCoreApplication.translate("Patient", u"Last Name:", None))
        self.lname.setText("")
        self.label_4.setText(QCoreApplication.translate("Patient", u"Patient Number:", None))
        self.pnumber.setText("")
        self.label_8.setText(QCoreApplication.translate("Patient", u"Patient Class: ", None))
        self.pclass.setText("")
        self.label_7.setText(QCoreApplication.translate("Patient", u"Last Clerked by:", None))
        self.plreview.setText("")
        self.label_6.setText(QCoreApplication.translate("Patient", u"Date of Last Visit:", None))
        self.lastdate.setDisplayFormat(QCoreApplication.translate("Patient", u"ddd, dd/MMM/yyyy", None))
        self.recordBtn.setText(QCoreApplication.translate("Patient", u"Record", None))
        self.pnewBtn.setText(QCoreApplication.translate("Patient", u"New Patient", None))
        self.bookBtn.setText(QCoreApplication.translate("Patient", u"Book Appointment", None))
        self.searchLabel.setText("")
        self.pclose.setText(QCoreApplication.translate("Patient", u"Close", None))
        self.send.setText(QCoreApplication.translate("Patient", u"Send File", None))
    # retranslateUi

