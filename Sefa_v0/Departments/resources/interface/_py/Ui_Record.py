# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Record.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Record(object):
    def setupUi(self, Record):
        if not Record.objectName():
            Record.setObjectName(u"Record")
        Record.resize(701, 1012)
        self.gridLayout = QGridLayout(Record)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Record)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
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
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMaximumSize(QSize(16777215, 130))
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet(u"border-color: rgb(2, 2, 2);\n"
"color: rgb(2, 2, 2);")
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, -1, 6, -1)
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setMargin(6)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.fname = QLineEdit(self.frame_3)
        self.fname.setObjectName(u"fname")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy2)
        self.fname.setAutoFillBackground(False)
        self.fname.setStyleSheet(u"color: rgb(4, 4, 4);\n"
"border-color: rgb(6, 6, 6);")
        self.fname.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.fname)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setMargin(6)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.lname = QLineEdit(self.frame_3)
        self.lname.setObjectName(u"lname")
        sizePolicy2.setHeightForWidth(self.lname.sizePolicy().hasHeightForWidth())
        self.lname.setSizePolicy(sizePolicy2)
        self.lname.setAutoFillBackground(False)
        self.lname.setStyleSheet(u"color: rgb(4, 4, 4);\n"
"border-color: rgb(6, 6, 6);")
        self.lname.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.lname)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(6, -1, 6, -1)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setMargin(6)
        self.label_5.setIndent(2)
        self.label_5.setOpenExternalLinks(False)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.gender = QLineEdit(self.frame_3)
        self.gender.setObjectName(u"gender")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(2)
        sizePolicy3.setHeightForWidth(self.gender.sizePolicy().hasHeightForWidth())
        self.gender.setSizePolicy(sizePolicy3)
        self.gender.setAutoFillBackground(False)
        self.gender.setStyleSheet(u"color: rgb(4, 4, 4);\n"
"border-color: rgb(6, 6, 6);")
        self.gender.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.gender)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setMargin(6)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.age = QLineEdit(self.frame_3)
        self.age.setObjectName(u"age")
        sizePolicy.setHeightForWidth(self.age.sizePolicy().hasHeightForWidth())
        self.age.setSizePolicy(sizePolicy)
        self.age.setAutoFillBackground(False)
        self.age.setStyleSheet(u"color: rgb(4, 4, 4);\n"
"border-color: rgb(6, 6, 6);")
        self.age.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.age)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setMargin(6)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.class_2 = QLineEdit(self.frame_3)
        self.class_2.setObjectName(u"class_2")
        sizePolicy2.setHeightForWidth(self.class_2.sizePolicy().hasHeightForWidth())
        self.class_2.setSizePolicy(sizePolicy2)
        self.class_2.setAutoFillBackground(False)
        self.class_2.setStyleSheet(u"color: rgb(4, 4, 4);\n"
"border-color: rgb(6, 6, 6);")
        self.class_2.setDragEnabled(True)
        self.class_2.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.class_2)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.gridLayout_3.addWidget(self.frame_3, 4, 0, 1, 5)

        self.verticalSpacer_2 = QSpacerItem(20, 22, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 3, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 2, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, -1, 6, -1)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(39, 39))
        self.logo.setPixmap(QPixmap(u"_ui/Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo)

        self.horizontalSpacer_2 = QSpacerItem(140, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 1, -1)
        self.horizontalSpacer = QSpacerItem(140, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.exitBtn = QPushButton(self.frame_4)
        self.exitBtn.setObjectName(u"exitBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy4)
        self.exitBtn.setMinimumSize(QSize(0, 40))
        self.exitBtn.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        self.exitBtn.setFont(font1)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setMouseTracking(True)
        self.exitBtn.setTabletTracking(True)
        self.exitBtn.setLayoutDirection(Qt.LeftToRight)
        self.exitBtn.setAutoFillBackground(False)
        self.exitBtn.setStyleSheet(u"color: rgb(255, 0, 34);\n"
"border-color: rgb(255, 0, 0);\n"
"alternate-background-color: rgb(255, 67, 34);\n"
"background-color: rgb(170,170,170);\n"
"selection-background-color: rgb(255, 0, 0);\n"
"selection-background-color: rgb(190, 13, 0);")
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setFlat(True)

        self.gridLayout_5.addWidget(self.exitBtn, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_4)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 5)

        self.cardNum = QLabel(self.frame)
        self.cardNum.setObjectName(u"cardNum")
        self.cardNum.setMaximumSize(QSize(200, 100))
        font2 = QFont()
        font2.setFamily(u"MS UI Gothic")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.cardNum.setFont(font2)
        self.cardNum.setAutoFillBackground(False)
        self.cardNum.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.cardNum, 2, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 4, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_3.setFont(font3)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)
        self.label_4.setFont(font3)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
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
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
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

        self.gridLayout_2.addWidget(self.table, 0, 0, 1, 2)


        self.gridLayout_3.addWidget(self.frame_2, 6, 0, 1, 5)

        self.verticalSpacer_5 = QSpacerItem(20, 33, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 5, 2, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.addNewBtn = QPushButton(self.frame)
        self.addNewBtn.setObjectName(u"addNewBtn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.addNewBtn.sizePolicy().hasHeightForWidth())
        self.addNewBtn.setSizePolicy(sizePolicy6)
        self.addNewBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.addNewBtn)

        self.horizontalSpacer_3 = QSpacerItem(183, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.closeBtn = QPushButton(self.frame)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy6.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy6)
        self.closeBtn.setMinimumSize(QSize(0, 30))
        self.closeBtn.setMouseTracking(True)
        self.closeBtn.setTabletTracking(True)

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 7, 0, 1, 5)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Record)

        QMetaObject.connectSlotsByName(Record)
    # setupUi

    def retranslateUi(self, Record):
        Record.setWindowTitle(QCoreApplication.translate("Record", u"Patient's Record", None))
        self.label_8.setText(QCoreApplication.translate("Record", u"First Name:", None))
        self.label_9.setText(QCoreApplication.translate("Record", u"Last Name:", None))
        self.label_5.setText(QCoreApplication.translate("Record", u"Gender:", None))
        self.label_6.setText(QCoreApplication.translate("Record", u"Age:", None))
        self.label_7.setText(QCoreApplication.translate("Record", u"Class:", None))
        self.logo.setText("")
        self.label.setText(QCoreApplication.translate("Record", u"Patient's Record No. 000000000", None))
        self.exitBtn.setText(QCoreApplication.translate("Record", u"X", None))
        self.cardNum.setText(QCoreApplication.translate("Record", u"Card No.: 00000000", None))
        self.label_3.setText(QCoreApplication.translate("Record", u" Medical Record", None))
        self.label_4.setText(QCoreApplication.translate("Record", u" Patient's Details", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Record", u"Date", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Record", u"Doctor", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Record", u"Diagnosis", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Record", u"Action", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Record", u"Status", None));
        self.addNewBtn.setText(QCoreApplication.translate("Record", u"Add New Record", None))
        self.closeBtn.setText(QCoreApplication.translate("Record", u"Close", None))
    # retranslateUi

