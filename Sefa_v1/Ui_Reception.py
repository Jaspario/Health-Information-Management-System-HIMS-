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
        Reception.setWindowModality(Qt.ApplicationModal)
        Reception.resize(693, 462)
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(7)
        Reception.setFont(font)
        Reception.setAutoFillBackground(True)
        Reception.setModal(True)
        self.verticalLayout = QVBoxLayout(Reception)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame = QFrame(Reception)
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
        self.minButton = QPushButton(self.frame)
        self.minButton.setObjectName(u"minButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minButton.sizePolicy().hasHeightForWidth())
        self.minButton.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(11)
        self.minButton.setFont(font1)
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minButton.setMouseTracking(True)
        self.minButton.setTabletTracking(True)
        self.minButton.setAutoFillBackground(False)
        self.minButton.setAutoDefault(False)
        self.minButton.setFlat(False)

        self.horizontalLayout_11.addWidget(self.minButton)

        self.closeButton = QPushButton(self.frame)
        self.closeButton.setObjectName(u"closeButton")
        sizePolicy1.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy1)
        self.closeButton.setMaximumSize(QSize(16777215, 16777215))
        self.closeButton.setFont(font1)
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setMouseTracking(True)
        self.closeButton.setTabletTracking(True)
        self.closeButton.setLayoutDirection(Qt.LeftToRight)
        self.closeButton.setAutoFillBackground(False)
        self.closeButton.setAutoDefault(False)
        self.closeButton.setFlat(False)

        self.horizontalLayout_11.addWidget(self.closeButton)


        self.gridLayout_13.addLayout(self.horizontalLayout_11, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(405, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_13)


        self.horizontalLayout_7.addWidget(self.frame)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.Layer1 = QFrame(Reception)
        self.Layer1.setObjectName(u"Layer1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.Layer1.sizePolicy().hasHeightForWidth())
        self.Layer1.setSizePolicy(sizePolicy2)
        self.Layer1.setMaximumSize(QSize(16777215, 380))
        self.Layer1.setMouseTracking(True)
        self.Layer1.setTabletTracking(True)
        self.Layer1.setAutoFillBackground(False)
        self.Layer1.setFrameShape(QFrame.Box)
        self.Layer1.setFrameShadow(QFrame.Raised)
        self.Layer1.setLineWidth(2)
        self.Layer1.setMidLineWidth(2)
        self.groupBox = QGroupBox(self.Layer1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(21, 75, 618, 190))
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.groupBox.setFont(font2)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.recordBtn = QPushButton(self.groupBox)
        self.recordBtn.setObjectName(u"recordBtn")
        self.recordBtn.setMaximumSize(QSize(16777215, 130))
        font3 = QFont()
        font3.setFamily(u"MS UI Gothic")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.recordBtn.setFont(font3)

        self.horizontalLayout_6.addWidget(self.recordBtn)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.docScheduleBtn = QPushButton(self.groupBox)
        self.docScheduleBtn.setObjectName(u"docScheduleBtn")
        self.docScheduleBtn.setMaximumSize(QSize(16777215, 130))
        self.docScheduleBtn.setFont(font3)

        self.horizontalLayout_9.addWidget(self.docScheduleBtn)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.billingBtn = QPushButton(self.groupBox)
        self.billingBtn.setObjectName(u"billingBtn")
        self.billingBtn.setMaximumSize(QSize(16777215, 130))
        self.billingBtn.setFont(font3)

        self.horizontalLayout_8.addWidget(self.billingBtn)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_8)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.Layer1)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(21, 285, 628, 70))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.createAptBtn = QPushButton(self.horizontalLayoutWidget)
        self.createAptBtn.setObjectName(u"createAptBtn")
        self.createAptBtn.setMaximumSize(QSize(16777215, 50))
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(10)
        self.createAptBtn.setFont(font4)

        self.horizontalLayout_2.addWidget(self.createAptBtn)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.horizontalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.repLogOut = QPushButton(self.horizontalLayoutWidget)
        self.repLogOut.setObjectName(u"repLogOut")
        self.repLogOut.setMaximumSize(QSize(16777215, 50))
        self.repLogOut.setFont(font4)

        self.horizontalLayout_3.addWidget(self.repLogOut)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)

        self.label = QLabel(self.Layer1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(4, 7, 658, 52))
        font5 = QFont()
        font5.setFamily(u"Tahoma")
        font5.setPointSize(18)
        font5.setUnderline(True)
        self.label.setFont(font5)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(2)

        self.verticalLayout.addWidget(self.Layer1)


        self.retranslateUi(Reception)

        QMetaObject.connectSlotsByName(Reception)
    # setupUi

    def retranslateUi(self, Reception):
        Reception.setWindowTitle(QCoreApplication.translate("Reception", u"Dialog", None))
        self.logo.setText("")
        self.label_29.setText(QCoreApplication.translate("Reception", u"Reception", None))
        self.minButton.setText(QCoreApplication.translate("Reception", u"__", None))
        self.closeButton.setText(QCoreApplication.translate("Reception", u"X", None))
        self.groupBox.setTitle(QCoreApplication.translate("Reception", u"Activities", None))
        self.recordBtn.setText(QCoreApplication.translate("Reception", u"Patient's Record", None))
        self.docScheduleBtn.setText(QCoreApplication.translate("Reception", u"Doctor's Schedule", None))
        self.billingBtn.setText(QCoreApplication.translate("Reception", u"Billing", None))
        self.createAptBtn.setText(QCoreApplication.translate("Reception", u"Create Appointment", None))
        self.repLogOut.setText(QCoreApplication.translate("Reception", u"Log Out", None))
        self.label.setText(QCoreApplication.translate("Reception", u"Reception", None))
    # retranslateUi

