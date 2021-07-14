# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AccountRecord.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AccountRecord(object):
    def setupUi(self, AccountRecord):
        if not AccountRecord.objectName():
            AccountRecord.setObjectName(u"AccountRecord")
        AccountRecord.resize(561, 671)
        self.gridLayout = QGridLayout(AccountRecord)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgflayer = QFrame(AccountRecord)
        self.bgflayer.setObjectName(u"bgflayer")
        self.bgflayer.setFrameShape(QFrame.StyledPanel)
        self.bgflayer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bgflayer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.logo = QLabel(self.bgflayer)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setPixmap(QPixmap(u"_ui/Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo)

        self.bgflbl = QLabel(self.bgflayer)
        self.bgflbl.setObjectName(u"bgflbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bgflbl.sizePolicy().hasHeightForWidth())
        self.bgflbl.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.bgflbl.setFont(font)
        self.bgflbl.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.bgflbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.bgflbl.setMargin(10)

        self.horizontalLayout_2.addWidget(self.bgflbl)

        self.miniBtn = QPushButton(self.bgflayer)
        self.miniBtn.setObjectName(u"miniBtn")
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(12)
        self.miniBtn.setFont(font1)
        self.miniBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.miniBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(self.bgflayer)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(11)
        self.exitBtn.setFont(font2)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setMouseTracking(True)
        self.exitBtn.setTabletTracking(True)
        self.exitBtn.setLayoutDirection(Qt.LeftToRight)
        self.exitBtn.setAutoFillBackground(False)
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.exitBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.bgLayer = QFrame(self.bgflayer)
        self.bgLayer.setObjectName(u"bgLayer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bgLayer.sizePolicy().hasHeightForWidth())
        self.bgLayer.setSizePolicy(sizePolicy2)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.bgLayer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 11, -1)
        self.label_3 = QLabel(self.bgLayer)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamily(u"Georgia")
        font3.setPointSize(7)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.cardNum = QLabel(self.bgLayer)
        self.cardNum.setObjectName(u"cardNum")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cardNum.sizePolicy().hasHeightForWidth())
        self.cardNum.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.cardNum)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(self.bgLayer)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font3)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(5, 2, 5, 2)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.fname = QLabel(self.groupBox)
        self.fname.setObjectName(u"fname")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(7)
        font4.setBold(False)
        font4.setWeight(50)
        self.fname.setFont(font4)
        self.fname.setFocusPolicy(Qt.StrongFocus)
        self.fname.setFrameShape(QFrame.StyledPanel)
        self.fname.setMargin(5)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gender = QLabel(self.groupBox)
        self.gender.setObjectName(u"gender")
        sizePolicy4.setHeightForWidth(self.gender.sizePolicy().hasHeightForWidth())
        self.gender.setSizePolicy(sizePolicy4)
        self.gender.setFont(font4)
        self.gender.setFrameShape(QFrame.StyledPanel)
        self.gender.setMargin(5)

        self.horizontalLayout_6.addWidget(self.gender)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.age = QLabel(self.groupBox)
        self.age.setObjectName(u"age")
        sizePolicy4.setHeightForWidth(self.age.sizePolicy().hasHeightForWidth())
        self.age.setSizePolicy(sizePolicy4)
        self.age.setFont(font4)
        self.age.setFrameShape(QFrame.StyledPanel)
        self.age.setMargin(5)

        self.horizontalLayout_6.addWidget(self.age)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_6)


        self.horizontalLayout_3.addLayout(self.formLayout)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(9)
        self.formLayout_3.setVerticalSpacing(9)
        self.formLayout_3.setContentsMargins(-1, 3, -1, -1)
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        font5 = QFont()
        font5.setFamily(u"Tahoma")
        font5.setPointSize(7)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_10.setFont(font5)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setMargin(6)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.lname = QLabel(self.groupBox)
        self.lname.setObjectName(u"lname")
        sizePolicy1.setHeightForWidth(self.lname.sizePolicy().hasHeightForWidth())
        self.lname.setSizePolicy(sizePolicy1)
        self.lname.setFont(font4)
        self.lname.setAutoFillBackground(False)
        self.lname.setFrameShape(QFrame.StyledPanel)
        self.lname.setMargin(2)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lname)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setMargin(6)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pclass = QLabel(self.groupBox)
        self.pclass.setObjectName(u"pclass")
        sizePolicy1.setHeightForWidth(self.pclass.sizePolicy().hasHeightForWidth())
        self.pclass.setSizePolicy(sizePolicy1)
        self.pclass.setFont(font4)
        self.pclass.setAutoFillBackground(False)
        self.pclass.setFrameShape(QFrame.StyledPanel)
        self.pclass.setMargin(2)

        self.horizontalLayout_7.addWidget(self.pclass)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font5)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setMargin(0)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.status = QLabel(self.groupBox)
        self.status.setObjectName(u"status")
        sizePolicy1.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy1)
        self.status.setFont(font4)
        self.status.setAutoFillBackground(False)
        self.status.setFrameShape(QFrame.StyledPanel)
        self.status.setMargin(2)

        self.horizontalLayout_7.addWidget(self.status)


        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_7)


        self.horizontalLayout_3.addLayout(self.formLayout_3)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.bgLayer)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font3)
        self.groupBox_2.setFlat(False)
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 26, -1, -1)
        self.table = QTableWidget(self.groupBox_2)
        if (self.table.columnCount() < 8):
            self.table.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.table.setObjectName(u"table")
        self.table.setFont(font3)
        self.table.setAutoFillBackground(True)
        self.table.setAlternatingRowColors(True)
        self.table.setColumnCount(8)

        self.gridLayout_6.addWidget(self.table, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.addNewBtn = QPushButton(self.bgLayer)
        self.addNewBtn.setObjectName(u"addNewBtn")
        self.addNewBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.addNewBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.closeBtn = QPushButton(self.bgLayer)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.closeBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.bgLayer)


        self.gridLayout.addWidget(self.bgflayer, 1, 0, 1, 1)


        self.retranslateUi(AccountRecord)

        QMetaObject.connectSlotsByName(AccountRecord)
    # setupUi

    def retranslateUi(self, AccountRecord):
        AccountRecord.setWindowTitle(QCoreApplication.translate("AccountRecord", u"Dialog", None))
        self.logo.setText("")
        self.bgflbl.setText(QCoreApplication.translate("AccountRecord", u"Patient's Accountl Record", None))
        self.miniBtn.setText(QCoreApplication.translate("AccountRecord", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("AccountRecord", u"X", None))
        self.label_3.setText(QCoreApplication.translate("AccountRecord", u"Patient's Number:", None))
        self.cardNum.setText(QCoreApplication.translate("AccountRecord", u"TextLabel", None))
        self.groupBox.setTitle(QCoreApplication.translate("AccountRecord", u"Patient's Details:", None))
        self.label_2.setText(QCoreApplication.translate("AccountRecord", u"First Name:", None))
        self.fname.setText("")
        self.label_6.setText(QCoreApplication.translate("AccountRecord", u"Gender:", None))
        self.gender.setText("")
        self.label_9.setText(QCoreApplication.translate("AccountRecord", u"Age:", None))
        self.age.setText("")
        self.label_10.setText(QCoreApplication.translate("AccountRecord", u"Last Name:", None))
        self.lname.setText("")
        self.label_7.setText(QCoreApplication.translate("AccountRecord", u"Class:", None))
        self.pclass.setText(QCoreApplication.translate("AccountRecord", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("AccountRecord", u"Status:", None))
        self.status.setText(QCoreApplication.translate("AccountRecord", u"TextLabel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("AccountRecord", u"Prescriptions", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AccountRecord", u"Date", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AccountRecord", u"Services", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AccountRecord", u"Cost", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AccountRecord", u"Discount", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AccountRecord", u"Amount Payable", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AccountRecord", u"Amount Payed", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AccountRecord", u"Outstanding Balance", None));
        self.addNewBtn.setText(QCoreApplication.translate("AccountRecord", u"Add New", None))
        self.closeBtn.setText(QCoreApplication.translate("AccountRecord", u"Close", None))
    # retranslateUi

