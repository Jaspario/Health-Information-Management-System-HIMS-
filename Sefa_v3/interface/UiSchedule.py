# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Schedule.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dSchedule(object):
    def setupUi(self, dSchedule):
        if not dSchedule.objectName():
            dSchedule.setObjectName(u"dSchedule")
        dSchedule.resize(494, 591)
        self.gridLayout = QGridLayout(dSchedule)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(dSchedule)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setContentsMargins(3, 0, 8, 0)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 45))
        self.logo.setMaximumSize(QSize(45, 45))
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logo)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalSpacer = QSpacerItem(300, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.closeButton = QPushButton(self.frame)
        self.closeButton.setObjectName(u"closeButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy1)
        self.closeButton.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        self.closeButton.setFont(font)
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setMouseTracking(True)
        self.closeButton.setTabletTracking(True)
        self.closeButton.setLayoutDirection(Qt.LeftToRight)
        self.closeButton.setAutoFillBackground(True)
        self.closeButton.setAutoDefault(False)
        self.closeButton.setFlat(False)

        self.gridLayout_13.addWidget(self.closeButton, 0, 3, 1, 1)

        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setWordWrap(True)
        self.label_29.setMargin(7)

        self.gridLayout_13.addWidget(self.label_29, 0, 0, 1, 1)

        self.minButton = QPushButton(self.frame)
        self.minButton.setObjectName(u"minButton")
        sizePolicy1.setHeightForWidth(self.minButton.sizePolicy().hasHeightForWidth())
        self.minButton.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(11)
        self.minButton.setFont(font1)
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minButton.setMouseTracking(True)
        self.minButton.setTabletTracking(True)
        self.minButton.setAutoFillBackground(True)
        self.minButton.setStyleSheet(u"")
        self.minButton.setAutoDefault(False)
        self.minButton.setFlat(False)

        self.gridLayout_13.addWidget(self.minButton, 0, 2, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_13)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.bgLayer = QFrame(dSchedule)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setAutoFillBackground(True)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableView = QTableView(self.bgLayer)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFrameShape(QFrame.Box)
        self.tableView.setFrameShadow(QFrame.Plain)
        self.tableView.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setProperty("showSortIndicator", True)
        self.tableView.verticalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.tableView, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 1, 0, 1, 1)


        self.retranslateUi(dSchedule)

        QMetaObject.connectSlotsByName(dSchedule)
    # setupUi

    def retranslateUi(self, dSchedule):
        dSchedule.setWindowTitle(QCoreApplication.translate("dSchedule", u"Dialog", None))
        self.logo.setText("")
        self.closeButton.setText(QCoreApplication.translate("dSchedule", u"X", None))
        self.label_29.setText(QCoreApplication.translate("dSchedule", u"Doctor's Schedule", None))
        self.minButton.setText(QCoreApplication.translate("dSchedule", u"__", None))
    # retranslateUi

