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
        Start.resize(559, 258)
        Start.setMaximumSize(QSize(827, 502))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(8)
        Start.setFont(font)
        Start.setCursor(QCursor(Qt.BlankCursor))
        Start.setMouseTracking(True)
        Start.setTabletTracking(True)
        Start.setWindowOpacity(0.800000000000000)
        Start.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(Start)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.bgLayer = QFrame(Start)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setMaximumSize(QSize(825, 500))
        self.bgLayer.setCursor(QCursor(Qt.BlankCursor))
        self.bgLayer.setMouseTracking(True)
        self.bgLayer.setTabletTracking(True)
        self.bgLayer.setAutoFillBackground(False)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(1)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout = QGridLayout(self.bgLayer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.bgLayer)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 3, 3, 1, 1)

        self.logo = QLabel(self.bgLayer)
        self.logo.setObjectName(u"logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
        self.logo.setMinimumSize(QSize(150, 200))

        self.gridLayout.addWidget(self.logo, 1, 2, 3, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.label = QLabel(self.bgLayer)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(30)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.bgLayer)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.bgLayer)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(12)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.verticalLayout, 1, 3, 2, 1)


        self.gridLayout_2.addWidget(self.bgLayer, 0, 1, 1, 1)


        self.retranslateUi(Start)

        QMetaObject.connectSlotsByName(Start)
    # setupUi

    def retranslateUi(self, Start):
        Start.setWindowTitle(QCoreApplication.translate("Start", u"Intro", None))
        self.label_4.setText(QCoreApplication.translate("Start", u"Loading...", None))
        self.logo.setText(QCoreApplication.translate("Start", u"logo", None))
        self.label.setText(QCoreApplication.translate("Start", u"SEFA", None))
        self.label_2.setText(QCoreApplication.translate("Start", u"Specialist Hospital", None))
        self.label_3.setText(QCoreApplication.translate("Start", u"Health Information Management System (HIMS)", None))
    # retranslateUi

