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
        Start.resize(591, 210)
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
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.frame = QFrame(Start)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(13)
        self.gridLayout_3.setVerticalSpacing(9)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.bgLayer1 = QFrame(self.frame)
        self.bgLayer1.setObjectName(u"bgLayer1")
        self.bgLayer1.setMaximumSize(QSize(825, 500))
        self.bgLayer1.setCursor(QCursor(Qt.BlankCursor))
        self.bgLayer1.setMouseTracking(True)
        self.bgLayer1.setTabletTracking(True)
        self.bgLayer1.setAutoFillBackground(False)
        self.bgLayer1.setFrameShape(QFrame.NoFrame)
        self.bgLayer1.setFrameShadow(QFrame.Raised)
        self.bgLayer1.setLineWidth(1)
        self.bgLayer1.setMidLineWidth(1)
        self.gridLayout = QGridLayout(self.bgLayer1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(13, -1, -1, -1)
        self.bgframe = QFrame(self.bgLayer1)
        self.bgframe.setObjectName(u"bgframe")
        self.bgframe.setFrameShape(QFrame.StyledPanel)
        self.bgframe.setFrameShadow(QFrame.Raised)
        self.bgframe.setLineWidth(2)
        self.gridLayout_4 = QGridLayout(self.bgframe)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.label = QLabel(self.bgframe)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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

        self.label_2 = QLabel(self.bgframe)
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

        self.label_3 = QLabel(self.bgframe)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(12)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.bgframe, 1, 0, 1, 4)

        self.label_4 = QLabel(self.bgLayer1)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_4.setFont(font4)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 4)


        self.gridLayout_3.addWidget(self.bgLayer1, 0, 1, 1, 1)

        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
        self.logo.setMinimumSize(QSize(150, 200))
        self.logo.setScaledContents(True)

        self.gridLayout_3.addWidget(self.logo, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 1)


        self.retranslateUi(Start)

        QMetaObject.connectSlotsByName(Start)
    # setupUi

    def retranslateUi(self, Start):
        Start.setWindowTitle(QCoreApplication.translate("Start", u"Intro", None))
        self.label.setText(QCoreApplication.translate("Start", u"SEFA", None))
        self.label_2.setText(QCoreApplication.translate("Start", u"Specialist Hospital", None))
        self.label_3.setText(QCoreApplication.translate("Start", u"Health Information Management System (HIMS) v3", None))
        self.label_4.setText(QCoreApplication.translate("Start", u"Loading...", None))
        self.logo.setText(QCoreApplication.translate("Start", u"logo", None))
    # retranslateUi

