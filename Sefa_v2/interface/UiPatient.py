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
        Patient.resize(734, 505)
        Patient.setMouseTracking(True)
        Patient.setTabletTracking(True)
        Patient.setFocusPolicy(Qt.StrongFocus)
        self.centralwidget = QWidget(Patient)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 2, 0)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")

        self.horizontalLayout_4.addWidget(self.logo)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.miniBtn = QPushButton(self.frame)
        self.miniBtn.setObjectName(u"miniBtn")

        self.horizontalLayout_4.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(self.frame)
        self.exitBtn.setObjectName(u"exitBtn")

        self.horizontalLayout_4.addWidget(self.exitBtn)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.bgLayer = QFrame(self.centralwidget)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bgLayer.sizePolicy().hasHeightForWidth())
        self.bgLayer.setSizePolicy(sizePolicy)
        self.bgLayer.setMouseTracking(True)
        self.bgLayer.setTabletTracking(True)
        self.bgLayer.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.bgLayer.setAutoFillBackground(True)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.bgLayer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.bgLayer)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.profileBtn = QPushButton(self.groupBox)
        self.profileBtn.setObjectName(u"profileBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.profileBtn.sizePolicy().hasHeightForWidth())
        self.profileBtn.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"MS UI Gothic")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        font1.setKerning(False)
        self.profileBtn.setFont(font1)
        self.profileBtn.setMouseTracking(True)
        self.profileBtn.setTabletTracking(True)
        self.profileBtn.setAutoFillBackground(True)

        self.horizontalLayout_5.addWidget(self.profileBtn)

        self.clinicBtn = QPushButton(self.groupBox)
        self.clinicBtn.setObjectName(u"clinicBtn")
        sizePolicy1.setHeightForWidth(self.clinicBtn.sizePolicy().hasHeightForWidth())
        self.clinicBtn.setSizePolicy(sizePolicy1)
        self.clinicBtn.setFont(font1)

        self.horizontalLayout_5.addWidget(self.clinicBtn)

        self.pharmacyBtn = QPushButton(self.groupBox)
        self.pharmacyBtn.setObjectName(u"pharmacyBtn")
        sizePolicy1.setHeightForWidth(self.pharmacyBtn.sizePolicy().hasHeightForWidth())
        self.pharmacyBtn.setSizePolicy(sizePolicy1)
        self.pharmacyBtn.setFont(font1)

        self.horizontalLayout_5.addWidget(self.pharmacyBtn)

        self.labBtn = QPushButton(self.groupBox)
        self.labBtn.setObjectName(u"labBtn")
        sizePolicy1.setHeightForWidth(self.labBtn.sizePolicy().hasHeightForWidth())
        self.labBtn.setSizePolicy(sizePolicy1)
        self.labBtn.setFont(font1)

        self.horizontalLayout_5.addWidget(self.labBtn)

        self.accountBtn = QPushButton(self.groupBox)
        self.accountBtn.setObjectName(u"accountBtn")
        sizePolicy1.setHeightForWidth(self.accountBtn.sizePolicy().hasHeightForWidth())
        self.accountBtn.setSizePolicy(sizePolicy1)
        self.accountBtn.setFont(font1)

        self.horizontalLayout_5.addWidget(self.accountBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 4, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.bgLayer)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.fullname = QLabel(self.bgLayer)
        self.fullname.setObjectName(u"fullname")
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(8)
        self.fullname.setFont(font3)

        self.horizontalLayout_6.addWidget(self.fullname)


        self.gridLayout_3.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.createApptBtn = QPushButton(self.bgLayer)
        self.createApptBtn.setObjectName(u"createApptBtn")
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(10)
        font4.setKerning(False)
        self.createApptBtn.setFont(font4)

        self.horizontalLayout_2.addWidget(self.createApptBtn)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.closeBtn = QPushButton(self.bgLayer)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setFont(font4)

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout_3.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.label = QLabel(self.bgLayer)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setFamily(u"Tahoma")
        font5.setPointSize(12)
        font5.setUnderline(True)
        font5.setKerning(False)
        self.label.setFont(font5)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(2)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.bgLayer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_2)

        self.cardNum = QLabel(self.bgLayer)
        self.cardNum.setObjectName(u"cardNum")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cardNum.sizePolicy().hasHeightForWidth())
        self.cardNum.setSizePolicy(sizePolicy2)
        self.cardNum.setFont(font3)

        self.horizontalLayout_8.addWidget(self.cardNum)


        self.gridLayout_3.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 1, 0, 1, 2)

        Patient.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Patient)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 734, 16))
        Patient.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Patient)
        self.statusbar.setObjectName(u"statusbar")
        Patient.setStatusBar(self.statusbar)

        self.retranslateUi(Patient)

        QMetaObject.connectSlotsByName(Patient)
    # setupUi

    def retranslateUi(self, Patient):
        Patient.setWindowTitle(QCoreApplication.translate("Patient", u"Patient Portal", None))
        self.logo.setText(QCoreApplication.translate("Patient", u"logo", None))
        self.label_4.setText(QCoreApplication.translate("Patient", u"Patient's Records", None))
        self.miniBtn.setText(QCoreApplication.translate("Patient", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("Patient", u"X", None))
        self.groupBox.setTitle(QCoreApplication.translate("Patient", u"Activities", None))
        self.profileBtn.setText(QCoreApplication.translate("Patient", u"Profile", None))
        self.clinicBtn.setText(QCoreApplication.translate("Patient", u"Clinic", None))
        self.pharmacyBtn.setText(QCoreApplication.translate("Patient", u"Pharmacy", None))
        self.labBtn.setText(QCoreApplication.translate("Patient", u"Lab", None))
        self.accountBtn.setText(QCoreApplication.translate("Patient", u"Account", None))
        self.label_3.setText(QCoreApplication.translate("Patient", u"Patient's Name:", None))
        self.fullname.setText("")
        self.createApptBtn.setText(QCoreApplication.translate("Patient", u"Create Appointment", None))
        self.closeBtn.setText(QCoreApplication.translate("Patient", u"Close", None))
        self.label.setText(QCoreApplication.translate("Patient", u"Patient's Records", None))
        self.label_2.setText(QCoreApplication.translate("Patient", u"Card Number: ", None))
        self.cardNum.setText(QCoreApplication.translate("Patient", u"0000000000", None))
    # retranslateUi

