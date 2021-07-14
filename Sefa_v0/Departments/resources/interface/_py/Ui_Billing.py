# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Billing.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Billing(object):
    def setupUi(self, Billing):
        if not Billing.objectName():
            Billing.setObjectName(u"Billing")
        Billing.resize(560, 846)
        Billing.setMinimumSize(QSize(500, 450))
        Billing.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(Billing)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(Billing)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setContentsMargins(3, 0, 8, 0)
        self.logo = QLabel(self.frame_2)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 45))
        self.logo.setMaximumSize(QSize(45, 45))
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logo)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_29 = QLabel(self.frame_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setWordWrap(True)
        self.label_29.setMargin(7)

        self.gridLayout_13.addWidget(self.label_29, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 1, -1)
        self.minButton = QPushButton(self.frame_2)
        self.minButton.setObjectName(u"minButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minButton.sizePolicy().hasHeightForWidth())
        self.minButton.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(11)
        self.minButton.setFont(font)
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minButton.setMouseTracking(True)
        self.minButton.setTabletTracking(True)
        self.minButton.setAutoFillBackground(True)
        self.minButton.setStyleSheet(u"")
        self.minButton.setAutoDefault(False)
        self.minButton.setFlat(False)

        self.horizontalLayout_6.addWidget(self.minButton)

        self.closeButton = QPushButton(self.frame_2)
        self.closeButton.setObjectName(u"closeButton")
        sizePolicy1.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy1)
        self.closeButton.setMaximumSize(QSize(16777215, 16777215))
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

        self.horizontalLayout_6.addWidget(self.closeButton)


        self.gridLayout_13.addLayout(self.horizontalLayout_6, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(260, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_13)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.bgLayer = QFrame(Billing)
        self.bgLayer.setObjectName(u"bgLayer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bgLayer.sizePolicy().hasHeightForWidth())
        self.bgLayer.setSizePolicy(sizePolicy2)
        self.bgLayer.setAutoFillBackground(True)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(1)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.bgLayer)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)

        self.print = QPushButton(self.bgLayer)
        self.print.setObjectName(u"print")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(3)
        sizePolicy3.setHeightForWidth(self.print.sizePolicy().hasHeightForWidth())
        self.print.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.print, 8, 1, 1, 1)

        self.label_2 = QLabel(self.bgLayer)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)

        self.label_4 = QLabel(self.bgLayer)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(5)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.remove = QPushButton(self.bgLayer)
        self.remove.setObjectName(u"remove")
        sizePolicy3.setHeightForWidth(self.remove.sizePolicy().hasHeightForWidth())
        self.remove.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.remove)

        self.calculate = QPushButton(self.bgLayer)
        self.calculate.setObjectName(u"calculate")
        sizePolicy3.setHeightForWidth(self.calculate.sizePolicy().hasHeightForWidth())
        self.calculate.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.calculate)


        self.gridLayout_2.addLayout(self.horizontalLayout, 8, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add = QPushButton(self.bgLayer)
        self.add.setObjectName(u"add")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.add)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.label = QLabel(self.bgLayer)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.label_3 = QLabel(self.bgLayer)
        self.label_3.setObjectName(u"label_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.tableView = QTableView(self.bgLayer)
        self.tableView.setObjectName(u"tableView")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.tableView, 3, 1, 5, 1)

        self.listView = QListView(self.bgLayer)
        self.listView.setObjectName(u"listView")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(2)
        sizePolicy8.setVerticalStretch(10)
        sizePolicy8.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy8)
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

        self.gridLayout_2.addWidget(self.listView, 3, 0, 1, 1)

        self.listView_2 = QListView(self.bgLayer)
        self.listView_2.setObjectName(u"listView_2")
        sizePolicy8.setHeightForWidth(self.listView_2.sizePolicy().hasHeightForWidth())
        self.listView_2.setSizePolicy(sizePolicy8)
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

        self.gridLayout_2.addWidget(self.listView_2, 5, 0, 1, 1)

        self.listView_3 = QListView(self.bgLayer)
        self.listView_3.setObjectName(u"listView_3")
        sizePolicy8.setHeightForWidth(self.listView_3.sizePolicy().hasHeightForWidth())
        self.listView_3.setSizePolicy(sizePolicy8)
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

        self.gridLayout_2.addWidget(self.listView_3, 7, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 1, 0, 1, 1)


        self.retranslateUi(Billing)

        QMetaObject.connectSlotsByName(Billing)
    # setupUi

    def retranslateUi(self, Billing):
        Billing.setWindowTitle(QCoreApplication.translate("Billing", u"Bill", None))
        self.logo.setText("")
        self.label_29.setText(QCoreApplication.translate("Billing", u"Bill", None))
        self.minButton.setText(QCoreApplication.translate("Billing", u"__", None))
        self.closeButton.setText(QCoreApplication.translate("Billing", u"X", None))
        self.label_5.setText(QCoreApplication.translate("Billing", u"Medical Consultation:", None))
        self.print.setText(QCoreApplication.translate("Billing", u"Print", None))
        self.label_2.setText(QCoreApplication.translate("Billing", u"Total:", None))
        self.label_4.setText(QCoreApplication.translate("Billing", u"Medical Bill", None))
        self.remove.setText(QCoreApplication.translate("Billing", u"Remove", None))
        self.calculate.setText(QCoreApplication.translate("Billing", u"Calculate", None))
        self.add.setText(QCoreApplication.translate("Billing", u"Add", None))
        self.label.setText(QCoreApplication.translate("Billing", u"Pharmacy", None))
        self.label_3.setText(QCoreApplication.translate("Billing", u"Lab", None))
    # retranslateUi

