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
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(ClinicalRecord)
        self.frame.setObjectName(u"frame")
        self.frame.setMouseTracking(True)
        self.frame.setTabletTracking(True)
        self.frame.setFocusPolicy(Qt.StrongFocus)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: rgb(179, 122, 42);\n"
"border-color: rgb(4, 4, 4);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(2)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 13)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, -1, 6, -1)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setPixmap(QPixmap(u"_ui/Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.miniBtn = QPushButton(self.frame)
        self.miniBtn.setObjectName(u"miniBtn")
        font1 = QFont()
        font1.setPointSize(12)
        self.miniBtn.setFont(font1)
        self.miniBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(self.frame)
        self.exitBtn.setObjectName(u"exitBtn")
        font2 = QFont()
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


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 5)

        self.verticalSpacer = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 4, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"border-color: rgb(2, 2, 2);\n"
"color: rgb(2, 2, 2);")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table = QTableWidget(self.frame_2)
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
        self.table.setMouseTracking(True)
        self.table.setTabletTracking(True)
        self.table.setAutoFillBackground(True)
        self.table.setFrameShape(QFrame.Box)
        self.table.setFrameShadow(QFrame.Plain)
        self.table.setLineWidth(2)
        self.table.setMidLineWidth(1)
        self.table.setAutoScrollMargin(10)
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
        self.table.horizontalHeader().setMinimumSectionSize(47)
        self.table.horizontalHeader().setDefaultSectionSize(115)
        self.table.horizontalHeader().setProperty("showSortIndicator", True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(True)
        self.table.verticalHeader().setCascadingSectionResizes(True)
        self.table.verticalHeader().setMinimumSectionSize(20)
        self.table.verticalHeader().setDefaultSectionSize(40)
        self.table.verticalHeader().setProperty("showSortIndicator", True)
        self.table.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.table, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 6, 0, 1, 5)

        self.verticalSpacer_5 = QSpacerItem(20, 33, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 5, 2, 1, 1)

        self.cardNum = QLabel(self.frame)
        self.cardNum.setObjectName(u"cardNum")
        font3 = QFont()
        font3.setFamily(u"MS UI Gothic")
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.cardNum.setFont(font3)
        self.cardNum.setAutoFillBackground(False)
        self.cardNum.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.cardNum, 2, 4, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet(u"border-color: rgb(2, 2, 2);\n"
"color: rgb(2, 2, 2);")
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setMargin(6)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(7)
        self.label_2.setFont(font4)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShape(QFrame.StyledPanel)
        self.label_2.setMargin(2)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_2)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setMargin(6)
        self.label_5.setIndent(2)
        self.label_5.setOpenExternalLinks(False)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setFont(font4)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setFrameShape(QFrame.StyledPanel)
        self.label_12.setMargin(2)

        self.horizontalLayout_4.addWidget(self.label_12)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setMargin(6)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setFont(font4)
        self.label_13.setAutoFillBackground(False)
        self.label_13.setFrameShape(QFrame.StyledPanel)
        self.label_13.setMargin(2)

        self.horizontalLayout_4.addWidget(self.label_13)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_4)


        self.horizontalLayout.addLayout(self.formLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setMargin(6)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setMargin(6)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setFont(font4)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setFrameShape(QFrame.StyledPanel)
        self.label_10.setMargin(2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_10)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setFont(font4)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setFrameShape(QFrame.StyledPanel)
        self.label_11.setMargin(2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_11)


        self.horizontalLayout.addLayout(self.formLayout)


        self.gridLayout_3.addWidget(self.frame_3, 4, 0, 1, 5)

        self.verticalSpacer_2 = QSpacerItem(20, 22, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 3, 3, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.addNewBtn = QPushButton(self.frame)
        self.addNewBtn.setObjectName(u"addNewBtn")

        self.horizontalLayout_3.addWidget(self.addNewBtn)

        self.horizontalSpacer_3 = QSpacerItem(183, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.closeBtn = QPushButton(self.frame)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMouseTracking(True)
        self.closeBtn.setTabletTracking(True)

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 7, 0, 1, 5)

        self.verticalSpacer_3 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 2, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.label_3.setFont(font5)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(ClinicalRecord)

        QMetaObject.connectSlotsByName(ClinicalRecord)
    # setupUi

    def retranslateUi(self, ClinicalRecord):
        ClinicalRecord.setWindowTitle(QCoreApplication.translate("ClinicalRecord", u"Patient's Record", None))
        self.logo.setText("")
        self.label.setText(QCoreApplication.translate("ClinicalRecord", u"Patient's Clinical Record", None))
        self.miniBtn.setText(QCoreApplication.translate("ClinicalRecord", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("ClinicalRecord", u"X", None))
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
        self.cardNum.setText(QCoreApplication.translate("ClinicalRecord", u"Card No.: 00000000", None))
        self.label_8.setText(QCoreApplication.translate("ClinicalRecord", u"First Name:", None))
        self.label_2.setText("")
        self.label_5.setText(QCoreApplication.translate("ClinicalRecord", u"Gender:", None))
        self.label_12.setText("")
        self.label_6.setText(QCoreApplication.translate("ClinicalRecord", u"Age:", None))
        self.label_13.setText("")
        self.label_9.setText(QCoreApplication.translate("ClinicalRecord", u"Last Name:", None))
        self.label_7.setText(QCoreApplication.translate("ClinicalRecord", u"Class:", None))
        self.label_10.setText("")
        self.label_11.setText("")
        self.addNewBtn.setText(QCoreApplication.translate("ClinicalRecord", u"Add New Record", None))
        self.closeBtn.setText(QCoreApplication.translate("ClinicalRecord", u"Close", None))
        self.label_3.setText(QCoreApplication.translate("ClinicalRecord", u" Medical Record", None))
        self.label_4.setText(QCoreApplication.translate("ClinicalRecord", u" Patient's Details", None))
    # retranslateUi

