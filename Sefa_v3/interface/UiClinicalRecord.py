# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClinicalRecord.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ClinicalRecord(object):
    def setupUi(self, ClinicalRecord):
        if not ClinicalRecord.objectName():
            ClinicalRecord.setObjectName(u"ClinicalRecord")
        ClinicalRecord.resize(567, 758)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ClinicalRecord.sizePolicy().hasHeightForWidth())
        ClinicalRecord.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(ClinicalRecord)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgflayer = QFrame(ClinicalRecord)
        self.bgflayer.setObjectName(u"bgflayer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bgflayer.sizePolicy().hasHeightForWidth())
        self.bgflayer.setSizePolicy(sizePolicy1)
        self.bgflayer.setCursor(QCursor(Qt.ArrowCursor))
        self.bgflayer.setMouseTracking(True)
        self.bgflayer.setTabletTracking(True)
        self.bgflayer.setFocusPolicy(Qt.StrongFocus)
        self.bgflayer.setAutoFillBackground(False)
        self.bgflayer.setFrameShape(QFrame.StyledPanel)
        self.bgflayer.setFrameShadow(QFrame.Raised)
        self.bgflayer.setLineWidth(2)
        self.verticalLayout = QVBoxLayout(self.bgflayer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(13, 13, 13, 13)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.logo = QLabel(self.bgflayer)
        self.logo.setObjectName(u"logo")
        self.logo.setPixmap(QPixmap(u"_ui/Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo)

        self.bgflbl = QLabel(self.bgflayer)
        self.bgflbl.setObjectName(u"bgflbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bgflbl.sizePolicy().hasHeightForWidth())
        self.bgflbl.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.bgflbl.setFont(font)
        self.bgflbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.bgflbl.setMargin(5)

        self.horizontalLayout_2.addWidget(self.bgflbl)

        self.miniBtn = QPushButton(self.bgflayer)
        self.miniBtn.setObjectName(u"miniBtn")
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(12)
        self.miniBtn.setFont(font1)
        self.miniBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.miniBtn.setAutoFillBackground(True)
        self.miniBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(self.bgflayer)
        self.exitBtn.setObjectName(u"exitBtn")
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(11)
        self.exitBtn.setFont(font2)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setMouseTracking(True)
        self.exitBtn.setTabletTracking(True)
        self.exitBtn.setLayoutDirection(Qt.LeftToRight)
        self.exitBtn.setAutoFillBackground(True)
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.exitBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.bgLayer = QFrame(self.bgflayer)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setAutoFillBackground(True)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.bgLayer)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label_10 = QLabel(self.bgLayer)
        self.label_10.setObjectName(u"label_10")
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_10.setFont(font3)
        self.label_10.setAutoFillBackground(False)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.cardNum = QLabel(self.bgLayer)
        self.cardNum.setObjectName(u"cardNum")
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(8)
        self.cardNum.setFont(font4)

        self.horizontalLayout_5.addWidget(self.cardNum)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.label_4 = QLabel(self.bgLayer)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(8)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_4.setFont(font5)
        self.label_4.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.label_4)

        self.frame_3 = QFrame(self.bgLayer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(-1, 3, -1, -1)
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        font6 = QFont()
        font6.setFamily(u"Tahoma")
        font6.setPointSize(7)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_8.setFont(font6)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setMargin(6)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.fname = QLabel(self.frame_3)
        self.fname.setObjectName(u"fname")
        sizePolicy2.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy2)
        font7 = QFont()
        font7.setFamily(u"Tahoma")
        font7.setPointSize(7)
        self.fname.setFont(font7)
        self.fname.setFocusPolicy(Qt.StrongFocus)
        self.fname.setAutoFillBackground(False)
        self.fname.setFrameShape(QFrame.StyledPanel)
        self.fname.setMargin(2)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font6)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setMargin(6)
        self.label_5.setIndent(2)
        self.label_5.setOpenExternalLinks(False)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gender = QLabel(self.frame_3)
        self.gender.setObjectName(u"gender")
        sizePolicy2.setHeightForWidth(self.gender.sizePolicy().hasHeightForWidth())
        self.gender.setSizePolicy(sizePolicy2)
        self.gender.setFont(font7)
        self.gender.setAutoFillBackground(False)
        self.gender.setFrameShape(QFrame.StyledPanel)
        self.gender.setMargin(2)

        self.horizontalLayout_4.addWidget(self.gender)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font6)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setMargin(6)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.age = QLabel(self.frame_3)
        self.age.setObjectName(u"age")
        sizePolicy2.setHeightForWidth(self.age.sizePolicy().hasHeightForWidth())
        self.age.setSizePolicy(sizePolicy2)
        self.age.setFont(font7)
        self.age.setAutoFillBackground(False)
        self.age.setFrameShape(QFrame.StyledPanel)
        self.age.setMargin(2)

        self.horizontalLayout_4.addWidget(self.age)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_4)


        self.horizontalLayout.addLayout(self.formLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(9)
        self.formLayout.setVerticalSpacing(9)
        self.formLayout.setContentsMargins(-1, 3, -1, -1)
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font6)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setMargin(6)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.lname = QLabel(self.frame_3)
        self.lname.setObjectName(u"lname")
        sizePolicy2.setHeightForWidth(self.lname.sizePolicy().hasHeightForWidth())
        self.lname.setSizePolicy(sizePolicy2)
        self.lname.setFont(font7)
        self.lname.setAutoFillBackground(False)
        self.lname.setFrameShape(QFrame.StyledPanel)
        self.lname.setMargin(2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lname)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font6)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setMargin(6)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pclass = QLabel(self.frame_3)
        self.pclass.setObjectName(u"pclass")
        sizePolicy2.setHeightForWidth(self.pclass.sizePolicy().hasHeightForWidth())
        self.pclass.setSizePolicy(sizePolicy2)
        self.pclass.setFont(font7)
        self.pclass.setAutoFillBackground(False)
        self.pclass.setFrameShape(QFrame.StyledPanel)
        self.pclass.setMargin(2)

        self.horizontalLayout_7.addWidget(self.pclass)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font6)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(0)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.status = QLabel(self.frame_3)
        self.status.setObjectName(u"status")
        sizePolicy2.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy2)
        self.status.setFont(font7)
        self.status.setAutoFillBackground(False)
        self.status.setFrameShape(QFrame.StyledPanel)
        self.status.setMargin(2)

        self.horizontalLayout_7.addWidget(self.status)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_7)


        self.horizontalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.label_3 = QLabel(self.bgLayer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font5)
        self.label_3.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.label_3)

        self.bgftable = QFrame(self.bgLayer)
        self.bgftable.setObjectName(u"bgftable")
        self.bgftable.setFont(font5)
        self.bgftable.setAutoFillBackground(False)
        self.bgftable.setFrameShape(QFrame.Panel)
        self.bgftable.setFrameShadow(QFrame.Plain)
        self.bgftable.setLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgftable)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table = QTableWidget(self.bgftable)
        if (self.table.columnCount() < 6):
            self.table.setColumnCount(6)
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
        self.table.setObjectName(u"table")
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(7)
        font8.setBold(True)
        font8.setWeight(75)
        self.table.setFont(font8)
        self.table.setMouseTracking(True)
        self.table.setTabletTracking(True)
        self.table.setAutoFillBackground(True)
        self.table.setFrameShape(QFrame.StyledPanel)
        self.table.setFrameShadow(QFrame.Plain)
        self.table.setLineWidth(1)
        self.table.setMidLineWidth(0)
        self.table.setAutoScrollMargin(36)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setTextElideMode(Qt.ElideMiddle)
        self.table.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table.setWordWrap(True)
        self.table.setCornerButtonEnabled(True)
        self.table.setRowCount(0)
        self.table.setColumnCount(6)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setProperty("showSortIndicator", True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(True)
        self.table.verticalHeader().setCascadingSectionResizes(True)
        self.table.verticalHeader().setProperty("showSortIndicator", True)
        self.table.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.table, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.bgftable)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.addNewBtn = QPushButton(self.bgLayer)
        self.addNewBtn.setObjectName(u"addNewBtn")
        self.addNewBtn.setMinimumSize(QSize(50, 25))
        self.addNewBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addNewBtn.setAutoFillBackground(True)

        self.horizontalLayout_3.addWidget(self.addNewBtn)

        self.horizontalSpacer_3 = QSpacerItem(150, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.closeBtn = QPushButton(self.bgLayer)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(50, 25))
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeBtn.setMouseTracking(True)
        self.closeBtn.setTabletTracking(True)
        self.closeBtn.setAutoFillBackground(True)

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.bgLayer)


        self.gridLayout.addWidget(self.bgflayer, 0, 0, 1, 1)


        self.retranslateUi(ClinicalRecord)

        QMetaObject.connectSlotsByName(ClinicalRecord)
    # setupUi

    def retranslateUi(self, ClinicalRecord):
        ClinicalRecord.setWindowTitle(QCoreApplication.translate("ClinicalRecord", u"Patient's Record", None))
        self.logo.setText("")
