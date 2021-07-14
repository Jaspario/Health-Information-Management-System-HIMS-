# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ApptSlip.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ApptSlip(object):
    def setupUi(self, ApptSlip):
        if not ApptSlip.objectName():
            ApptSlip.setObjectName(u"ApptSlip")
        ApptSlip.setWindowModality(Qt.NonModal)
        ApptSlip.resize(541, 318)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ApptSlip.sizePolicy().hasHeightForWidth())
        ApptSlip.setSizePolicy(sizePolicy)
        ApptSlip.setMouseTracking(True)
        ApptSlip.setTabletTracking(True)
        ApptSlip.setWindowOpacity(1.000000000000000)
        ApptSlip.setAutoFillBackground(True)
        ApptSlip.setModal(True)
        self.gridLayout = QGridLayout(ApptSlip)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(ApptSlip)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setContentsMargins(3, 0, 8, 0)
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 1, -1)
        self.miniBtn = QPushButton(self.frame)
        self.miniBtn.setObjectName(u"miniBtn")
        sizePolicy.setHeightForWidth(self.miniBtn.sizePolicy().hasHeightForWidth())
        self.miniBtn.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(11)
        self.miniBtn.setFont(font)
        self.miniBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.miniBtn.setMouseTracking(True)
        self.miniBtn.setTabletTracking(True)
        self.miniBtn.setAutoFillBackground(True)
        self.miniBtn.setStyleSheet(u"")
        self.miniBtn.setAutoDefault(False)
        self.miniBtn.setFlat(False)

        self.horizontalLayout_6.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(self.frame)
        self.exitBtn.setObjectName(u"exitBtn")
        sizePolicy.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy)
        self.exitBtn.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(12)
        self.exitBtn.setFont(font1)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setMouseTracking(True)
        self.exitBtn.setTabletTracking(True)
        self.exitBtn.setLayoutDirection(Qt.LeftToRight)
        self.exitBtn.setAutoFillBackground(True)
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setFlat(False)

        self.horizontalLayout_6.addWidget(self.exitBtn)


        self.gridLayout_13.addLayout(self.horizontalLayout_6, 0, 2, 1, 1)

        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy2)
        self.label_29.setWordWrap(True)
        self.label_29.setMargin(7)

        self.gridLayout_13.addWidget(self.label_29, 0, 1, 1, 1)

        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(40, 40))
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.gridLayout_13.addWidget(self.logo, 0, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_13)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.bgLayer = QFrame(ApptSlip)
        self.bgLayer.setObjectName(u"bgLayer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bgLayer.sizePolicy().hasHeightForWidth())
        self.bgLayer.setSizePolicy(sizePolicy3)
        self.bgLayer.setAutoFillBackground(True)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cancelBtn = QPushButton(self.bgLayer)
        self.cancelBtn.setObjectName(u"cancelBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(8)
        self.cancelBtn.setFont(font2)

        self.gridLayout_2.addWidget(self.cancelBtn, 6, 0, 1, 7)

        self.label_3 = QLabel(self.bgLayer)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setMargin(5)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 7)

        self.label = QLabel(self.bgLayer)
        self.label.setObjectName(u"label")
        self.label.setMargin(5)

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.scheduledTime = QDateTimeEdit(self.bgLayer)
        self.scheduledTime.setObjectName(u"scheduledTime")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scheduledTime.sizePolicy().hasHeightForWidth())
        self.scheduledTime.setSizePolicy(sizePolicy5)
        self.scheduledTime.setMinimumSize(QSize(0, 30))
        self.scheduledTime.setWrapping(True)
        self.scheduledTime.setAlignment(Qt.AlignCenter)
        self.scheduledTime.setButtonSymbols(QAbstractSpinBox.PlusMinus)

        self.gridLayout_2.addWidget(self.scheduledTime, 3, 5, 1, 2)

        self.bookBtn = QPushButton(self.bgLayer)
        self.bookBtn.setObjectName(u"bookBtn")
        sizePolicy4.setHeightForWidth(self.bookBtn.sizePolicy().hasHeightForWidth())
        self.bookBtn.setSizePolicy(sizePolicy4)
        self.bookBtn.setFont(font2)

        self.gridLayout_2.addWidget(self.bookBtn, 5, 0, 1, 7)

        self.docLists = QComboBox(self.bgLayer)
        self.docLists.setObjectName(u"docLists")
        sizePolicy5.setHeightForWidth(self.docLists.sizePolicy().hasHeightForWidth())
        self.docLists.setSizePolicy(sizePolicy5)
        self.docLists.setMinimumSize(QSize(150, 30))

        self.gridLayout_2.addWidget(self.docLists, 3, 1, 1, 3)

        self.line = QFrame(self.bgLayer)
        self.line.setObjectName(u"line")
        sizePolicy5.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy5)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 7)

        self.line_2 = QFrame(self.bgLayer)
        self.line_2.setObjectName(u"line_2")
        sizePolicy5.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy5)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 2, 0, 1, 7)

        self.label_2 = QLabel(self.bgLayer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMargin(5)

        self.gridLayout_2.addWidget(self.label_2, 3, 4, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.bgLayer)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_4.setFont(font4)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(5)

        self.horizontalLayout.addWidget(self.label_4)

        self.cardNum = QLabel(self.bgLayer)
        self.cardNum.setObjectName(u"cardNum")
        self.cardNum.setFont(font2)

        self.horizontalLayout.addWidget(self.cardNum)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 4, 1, 3)


        self.gridLayout.addWidget(self.bgLayer, 1, 1, 1, 1)


        self.retranslateUi(ApptSlip)

        QMetaObject.connectSlotsByName(ApptSlip)
    # setupUi

    def retranslateUi(self, ApptSlip):
        ApptSlip.setWindowTitle(QCoreApplication.translate("ApptSlip", u"Appointment Slip", None))
        self.miniBtn.setText(QCoreApplication.translate("ApptSlip", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("ApptSlip", u"X", None))
        self.label_29.setText(QCoreApplication.translate("ApptSlip", u"Appointment Slip", None))
        self.logo.setText("")
        self.cancelBtn.setText(QCoreApplication.translate("ApptSlip", u"Cancel", None))
        self.label_3.setText(QCoreApplication.translate("ApptSlip", u"Appointment Slip", None))
        self.label.setText(QCoreApplication.translate("ApptSlip", u"Available Doctors: ", None))
        self.bookBtn.setText(QCoreApplication.translate("ApptSlip", u"Book", None))
        self.label_2.setText(QCoreApplication.translate("ApptSlip", u"Date:", None))
        self.label_4.setText(QCoreApplication.translate("ApptSlip", u"Patient No.:", None))
        self.cardNum.setText("")
    # retranslateUi

