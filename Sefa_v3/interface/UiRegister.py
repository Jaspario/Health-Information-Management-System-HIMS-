# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(731, 793)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Register.sizePolicy().hasHeightForWidth())
        Register.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(Register)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.bgflayer = QFrame(Register)
        self.bgflayer.setObjectName(u"bgflayer")
        self.bgflayer.setFocusPolicy(Qt.StrongFocus)
        self.bgflayer.setAutoFillBackground(False)
        self.bgflayer.setFrameShape(QFrame.StyledPanel)
        self.bgflayer.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.bgflayer)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(9)
        self.gridLayout_5.setVerticalSpacing(5)
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.bgfFrame = QFrame(self.bgflayer)
        self.bgfFrame.setObjectName(u"bgfFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bgfFrame.sizePolicy().hasHeightForWidth())
        self.bgfFrame.setSizePolicy(sizePolicy1)
        self.bgfFrame.setAutoFillBackground(True)
        self.bgfFrame.setFrameShape(QFrame.Box)
        self.bgfFrame.setFrameShadow(QFrame.Raised)
        self.bgfFrame.setLineWidth(2)
        self.bgfFrame.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgfFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, -1, 6, -1)
        self.bookBtn = QPushButton(self.bgfFrame)
        self.bookBtn.setObjectName(u"bookBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(3)
        sizePolicy2.setHeightForWidth(self.bookBtn.sizePolicy().hasHeightForWidth())
        self.bookBtn.setSizePolicy(sizePolicy2)
        self.bookBtn.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(8)
        self.bookBtn.setFont(font)
        self.bookBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bookBtn.setAutoFillBackground(False)
        self.bookBtn.setStyleSheet(u"background-color: rgb(118, 118, 118);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.bookBtn)

        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(self.bgfFrame)
        self.cancelBtn.setObjectName(u"cancelBtn")
        sizePolicy2.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy2)
        self.cancelBtn.setMinimumSize(QSize(0, 30))
        self.cancelBtn.setFont(font)
        self.cancelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelBtn.setAutoFillBackground(False)
        self.cancelBtn.setStyleSheet(u"background-color: rgb(118, 118, 118);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.regBtn = QPushButton(self.bgfFrame)
        self.regBtn.setObjectName(u"regBtn")
        sizePolicy2.setHeightForWidth(self.regBtn.sizePolicy().hasHeightForWidth())
        self.regBtn.setSizePolicy(sizePolicy2)
        self.regBtn.setMinimumSize(QSize(0, 30))
        self.regBtn.setFont(font)
        self.regBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.regBtn.setAutoFillBackground(False)
        self.regBtn.setStyleSheet(u"background-color: rgb(118, 118, 118);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.regBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.bgfFrame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.groupBox_3.setFlat(True)
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.groupBox_3)
        self.frame.setObjectName(u"frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, -1, -1, 4)
        self.pfnamelbl = QLabel(self.frame)
        self.pfnamelbl.setObjectName(u"pfnamelbl")
        self.pfnamelbl.setAlignment(Qt.AlignCenter)
        self.pfnamelbl.setWordWrap(True)
        self.pfnamelbl.setMargin(5)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pfnamelbl)

        self.pfname = QLineEdit(self.frame)
        self.pfname.setObjectName(u"pfname")
        self.pfname.setMinimumSize(QSize(0, 0))
        self.pfname.setFont(font)
        self.pfname.setAutoFillBackground(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.pfname)

        self.plnamelbl = QLabel(self.frame)
        self.plnamelbl.setObjectName(u"plnamelbl")
        self.plnamelbl.setAlignment(Qt.AlignCenter)
        self.plnamelbl.setWordWrap(True)
        self.plnamelbl.setMargin(5)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.plnamelbl)

        self.plname = QLineEdit(self.frame)
        self.plname.setObjectName(u"plname")
        self.plname.setFont(font)
        self.plname.setAutoFillBackground(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.plname)

        self.ponamelbl = QLabel(self.frame)
        self.ponamelbl.setObjectName(u"ponamelbl")
        self.ponamelbl.setAlignment(Qt.AlignCenter)
        self.ponamelbl.setWordWrap(True)
        self.ponamelbl.setMargin(5)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.ponamelbl)

        self.poname = QLineEdit(self.frame)
        self.poname.setObjectName(u"poname")
        self.poname.setFont(font)
        self.poname.setAutoFillBackground(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.poname)

        self.pgenderlbl = QLabel(self.frame)
        self.pgenderlbl.setObjectName(u"pgenderlbl")
        self.pgenderlbl.setAlignment(Qt.AlignCenter)
        self.pgenderlbl.setWordWrap(True)
        self.pgenderlbl.setMargin(5)
        self.pgenderlbl.setIndent(2)
        self.pgenderlbl.setOpenExternalLinks(False)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.pgenderlbl)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pgender = QComboBox(self.frame)
        self.pgender.addItem("")
        self.pgender.addItem("")
        self.pgender.addItem("")
        self.pgender.setObjectName(u"pgender")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pgender.sizePolicy().hasHeightForWidth())
        self.pgender.setSizePolicy(sizePolicy5)
        self.pgender.setFont(font)

        self.horizontalLayout_14.addWidget(self.pgender)

        self.pagelbl = QLabel(self.frame)
        self.pagelbl.setObjectName(u"pagelbl")
        self.pagelbl.setAlignment(Qt.AlignCenter)
        self.pagelbl.setWordWrap(True)
        self.pagelbl.setMargin(6)

        self.horizontalLayout_14.addWidget(self.pagelbl)

        self.page = QLineEdit(self.frame)
        self.page.setObjectName(u"page")
        self.page.setFont(font)
        self.page.setAutoFillBackground(True)

        self.horizontalLayout_14.addWidget(self.page)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_14)

        self.pclasslbl = QLabel(self.frame)
        self.pclasslbl.setObjectName(u"pclasslbl")
        self.pclasslbl.setAlignment(Qt.AlignCenter)
        self.pclasslbl.setWordWrap(True)
        self.pclasslbl.setMargin(5)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.pclasslbl)

        self.pclass = QComboBox(self.frame)
        self.pclass.addItem("")
        self.pclass.addItem("")
        self.pclass.addItem("")
        self.pclass.addItem("")
        self.pclass.setObjectName(u"pclass")
        sizePolicy5.setHeightForWidth(self.pclass.sizePolicy().hasHeightForWidth())
        self.pclass.setSizePolicy(sizePolicy5)
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(8)
        self.pclass.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pclass)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.paddressL1lbl = QLabel(self.groupBox_3)
        self.paddressL1lbl.setObjectName(u"paddressL1lbl")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.paddressL1lbl.sizePolicy().hasHeightForWidth())
        self.paddressL1lbl.setSizePolicy(sizePolicy6)
        self.paddressL1lbl.setAlignment(Qt.AlignCenter)
        self.paddressL1lbl.setWordWrap(True)
        self.paddressL1lbl.setMargin(5)

        self.horizontalLayout_3.addWidget(self.paddressL1lbl)

        self.paddressL1 = QLineEdit(self.groupBox_3)
        self.paddressL1.setObjectName(u"paddressL1")
        self.paddressL1.setFont(font)
        self.paddressL1.setAutoFillBackground(True)

        self.horizontalLayout_3.addWidget(self.paddressL1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pstatelbl = QLabel(self.groupBox_3)
        self.pstatelbl.setObjectName(u"pstatelbl")
        self.pstatelbl.setMargin(5)

        self.horizontalLayout_4.addWidget(self.pstatelbl)

        self.pstate = QLineEdit(self.groupBox_3)
        self.pstate.setObjectName(u"pstate")

        self.horizontalLayout_4.addWidget(self.pstate)

        self.pcountrylbl = QLabel(self.groupBox_3)
        self.pcountrylbl.setObjectName(u"pcountrylbl")
        sizePolicy6.setHeightForWidth(self.pcountrylbl.sizePolicy().hasHeightForWidth())
        self.pcountrylbl.setSizePolicy(sizePolicy6)
        self.pcountrylbl.setAlignment(Qt.AlignCenter)
        self.pcountrylbl.setMargin(5)

        self.horizontalLayout_4.addWidget(self.pcountrylbl)

        self.pcountry = QLineEdit(self.groupBox_3)
        self.pcountry.setObjectName(u"pcountry")
        self.pcountry.setFont(font)
        self.pcountry.setAutoFillBackground(True)

        self.horizontalLayout_4.addWidget(self.pcountry)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 2)

        self.frame_2 = QFrame(self.groupBox_3)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.formLayout_2 = QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(-1, -1, -1, 5)
        self.pmobilelbl = QLabel(self.frame_2)
        self.pmobilelbl.setObjectName(u"pmobilelbl")
        self.pmobilelbl.setAlignment(Qt.AlignCenter)
        self.pmobilelbl.setWordWrap(True)
        self.pmobilelbl.setMargin(5)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.pmobilelbl)

        self.pmobile = QLineEdit(self.frame_2)
        self.pmobile.setObjectName(u"pmobile")
        self.pmobile.setFont(font)
        self.pmobile.setAutoFillBackground(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.pmobile)

        self.pemaillbl = QLabel(self.frame_2)
        self.pemaillbl.setObjectName(u"pemaillbl")
        self.pemaillbl.setAlignment(Qt.AlignCenter)
        self.pemaillbl.setMargin(5)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.pemaillbl)

        self.pemail = QLineEdit(self.frame_2)
        self.pemail.setObjectName(u"pemail")
        self.pemail.setFont(font)
        self.pemail.setAutoFillBackground(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.pemail)

        self.poriginlbl = QLabel(self.frame_2)
        self.poriginlbl.setObjectName(u"poriginlbl")
        self.poriginlbl.setAlignment(Qt.AlignCenter)
        self.poriginlbl.setWordWrap(True)
        self.poriginlbl.setMargin(5)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.poriginlbl)

        self.porigin = QLineEdit(self.frame_2)
        self.porigin.setObjectName(u"porigin")
        self.porigin.setFont(font)
        self.porigin.setAutoFillBackground(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.porigin)

        self.pnumberlbl = QLabel(self.frame_2)
        self.pnumberlbl.setObjectName(u"pnumberlbl")
        self.pnumberlbl.setMargin(5)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.pnumberlbl)

        self.pnumber = QLineEdit(self.frame_2)
        self.pnumber.setObjectName(u"pnumber")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.pnumber)

        self.pstatuslbl = QLabel(self.frame_2)
        self.pstatuslbl.setObjectName(u"pstatuslbl")
        self.pstatuslbl.setMargin(5)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.pstatuslbl)

        self.pstatus = QComboBox(self.frame_2)
        self.pstatus.addItem("")
        self.pstatus.addItem("")
        self.pstatus.addItem("")
        self.pstatus.setObjectName(u"pstatus")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.pstatus)

        self.pnationalitylbl = QLabel(self.frame_2)
        self.pnationalitylbl.setObjectName(u"pnationalitylbl")
        self.pnationalitylbl.setAlignment(Qt.AlignCenter)
        self.pnationalitylbl.setMargin(5)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.pnationalitylbl)

        self.pnationality = QLineEdit(self.frame_2)
        self.pnationality.setObjectName(u"pnationality")
        self.pnationality.setFont(font)
        self.pnationality.setAutoFillBackground(True)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.pnationality)


        self.gridLayout_3.addWidget(self.frame_2, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.pinfo = QLabel(self.bgfFrame)
        self.pinfo.setObjectName(u"pinfo")
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(6)
        font2.setItalic(True)
        self.pinfo.setFont(font2)
        self.pinfo.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.pinfo, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.bgfFrame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.groupBox_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.formLayout_3 = QFormLayout(self.frame_4)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.pkfnamelbl = QLabel(self.frame_4)
        self.pkfnamelbl.setObjectName(u"pkfnamelbl")
        self.pkfnamelbl.setAlignment(Qt.AlignCenter)
        self.pkfnamelbl.setWordWrap(True)
        self.pkfnamelbl.setMargin(5)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.pkfnamelbl)

        self.pkfname = QLineEdit(self.frame_4)
        self.pkfname.setObjectName(u"pkfname")
        self.pkfname.setMinimumSize(QSize(0, 0))
        self.pkfname.setFont(font)
        self.pkfname.setAutoFillBackground(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.pkfname)

        self.pklnamelbl = QLabel(self.frame_4)
        self.pklnamelbl.setObjectName(u"pklnamelbl")
        self.pklnamelbl.setAlignment(Qt.AlignCenter)
        self.pklnamelbl.setWordWrap(True)
        self.pklnamelbl.setMargin(5)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.pklnamelbl)

        self.pklname = QLineEdit(self.frame_4)
        self.pklname.setObjectName(u"pklname")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.pklname)


        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.groupBox_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy4.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy4)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.formLayout_4 = QFormLayout(self.frame_6)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.pkrelationshiplbl = QLabel(self.frame_6)
        self.pkrelationshiplbl.setObjectName(u"pkrelationshiplbl")
        self.pkrelationshiplbl.setAlignment(Qt.AlignCenter)
        self.pkrelationshiplbl.setWordWrap(True)
        self.pkrelationshiplbl.setMargin(5)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.pkrelationshiplbl)

        self.pkrelationship = QComboBox(self.frame_6)
        self.pkrelationship.addItem("")
        self.pkrelationship.addItem("")
        self.pkrelationship.addItem("")
        self.pkrelationship.addItem("")
        self.pkrelationship.addItem("")
        self.pkrelationship.addItem("")
        self.pkrelationship.addItem("")
        self.pkrelationship.setObjectName(u"pkrelationship")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.pkrelationship)

        self.pkmobilelbl = QLabel(self.frame_6)
        self.pkmobilelbl.setObjectName(u"pkmobilelbl")
        self.pkmobilelbl.setAlignment(Qt.AlignCenter)
        self.pkmobilelbl.setWordWrap(True)
        self.pkmobilelbl.setMargin(5)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.pkmobilelbl)

        self.pkmobile = QLineEdit(self.frame_6)
        self.pkmobile.setObjectName(u"pkmobile")
        self.pkmobile.setFont(font)
        self.pkmobile.setAutoFillBackground(True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.pkmobile)


        self.gridLayout.addWidget(self.frame_6, 1, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pkaddressL1lbl = QLabel(self.groupBox_2)
        self.pkaddressL1lbl.setObjectName(u"pkaddressL1lbl")
        sizePolicy6.setHeightForWidth(self.pkaddressL1lbl.sizePolicy().hasHeightForWidth())
        self.pkaddressL1lbl.setSizePolicy(sizePolicy6)
        self.pkaddressL1lbl.setAlignment(Qt.AlignCenter)
        self.pkaddressL1lbl.setWordWrap(True)
        self.pkaddressL1lbl.setMargin(5)

        self.horizontalLayout_5.addWidget(self.pkaddressL1lbl)

        self.pkaddressL1 = QLineEdit(self.groupBox_2)
        self.pkaddressL1.setObjectName(u"pkaddressL1")
        self.pkaddressL1.setFont(font)
        self.pkaddressL1.setAutoFillBackground(True)

        self.horizontalLayout_5.addWidget(self.pkaddressL1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pkstatelbl = QLabel(self.groupBox_2)
        self.pkstatelbl.setObjectName(u"pkstatelbl")
        sizePolicy6.setHeightForWidth(self.pkstatelbl.sizePolicy().hasHeightForWidth())
        self.pkstatelbl.setSizePolicy(sizePolicy6)
        self.pkstatelbl.setAlignment(Qt.AlignCenter)
        self.pkstatelbl.setMargin(5)

        self.horizontalLayout_6.addWidget(self.pkstatelbl)

        self.pkstate = QLineEdit(self.groupBox_2)
        self.pkstate.setObjectName(u"pkstate")
        self.pkstate.setFont(font)
        self.pkstate.setAutoFillBackground(True)

        self.horizontalLayout_6.addWidget(self.pkstate)

        self.pkcountrylbl = QLabel(self.groupBox_2)
        self.pkcountrylbl.setObjectName(u"pkcountrylbl")
        self.pkcountrylbl.setMargin(5)

        self.horizontalLayout_6.addWidget(self.pkcountrylbl)

        self.pkcountry = QLineEdit(self.groupBox_2)
        self.pkcountry.setObjectName(u"pkcountry")

        self.horizontalLayout_6.addWidget(self.pkcountry)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox_2, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.bgfFrame)
        self.label.setObjectName(u"label")
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(16)
        font3.setUnderline(True)
        self.label.setFont(font3)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(6)

        self.horizontalLayout_2.addWidget(self.label)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.bgfFrame, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, -1, 2, -1)
        self.logo = QLabel(self.bgflayer)
        self.logo.setObjectName(u"logo")

        self.horizontalLayout_7.addWidget(self.logo)

        self.bgflbl = QLabel(self.bgflayer)
        self.bgflbl.setObjectName(u"bgflbl")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.bgflbl.sizePolicy().hasHeightForWidth())
        self.bgflbl.setSizePolicy(sizePolicy7)

        self.horizontalLayout_7.addWidget(self.bgflbl)

        self.miniBtn = QPushButton(self.bgflayer)
        self.miniBtn.setObjectName(u"miniBtn")
        sizePolicy.setHeightForWidth(self.miniBtn.sizePolicy().hasHeightForWidth())
        self.miniBtn.setSizePolicy(sizePolicy)
        self.miniBtn.setFont(font)
        self.miniBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.miniBtn.setMouseTracking(True)
        self.miniBtn.setTabletTracking(True)
        self.miniBtn.setAutoFillBackground(False)
        self.miniBtn.setAutoDefault(False)
        self.miniBtn.setFlat(False)

        self.horizontalLayout_7.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(self.bgflayer)
        self.exitBtn.setObjectName(u"exitBtn")
        sizePolicy.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy)
        self.exitBtn.setMaximumSize(QSize(16777215, 16777215))
        self.exitBtn.setFont(font)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setMouseTracking(True)
        self.exitBtn.setTabletTracking(True)
        self.exitBtn.setLayoutDirection(Qt.LeftToRight)
        self.exitBtn.setAutoFillBackground(False)
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setFlat(False)

        self.horizontalLayout_7.addWidget(self.exitBtn)


        self.gridLayout_5.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.bgflayer, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)


        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Dialog", None))
        self.bookBtn.setText(QCoreApplication.translate("Register", u"Book Appointment", None))
        self.cancelBtn.setText(QCoreApplication.translate("Register", u"Cancel", None))
        self.regBtn.setText(QCoreApplication.translate("Register", u"Register", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Register", u"Patient's Details", None))
        self.pfnamelbl.setText(QCoreApplication.translate("Register", u"First Name:", None))
        self.plnamelbl.setText(QCoreApplication.translate("Register", u"Last Name:", None))
        self.ponamelbl.setText(QCoreApplication.translate("Register", u"Other Name:", None))
        self.pgenderlbl.setText(QCoreApplication.translate("Register", u"Gender:", None))
        self.pgender.setItemText(0, QCoreApplication.translate("Register", u"Male", None))
        self.pgender.setItemText(1, QCoreApplication.translate("Register", u"Female", None))
        self.pgender.setItemText(2, QCoreApplication.translate("Register", u"Other", None))

        self.pagelbl.setText(QCoreApplication.translate("Register", u"Age:", None))
        self.pclasslbl.setText(QCoreApplication.translate("Register", u"Class:", None))
        self.pclass.setItemText(0, QCoreApplication.translate("Register", u"Private", None))
        self.pclass.setItemText(1, QCoreApplication.translate("Register", u"Company", None))
        self.pclass.setItemText(2, QCoreApplication.translate("Register", u"HMO", None))
        self.pclass.setItemText(3, QCoreApplication.translate("Register", u"Family", None))

        self.paddressL1lbl.setText(QCoreApplication.translate("Register", u"Street: ", None))
        self.pstatelbl.setText(QCoreApplication.translate("Register", u"State:  ", None))
        self.pcountrylbl.setText(QCoreApplication.translate("Register", u"Country:", None))
        self.pmobilelbl.setText(QCoreApplication.translate("Register", u"Mobile:", None))
        self.pemaillbl.setText(QCoreApplication.translate("Register", u"Email: ", None))
        self.poriginlbl.setText(QCoreApplication.translate("Register", u"State of Origin:", None))
        self.pnumberlbl.setText(QCoreApplication.translate("Register", u"Patient Number:", None))
        self.pstatuslbl.setText(QCoreApplication.translate("Register", u"Status:", None))
        self.pstatus.setItemText(0, QCoreApplication.translate("Register", u"In-patient", None))
        self.pstatus.setItemText(1, QCoreApplication.translate("Register", u"Out-patient", None))
        self.pstatus.setItemText(2, QCoreApplication.translate("Register", u"Discharged", None))

        self.pnationalitylbl.setText(QCoreApplication.translate("Register", u"Nationality:", None))
        self.pinfo.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Register", u"Next of Kin Details:", None))
        self.pkfnamelbl.setText(QCoreApplication.translate("Register", u"First Name:", None))
        self.pklnamelbl.setText(QCoreApplication.translate("Register", u"Last Name:", None))
        self.pkrelationshiplbl.setText(QCoreApplication.translate("Register", u"Relationship:", None))
        self.pkrelationship.setItemText(0, QCoreApplication.translate("Register", u"Father", None))
        self.pkrelationship.setItemText(1, QCoreApplication.translate("Register", u"Mother", None))
        self.pkrelationship.setItemText(2, QCoreApplication.translate("Register", u"Husband", None))
        self.pkrelationship.setItemText(3, QCoreApplication.translate("Register", u"Wife", None))
        self.pkrelationship.setItemText(4, QCoreApplication.translate("Register", u"Brother", None))
        self.pkrelationship.setItemText(5, QCoreApplication.translate("Register", u"Sister", None))
        self.pkrelationship.setItemText(6, QCoreApplication.translate("Register", u"Friend", None))

        self.pkmobilelbl.setText(QCoreApplication.translate("Register", u"Mobile:", None))
        self.pkaddressL1lbl.setText(QCoreApplication.translate("Register", u"Street:", None))
        self.pkstatelbl.setText(QCoreApplication.translate("Register", u"State:  ", None))
        self.pkcountrylbl.setText(QCoreApplication.translate("Register", u"Country:", None))
        self.label.setText(QCoreApplication.translate("Register", u"Patient's Registration Form", None))
        self.logo.setText(QCoreApplication.translate("Register", u"logo", None))
        self.bgflbl.setText(QCoreApplication.translate("Register", u"Register New Patient", None))
        self.miniBtn.setText(QCoreApplication.translate("Register", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("Register", u"X", None))
    # retranslateUi

