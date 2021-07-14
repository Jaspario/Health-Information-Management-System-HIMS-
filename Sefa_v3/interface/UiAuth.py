# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Auth.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Auth(object):
    def setupUi(self, Auth):
        if not Auth.objectName():
            Auth.setObjectName(u"Auth")
        Auth.resize(700, 822)
        Auth.setMinimumSize(QSize(480, 640))
        Auth.setMaximumSize(QSize(700, 850))
        self.gridLayout = QGridLayout(Auth)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 0, 1, 1, 1)

        self.bgLayer = QFrame(Auth)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setFrameShape(QFrame.StyledPanel)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.bgLayer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(9)
        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_3.setContentsMargins(13, 13, 13, 13)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, -1, -1, -1)
        self.logo = QLabel(self.bgLayer)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.logo)

        self.label = QLabel(self.bgLayer)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(13)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 13, -1)
        self.miniBtn = QPushButton(self.bgLayer)
        self.miniBtn.setObjectName(u"miniBtn")
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(10)
        self.miniBtn.setFont(font)
        self.miniBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.miniBtn.setFlat(True)

        self.horizontalLayout_2.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(self.bgLayer)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setFont(font)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setFlat(True)

        self.horizontalLayout_2.addWidget(self.exitBtn)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.bgframe = QFrame(self.bgLayer)
        self.bgframe.setObjectName(u"bgframe")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bgframe.sizePolicy().hasHeightForWidth())
        self.bgframe.setSizePolicy(sizePolicy2)
        self.bgframe.setFrameShape(QFrame.Box)
        self.bgframe.setFrameShadow(QFrame.Raised)
        self.bgframe.setLineWidth(2)
        self.bgframe.setMidLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.bgframe)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.bgframe)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy4)
        self.frame_5.setMinimumSize(QSize(350, 450))
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(3)
        self.frame_5.setMidLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy5)
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.frame_6.setLineWidth(3)
        self.frame_6.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.imgView = QLabel(self.frame_6)
        self.imgView.setObjectName(u"imgView")
        sizePolicy6 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.imgView.sizePolicy().hasHeightForWidth())
        self.imgView.setSizePolicy(sizePolicy6)
        self.imgView.setFrameShape(QFrame.Box)
        self.imgView.setLineWidth(2)
        self.imgView.setPixmap(QPixmap(u"../../../Work-Space/pyInstaller-Projects/Sefa_v2/resources/icons/logo_dark.ico"))
        self.imgView.setScaledContents(False)

        self.gridLayout_2.addWidget(self.imgView, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_5)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.contactBtn = QPushButton(self.frame_3)
        self.contactBtn.setObjectName(u"contactBtn")
        font1 = QFont()
        font1.setFamily(u"Georgia")
        font1.setPointSize(7)
        font1.setItalic(True)
        self.contactBtn.setFont(font1)
        self.contactBtn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.contactBtn)

        self.horizontalSpacer = QSpacerItem(155, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_10.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame_2)

        self.line = QFrame(self.bgframe)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(9)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line)

        self.frame_4 = QFrame(self.bgframe)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.stackedWidget = QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(7)
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.stackedWidget.setLineWidth(1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_4 = QSpacerItem(20, 225, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.frame_7 = QFrame(self.page)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy5.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy5)
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.frame_7.setLineWidth(1)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Box)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.frame_8.setLineWidth(2)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 3, 5, 3)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamily(u"Comic Sans MS")
        font3.setPointSize(7)
        font3.setBold(True)
        font3.setUnderline(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)
        self.label_3.setMouseTracking(True)
        self.label_3.setTabletTracking(True)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.loginStatus = QLabel(self.frame_8)
        self.loginStatus.setObjectName(u"loginStatus")
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(6)
        font4.setBold(False)
        font4.setItalic(True)
        font4.setWeight(50)
        self.loginStatus.setFont(font4)
        self.loginStatus.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.loginStatus)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(3)
        self.formLayout.setVerticalSpacing(5)
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setFamily(u"Georgia")
        font5.setPointSize(7)
        font5.setBold(False)
        font5.setWeight(50)
        self.label_4.setFont(font5)
        self.label_4.setMargin(5)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.userid = QLineEdit(self.frame_8)
        self.userid.setObjectName(u"userid")
        font6 = QFont()
        font6.setFamily(u"Tahoma")
        font6.setPointSize(8)
        self.userid.setFont(font6)
        self.userid.setFocusPolicy(Qt.ClickFocus)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.userid)

        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setMargin(5)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.password = QLineEdit(self.frame_8)
        self.password.setObjectName(u"password")
        self.password.setFont(font6)
        self.password.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.password)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 11, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.loginBtn = QPushButton(self.frame_8)
        self.loginBtn.setObjectName(u"loginBtn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.loginBtn.sizePolicy().hasHeightForWidth())
        self.loginBtn.setSizePolicy(sizePolicy7)
        self.loginBtn.setMinimumSize(QSize(45, 0))
        self.loginBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.loginBtn)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.spacer = QLabel(self.frame_8)
        self.spacer.setObjectName(u"spacer")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.spacer)


        self.verticalLayout_6.addLayout(self.formLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.reglinkBtn = QPushButton(self.frame_8)
        self.reglinkBtn.setObjectName(u"reglinkBtn")
        self.reglinkBtn.setMinimumSize(QSize(2, 0))
        self.reglinkBtn.setFont(font1)
        self.reglinkBtn.setFlat(True)

        self.horizontalLayout_5.addWidget(self.reglinkBtn)

        self.updatelinkBtn = QPushButton(self.frame_8)
        self.updatelinkBtn.setObjectName(u"updatelinkBtn")
        self.updatelinkBtn.setFont(font1)
        self.updatelinkBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updatelinkBtn.setFlat(True)

        self.horizontalLayout_5.addWidget(self.updatelinkBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.verticalSpacer_3 = QSpacerItem(20, 225, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.regForm = QFrame(self.page_2)
        self.regForm.setObjectName(u"regForm")
        self.regForm.setEnabled(True)
        self.regForm.setMaximumSize(QSize(16777215, 16777215))
        self.regForm.setAutoFillBackground(False)
        self.regForm.setStyleSheet(u"background-color: rgb(179, 176, 87);\n"
"color: rgb(2, 2, 2);")
        self.regForm.setFrameShape(QFrame.StyledPanel)
        self.regForm.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.regForm)
        self.gridLayout_8.setSpacing(2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.groupBox_4 = QGroupBox(self.regForm)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy8)
        self.groupBox_4.setMaximumSize(QSize(16777215, 150))
        font7 = QFont()
        font7.setFamily(u"Courier New")
        font7.setPointSize(6)
        font7.setBold(True)
        font7.setWeight(75)
        self.groupBox_4.setFont(font7)
        self.groupBox_4.setAutoFillBackground(False)
        self.gridLayout_9 = QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.userlbl = QLabel(self.groupBox_4)
        self.userlbl.setObjectName(u"userlbl")
        font8 = QFont()
        font8.setFamily(u"Georgia")
        font8.setPointSize(5)
        self.userlbl.setFont(font8)

        self.gridLayout_9.addWidget(self.userlbl, 0, 0, 1, 1)

        self.paswdlbl = QLabel(self.groupBox_4)
        self.paswdlbl.setObjectName(u"paswdlbl")
        self.paswdlbl.setFont(font8)

        self.gridLayout_9.addWidget(self.paswdlbl, 1, 0, 1, 1)

        self.regUserid = QLineEdit(self.groupBox_4)
        self.regUserid.setObjectName(u"regUserid")
        sizePolicy4.setHeightForWidth(self.regUserid.sizePolicy().hasHeightForWidth())
        self.regUserid.setSizePolicy(sizePolicy4)
        font9 = QFont()
        font9.setFamily(u"Courier New")
        font9.setPointSize(7)
        self.regUserid.setFont(font9)
        self.regUserid.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.regUserid, 0, 1, 1, 1)

        self.regPaswd = QLineEdit(self.groupBox_4)
        self.regPaswd.setObjectName(u"regPaswd")
        sizePolicy4.setHeightForWidth(self.regPaswd.sizePolicy().hasHeightForWidth())
        self.regPaswd.setSizePolicy(sizePolicy4)
        self.regPaswd.setFont(font9)
        self.regPaswd.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")
        self.regPaswd.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout_9.addWidget(self.regPaswd, 1, 1, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_4, 5, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.regForm)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(40)
        sizePolicy9.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy9)
        self.groupBox_3.setMaximumSize(QSize(16777215, 356))
        self.groupBox_3.setFont(font7)
        self.gridLayout_11 = QGridLayout(self.groupBox_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, 9, -1, 3)
        self.rank = QComboBox(self.groupBox_3)
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.addItem("")
        self.rank.setObjectName(u"rank")
        sizePolicy2.setHeightForWidth(self.rank.sizePolicy().hasHeightForWidth())
        self.rank.setSizePolicy(sizePolicy2)
        font10 = QFont()
        font10.setPointSize(7)
        self.rank.setFont(font10)

        self.gridLayout_11.addWidget(self.rank, 7, 1, 1, 1)

        self.gender = QComboBox(self.groupBox_3)
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.setObjectName(u"gender")
        sizePolicy2.setHeightForWidth(self.gender.sizePolicy().hasHeightForWidth())
        self.gender.setSizePolicy(sizePolicy2)
        self.gender.setFont(font10)

        self.gridLayout_11.addWidget(self.gender, 2, 1, 1, 1)

        self.lnamelbl = QLabel(self.groupBox_3)
        self.lnamelbl.setObjectName(u"lnamelbl")
        self.lnamelbl.setFont(font8)

        self.gridLayout_11.addWidget(self.lnamelbl, 1, 0, 1, 1)

        self.idlbl = QLabel(self.groupBox_3)
        self.idlbl.setObjectName(u"idlbl")
        self.idlbl.setFont(font8)

        self.gridLayout_11.addWidget(self.idlbl, 6, 0, 1, 1)

        self.phone = QLineEdit(self.groupBox_3)
        self.phone.setObjectName(u"phone")
        sizePolicy4.setHeightForWidth(self.phone.sizePolicy().hasHeightForWidth())
        self.phone.setSizePolicy(sizePolicy4)
        self.phone.setFont(font9)
        self.phone.setAutoFillBackground(False)
        self.phone.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")
        self.phone.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly|Qt.ImhPreferNumbers)

        self.gridLayout_11.addWidget(self.phone, 9, 1, 1, 1)

        self.genlbl = QLabel(self.groupBox_3)
        self.genlbl.setObjectName(u"genlbl")
        self.genlbl.setFont(font8)

        self.gridLayout_11.addWidget(self.genlbl, 2, 0, 1, 1)

        self.firstName = QLineEdit(self.groupBox_3)
        self.firstName.setObjectName(u"firstName")
        sizePolicy4.setHeightForWidth(self.firstName.sizePolicy().hasHeightForWidth())
        self.firstName.setSizePolicy(sizePolicy4)
        self.firstName.setFont(font9)
        self.firstName.setStyleSheet(u"color: rgb(8, 8, 8);\n"
"background-color: rgb(255, 255, 255);")
        self.firstName.setInputMethodHints(Qt.ImhPreferUppercase)

        self.gridLayout_11.addWidget(self.firstName, 0, 1, 1, 1)

        self.fnamelbl = QLabel(self.groupBox_3)
        self.fnamelbl.setObjectName(u"fnamelbl")
        self.fnamelbl.setFont(font8)

        self.gridLayout_11.addWidget(self.fnamelbl, 0, 0, 1, 1)

        self.phonelbl = QLabel(self.groupBox_3)
        self.phonelbl.setObjectName(u"phonelbl")
        self.phonelbl.setFont(font8)

        self.gridLayout_11.addWidget(self.phonelbl, 9, 0, 1, 1)

        self.employeeID = QLineEdit(self.groupBox_3)
        self.employeeID.setObjectName(u"employeeID")
        sizePolicy4.setHeightForWidth(self.employeeID.sizePolicy().hasHeightForWidth())
        self.employeeID.setSizePolicy(sizePolicy4)
        self.employeeID.setFont(font9)
        self.employeeID.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")
        self.employeeID.setInputMethodHints(Qt.ImhSensitiveData)

        self.gridLayout_11.addWidget(self.employeeID, 6, 1, 1, 1)

        self.ranklbl = QLabel(self.groupBox_3)
        self.ranklbl.setObjectName(u"ranklbl")
        self.ranklbl.setFont(font8)

        self.gridLayout_11.addWidget(self.ranklbl, 7, 0, 1, 1)

        self.joblbl = QLabel(self.groupBox_3)
        self.joblbl.setObjectName(u"joblbl")
        self.joblbl.setFont(font8)

        self.gridLayout_11.addWidget(self.joblbl, 3, 0, 1, 1)

        self.emaillbl = QLabel(self.groupBox_3)
        self.emaillbl.setObjectName(u"emaillbl")
        self.emaillbl.setFont(font8)

        self.gridLayout_11.addWidget(self.emaillbl, 8, 0, 1, 1)

        self.deptlbl = QLabel(self.groupBox_3)
        self.deptlbl.setObjectName(u"deptlbl")
        self.deptlbl.setFont(font8)

        self.gridLayout_11.addWidget(self.deptlbl, 4, 0, 1, 1)

        self.surname = QLineEdit(self.groupBox_3)
        self.surname.setObjectName(u"surname")
        sizePolicy4.setHeightForWidth(self.surname.sizePolicy().hasHeightForWidth())
        self.surname.setSizePolicy(sizePolicy4)
        self.surname.setFont(font9)
        self.surname.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")
        self.surname.setInputMethodHints(Qt.ImhPreferUppercase)

        self.gridLayout_11.addWidget(self.surname, 1, 1, 1, 1)

        self.email = QLineEdit(self.groupBox_3)
        self.email.setObjectName(u"email")
        sizePolicy4.setHeightForWidth(self.email.sizePolicy().hasHeightForWidth())
        self.email.setSizePolicy(sizePolicy4)
        self.email.setFont(font9)
        self.email.setAutoFillBackground(False)
        self.email.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")
        self.email.setInputMethodHints(Qt.ImhEmailCharactersOnly)

        self.gridLayout_11.addWidget(self.email, 8, 1, 1, 1)

        self.dept = QComboBox(self.groupBox_3)
        self.dept.addItem("")
        self.dept.addItem("")
        self.dept.addItem("")
        self.dept.addItem("")
        self.dept.addItem("")
        self.dept.addItem("")
        self.dept.addItem("")
        self.dept.setObjectName(u"dept")

        self.gridLayout_11.addWidget(self.dept, 4, 1, 1, 1)

        self.jobtitle = QComboBox(self.groupBox_3)
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.addItem("")
        self.jobtitle.setObjectName(u"jobtitle")

        self.gridLayout_11.addWidget(self.jobtitle, 3, 1, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_3, 3, 0, 1, 1)

        self.regStatus = QLabel(self.regForm)
        self.regStatus.setObjectName(u"regStatus")
        sizePolicy8.setHeightForWidth(self.regStatus.sizePolicy().hasHeightForWidth())
        self.regStatus.setSizePolicy(sizePolicy8)
        font11 = QFont()
        font11.setFamily(u"Segoe UI Symbol")
        font11.setPointSize(6)
        font11.setBold(False)
        font11.setItalic(True)
        font11.setWeight(50)
        self.regStatus.setFont(font11)
        self.regStatus.setAlignment(Qt.AlignCenter)
        self.regStatus.setMargin(5)

        self.gridLayout_8.addWidget(self.regStatus, 4, 0, 1, 1)

        self.label_25 = QLabel(self.regForm)
        self.label_25.setObjectName(u"label_25")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy10)
        self.label_25.setFont(font7)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_25, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.regForm)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy8.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy8)
        self.groupBox.setFont(font7)
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.regCancelBtn = QPushButton(self.groupBox)
        self.regCancelBtn.setObjectName(u"regCancelBtn")
        sizePolicy11 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.regCancelBtn.sizePolicy().hasHeightForWidth())
        self.regCancelBtn.setSizePolicy(sizePolicy11)
        self.regCancelBtn.setFont(font10)
        self.regCancelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.regCancelBtn.setStyleSheet(u"border-color: rgb(8, 8, 8);")

        self.horizontalLayout_6.addWidget(self.regCancelBtn)

        self.registerBtn = QPushButton(self.groupBox)
        self.registerBtn.setObjectName(u"registerBtn")
        sizePolicy11.setHeightForWidth(self.registerBtn.sizePolicy().hasHeightForWidth())
        self.registerBtn.setSizePolicy(sizePolicy11)
        self.registerBtn.setFont(font10)
        self.registerBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.registerBtn.setAutoFillBackground(False)
        self.registerBtn.setStyleSheet(u"border-color: rgb(8, 8, 8);")
        self.registerBtn.setFlat(False)

        self.horizontalLayout_6.addWidget(self.registerBtn)


        self.gridLayout_6.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.authIdlbl = QLabel(self.groupBox)
        self.authIdlbl.setObjectName(u"authIdlbl")
        self.authIdlbl.setFont(font8)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.authIdlbl)

        self.authID = QLineEdit(self.groupBox)
        self.authID.setObjectName(u"authID")
        sizePolicy4.setHeightForWidth(self.authID.sizePolicy().hasHeightForWidth())
        self.authID.setSizePolicy(sizePolicy4)
        self.authID.setFont(font9)
        self.authID.setAutoFillBackground(False)
        self.authID.setStyleSheet(u"color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.authID.setInputMethodHints(Qt.ImhSensitiveData)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.authID)


        self.gridLayout_6.addLayout(self.formLayout_2, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox, 6, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.regForm)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_6)

        self.regForm_2 = QFrame(self.page_3)
        self.regForm_2.setObjectName(u"regForm_2")
        self.regForm_2.setEnabled(True)
        self.regForm_2.setMaximumSize(QSize(16777215, 16777215))
        self.regForm_2.setAutoFillBackground(False)
        self.regForm_2.setStyleSheet(u"background-color: rgb(179, 176, 87);\n"
"color: rgb(2, 2, 2);")
        self.regForm_2.setFrameShape(QFrame.StyledPanel)
        self.regForm_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.regForm_2)
        self.gridLayout_10.setSpacing(2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(5, 5, 5, 5)
        self.groupBox_5 = QGroupBox(self.regForm_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy12 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(40)
        sizePolicy12.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy12)
        self.groupBox_5.setMaximumSize(QSize(16777215, 356))
        self.groupBox_5.setFont(font7)
        self.gridLayout_12 = QGridLayout(self.groupBox_5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(-1, 9, -1, 3)
        self.deptlbl_2 = QLabel(self.groupBox_5)
        self.deptlbl_2.setObjectName(u"deptlbl_2")
        self.deptlbl_2.setFont(font8)

        self.gridLayout_12.addWidget(self.deptlbl_2, 1, 0, 1, 1)

        self.phonelbl_2 = QLabel(self.groupBox_5)
        self.phonelbl_2.setObjectName(u"phonelbl_2")
        self.phonelbl_2.setFont(font8)

        self.gridLayout_12.addWidget(self.phonelbl_2, 5, 0, 1, 1)

        self.emaillbl_2 = QLabel(self.groupBox_5)
        self.emaillbl_2.setObjectName(u"emaillbl_2")
        self.emaillbl_2.setFont(font8)

        self.gridLayout_12.addWidget(self.emaillbl_2, 4, 0, 1, 1)

        self.rank_2 = QComboBox(self.groupBox_5)
        self.rank_2.addItem("")
        self.rank_2.addItem("")
        self.rank_2.addItem("")
        self.rank_2.addItem("")
        self.rank_2.addItem("")
        self.rank_2.addItem("")
        self.rank_2.addItem("")
        self.rank_2.addItem("")
        self.rank_2.addItem("")
        self.rank_2.setObjectName(u"rank_2")
        self.rank_2.setFont(font10)

        self.gridLayout_12.addWidget(self.rank_2, 3, 1, 1, 1)

        self.ranklbl_2 = QLabel(self.groupBox_5)
        self.ranklbl_2.setObjectName(u"ranklbl_2")
        self.ranklbl_2.setFont(font8)

        self.gridLayout_12.addWidget(self.ranklbl_2, 3, 0, 1, 1)

        self.phone_2 = QLineEdit(self.groupBox_5)
        self.phone_2.setObjectName(u"phone_2")
        self.phone_2.setFont(font9)
        self.phone_2.setAutoFillBackground(False)
        self.phone_2.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")
        self.phone_2.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly|Qt.ImhPreferNumbers)

        self.gridLayout_12.addWidget(self.phone_2, 5, 1, 1, 1)

        self.email_2 = QLineEdit(self.groupBox_5)
        self.email_2.setObjectName(u"email_2")
        self.email_2.setFont(font9)
        self.email_2.setAutoFillBackground(False)
        self.email_2.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")
        self.email_2.setInputMethodHints(Qt.ImhEmailCharactersOnly)

        self.gridLayout_12.addWidget(self.email_2, 4, 1, 1, 1)

        self.joblbl_2 = QLabel(self.groupBox_5)
        self.joblbl_2.setObjectName(u"joblbl_2")
        self.joblbl_2.setFont(font8)

        self.gridLayout_12.addWidget(self.joblbl_2, 0, 0, 1, 1)

        self.jobtitle_2 = QComboBox(self.groupBox_5)
        self.jobtitle_2.addItem("")
        self.jobtitle_2.addItem("")
        self.jobtitle_2.addItem("")
        self.jobtitle_2.addItem("")
        self.jobtitle_2.addItem("")
        self.jobtitle_2.addItem("")
        self.jobtitle_2.addItem("")
        self.jobtitle_2.addItem("")
        self.jobtitle_2.addItem("")
        self.jobtitle_2.addItem("")
        self.jobtitle_2.addItem("")
        self.jobtitle_2.addItem("")
        self.jobtitle_2.setObjectName(u"jobtitle_2")

        self.gridLayout_12.addWidget(self.jobtitle_2, 0, 1, 1, 1)

        self.dept_2 = QComboBox(self.groupBox_5)
        self.dept_2.addItem("")
        self.dept_2.addItem("")
        self.dept_2.addItem("")
        self.dept_2.addItem("")
        self.dept_2.addItem("")
        self.dept_2.addItem("")
        self.dept_2.addItem("")
        self.dept_2.setObjectName(u"dept_2")

        self.gridLayout_12.addWidget(self.dept_2, 1, 1, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_5, 3, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.regForm_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy8.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy8)
        self.groupBox_6.setMaximumSize(QSize(16777215, 150))
        self.groupBox_6.setFont(font7)
        self.groupBox_6.setAutoFillBackground(False)
        self.gridLayout_13 = QGridLayout(self.groupBox_6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.userlbl_2 = QLabel(self.groupBox_6)
        self.userlbl_2.setObjectName(u"userlbl_2")
        self.userlbl_2.setFont(font8)

        self.gridLayout_13.addWidget(self.userlbl_2, 0, 0, 1, 1)

        self.paswdlbl_2 = QLabel(self.groupBox_6)
        self.paswdlbl_2.setObjectName(u"paswdlbl_2")
        self.paswdlbl_2.setFont(font8)

        self.gridLayout_13.addWidget(self.paswdlbl_2, 1, 0, 1, 1)

        self.regUserid_2 = QLineEdit(self.groupBox_6)
        self.regUserid_2.setObjectName(u"regUserid_2")
        self.regUserid_2.setFont(font9)
        self.regUserid_2.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_13.addWidget(self.regUserid_2, 0, 1, 1, 1)

        self.regPaswd_2 = QLineEdit(self.groupBox_6)
        self.regPaswd_2.setObjectName(u"regPaswd_2")
        self.regPaswd_2.setFont(font9)
        self.regPaswd_2.setStyleSheet(u"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 255, 255);")
        self.regPaswd_2.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout_13.addWidget(self.regPaswd_2, 1, 1, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_6, 5, 0, 1, 1)

        self.updateStatus = QLabel(self.regForm_2)
        self.updateStatus.setObjectName(u"updateStatus")
        sizePolicy8.setHeightForWidth(self.updateStatus.sizePolicy().hasHeightForWidth())
        self.updateStatus.setSizePolicy(sizePolicy8)
        font12 = QFont()
        font12.setFamily(u"Segoe UI Symbol")
        font12.setPointSize(4)
        font12.setBold(True)
        font12.setItalic(True)
        font12.setWeight(75)
        self.updateStatus.setFont(font12)
        self.updateStatus.setAlignment(Qt.AlignCenter)
        self.updateStatus.setMargin(5)

        self.gridLayout_10.addWidget(self.updateStatus, 4, 0, 1, 1)

        self.label_26 = QLabel(self.regForm_2)
        self.label_26.setObjectName(u"label_26")
        sizePolicy10.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy10)
        self.label_26.setFont(font7)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_26, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.regForm_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy8.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy8)
        self.groupBox_2.setFont(font7)
        self.gridLayout_7 = QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.updateCancelBtn = QPushButton(self.groupBox_2)
        self.updateCancelBtn.setObjectName(u"updateCancelBtn")
        sizePolicy11.setHeightForWidth(self.updateCancelBtn.sizePolicy().hasHeightForWidth())
        self.updateCancelBtn.setSizePolicy(sizePolicy11)
        font13 = QFont()
        font13.setPointSize(6)
        self.updateCancelBtn.setFont(font13)
        self.updateCancelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateCancelBtn.setStyleSheet(u"border-color: rgb(8, 8, 8);")

        self.horizontalLayout_7.addWidget(self.updateCancelBtn)

        self.updateBtn = QPushButton(self.groupBox_2)
        self.updateBtn.setObjectName(u"updateBtn")
        sizePolicy11.setHeightForWidth(self.updateBtn.sizePolicy().hasHeightForWidth())
        self.updateBtn.setSizePolicy(sizePolicy11)
        self.updateBtn.setFont(font13)
        self.updateBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateBtn.setAutoFillBackground(False)
        self.updateBtn.setStyleSheet(u"border-color: rgb(8, 8, 8);")
        self.updateBtn.setFlat(False)

        self.horizontalLayout_7.addWidget(self.updateBtn)


        self.gridLayout_7.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.authIdlbl_2 = QLabel(self.groupBox_2)
        self.authIdlbl_2.setObjectName(u"authIdlbl_2")
        self.authIdlbl_2.setFont(font8)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.authIdlbl_2)

        self.authID_2 = QLineEdit(self.groupBox_2)
        self.authID_2.setObjectName(u"authID_2")
        self.authID_2.setFont(font9)
        self.authID_2.setAutoFillBackground(False)
        self.authID_2.setStyleSheet(u"color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.authID_2.setInputMethodHints(Qt.ImhSensitiveData)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.authID_2)


        self.gridLayout_7.addLayout(self.formLayout_3, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_2, 6, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.regForm_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_4)


        self.gridLayout_3.addWidget(self.bgframe, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 1, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)


        self.retranslateUi(Auth)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Auth)
    # setupUi

    def retranslateUi(self, Auth):
        Auth.setWindowTitle(QCoreApplication.translate("Auth", u"Login", None))
        self.logo.setText(QCoreApplication.translate("Auth", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Auth", u"User Authentication", None))
#if QT_CONFIG(tooltip)
        self.miniBtn.setToolTip(QCoreApplication.translate("Auth", u"<html><head/><body><p>Click to minimize window</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.miniBtn.setText(QCoreApplication.translate("Auth", u"__", None))
#if QT_CONFIG(tooltip)
        self.exitBtn.setToolTip(QCoreApplication.translate("Auth", u"<html><head/><body><p>Click to exit app</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.exitBtn.setText(QCoreApplication.translate("Auth", u"X", None))
        self.imgView.setText("")
#if QT_CONFIG(tooltip)
        self.contactBtn.setToolTip(QCoreApplication.translate("Auth", u"<html><head/><body><p>Click to get author's details</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.contactBtn.setText(QCoreApplication.translate("Auth", u"Contact Author", None))
        self.label_3.setText(QCoreApplication.translate("Auth", u"Login", None))
        self.loginStatus.setText(QCoreApplication.translate("Auth", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Auth", u"Username:", None))
        self.userid.setText("")
        self.userid.setPlaceholderText(QCoreApplication.translate("Auth", u"Please input usersname here", None))
        self.label_5.setText(QCoreApplication.translate("Auth", u"Password:", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("Auth", u"Please Input Password here", None))
        self.loginBtn.setText(QCoreApplication.translate("Auth", u"login", None))
        self.spacer.setText("")
#if QT_CONFIG(tooltip)
        self.reglinkBtn.setToolTip(QCoreApplication.translate("Auth", u"<html><head/><body><p>Click to register new employees</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.reglinkBtn.setText(QCoreApplication.translate("Auth", u"Register", None))
#if QT_CONFIG(tooltip)
        self.updatelinkBtn.setToolTip(QCoreApplication.translate("Auth", u"<html><head/><body><p>Click to update record</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.updatelinkBtn.setText(QCoreApplication.translate("Auth", u"Forgot password", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Auth", u"Login Details", None))
        self.userlbl.setText(QCoreApplication.translate("Auth", u"Username", None))
        self.paswdlbl.setText(QCoreApplication.translate("Auth", u"Password", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Auth", u"Personal Details", None))
        self.rank.setItemText(0, QCoreApplication.translate("Auth", u"1", None))
        self.rank.setItemText(1, QCoreApplication.translate("Auth", u"2", None))
        self.rank.setItemText(2, QCoreApplication.translate("Auth", u"3", None))
        self.rank.setItemText(3, QCoreApplication.translate("Auth", u"4", None))
        self.rank.setItemText(4, QCoreApplication.translate("Auth", u"5", None))
        self.rank.setItemText(5, QCoreApplication.translate("Auth", u"6", None))
        self.rank.setItemText(6, QCoreApplication.translate("Auth", u"7", None))
        self.rank.setItemText(7, QCoreApplication.translate("Auth", u"8", None))
        self.rank.setItemText(8, QCoreApplication.translate("Auth", u"9", None))

        self.gender.setItemText(0, QCoreApplication.translate("Auth", u"Female", None))
        self.gender.setItemText(1, QCoreApplication.translate("Auth", u"Male", None))
        self.gender.setItemText(2, QCoreApplication.translate("Auth", u"Other", None))

        self.lnamelbl.setText(QCoreApplication.translate("Auth", u"Surname", None))
        self.idlbl.setText(QCoreApplication.translate("Auth", u"Employment ID", None))
        self.genlbl.setText(QCoreApplication.translate("Auth", u"Gender", None))
        self.firstName.setText("")
        self.fnamelbl.setText(QCoreApplication.translate("Auth", u"First Name", None))
        self.phonelbl.setText(QCoreApplication.translate("Auth", u"Phone No.", None))
        self.ranklbl.setText(QCoreApplication.translate("Auth", u"Rank", None))
        self.joblbl.setText(QCoreApplication.translate("Auth", u"Job Title", None))
        self.emaillbl.setText(QCoreApplication.translate("Auth", u"Email", None))
        self.deptlbl.setText(QCoreApplication.translate("Auth", u"Department", None))
        self.dept.setItemText(0, QCoreApplication.translate("Auth", u"Medical", None))
        self.dept.setItemText(1, QCoreApplication.translate("Auth", u"Pharmacy", None))
        self.dept.setItemText(2, QCoreApplication.translate("Auth", u"Laboratory", None))
        self.dept.setItemText(3, QCoreApplication.translate("Auth", u"Administration", None))
        self.dept.setItemText(4, QCoreApplication.translate("Auth", u"Reception", None))
        self.dept.setItemText(5, QCoreApplication.translate("Auth", u"Human Resource", None))
        self.dept.setItemText(6, QCoreApplication.translate("Auth", u"Account", None))

        self.jobtitle.setItemText(0, QCoreApplication.translate("Auth", u"Medical Doctor", None))
        self.jobtitle.setItemText(1, QCoreApplication.translate("Auth", u"Nurse", None))
        self.jobtitle.setItemText(2, QCoreApplication.translate("Auth", u"Receptionist", None))
        self.jobtitle.setItemText(3, QCoreApplication.translate("Auth", u"Principal HR", None))
        self.jobtitle.setItemText(4, QCoreApplication.translate("Auth", u"HR Officer", None))
        self.jobtitle.setItemText(5, QCoreApplication.translate("Auth", u"HR Manager", None))
        self.jobtitle.setItemText(6, QCoreApplication.translate("Auth", u"Chief Admin Officer", None))
        self.jobtitle.setItemText(7, QCoreApplication.translate("Auth", u"Admin Officer", None))
        self.jobtitle.setItemText(8, QCoreApplication.translate("Auth", u"Lab Scientist", None))
        self.jobtitle.setItemText(9, QCoreApplication.translate("Auth", u"Pharmacist", None))
        self.jobtitle.setItemText(10, QCoreApplication.translate("Auth", u"Accounting Officer", None))
        self.jobtitle.setItemText(11, QCoreApplication.translate("Auth", u"Chief Accounting Officer", None))

        self.regStatus.setText(QCoreApplication.translate("Auth", u"val", None))
        self.label_25.setText(QCoreApplication.translate("Auth", u"Employee Registration Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Auth", u"Authorized Signatory", None))
        self.regCancelBtn.setText(QCoreApplication.translate("Auth", u"Cancel", None))
        self.registerBtn.setText(QCoreApplication.translate("Auth", u"Register", None))
        self.authIdlbl.setText(QCoreApplication.translate("Auth", u"Authorized ID", None))
        self.authID.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("Auth", u"Personal Details", None))
        self.deptlbl_2.setText(QCoreApplication.translate("Auth", u"Department", None))
        self.phonelbl_2.setText(QCoreApplication.translate("Auth", u"Phone No.", None))
        self.emaillbl_2.setText(QCoreApplication.translate("Auth", u"Email", None))
        self.rank_2.setItemText(0, QCoreApplication.translate("Auth", u"1", None))
        self.rank_2.setItemText(1, QCoreApplication.translate("Auth", u"2", None))
        self.rank_2.setItemText(2, QCoreApplication.translate("Auth", u"3", None))
        self.rank_2.setItemText(3, QCoreApplication.translate("Auth", u"4", None))
        self.rank_2.setItemText(4, QCoreApplication.translate("Auth", u"5", None))
        self.rank_2.setItemText(5, QCoreApplication.translate("Auth", u"6", None))
        self.rank_2.setItemText(6, QCoreApplication.translate("Auth", u"7", None))
        self.rank_2.setItemText(7, QCoreApplication.translate("Auth", u"8", None))
        self.rank_2.setItemText(8, QCoreApplication.translate("Auth", u"9", None))

        self.ranklbl_2.setText(QCoreApplication.translate("Auth", u"Rank", None))
        self.joblbl_2.setText(QCoreApplication.translate("Auth", u"Job Title", None))
        self.jobtitle_2.setItemText(0, QCoreApplication.translate("Auth", u"Medical Doctor", None))
        self.jobtitle_2.setItemText(1, QCoreApplication.translate("Auth", u"Nurse", None))
        self.jobtitle_2.setItemText(2, QCoreApplication.translate("Auth", u"Receptionist", None))
        self.jobtitle_2.setItemText(3, QCoreApplication.translate("Auth", u"Principal HR", None))
        self.jobtitle_2.setItemText(4, QCoreApplication.translate("Auth", u"HR Officer", None))
        self.jobtitle_2.setItemText(5, QCoreApplication.translate("Auth", u"HR Manager", None))
        self.jobtitle_2.setItemText(6, QCoreApplication.translate("Auth", u"Chief Admin Officer", None))
        self.jobtitle_2.setItemText(7, QCoreApplication.translate("Auth", u"Admin Officer", None))
        self.jobtitle_2.setItemText(8, QCoreApplication.translate("Auth", u"Lab Scientist", None))
        self.jobtitle_2.setItemText(9, QCoreApplication.translate("Auth", u"Pharmacist", None))
        self.jobtitle_2.setItemText(10, QCoreApplication.translate("Auth", u"Accounting Officer", None))
        self.jobtitle_2.setItemText(11, QCoreApplication.translate("Auth", u"Chief Accounting Officer", None))

        self.dept_2.setItemText(0, QCoreApplication.translate("Auth", u"Medical", None))
        self.dept_2.setItemText(1, QCoreApplication.translate("Auth", u"Pharmacy", None))
        self.dept_2.setItemText(2, QCoreApplication.translate("Auth", u"Laboratory", None))
        self.dept_2.setItemText(3, QCoreApplication.translate("Auth", u"Administration", None))
        self.dept_2.setItemText(4, QCoreApplication.translate("Auth", u"Reception", None))
        self.dept_2.setItemText(5, QCoreApplication.translate("Auth", u"Human Resource", None))
        self.dept_2.setItemText(6, QCoreApplication.translate("Auth", u"Account", None))

        self.groupBox_6.setTitle(QCoreApplication.translate("Auth", u"Login Details", None))
        self.userlbl_2.setText(QCoreApplication.translate("Auth", u"Username", None))
        self.paswdlbl_2.setText(QCoreApplication.translate("Auth", u"Password", None))
        self.updateStatus.setText(QCoreApplication.translate("Auth", u"val", None))
        self.label_26.setText(QCoreApplication.translate("Auth", u"Employee Update Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Auth", u"Authorized Signatory", None))
        self.updateCancelBtn.setText(QCoreApplication.translate("Auth", u"Cancel", None))
        self.updateBtn.setText(QCoreApplication.translate("Auth", u"Update", None))
        self.authIdlbl_2.setText(QCoreApplication.translate("Auth", u"Authorized ID", None))
        self.authID_2.setText("")
    # retranslateUi

