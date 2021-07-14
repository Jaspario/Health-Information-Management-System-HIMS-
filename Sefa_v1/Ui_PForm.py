# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PForm(object):
    def setupUi(self, PForm):
        if not PForm.objectName():
            PForm.setObjectName(u"PForm")
        PForm.resize(708, 493)
        self.gridLayout = QGridLayout(PForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_5 = QFrame(PForm)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_10.setContentsMargins(3, 0, 8, 0)
        self.logo = QLabel(self.frame_5)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 45))
        self.logo.setMaximumSize(QSize(45, 45))
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.logo)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_29 = QLabel(self.frame_5)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_13.addWidget(self.label_29, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, 1, -1)
        self.minButton = QPushButton(self.frame_5)
        self.minButton.setObjectName(u"minButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minButton.sizePolicy().hasHeightForWidth())
        self.minButton.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        self.minButton.setFont(font)
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minButton.setMouseTracking(True)
        self.minButton.setTabletTracking(True)
        self.minButton.setAutoFillBackground(False)
        self.minButton.setAutoDefault(False)
        self.minButton.setFlat(False)

        self.horizontalLayout_11.addWidget(self.minButton)

        self.closeButton = QPushButton(self.frame_5)
        self.closeButton.setObjectName(u"closeButton")
        sizePolicy1.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy1)
        self.closeButton.setMaximumSize(QSize(16777215, 16777215))
        self.closeButton.setFont(font)
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setMouseTracking(True)
        self.closeButton.setTabletTracking(True)
        self.closeButton.setLayoutDirection(Qt.LeftToRight)
        self.closeButton.setAutoFillBackground(False)
        self.closeButton.setAutoDefault(False)
        self.closeButton.setFlat(False)

        self.horizontalLayout_11.addWidget(self.closeButton)


        self.gridLayout_13.addLayout(self.horizontalLayout_11, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(405, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_13)


        self.horizontalLayout_9.addWidget(self.frame_5)


        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.frame = QFrame(PForm)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMaximumSize(QSize(400, 16777215))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setUnderline(True)
        self.label.setFont(font1)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(6)

        self.horizontalLayout_2.addWidget(self.label)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(2)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setMaximumSize(QSize(16777215, 245))
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet(u"border-color: rgb(2, 2, 2);\n"
"color: rgb(2, 2, 2);")
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet(u"border-color: rgb(254, 21, 0);")
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(4, -1, 10, -1)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setMargin(6)
        self.label_5.setIndent(2)
        self.label_5.setOpenExternalLinks(False)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.pGender = QLineEdit(self.frame_4)
        self.pGender.setObjectName(u"pGender")
        self.pGender.setMaximumSize(QSize(130, 40))
        self.pGender.setAutoFillBackground(False)
        self.pGender.setStyleSheet(u"background-color: rgb(188, 154, 75);\n"
"color: rgb(4, 4, 4);")

        self.horizontalLayout_7.addWidget(self.pGender)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setMargin(6)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.pAge = QLineEdit(self.frame_4)
        self.pAge.setObjectName(u"pAge")
        self.pAge.setMaximumSize(QSize(80, 40))

        self.horizontalLayout_7.addWidget(self.pAge)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setMargin(6)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.pclass = QComboBox(self.frame_4)
        self.pclass.addItem("")
        self.pclass.addItem("")
        self.pclass.addItem("")
        self.pclass.addItem("")
        self.pclass.setObjectName(u"pclass")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.pclass.sizePolicy().hasHeightForWidth())
        self.pclass.setSizePolicy(sizePolicy4)
        self.pclass.setMaximumSize(QSize(399, 40))

        self.horizontalLayout_7.addWidget(self.pclass)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"border-color: rgb(254, 21, 0);")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(4, -1, 10, -1)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setMargin(6)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.pFirstname = QLineEdit(self.frame_2)
        self.pFirstname.setObjectName(u"pFirstname")
        self.pFirstname.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_8.addWidget(self.pFirstname)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setMargin(6)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.pLastname = QLineEdit(self.frame_2)
        self.pLastname.setObjectName(u"pLastname")
        self.pLastname.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_8.addWidget(self.pLastname)


        self.gridLayout_5.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, -1, 12, -1)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 16777215))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(4)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.doctorList = QComboBox(self.frame_3)
        self.doctorList.addItem("")
        self.doctorList.addItem("")
        self.doctorList.setObjectName(u"doctorList")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(2)
        sizePolicy5.setHeightForWidth(self.doctorList.sizePolicy().hasHeightForWidth())
        self.doctorList.setSizePolicy(sizePolicy5)
        self.doctorList.setMaximumSize(QSize(400, 40))

        self.horizontalLayout_3.addWidget(self.doctorList)

        self.horizontalSpacer_3 = QSpacerItem(139, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, -1, 6, -1)
        self.pBookApt = QPushButton(self.frame)
        self.pBookApt.setObjectName(u"pBookApt")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(3)
        sizePolicy6.setHeightForWidth(self.pBookApt.sizePolicy().hasHeightForWidth())
        self.pBookApt.setSizePolicy(sizePolicy6)
        self.pBookApt.setMaximumSize(QSize(16777215, 40))
        self.pBookApt.setCursor(QCursor(Qt.PointingHandCursor))
        self.pBookApt.setAutoFillBackground(False)
        self.pBookApt.setStyleSheet(u"background-color: rgb(118, 118, 118);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.pBookApt)

        self.horizontalSpacer = QSpacerItem(173, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pCancel = QPushButton(self.frame)
        self.pCancel.setObjectName(u"pCancel")
        sizePolicy6.setHeightForWidth(self.pCancel.sizePolicy().hasHeightForWidth())
        self.pCancel.setSizePolicy(sizePolicy6)
        self.pCancel.setMaximumSize(QSize(16777215, 40))
        self.pCancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.pCancel.setAutoFillBackground(False)
        self.pCancel.setStyleSheet(u"background-color: rgb(118, 118, 118);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.pCancel)

        self.pRegister = QPushButton(self.frame)
        self.pRegister.setObjectName(u"pRegister")
        sizePolicy6.setHeightForWidth(self.pRegister.sizePolicy().hasHeightForWidth())
        self.pRegister.setSizePolicy(sizePolicy6)
        self.pRegister.setMaximumSize(QSize(16777215, 40))
        self.pRegister.setCursor(QCursor(Qt.PointingHandCursor))
        self.pRegister.setAutoFillBackground(False)
        self.pRegister.setStyleSheet(u"background-color: rgb(118, 118, 118);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.pRegister)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(PForm)

        QMetaObject.connectSlotsByName(PForm)
    # setupUi

    def retranslateUi(self, PForm):
        PForm.setWindowTitle(QCoreApplication.translate("PForm", u"Dialog", None))
        self.logo.setText("")
        self.label_29.setText(QCoreApplication.translate("PForm", u"Reception", None))
        self.minButton.setText(QCoreApplication.translate("PForm", u"__", None))
        self.closeButton.setText(QCoreApplication.translate("PForm", u"X", None))
        self.label.setText(QCoreApplication.translate("PForm", u"Patient's Registraion Form", None))
        self.label_5.setStyleSheet(QCoreApplication.translate("PForm", u"color: rgb(255, 255, 255);", None))
        self.label_5.setText(QCoreApplication.translate("PForm", u"Gender:", None))
        self.label_6.setStyleSheet(QCoreApplication.translate("PForm", u"color: rgb(255, 255, 255);", None))
        self.label_6.setText(QCoreApplication.translate("PForm", u"Age:", None))
        self.pAge.setStyleSheet(QCoreApplication.translate("PForm", u"background-color: rgb(188, 154, 75);\n"
"color: rgb(4, 4, 4);", None))
        self.label_7.setStyleSheet(QCoreApplication.translate("PForm", u"color: rgb(255, 255, 255);", None))
        self.label_7.setText(QCoreApplication.translate("PForm", u"Class:", None))
        self.pclass.setItemText(0, QCoreApplication.translate("PForm", u"Company", None))
        self.pclass.setItemText(1, QCoreApplication.translate("PForm", u"Private", None))
        self.pclass.setItemText(2, QCoreApplication.translate("PForm", u"HMO", None))
        self.pclass.setItemText(3, QCoreApplication.translate("PForm", u"Family", None))

        self.pclass.setStyleSheet(QCoreApplication.translate("PForm", u"color: rgb(255, 255, 255);", None))
        self.label_8.setStyleSheet(QCoreApplication.translate("PForm", u"color: rgb(255, 255, 255);", None))
        self.label_8.setText(QCoreApplication.translate("PForm", u"First Name:", None))
        self.pFirstname.setStyleSheet(QCoreApplication.translate("PForm", u"background-color: rgb(188, 154, 75);\n"
"color: rgb(4, 4, 4);", None))
        self.label_9.setStyleSheet(QCoreApplication.translate("PForm", u"color: rgb(255, 255, 255);", None))
        self.label_9.setText(QCoreApplication.translate("PForm", u"Last Name:", None))
        self.pLastname.setStyleSheet(QCoreApplication.translate("PForm", u"background-color: rgb(188, 154, 75);\n"
"color: rgb(4, 4, 4);", None))
        self.label_2.setText(QCoreApplication.translate("PForm", u"Available Doctor:", None))
        self.doctorList.setItemText(0, QCoreApplication.translate("PForm", u"Dr. Ahmadu Bello", None))
        self.doctorList.setItemText(1, QCoreApplication.translate("PForm", u"Dr. Christian Opara", None))

        self.doctorList.setStyleSheet(QCoreApplication.translate("PForm", u"color: rgb(255, 255, 255);", None))
        self.pBookApt.setText(QCoreApplication.translate("PForm", u"Book Appointment", None))
        self.pCancel.setText(QCoreApplication.translate("PForm", u"Cancel", None))
        self.pRegister.setText(QCoreApplication.translate("PForm", u"Register", None))
    # retranslateUi

