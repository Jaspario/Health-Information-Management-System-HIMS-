# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PharmacyRecord.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PharmacyRecord(object):
    def setupUi(self, PharmacyRecord):
        if not PharmacyRecord.objectName():
            PharmacyRecord.setObjectName(u"PharmacyRecord")
        PharmacyRecord.resize(598, 770)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PharmacyRecord.sizePolicy().hasHeightForWidth())
        PharmacyRecord.setSizePolicy(sizePolicy)
        PharmacyRecord.setSizeGripEnabled(True)
        self.gridLayout = QGridLayout(PharmacyRecord)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgflayer = QFrame(PharmacyRecord)
        self.bgflayer.setObjectName(u"bgflayer")
        self.bgflayer.setFrameShape(QFrame.StyledPanel)
        self.bgflayer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.bgflayer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, -1, 6, -1)
        self.logo = QLabel(self.bgflayer)
        self.logo.setObjectName(u"logo")
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


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.bgLayer = QFrame(self.bgflayer)
        self.bgLayer.setObjectName(u"bgLayer")
        font3 = QFont()
        font3.setFamily(u"Georgia")
        font3.setPointSize(7)
        self.bgLayer.setFont(font3)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.bgLayer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
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


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.bgLayer)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font4 = QFont()
        font4.setFamily(u"Georgia")
        font4.setPointSize(7)
        font4.setBold(True)
        font4.setWeight(75)
        self.groupBox_2.setFont(font4)
        self.groupBox_2.setFlat(False)
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 26, -1, -1)
        self.table = QTableWidget(self.groupBox_2)
        if (self.table.columnCount() < 7):
            self.table.setColumnCount(7)
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
        self.table.setObjectName(u"table")
        self.table.setFont(font4)
        self.table.setAutoFillBackground(True)
        self.table.setAlternatingRowColors(True)
        self.table.setColumnCount(7)

        self.gridLayout_6.addWidget(self.table, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 3, 0, 1, 1)

        self.groupBox = QGroupBox(self.bgLayer)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font4)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(5, 2, 5, 2)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.fname = QLabel(self.groupBox)
        self.fname.setObjectName(u"fname")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy2)
        font5 = QFont()
        font5.setFamily(u"Tahoma")
        font5.setPointSize(7)
        font5.setBold(False)
        font5.setWeight(50)
        self.fname.setFont(font5)
        self.fname.setFocusPolicy(Qt.StrongFocus)
        self.fname.setFrameShape(QFrame.StyledPanel)
        self.fname.setMargin(5)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gender = QLabel(self.groupBox)
        self.gender.setObjectName(u"gender")
        sizePolicy2.setHeightForWidth(self.gender.sizePolicy().hasHeightForWidth())
        self.gender.setSizePolicy(sizePolicy2)
        self.gender.setFont(font5)
        self.gender.setFrameShape(QFrame.StyledPanel)
        self.gender.setMargin(5)

        self.horizontalLayout_6.addWidget(self.gender)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.age = QLabel(self.groupBox)
        self.age.setObjectName(u"age")
        sizePolicy2.setHeightForWidth(self.age.sizePolicy().hasHeightForWidth())
        self.age.setSizePolicy(sizePolicy2)
        self.age.setFont(font5)
        self.age.setFrameShape(QFrame.StyledPanel)
        self.age.setMargin(5)

        self.horizontalLayout_6.addWidget(self.age)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_6)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(5, 2, 5, 2)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lname = QLabel(self.groupBox)
        self.lname.setObjectName(u"lname")
        sizePolicy2.setHeightForWidth(self.lname.sizePolicy().hasHeightForWidth())
        self.lname.setSizePolicy(sizePolicy2)
        self.lname.setFont(font5)
        self.lname.setFrameShape(QFrame.StyledPanel)
        self.lname.setMargin(5)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lname)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.pclass = QLabel(self.groupBox)
        self.pclass.setObjectName(u"pclass")
        sizePolicy2.setHeightForWidth(self.pclass.sizePolicy().hasHeightForWidth())
        self.pclass.setSizePolicy(sizePolicy2)
        self.pclass.setFont(font5)
        self.pclass.setFrameShape(QFrame.StyledPanel)
        self.pclass.setMargin(5)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.pclass)


        self.gridLayout_2.addLayout(self.formLayout_2, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.bgLayer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.cardNum = QLabel(self.bgLayer)
        self.cardNum.setObjectName(u"cardNum")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cardNum.sizePolicy().hasHeightForWidth())
        self.cardNum.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.cardNum)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.bgLayer)


        self.gridLayout.addWidget(self.bgflayer, 1, 0, 1, 1)


        self.retranslateUi(PharmacyRecord)

        QMetaObject.connectSlotsByName(PharmacyRecord)
    # setupUi

    def retranslateUi(self, PharmacyRecord):
        PharmacyRecord.setWindowTitle(QCoreApplication.translate("PharmacyRecord", u"Dialog", None))
        self.logo.setText("")
        self.bgflbl.setText(QCoreApplication.translate("PharmacyRecord", u"Patient's Pharmacetical Record", None))
        self.miniBtn.setText(QCoreApplication.translate("PharmacyRecord", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("PharmacyRecord", u"X", None))
        self.addNewBtn.setText(QCoreApplication.translate("PharmacyRecord", u"Add New Record", None))
        self.closeBtn.setText(QCoreApplication.translate("PharmacyRecord", u"Close", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PharmacyRecord", u"Prescriptions", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PharmacyRecord", u"Date Requested", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PharmacyRecord", u"Drug List", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PharmacyRecord", u"Prescribed By", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PharmacyRecord", u"Diagnosis", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PharmacyRecord", u"Pharmacist", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PharmacyRecord", u"Status", None));
        self.groupBox.setTitle(QCoreApplication.translate("PharmacyRecord", u"Patient's Details:", None))
        self.label_2.setText(QCoreApplication.translate("PharmacyRecord", u"First Name:", None))
        self.fname.setText("")
        self.label_6.setText(QCoreApplication.translate("PharmacyRecord", u"Gender:", None))
        self.gender.setText("")
        self.label_9.setText(QCoreApplication.translate("PharmacyRecord", u"Age:", None))
        self.age.setText("")
        self.label_4.setText(QCoreApplication.translate("PharmacyRecord", u"Last Name:", None))
        self.lname.setText("")
        self.label_8.setText(QCoreApplication.translate("PharmacyRecord", u"Class:", None))
        self.pclass.setText("")
        self.label_3.setText(QCoreApplication.translate("PharmacyRecord", u"Patient's Number:", None))
        self.cardNum.setText(QCoreApplication.translate("PharmacyRecord", u"00000000000", None))
    # retranslateUi

