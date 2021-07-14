# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PRecord.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PRecord(object):
    def setupUi(self, PRecord):
        if not PRecord.objectName():
            PRecord.setObjectName(u"PRecord")
        PRecord.setWindowModality(Qt.ApplicationModal)
        PRecord.resize(750, 1050)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PRecord.sizePolicy().hasHeightForWidth())
        PRecord.setSizePolicy(sizePolicy)
        PRecord.setMinimumSize(QSize(750, 1050))
        PRecord.setMaximumSize(QSize(750, 1050))
        PRecord.setAutoFillBackground(False)
        PRecord.setStyleSheet(u"background-color: rgb(170, 170, 170);")
        PRecord.setSizeGripEnabled(False)
        PRecord.setModal(True)
        self.gridLayout = QGridLayout(PRecord)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(PRecord)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: rgb(179, 122, 42);\n"
"border-color: rgb(4, 4, 4);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(2)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 52, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 2, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.addNewBtn = QPushButton(self.frame)
        self.addNewBtn.setObjectName(u"addNewBtn")
        sizePolicy1.setHeightForWidth(self.addNewBtn.sizePolicy().hasHeightForWidth())
        self.addNewBtn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.addNewBtn)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 7, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_3, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 23, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 5, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 33, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 5, 2, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(129, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.deleteBtn = QPushButton(self.frame)
        self.deleteBtn.setObjectName(u"deleteBtn")
        sizePolicy1.setHeightForWidth(self.deleteBtn.sizePolicy().hasHeightForWidth())
        self.deleteBtn.setSizePolicy(sizePolicy1)
        self.deleteBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteBtn.setMouseTracking(True)
        self.deleteBtn.setTabletTracking(True)

        self.horizontalLayout.addWidget(self.deleteBtn)

        self.closeBtn = QPushButton(self.frame)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy3)
        self.closeBtn.setMouseTracking(True)
        self.closeBtn.setTabletTracking(True)

        self.horizontalLayout.addWidget(self.closeBtn)


        self.gridLayout_3.addLayout(self.horizontalLayout, 7, 3, 1, 3)

        self.verticalSpacer_4 = QSpacerItem(20, 45, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 7, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 22, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 3, 4, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, -1, 6, -1)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(39, 39))
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo)

        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setUnderline(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 1, -1)
        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.minButton = QPushButton(self.frame_5)
        self.minButton.setObjectName(u"minButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.minButton.sizePolicy().hasHeightForWidth())
        self.minButton.setSizePolicy(sizePolicy4)
        self.minButton.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setPointSize(11)
        self.minButton.setFont(font2)
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minButton.setMouseTracking(True)
        self.minButton.setTabletTracking(True)
        self.minButton.setAutoFillBackground(False)
        self.minButton.setStyleSheet(u"color: rgb(7, 7, 7);\n"
"background-color: rgb(170,170,170);\n"
"selection-color: rgb(2, 2, 2);\n"
"selection-background-color: rgb(190, 13, 0);\n"
"border-color: rgb(9, 9, 9);")
        self.minButton.setAutoDefault(False)
        self.minButton.setFlat(True)

        self.gridLayout_6.addWidget(self.minButton, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.closeButton = QPushButton(self.frame_4)
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
        self.closeButton.setStyleSheet(u"color: rgb(255, 0, 34);\n"
"border-color: rgb(255, 0, 0);\n"
"alternate-background-color: rgb(255, 67, 34);\n"
"background-color: rgb(170,170,170);\n"
"selection-background-color: rgb(255, 0, 0);\n"
"selection-background-color: rgb(190, 13, 0);")
        self.closeButton.setAutoDefault(False)
        self.closeButton.setFlat(True)

        self.gridLayout_5.addWidget(self.closeButton, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_4)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 6)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy5)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"border-color: rgb(2, 2, 2);\n"
"color: rgb(2, 2, 2);")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table = QTableWidget(self.frame_2)
        if (self.table.columnCount() < 5):
            self.table.setColumnCount(5)
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
        self.table.setObjectName(u"table")
        sizePolicy1.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy1)
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
        self.table.setColumnCount(5)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setMinimumSectionSize(60)
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


        self.gridLayout_3.addWidget(self.frame_2, 6, 0, 1, 6)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy5.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy5)
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

        self.lineEdit_4 = QLineEdit(self.frame_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(2)
        sizePolicy6.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy6)
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setStyleSheet(u"color: rgb(4, 4, 4);\n"
"border-color: rgb(6, 6, 6);")
        self.lineEdit_4.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.lineEdit_4)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setMargin(6)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.lineEdit_5 = QLineEdit(self.frame_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy6.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy6)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet(u"color: rgb(4, 4, 4);\n"
"border-color: rgb(6, 6, 6);")
        self.lineEdit_5.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.lineEdit_5)


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

        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(2)
        sizePolicy7.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy7)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(u"color: rgb(4, 4, 4);\n"
"border-color: rgb(6, 6, 6);")
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setMargin(6)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet(u"color: rgb(4, 4, 4);\n"
"border-color: rgb(6, 6, 6);")
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.lineEdit_2)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setMargin(6)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lineEdit_3 = QLineEdit(self.frame_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy6.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy6)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet(u"color: rgb(4, 4, 4);\n"
"border-color: rgb(6, 6, 6);")
        self.lineEdit_3.setDragEnabled(True)
        self.lineEdit_3.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.gridLayout_3.addWidget(self.frame_3, 4, 0, 1, 6)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 100))
        font3 = QFont()
        font3.setFamily(u"MS UI Gothic")
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_2.setFont(font3)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_2, 2, 5, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)


        self.retranslateUi(PRecord)

        QMetaObject.connectSlotsByName(PRecord)
    # setupUi

    def retranslateUi(self, PRecord):
        PRecord.setWindowTitle(QCoreApplication.translate("PRecord", u"Patient's Record", None))
        self.addNewBtn.setText(QCoreApplication.translate("PRecord", u"Add New Record", None))
        self.label_3.setText(QCoreApplication.translate("PRecord", u" Medical Record", None))
        self.label_4.setText(QCoreApplication.translate("PRecord", u" Patient's Details", None))
        self.deleteBtn.setText(QCoreApplication.translate("PRecord", u"Delete", None))
        self.closeBtn.setText(QCoreApplication.translate("PRecord", u"Close", None))
        self.logo.setText("")
        self.label.setText(QCoreApplication.translate("PRecord", u"Patient's Record No. 000000000", None))
        self.minButton.setText(QCoreApplication.translate("PRecord", u"__", None))
        self.closeButton.setText(QCoreApplication.translate("PRecord", u"X", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PRecord", u"Date", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PRecord", u"Doctor", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PRecord", u"Diagnosis", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PRecord", u"Action", None));
        self.label_8.setText(QCoreApplication.translate("PRecord", u"First Name:", None))
        self.label_9.setText(QCoreApplication.translate("PRecord", u"Last Name:", None))
        self.label_5.setText(QCoreApplication.translate("PRecord", u"Gender:", None))
        self.label_6.setText(QCoreApplication.translate("PRecord", u"Age:", None))
        self.label_7.setText(QCoreApplication.translate("PRecord", u"Class:", None))
        self.label_2.setText(QCoreApplication.translate("PRecord", u"Card No.: 00000000", None))
    # retranslateUi

