# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LabRecord.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LabRecord(object):
    def setupUi(self, LabRecord):
        if not LabRecord.objectName():
            LabRecord.setObjectName(u"LabRecord")
        LabRecord.resize(563, 725)
        self.gridLayout = QGridLayout(LabRecord)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgflayer = QFrame(LabRecord)
        self.bgflayer.setObjectName(u"bgflayer")
        self.bgflayer.setFrameShape(QFrame.StyledPanel)
        self.bgflayer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bgflayer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.logo = QLabel(self.bgflayer)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(40, 40))
        self.logo.setMaximumSize(QSize(39, 39))
        self.logo.setPixmap(QPixmap(u"_ui/Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo)

        self.bgflbl = QLabel(self.bgflayer)
        self.bgflbl.setObjectName(u"bgflbl")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bgflbl.sizePolicy().hasHeightForWidth())
        self.bgflbl.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.bgflbl.setFont(font)
        self.bgflbl.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.bgflbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.bgflbl.setMargin(5)

        self.horizontalLayout_2.addWidget(self.bgflbl)

        self.miniBtn = QPushButton(self.bgflayer)
        self.miniBtn.setObjectName(u"miniBtn")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(11)
        self.miniBtn.setFont(font1)
        self.miniBtn.setCursor(QCursor(Qt.PointingHandCursor))

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
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.bgLayer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.bgLayer)
        self.groupBox.setObjectName(u"groupBox")
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.groupBox.setFont(font3)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setMargin(5)

        self.horizontalLayout.addWidget(self.label_2)

        self.fname = QLabel(self.groupBox)
        self.fname.setObjectName(u"fname")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(7)
        font4.setBold(False)
        font4.setWeight(50)
        self.fname.setFont(font4)
        self.fname.setFocusPolicy(Qt.StrongFocus)
        self.fname.setFrameShape(QFrame.StyledPanel)
        self.fname.setMargin(2)

        self.horizontalLayout.addWidget(self.fname)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setMargin(5)

        self.horizontalLayout.addWidget(self.label_4)

        self.lname = QLabel(self.groupBox)
        self.lname.setObjectName(u"lname")
        sizePolicy1.setHeightForWidth(self.lname.sizePolicy().hasHeightForWidth())
        self.lname.setSizePolicy(sizePolicy1)
        self.lname.setFont(font4)
        self.lname.setFrameShape(QFrame.StyledPanel)
        self.lname.setMargin(2)

        self.horizontalLayout.addWidget(self.lname)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.gender = QLabel(self.groupBox)
        self.gender.setObjectName(u"gender")
        sizePolicy1.setHeightForWidth(self.gender.sizePolicy().hasHeightForWidth())
        self.gender.setSizePolicy(sizePolicy1)
        self.gender.setFont(font4)
        self.gender.setFrameShape(QFrame.StyledPanel)
        self.gender.setMargin(2)

        self.horizontalLayout_3.addWidget(self.gender)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.age = QLabel(self.groupBox)
        self.age.setObjectName(u"age")
        sizePolicy1.setHeightForWidth(self.age.sizePolicy().hasHeightForWidth())
        self.age.setSizePolicy(sizePolicy1)
        self.age.setMinimumSize(QSize(100, 0))
        self.age.setFont(font4)
        self.age.setFrameShape(QFrame.StyledPanel)
        self.age.setMargin(2)

        self.horizontalLayout_3.addWidget(self.age)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.pclass = QLabel(self.groupBox)
        self.pclass.setObjectName(u"pclass")
        sizePolicy1.setHeightForWidth(self.pclass.sizePolicy().hasHeightForWidth())
        self.pclass.setSizePolicy(sizePolicy1)
        self.pclass.setFont(font4)
        self.pclass.setFrameShape(QFrame.StyledPanel)
        self.pclass.setMargin(2)

        self.horizontalLayout_3.addWidget(self.pclass)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.bgLayer)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font3)
        self.groupBox_2.setFlat(False)
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 26, -1, -1)
        self.table = QTableWidget(self.groupBox_2)
        if (self.table.columnCount() < 11):
            self.table.setColumnCount(11)
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
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.table.setObjectName(u"table")
        self.table.setFont(font3)
        self.table.setAutoFillBackground(True)
        self.table.setAlternatingRowColors(True)
        self.table.setRowCount(0)
        self.table.setColumnCount(11)
        self.table.horizontalHeader().setStretchLastSection(False)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.verticalHeader().setStretchLastSection(False)

        self.gridLayout_4.addWidget(self.table, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 4, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.bgLayer)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setFamily(u"Tahoma")
        font5.setPointSize(7)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_3.setFont(font5)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.cardNum = QLabel(self.bgLayer)
        self.cardNum.setObjectName(u"cardNum")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cardNum.sizePolicy().hasHeightForWidth())
        self.cardNum.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.cardNum)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

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


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.bgLayer)


        self.gridLayout.addWidget(self.bgflayer, 0, 0, 1, 1)


        self.retranslateUi(LabRecord)

        QMetaObject.connectSlotsByName(LabRecord)
    # setupUi

    def retranslateUi(self, LabRecord):
        LabRecord.setWindowTitle(QCoreApplication.translate("LabRecord", u"Dialog", None))
        self.logo.setText("")
        self.bgflbl.setText(QCoreApplication.translate("LabRecord", u"Patient's Laboratory Record", None))
        self.miniBtn.setText(QCoreApplication.translate("LabRecord", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("LabRecord", u"X", None))
        self.groupBox.setTitle(QCoreApplication.translate("LabRecord", u"Patient's Details:", None))
        self.label_2.setText(QCoreApplication.translate("LabRecord", u"First Name:", None))
        self.fname.setText("")
        self.label_4.setText(QCoreApplication.translate("LabRecord", u"Last Name:", None))
        self.lname.setText("")
        self.label_6.setText(QCoreApplication.translate("LabRecord", u"Gender:", None))
        self.gender.setText("")
        self.label_9.setText(QCoreApplication.translate("LabRecord", u"Age:", None))
        self.age.setText("")
        self.label_8.setText(QCoreApplication.translate("LabRecord", u"Class:", None))
        self.pclass.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("LabRecord", u"Lab Requests", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LabRecord", u"Date Requested", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LabRecord", u"Date Completed", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("LabRecord", u"Date Collected", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("LabRecord", u"Doctor", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("LabRecord", u"Lab Scientist", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("LabRecord", u"Clinical Diagnosis", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("LabRecord", u"Examinations", None));
        ___qtablewidgetitem7 = self.table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("LabRecord", u"Pathology", None));
        ___qtablewidgetitem8 = self.table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("LabRecord", u"Specimens", None));
        ___qtablewidgetitem9 = self.table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("LabRecord", u"Status", None));
        ___qtablewidgetitem10 = self.table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("LabRecord", u"Report/Result", None));
        self.label_3.setText(QCoreApplication.translate("LabRecord", u"Patient's Number:", None))
        self.cardNum.setText(QCoreApplication.translate("LabRecord", u"00000000000", None))
        self.addNewBtn.setText(QCoreApplication.translate("LabRecord", u"Add New Record", None))
        self.closeBtn.setText(QCoreApplication.translate("LabRecord", u"Close", None))
    # retranslateUi

