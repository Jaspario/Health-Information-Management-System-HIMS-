# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PSearch.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PSearch(object):
    def setupUi(self, PSearch):
        if not PSearch.objectName():
            PSearch.setObjectName(u"PSearch")
        PSearch.resize(740, 338)
        self.gridLayout = QGridLayout(PSearch)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(PSearch)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayoutWidget = QWidget(self.frame)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(27, 84, 667, 46))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pSearch = QPushButton(self.formLayoutWidget)
        self.pSearch.setObjectName(u"pSearch")
        self.pSearch.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(150)
        sizePolicy1.setHeightForWidth(self.pSearch.sizePolicy().hasHeightForWidth())
        self.pSearch.setSizePolicy(sizePolicy1)
        self.pSearch.setMaximumSize(QSize(100, 150))
        self.pSearch.setStyleSheet(u"background-color: rgb(53, 0, 159);")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.pSearch)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(150)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setMaximumSize(QSize(16777215, 150))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(6, 6, 6);")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.pCreateNew = QPushButton(self.frame)
        self.pCreateNew.setObjectName(u"pCreateNew")
        self.pCreateNew.setGeometry(QRect(24, 192, 217, 40))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(9)
        self.pCreateNew.setFont(font)
        self.pCreateNew.setAutoFillBackground(False)
        self.pCreateNew.setStyleSheet(u"background-color: rgb(103, 103, 12);\n"
"color: rgb(0, 0, 0);")
        self.pCloseSearch = QPushButton(self.frame)
        self.pCloseSearch.setObjectName(u"pCloseSearch")
        self.pCloseSearch.setGeometry(QRect(589, 195, 106, 40))
        self.pCloseSearch.setFont(font)
        self.pCloseSearch.setAutoFillBackground(False)
        self.pCloseSearch.setStyleSheet(u"background-color: rgb(69, 69, 69);\n"
"color: rgb(0, 0, 0);")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(3, 15, 706, 37))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setUnderline(True)
        self.label.setFont(font1)
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_2 = QFrame(PSearch)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
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
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.logo)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_29 = QLabel(self.frame_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setWordWrap(True)
        self.label_29.setMargin(7)

        self.gridLayout_13.addWidget(self.label_29, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, 1, -1)
        self.minButton = QPushButton(self.frame_2)
        self.minButton.setObjectName(u"minButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.minButton.sizePolicy().hasHeightForWidth())
        self.minButton.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setPointSize(11)
        self.minButton.setFont(font2)
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minButton.setMouseTracking(True)
        self.minButton.setTabletTracking(True)
        self.minButton.setAutoFillBackground(False)
        self.minButton.setAutoDefault(False)
        self.minButton.setFlat(False)

        self.horizontalLayout_11.addWidget(self.minButton)

        self.closeButton = QPushButton(self.frame_2)
        self.closeButton.setObjectName(u"closeButton")
        sizePolicy4.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy4)
        self.closeButton.setMaximumSize(QSize(16777215, 16777215))
        self.closeButton.setFont(font2)
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


        self.horizontalLayout_7.addWidget(self.frame_2)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)


        self.retranslateUi(PSearch)
        self.pCloseSearch.clicked.connect(PSearch.hide)

        QMetaObject.connectSlotsByName(PSearch)
    # setupUi

    def retranslateUi(self, PSearch):
        PSearch.setWindowTitle(QCoreApplication.translate("PSearch", u"Find Patient", None))
        self.pSearch.setText(QCoreApplication.translate("PSearch", u"SEARCH", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("PSearch", u"Please insert name or card number of patient", None))
        self.pCreateNew.setText(QCoreApplication.translate("PSearch", u"Create New Record", None))
        self.pCloseSearch.setText(QCoreApplication.translate("PSearch", u"Close", None))
        self.label.setText(QCoreApplication.translate("PSearch", u"Find Patient's Record", None))
        self.logo.setText("")
        self.label_29.setText(QCoreApplication.translate("PSearch", u"Find Patient", None))
        self.minButton.setText(QCoreApplication.translate("PSearch", u"__", None))
        self.closeButton.setText(QCoreApplication.translate("PSearch", u"X", None))
    # retranslateUi

