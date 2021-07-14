# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LabReport.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LabReport(object):
    def setupUi(self, LabReport):
        if not LabReport.objectName():
            LabReport.setObjectName(u"LabReport")
        LabReport.resize(888, 591)
        self.gridLayout = QGridLayout(LabReport)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(LabReport)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, -1)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.frame_2)
        self.logo.setObjectName(u"logo")

        self.horizontalLayout_4.addWidget(self.logo)

        self.bgflbl = QLabel(self.frame_2)
        self.bgflbl.setObjectName(u"bgflbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bgflbl.sizePolicy().hasHeightForWidth())
        self.bgflbl.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(8)
        self.bgflbl.setFont(font)
        self.bgflbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.bgflbl.setMargin(5)

        self.horizontalLayout_4.addWidget(self.bgflbl)

        self.miniBtn = QPushButton(self.frame_2)
        self.miniBtn.setObjectName(u"miniBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.miniBtn.sizePolicy().hasHeightForWidth())
        self.miniBtn.setSizePolicy(sizePolicy2)
        self.miniBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(self.frame_2)
        self.exitBtn.setObjectName(u"exitBtn")
        sizePolicy2.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy2)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.exitBtn)


        self.verticalLayout.addWidget(self.frame_2)

        self.bgLayer = QFrame(self.frame)
        self.bgLayer.setObjectName(u"bgLayer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bgLayer.sizePolicy().hasHeightForWidth())
        self.bgLayer.setSizePolicy(sizePolicy3)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addBtn = QPushButton(self.bgLayer)
        self.addBtn.setObjectName(u"addBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.addBtn.sizePolicy().hasHeightForWidth())
        self.addBtn.setSizePolicy(sizePolicy4)
        self.addBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.addBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.closeBtn = QPushButton(self.bgLayer)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(0, 30))
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.closeBtn)

        self.submitBtn = QPushButton(self.bgLayer)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setMinimumSize(QSize(0, 30))
        self.submitBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.submitBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.label_9 = QLabel(self.bgLayer)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMargin(5)

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.bgLayer)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(244, 208, 116);\n"
"color: rgb(4, 4, 4);")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setColumnCount(9)

        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.bgLayer)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(LabReport)

        QMetaObject.connectSlotsByName(LabReport)
    # setupUi

    def retranslateUi(self, LabReport):
        LabReport.setWindowTitle(QCoreApplication.translate("LabReport", u"Lab Report", None))
        self.logo.setText(QCoreApplication.translate("LabReport", u"llogo", None))
        self.bgflbl.setText(QCoreApplication.translate("LabReport", u"Lab Report", None))
        self.miniBtn.setText(QCoreApplication.translate("LabReport", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("LabReport", u"X", None))
        self.addBtn.setText(QCoreApplication.translate("LabReport", u"Add Sample", None))
        self.closeBtn.setText(QCoreApplication.translate("LabReport", u"Close", None))
        self.submitBtn.setText(QCoreApplication.translate("LabReport", u"Submit", None))
        self.label_9.setText(QCoreApplication.translate("LabReport", u"Sample Tests", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LabReport", u"Date/Time", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LabReport", u"Section", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("LabReport", u"Category", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("LabReport", u"Type", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("LabReport", u"Test", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("LabReport", u"Samples", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("LabReport", u"Units", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("LabReport", u"Result", None));
    # retranslateUi

