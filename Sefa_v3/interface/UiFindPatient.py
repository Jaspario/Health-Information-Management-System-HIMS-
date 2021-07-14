# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FindPatient.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FindPatient(object):
    def setupUi(self, FindPatient):
        if not FindPatient.objectName():
            FindPatient.setObjectName(u"FindPatient")
        FindPatient.resize(542, 522)
        self.verticalLayout = QVBoxLayout(FindPatient)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bgLayer = QFrame(FindPatient)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setFrameShape(QFrame.StyledPanel)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.bgLayer)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 5, 2, 4)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.logo = QLabel(self.bgLayer)
        self.logo.setObjectName(u"logo")

        self.horizontalLayout_4.addWidget(self.logo)

        self.label_2 = QLabel(self.bgLayer)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(13)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 13, -1)
        self.miniBtn = QPushButton(self.bgLayer)
        self.miniBtn.setObjectName(u"miniBtn")
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(10)
        self.miniBtn.setFont(font)
        self.miniBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(self.bgLayer)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setFont(font)
        self.exitBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.exitBtn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.frame = QFrame(self.bgLayer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.bgframe = QFrame(self.frame)
        self.bgframe.setObjectName(u"bgframe")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bgframe.sizePolicy().hasHeightForWidth())
        self.bgframe.setSizePolicy(sizePolicy1)
        self.bgframe.setFrameShape(QFrame.Box)
        self.bgframe.setFrameShadow(QFrame.Raised)
        self.bgframe.setLineWidth(2)
        self.bgframe.setMidLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.bgframe)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 13)
        self.label = QLabel(self.bgframe)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(12)
        font1.setUnderline(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchBtn = QPushButton(self.bgframe)
        self.searchBtn.setObjectName(u"searchBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamily(u"Comic Sans MS")
        font2.setPointSize(8)
        self.searchBtn.setFont(font2)

        self.horizontalLayout_2.addWidget(self.searchBtn)

        self.searchField = QLineEdit(self.bgframe)
        self.searchField.setObjectName(u"searchField")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(4)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.searchField.sizePolicy().hasHeightForWidth())
        self.searchField.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(8)
        self.searchField.setFont(font3)
        self.searchField.setAcceptDrops(False)

        self.horizontalLayout_2.addWidget(self.searchField)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.searchlbl = QLabel(self.bgframe)
        self.searchlbl.setObjectName(u"searchlbl")
        font4 = QFont()
        font4.setFamily(u"Courier New")
        font4.setPointSize(7)
        font4.setBold(True)
        font4.setItalic(True)
        font4.setWeight(75)
        self.searchlbl.setFont(font4)
        self.searchlbl.setMargin(0)

        self.verticalLayout_2.addWidget(self.searchlbl)

        self.pinfoBox = QGroupBox(self.bgframe)
        self.pinfoBox.setObjectName(u"pinfoBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(3)
        sizePolicy5.setVerticalStretch(2)
        sizePolicy5.setHeightForWidth(self.pinfoBox.sizePolicy().hasHeightForWidth())
        self.pinfoBox.setSizePolicy(sizePolicy5)
        font5 = QFont()
        font5.setFamily(u"Tahoma")
        font5.setPointSize(7)
        font5.setBold(True)
        font5.setWeight(75)
        self.pinfoBox.setFont(font5)
        self.horizontalLayout_7 = QHBoxLayout(self.pinfoBox)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 19, -1, -1)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(15)
        self.formLayout_2.setContentsMargins(4, 2, 4, 2)
        self.label_3 = QLabel(self.pinfoBox)
        self.label_3.setObjectName(u"label_3")
        font6 = QFont()
        font6.setFamily(u"Georgia")
        font6.setPointSize(7)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_3.setFont(font6)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.fnamelbl = QLabel(self.pinfoBox)
        self.fnamelbl.setObjectName(u"fnamelbl")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.fnamelbl.sizePolicy().hasHeightForWidth())
        self.fnamelbl.setSizePolicy(sizePolicy6)
        font7 = QFont()
        font7.setFamily(u"Times New Roman")
        font7.setPointSize(7)
        font7.setBold(False)
        font7.setWeight(50)
        self.fnamelbl.setFont(font7)
        self.fnamelbl.setAutoFillBackground(True)
        self.fnamelbl.setFrameShape(QFrame.StyledPanel)
        self.fnamelbl.setWordWrap(True)
        self.fnamelbl.setMargin(5)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.fnamelbl)

        self.label_7 = QLabel(self.pinfoBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font6)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.label_11 = QLabel(self.pinfoBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font6)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.doctorlbl = QLabel(self.pinfoBox)
        self.doctorlbl.setObjectName(u"doctorlbl")
        self.doctorlbl.setFont(font7)
        self.doctorlbl.setAutoFillBackground(True)
        self.doctorlbl.setFrameShape(QFrame.StyledPanel)
        self.doctorlbl.setWordWrap(True)
        self.doctorlbl.setMargin(5)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.doctorlbl)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.genderlbl = QLabel(self.pinfoBox)
        self.genderlbl.setObjectName(u"genderlbl")
        self.genderlbl.setFont(font7)
        self.genderlbl.setAutoFillBackground(True)
        self.genderlbl.setFrameShape(QFrame.StyledPanel)
        self.genderlbl.setWordWrap(True)
        self.genderlbl.setMargin(5)

        self.horizontalLayout_6.addWidget(self.genderlbl)

        self.label_8 = QLabel(self.pinfoBox)
        self.label_8.setObjectName(u"label_8")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy7)
        self.label_8.setFont(font6)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.agelbl = QLabel(self.pinfoBox)
        self.agelbl.setObjectName(u"agelbl")
        self.agelbl.setFont(font7)
        self.agelbl.setAutoFillBackground(True)
        self.agelbl.setFrameShape(QFrame.StyledPanel)
        self.agelbl.setWordWrap(True)
        self.agelbl.setMargin(5)

        self.horizontalLayout_6.addWidget(self.agelbl)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.label_5 = QLabel(self.pinfoBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font6)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.classlbl = QLabel(self.pinfoBox)
        self.classlbl.setObjectName(u"classlbl")
        font8 = QFont()
        font8.setFamily(u"Times New Roman")
        font8.setPointSize(7)
        font8.setBold(True)
        font8.setWeight(75)
        self.classlbl.setFont(font8)
        self.classlbl.setAutoFillBackground(True)
        self.classlbl.setFrameShape(QFrame.StyledPanel)
        self.classlbl.setWordWrap(True)
        self.classlbl.setMargin(5)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.classlbl)


        self.horizontalLayout_7.addLayout(self.formLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(4, 2, 4, 2)
        self.label_4 = QLabel(self.pinfoBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font6)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lnamelbl = QLabel(self.pinfoBox)
        self.lnamelbl.setObjectName(u"lnamelbl")
        sizePolicy6.setHeightForWidth(self.lnamelbl.sizePolicy().hasHeightForWidth())
        self.lnamelbl.setSizePolicy(sizePolicy6)
        self.lnamelbl.setFont(font7)
        self.lnamelbl.setAutoFillBackground(True)
        self.lnamelbl.setFrameShape(QFrame.StyledPanel)
        self.lnamelbl.setWordWrap(True)
        self.lnamelbl.setMargin(5)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lnamelbl)

        self.pnumlbl = QLabel(self.pinfoBox)
        self.pnumlbl.setObjectName(u"pnumlbl")
        self.pnumlbl.setFont(font7)
        self.pnumlbl.setAutoFillBackground(True)
        self.pnumlbl.setFrameShape(QFrame.StyledPanel)
        self.pnumlbl.setWordWrap(True)
        self.pnumlbl.setMargin(5)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pnumlbl)

        self.label_10 = QLabel(self.pinfoBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font6)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.label_13 = QLabel(self.pinfoBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font6)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.pstatuslbl = QLabel(self.pinfoBox)
        self.pstatuslbl.setObjectName(u"pstatuslbl")
        self.pstatuslbl.setFont(font7)
        self.pstatuslbl.setAutoFillBackground(True)
        self.pstatuslbl.setFrameShape(QFrame.StyledPanel)
        self.pstatuslbl.setWordWrap(True)
        self.pstatuslbl.setMargin(5)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pstatuslbl)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lastvisitlbl = QLabel(self.pinfoBox)
        self.lastvisitlbl.setObjectName(u"lastvisitlbl")
        self.lastvisitlbl.setFont(font7)
        self.lastvisitlbl.setAutoFillBackground(True)
        self.lastvisitlbl.setFrameShape(QFrame.StyledPanel)
        self.lastvisitlbl.setWordWrap(True)
        self.lastvisitlbl.setMargin(5)

        self.horizontalLayout_8.addWidget(self.lastvisitlbl)

        self.label_17 = QLabel(self.pinfoBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font6)

        self.horizontalLayout_8.addWidget(self.label_17)

        self.regdatelbl = QLabel(self.pinfoBox)
        self.regdatelbl.setObjectName(u"regdatelbl")
        self.regdatelbl.setFont(font7)
        self.regdatelbl.setAutoFillBackground(True)
        self.regdatelbl.setFrameShape(QFrame.StyledPanel)
        self.regdatelbl.setWordWrap(True)
        self.regdatelbl.setMargin(5)

        self.horizontalLayout_8.addWidget(self.regdatelbl)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_8)

        self.label_15 = QLabel(self.pinfoBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font6)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_15)


        self.horizontalLayout_7.addLayout(self.formLayout)


        self.verticalLayout_2.addWidget(self.pinfoBox)

        self.frame_3 = QFrame(self.bgframe)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(2)
        sizePolicy8.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy8)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.viewBtn = QPushButton(self.frame_3)
        self.viewBtn.setObjectName(u"viewBtn")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.viewBtn.sizePolicy().hasHeightForWidth())
        self.viewBtn.setSizePolicy(sizePolicy9)
        font9 = QFont()
        font9.setFamily(u"Comic Sans MS")
        font9.setPointSize(11)
        self.viewBtn.setFont(font9)

        self.horizontalLayout_5.addWidget(self.viewBtn)

        self.newBtn = QPushButton(self.frame_3)
        self.newBtn.setObjectName(u"newBtn")
        sizePolicy9.setHeightForWidth(self.newBtn.sizePolicy().hasHeightForWidth())
        self.newBtn.setSizePolicy(sizePolicy9)
        self.newBtn.setFont(font9)

        self.horizontalLayout_5.addWidget(self.newBtn)

        self.bookBtn = QPushButton(self.frame_3)
        self.bookBtn.setObjectName(u"bookBtn")
        sizePolicy9.setHeightForWidth(self.bookBtn.sizePolicy().hasHeightForWidth())
        self.bookBtn.setSizePolicy(sizePolicy9)
        self.bookBtn.setFont(font9)

        self.horizontalLayout_5.addWidget(self.bookBtn)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sendBtn = QPushButton(self.bgframe)
        self.sendBtn.setObjectName(u"sendBtn")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.sendBtn.sizePolicy().hasHeightForWidth())
        self.sendBtn.setSizePolicy(sizePolicy10)
        self.sendBtn.setMinimumSize(QSize(136, 0))
        font10 = QFont()
        font10.setFamily(u"Comic Sans MS")
        font10.setPointSize(9)
        font10.setBold(False)
        font10.setWeight(50)
        self.sendBtn.setFont(font10)

        self.horizontalLayout_3.addWidget(self.sendBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.closeBtn = QPushButton(self.bgframe)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy10.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy10)
        self.closeBtn.setFont(font10)

        self.horizontalLayout_3.addWidget(self.closeBtn)

        self.logoutBtn = QPushButton(self.bgframe)
        self.logoutBtn.setObjectName(u"logoutBtn")
        sizePolicy10.setHeightForWidth(self.logoutBtn.sizePolicy().hasHeightForWidth())
        self.logoutBtn.setSizePolicy(sizePolicy10)
        self.logoutBtn.setFont(font10)

        self.horizontalLayout_3.addWidget(self.logoutBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.bgframe, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame)

        self.progressBar = QProgressBar(self.bgLayer)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.bgLayer)


        self.retranslateUi(FindPatient)

        QMetaObject.connectSlotsByName(FindPatient)
    # setupUi

    def retranslateUi(self, FindPatient):
        FindPatient.setWindowTitle(QCoreApplication.translate("FindPatient", u"Find Patient", None))
        self.logo.setText(QCoreApplication.translate("FindPatient", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("FindPatient", u"Find Patient", None))
        self.miniBtn.setText(QCoreApplication.translate("FindPatient", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("FindPatient", u"X", None))
        self.label.setText(QCoreApplication.translate("FindPatient", u"Find Patient", None))
#if QT_CONFIG(tooltip)
        self.searchBtn.setToolTip(QCoreApplication.translate("FindPatient", u"<html><head/><body><p>Click to search for patient's record</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.searchBtn.setText(QCoreApplication.translate("FindPatient", u"Search", None))
        self.searchField.setText("")
        self.searchField.setPlaceholderText(QCoreApplication.translate("FindPatient", u"Please input Patient's firstname and lastname or Patient's Number", None))
        self.searchlbl.setText("")
        self.pinfoBox.setTitle(QCoreApplication.translate("FindPatient", u"Patient's Information Summary:", None))
        self.label_3.setText(QCoreApplication.translate("FindPatient", u"First Name:", None))
        self.fnamelbl.setText("")
        self.label_7.setText(QCoreApplication.translate("FindPatient", u"Gender:", None))
        self.label_11.setText(QCoreApplication.translate("FindPatient", u"Last Seen By:", None))
        self.doctorlbl.setText("")
        self.genderlbl.setText("")
        self.label_8.setText(QCoreApplication.translate("FindPatient", u"Age:", None))
        self.agelbl.setText("")
        self.label_5.setText(QCoreApplication.translate("FindPatient", u"Class:", None))
        self.classlbl.setText("")
        self.label_4.setText(QCoreApplication.translate("FindPatient", u"Last Name:", None))
        self.lnamelbl.setText("")
        self.pnumlbl.setText("")
        self.label_10.setText(QCoreApplication.translate("FindPatient", u"Patient's No.: ", None))
        self.label_13.setText(QCoreApplication.translate("FindPatient", u"Patient's Status:", None))
        self.pstatuslbl.setText("")
        self.lastvisitlbl.setText("")
        self.label_17.setText(QCoreApplication.translate("FindPatient", u"Last Visit:", None))
        self.regdatelbl.setText("")
        self.label_15.setText(QCoreApplication.translate("FindPatient", u"Reg Date:", None))
#if QT_CONFIG(tooltip)
        self.viewBtn.setToolTip(QCoreApplication.translate("FindPatient", u"<html><head/><body><p>Click here to view patient's medical record</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.viewBtn.setText(QCoreApplication.translate("FindPatient", u"View Record", None))
#if QT_CONFIG(tooltip)
        self.newBtn.setToolTip(QCoreApplication.translate("FindPatient", u"<html><head/><body><p>Click here to register a new patient</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.newBtn.setText(QCoreApplication.translate("FindPatient", u"New Patient", None))
#if QT_CONFIG(tooltip)
        self.bookBtn.setToolTip(QCoreApplication.translate("FindPatient", u"<html><head/><body><p>Click here to book an appointment</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bookBtn.setText(QCoreApplication.translate("FindPatient", u"Book Appointment", None))
#if QT_CONFIG(tooltip)
        self.sendBtn.setToolTip(QCoreApplication.translate("FindPatient", u"<html><head/><body><p>Click to send patient's file</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sendBtn.setText(QCoreApplication.translate("FindPatient", u"Send File", None))
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("FindPatient", u"<html><head/><body><p>Click to close patient's record</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText(QCoreApplication.translate("FindPatient", u"Close Record", None))
#if QT_CONFIG(tooltip)
        self.logoutBtn.setToolTip(QCoreApplication.translate("FindPatient", u"<html><head/><body><p>Click to logout</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.logoutBtn.setText(QCoreApplication.translate("FindPatient", u"Log Out", None))
    # retranslateUi

