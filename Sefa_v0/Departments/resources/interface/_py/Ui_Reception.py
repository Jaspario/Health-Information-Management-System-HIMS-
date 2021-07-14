# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Reception.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Reception(object):
    def setupUi(self, Reception):
        if not Reception.objectName():
            Reception.setObjectName(u"Reception")
        Reception.resize(1078, 640)
        Reception.setMouseTracking(True)
        Reception.setTabletTracking(True)
        Reception.setFocusPolicy(Qt.StrongFocus)
        self.centralwidget = QWidget(Reception)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_10.setContentsMargins(3, 0, 8, 0)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 45))
        self.logo.setMaximumSize(QSize(45, 45))
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.logo)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_13.addWidget(self.label_29, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, 1, -1)
        self.minBtn = QPushButton(self.frame)
        self.minBtn.setObjectName(u"minBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minBtn.sizePolicy().hasHeightForWidth())
        self.minBtn.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(11)
        font.setKerning(False)
        self.minBtn.setFont(font)
        self.minBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minBtn.setMouseTracking(True)
        self.minBtn.setTabletTracking(True)
        self.minBtn.setAutoFillBackground(False)
        self.minBtn.setAutoDefault(False)
        self.minBtn.setFlat(False)

        self.horizontalLayout_11.addWidget(self.minBtn)

        self.exitBtn = QPushButton(self.frame)
        self.exitBtn.setObjectName(u"exitBtn")
        sizePolicy1.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy1)
        self.exitBtn.setMaximumSize(QSize(16777215, 16777215))
        self.exitBtn.setFont(font)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setMouseTracking(True)
        self.exitBtn.setTabletTracking(True)
        self.exitBtn.setLayoutDirection(Qt.LeftToRight)
        self.exitBtn.setAutoFillBackground(False)
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setFlat(False)

        self.horizontalLayout_11.addWidget(self.exitBtn)


        self.gridLayout_13.addLayout(self.horizontalLayout_11, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(430, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_13)


        self.horizontalLayout_7.addWidget(self.frame)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.rbgLayer = QFrame(self.centralwidget)
        self.rbgLayer.setObjectName(u"rbgLayer")
        self.rbgLayer.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rbgLayer.sizePolicy().hasHeightForWidth())
        self.rbgLayer.setSizePolicy(sizePolicy2)
        self.rbgLayer.setMouseTracking(True)
        self.rbgLayer.setTabletTracking(True)
        self.rbgLayer.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.rbgLayer.setAutoFillBackground(True)
        self.rbgLayer.setFrameShape(QFrame.Box)
        self.rbgLayer.setFrameShadow(QFrame.Raised)
        self.rbgLayer.setLineWidth(2)
        self.rbgLayer.setMidLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.rbgLayer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.rbgLayer)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setWeight(50)
        font1.setKerning(False)
        self.groupBox.setFont(font1)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.patientBtn = QPushButton(self.groupBox)
        self.patientBtn.setObjectName(u"patientBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.patientBtn.sizePolicy().hasHeightForWidth())
        self.patientBtn.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamily(u"MS UI Gothic")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(False)
        self.patientBtn.setFont(font2)
        self.patientBtn.setMouseTracking(True)
        self.patientBtn.setTabletTracking(True)
        self.patientBtn.setAutoFillBackground(True)

        self.horizontalLayout_5.addWidget(self.patientBtn)

        self.clinicBtn = QPushButton(self.groupBox)
        self.clinicBtn.setObjectName(u"clinicBtn")
        sizePolicy3.setHeightForWidth(self.clinicBtn.sizePolicy().hasHeightForWidth())
        self.clinicBtn.setSizePolicy(sizePolicy3)
        self.clinicBtn.setFont(font2)

        self.horizontalLayout_5.addWidget(self.clinicBtn)

        self.pharmacyBtn = QPushButton(self.groupBox)
        self.pharmacyBtn.setObjectName(u"pharmacyBtn")
        sizePolicy3.setHeightForWidth(self.pharmacyBtn.sizePolicy().hasHeightForWidth())
        self.pharmacyBtn.setSizePolicy(sizePolicy3)
        self.pharmacyBtn.setFont(font2)

        self.horizontalLayout_5.addWidget(self.pharmacyBtn)

        self.labBtn = QPushButton(self.groupBox)
        self.labBtn.setObjectName(u"labBtn")
        sizePolicy3.setHeightForWidth(self.labBtn.sizePolicy().hasHeightForWidth())
        self.labBtn.setSizePolicy(sizePolicy3)
        self.labBtn.setFont(font2)

        self.horizontalLayout_5.addWidget(self.labBtn)

        self.accountBtn = QPushButton(self.groupBox)
        self.accountBtn.setObjectName(u"accountBtn")
        sizePolicy3.setHeightForWidth(self.accountBtn.sizePolicy().hasHeightForWidth())
        self.accountBtn.setSizePolicy(sizePolicy3)
        self.accountBtn.setFont(font2)

        self.horizontalLayout_5.addWidget(self.accountBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)

        self.label = QLabel(self.rbgLayer)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(18)
        font3.setUnderline(True)
        font3.setKerning(False)
        self.label.setFont(font3)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(2)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.createAptBtn = QPushButton(self.rbgLayer)
        self.createAptBtn.setObjectName(u"createAptBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.createAptBtn.sizePolicy().hasHeightForWidth())
        self.createAptBtn.setSizePolicy(sizePolicy4)
        self.createAptBtn.setMinimumSize(QSize(0, 50))
        self.createAptBtn.setMaximumSize(QSize(16777215, 50))
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(10)
        font4.setKerning(False)
        self.createAptBtn.setFont(font4)

        self.horizontalLayout_2.addWidget(self.createAptBtn)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.horizontalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.repLogOut = QPushButton(self.rbgLayer)
        self.repLogOut.setObjectName(u"repLogOut")
        self.repLogOut.setMaximumSize(QSize(16777215, 50))
        self.repLogOut.setFont(font4)

        self.horizontalLayout_3.addWidget(self.repLogOut)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 23, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.rbgLayer, 1, 0, 1, 1)

        Reception.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Reception)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1078, 16))
        Reception.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Reception)
        self.statusbar.setObjectName(u"statusbar")
        Reception.setStatusBar(self.statusbar)

        self.retranslateUi(Reception)

        QMetaObject.connectSlotsByName(Reception)
    # setupUi

    def retranslateUi(self, Reception):
        Reception.setWindowTitle(QCoreApplication.translate("Reception", u"MainWindow", None))
        self.logo.setText("")
        self.label_29.setText(QCoreApplication.translate("Reception", u"Reception", None))
        self.minBtn.setText(QCoreApplication.translate("Reception", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("Reception", u"X", None))
        self.groupBox.setTitle(QCoreApplication.translate("Reception", u"Activities", None))
        self.patientBtn.setText(QCoreApplication.translate("Reception", u"Patient", None))
        self.clinicBtn.setText(QCoreApplication.translate("Reception", u"Clinic", None))
        self.pharmacyBtn.setText(QCoreApplication.translate("Reception", u"Pharmacy", None))
        self.labBtn.setText(QCoreApplication.translate("Reception", u"Lab", None))
        self.accountBtn.setText(QCoreApplication.translate("Reception", u"Account", None))
        self.label.setText(QCoreApplication.translate("Reception", u"Reception", None))
        self.createAptBtn.setText(QCoreApplication.translate("Reception", u"Create Appointment", None))
        self.repLogOut.setText(QCoreApplication.translate("Reception", u"Log Out", None))
    # retranslateUi

