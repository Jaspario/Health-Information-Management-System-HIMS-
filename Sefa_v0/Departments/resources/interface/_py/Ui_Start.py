# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Start.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Start(object):
    def setupUi(self, Start):
        if not Start.objectName():
            Start.setObjectName(u"Start")
        Start.resize(629, 442)
        Start.setMaximumSize(QSize(827, 502))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(8)
        Start.setFont(font)
        Start.setCursor(QCursor(Qt.BlankCursor))
        Start.setMouseTracking(True)
        Start.setTabletTracking(True)
        Start.setWindowOpacity(0.600000000000000)
        Start.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(Start)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.bgLayer = QFrame(Start)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setMaximumSize(QSize(825, 500))
        self.bgLayer.setCursor(QCursor(Qt.BlankCursor))
        self.bgLayer.setMouseTracking(True)
        self.bgLayer.setTabletTracking(True)
        self.bgLayer.setAutoFillBackground(True)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(1)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout = QGridLayout(self.bgLayer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(160, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.frame = QFrame(self.bgLayer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(207, 223))
        self.logo.setAutoFillBackground(True)
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setPixmap(QPixmap(u"../../logos/Sefa logo2.png"))
        self.logo.setScaledContents(False)

        self.verticalLayout.addWidget(self.logo)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(160, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.label_2 = QLabel(self.bgLayer)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"EngraversGothic BT")
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(2)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.load = QLabel(self.bgLayer)
        self.load.setObjectName(u"load")
        sizePolicy1.setHeightForWidth(self.load.sizePolicy().hasHeightForWidth())
        self.load.setSizePolicy(sizePolicy1)
        self.load.setFont(font)
        self.load.setAutoFillBackground(False)
        self.load.setScaledContents(False)
        self.load.setWordWrap(True)
        self.load.setMargin(7)

        self.gridLayout.addWidget(self.load, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.bgLayer, 0, 1, 1, 1)


        self.retranslateUi(Start)

        QMetaObject.connectSlotsByName(Start)
    # setupUi

    def retranslateUi(self, Start):
        Start.setWindowTitle(QCoreApplication.translate("Start", u"Intro", None))
        self.logo.setText("")
        self.label_2.setText(QCoreApplication.translate("Start", u"SEFA SPECIALIST HOSPITAL", None))
        self.load.setText(QCoreApplication.translate("Start", u"Loading....", None))
    # retranslateUi

