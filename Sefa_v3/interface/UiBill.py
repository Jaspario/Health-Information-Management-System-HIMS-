# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Bill.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Bill(object):
    def setupUi(self, Bill):
        if not Bill.objectName():
            Bill.setObjectName(u"Bill")
        Bill.resize(504, 614)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Bill.sizePolicy().hasHeightForWidth())
        Bill.setSizePolicy(sizePolicy)
        Bill.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(Bill)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_2 = QFrame(Bill)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setContentsMargins(3, 0, 8, 0)

        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.bgflayer = QFrame(Bill)
        self.bgflayer.setObjectName(u"bgflayer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bgflayer.sizePolicy().hasHeightForWidth())
        self.bgflayer.setSizePolicy(sizePolicy1)
        self.bgflayer.setFrameShape(QFrame.StyledPanel)
        self.bgflayer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.bgflayer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.logo = QLabel(self.bgflayer)
        self.logo.setObjectName(u"logo")
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.logo)

        self.label_6 = QLabel(self.bgflayer)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMargin(5)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.miniBtn = QPushButton(self.bgflayer)
        self.miniBtn.setObjectName(u"miniBtn")
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(11)
        self.miniBtn.setFont(font)
        self.miniBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.miniBtn.setMouseTracking(True)
        self.miniBtn.setTabletTracking(True)
        self.miniBtn.setAutoFillBackground(True)
        self.miniBtn.setStyleSheet(u"")
        self.miniBtn.setAutoDefault(False)
        self.miniBtn.setFlat(False)

        self.horizontalLayout_5.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(self.bgflayer)
        self.exitBtn.setObjectName(u"exitBtn")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(12)
        self.exitBtn.setFont(font1)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setMouseTracking(True)
        self.exitBtn.setTabletTracking(True)
        self.exitBtn.setLayoutDirection(Qt.LeftToRight)
        self.exitBtn.setAutoFillBackground(True)
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setFlat(False)

        self.horizontalLayout_5.addWidget(self.exitBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.bgLayer = QFrame(self.bgflayer)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setAutoFillBackground(True)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listView_2 = QListView(self.bgLayer)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setAutoFillBackground(True)
        self.listView_2.setFrameShape(QFrame.Box)
        self.listView_2.setFrameShadow(QFrame.Plain)
        self.listView_2.setLineWidth(1)
        self.listView_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listView_2.setDragDropOverwriteMode(True)
        self.listView_2.setDefaultDropAction(Qt.CopyAction)
        self.listView_2.setAlternatingRowColors(True)
        self.listView_2.setMovement(QListView.Free)
        self.listView_2.setProperty("isWrapping", True)
        self.listView_2.setSpacing(2)
        self.listView_2.setUniformItemSizes(True)
        self.listView_2.setWordWrap(True)
        self.listView_2.setSelectionRectVisible(True)
        self.listView_2.setItemAlignment(Qt.AlignAbsolute|Qt.AlignCenter|Qt.AlignHCenter|Qt.AlignHorizontal_Mask|Qt.AlignJustify|Qt.AlignLeading|Qt.AlignLeft|Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.listView_2, 8, 0, 1, 1)

        self.label_2 = QLabel(self.bgLayer)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 5, 1, 1, 1)

        self.label_4 = QLabel(self.bgLayer)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(5)

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 2)

        self.label_3 = QLabel(self.bgLayer)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 7, 0, 1, 1)

        self.label_5 = QLabel(self.bgLayer)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 9, 0, 1, 1)

        self.listView_3 = QListView(self.bgLayer)
        self.listView_3.setObjectName(u"listView_3")
        self.listView_3.setAutoFillBackground(True)
        self.listView_3.setFrameShape(QFrame.Box)
        self.listView_3.setFrameShadow(QFrame.Plain)
        self.listView_3.setLineWidth(1)
        self.listView_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listView_3.setDragEnabled(True)
        self.listView_3.setDragDropOverwriteMode(True)
        self.listView_3.setDragDropMode(QAbstractItemView.DragOnly)
        self.listView_3.setDefaultDropAction(Qt.CopyAction)
        self.listView_3.setAlternatingRowColors(True)
        self.listView_3.setMovement(QListView.Free)
        self.listView_3.setProperty("isWrapping", True)
        self.listView_3.setSpacing(2)
        self.listView_3.setUniformItemSizes(True)
        self.listView_3.setWordWrap(True)
        self.listView_3.setSelectionRectVisible(True)
        self.listView_3.setItemAlignment(Qt.AlignAbsolute|Qt.AlignCenter|Qt.AlignHCenter|Qt.AlignHorizontal_Mask|Qt.AlignJustify|Qt.AlignLeading|Qt.AlignLeft|Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.listView_3, 10, 0, 1, 1)

        self.tableView = QTableView(self.bgLayer)
        self.tableView.setObjectName(u"tableView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.tableView, 6, 1, 5, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.saveBtn = QPushButton(self.bgLayer)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout_4.addWidget(self.saveBtn)

        self.printBtn = QPushButton(self.bgLayer)
        self.printBtn.setObjectName(u"printBtn")

        self.horizontalLayout_4.addWidget(self.printBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 11, 1, 1, 1)

        self.label = QLabel(self.bgLayer)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.removeBtn = QPushButton(self.bgLayer)
        self.removeBtn.setObjectName(u"removeBtn")

        self.horizontalLayout.addWidget(self.removeBtn)

        self.calculateBtn = QPushButton(self.bgLayer)
        self.calculateBtn.setObjectName(u"calculateBtn")

        self.horizontalLayout.addWidget(self.calculateBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout, 11, 0, 1, 1)

        self.listView = QListView(self.bgLayer)
        self.listView.setObjectName(u"listView")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(3)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy4)
        self.listView.setAutoFillBackground(True)
        self.listView.setFrameShape(QFrame.Box)
        self.listView.setFrameShadow(QFrame.Plain)
        self.listView.setLineWidth(1)
        self.listView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listView.setDragEnabled(True)
        self.listView.setDragDropOverwriteMode(True)
        self.listView.setDefaultDropAction(Qt.CopyAction)
        self.listView.setAlternatingRowColors(True)
        self.listView.setSelectionMode(QAbstractItemView.SingleSelection)

        self.gridLayout_2.addWidget(self.listView, 6, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.bgLayer)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 2)


        self.verticalLayout.addWidget(self.bgLayer)


        self.gridLayout.addWidget(self.bgflayer, 1, 0, 1, 1)


        self.retranslateUi(Bill)

        QMetaObject.connectSlotsByName(Bill)
    # setupUi

    def retranslateUi(self, Bill):
        Bill.setWindowTitle(QCoreApplication.translate("Bill", u"Bill", None))
        self.logo.setText("")
        self.label_6.setText(QCoreApplication.translate("Bill", u"Medical Bill", None))
        self.miniBtn.setText(QCoreApplication.translate("Bill", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("Bill", u"X", None))
        self.label_2.setText(QCoreApplication.translate("Bill", u"Total:", None))
        self.label_4.setText(QCoreApplication.translate("Bill", u"Medical Bill", None))
        self.label_3.setText(QCoreApplication.translate("Bill", u"Lab", None))
        self.label_5.setText(QCoreApplication.translate("Bill", u"Medical Consultation:", None))
        self.saveBtn.setText(QCoreApplication.translate("Bill", u"Save", None))
        self.printBtn.setText(QCoreApplication.translate("Bill", u"Print", None))
        self.label.setText(QCoreApplication.translate("Bill", u"Pharmacy", None))
        self.removeBtn.setText(QCoreApplication.translate("Bill", u"Remove", None))
        self.calculateBtn.setText(QCoreApplication.translate("Bill", u"Calculate", None))
        self.pushButton.setText(QCoreApplication.translate("Bill", u"Edit", None))
    # retranslateUi