#if QT_CONFIG(tooltip)
        self.bgflbl.setToolTip(QCoreApplication.translate("ClinicalRecord", u"<html><head/><body><p>Title: Clinical Records</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bgflbl.setText(QCoreApplication.translate("ClinicalRecord", u"Patient's Clinical Record", None))
#if QT_CONFIG(tooltip)
        self.miniBtn.setToolTip(QCoreApplication.translate("ClinicalRecord", u"<html><head/><body><p>Click to minimize window</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.miniBtn.setText(QCoreApplication.translate("ClinicalRecord", u"__", None))
#if QT_CONFIG(tooltip)
        self.exitBtn.setToolTip(QCoreApplication.translate("ClinicalRecord", u"<html><head/><body><p>Click to exit app</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.exitBtn.setText(QCoreApplication.translate("ClinicalRecord", u"X", None))
        self.label_10.setText(QCoreApplication.translate("ClinicalRecord", u"Card Number:", None))
        self.cardNum.setText(QCoreApplication.translate("ClinicalRecord", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("ClinicalRecord", u" Patient's Details", None))
        self.label_8.setText(QCoreApplication.translate("ClinicalRecord", u"First Name:", None))
        self.fname.setText("")
        self.label_5.setText(QCoreApplication.translate("ClinicalRecord", u"Gender:", None))
        self.gender.setText("")
        self.label_6.setText(QCoreApplication.translate("ClinicalRecord", u"Age:", None))
        self.age.setText("")
        self.label_9.setText(QCoreApplication.translate("ClinicalRecord", u"Last Name:", None))
        self.lname.setText("")
        self.label_7.setText(QCoreApplication.translate("ClinicalRecord", u"Class:", None))
        self.pclass.setText(QCoreApplication.translate("ClinicalRecord", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("ClinicalRecord", u"Status:", None))
        self.status.setText(QCoreApplication.translate("ClinicalRecord", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("ClinicalRecord", u" Medical Record", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ClinicalRecord", u"Date", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ClinicalRecord", u"Doctor", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ClinicalRecord", u"Diagnosis", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ClinicalRecord", u"Action", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ClinicalRecord", u"Status", None));
#if QT_CONFIG(tooltip)
        self.addNewBtn.setToolTip(QCoreApplication.translate("ClinicalRecord", u"<html><head/><body><p>Click to add new record</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.addNewBtn.setText(QCoreApplication.translate("ClinicalRecord", u"Add New Record", None))
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("ClinicalRecord", u"<html><head/><body><p>Click to close record</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText(QCoreApplication.translate("ClinicalRecord", u"Close", None))
    # retranslateUi

