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
        Bill.resize(446, 608)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Bill.sizePolicy().hasHeightForWidth())
        Bill.setSizePolicy(sizePolicy)
        Bill.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(Bill)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bgLayer = QFrame(Bill)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setAutoFillBackground(True)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
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

        self.gridLayout_2.addWidget(self.listView_3, 9, 0, 1, 1)

        self.label_2 = QLabel(self.bgLayer)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 4, 1, 1, 1)

        self.label_3 = QLabel(self.bgLayer)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)

        self.label = QLabel(self.bgLayer)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)

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

        self.gridLayout_2.addWidget(self.listView_2, 7, 0, 1, 1)

        self.label_5 = QLabel(self.bgLayer)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 8, 0, 1, 1)

        self.listView = QListView(self.bgLayer)
        self.listView.setObjectName(u"listView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy1)
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

        self.gridLayout_2.addWidget(self.listView, 5, 0, 1, 1)

        self.tableView = QTableView(self.bgLayer)
        self.tableView.setObjectName(u"tableView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.tableView, 5, 1, 5, 1)

        self.label_4 = QLabel(self.bgLayer)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(5)

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.remove = QPushButton(self.bgLayer)
        self.remove.setObjectName(u"remove")

        self.horizontalLayout.addWidget(self.remove)

        self.calculate = QPushButton(self.bgLayer)
        self.calculate.setObjectName(u"calculate")

        self.horizontalLayout.addWidget(self.calculate)


        self.gridLayout_2.addLayout(self.horizontalLayout, 10, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.save = QPushButton(self.bgLayer)
        self.save.setObjectName(u"save")

        self.horizontalLayout_4.addWidget(self.save)

        self.print = QPushButton(self.bgLayer)
        self.print.setObjectName(u"print")

        self.horizontalLayout_4.addWidget(self.print)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 10, 1, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 5, 0, 1, 1)

        self.frame_2 = QFrame(Bill)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setContentsMargins(3, 0, 8, 0)

        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.logo = QLabel(Bill)
        self.logo.setObjectName(u"logo")
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.logo)

        self.label_6 = QLabel(Bill)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.closeButton = QPushButton(Bill)
        self.closeButton.setObjectName(u"closeButton")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(12)
        self.closeButton.setFont(font1)
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setMouseTracking(True)
        self.closeButton.setTabletTracking(True)
        self.closeButton.setLayoutDirection(Qt.LeftToRight)
        self.closeButton.setAutoFillBackground(True)
        self.closeButton.setAutoDefault(False)
        self.closeButton.setFlat(False)

        self.horizontalLayout_5.addWidget(self.closeButton)

        self.minButton = QPushButton(Bill)
        self.minButton.setObjectName(u"minButton")
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(11)
        self.minButton.setFont(font2)
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minButton.setMouseTracking(True)
        self.minButton.setTabletTracking(True)
        self.minButton.setAutoFillBackground(True)
        self.minButton.setStyleSheet(u"")
        self.minButton.setAutoDefault(False)
        self.minButton.setFlat(False)

        self.horizontalLayout_5.addWidget(self.minButton)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)


        self.retranslateUi(Bill)

        QMetaObject.connectSlotsByName(Bill)
    # setupUi

    def retranslateUi(self, Bill):
        Bill.setWindowTitle(QCoreApplication.translate("Bill", u"Bill", None))
        self.label_2.setText(QCoreApplication.translate("Bill", u"Total:", None))
        self.label_3.setText(QCoreApplication.translate("Bill", u"Lab", None))
        self.label.setText(QCoreApplication.translate("Bill", u"Pharmacy", None))
        self.label_5.setText(QCoreApplication.translate("Bill", u"Medical Consultation:", None))
        self.label_4.setText(QCoreApplication.translate("Bill", u"Medical Bill", None))
        self.remove.setText(QCoreApplication.translate("Bill", u"Remove", None))
        self.calculate.setText(QCoreApplication.translate("Bill", u"Calculate", None))
        self.save.setText(QCoreApplication.translate("Bill", u"Save", None))
        self.print.setText(QCoreApplication.translate("Bill", u"Print", None))
        self.logo.setText("")
        self.label_6.setText(QCoreApplication.translate("Bill", u"TextLabel", None))
        self.closeButton.setText(QCoreApplication.translate("Bill", u"X", None))
        self.minButton.setText(QCoreApplication.translate("Bill", u"__", None))
    # retranslateUi

