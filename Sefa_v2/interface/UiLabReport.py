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
        LabReport.resize(782, 552)
        self.gridLayout = QGridLayout(LabReport)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(LabReport)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 2, 0)
        self.logo = QLabel(self.frame_2)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_4.addWidget(self.logo)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setMargin(6)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.miniBtn = QPushButton(self.frame_2)
        self.miniBtn.setObjectName(u"miniBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.miniBtn.sizePolicy().hasHeightForWidth())
        self.miniBtn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(self.frame_2)
        self.exitBtn.setObjectName(u"exitBtn")
        sizePolicy1.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.exitBtn)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.bgLayer = QFrame(LabReport)
        self.bgLayer.setObjectName(u"bgLayer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bgLayer.sizePolicy().hasHeightForWidth())
        self.bgLayer.setSizePolicy(sizePolicy2)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.bgLayer)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.closeBtn = QPushButton(self.bgLayer)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.closeBtn)

        self.submitBtn = QPushButton(self.bgLayer)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.submitBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.label_9 = QLabel(self.bgLayer)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMargin(5)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.bgLayer)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
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


        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 1, 0, 1, 1)


        self.retranslateUi(LabReport)

        QMetaObject.connectSlotsByName(LabReport)
    # setupUi

    def retranslateUi(self, LabReport):
        LabReport.setWindowTitle(QCoreApplication.translate("LabReport", u"Dialog", None))
        self.logo.setText(QCoreApplication.translate("LabReport", u"llogo", None))
        self.label_4.setText(QCoreApplication.translate("LabReport", u"Lab Report", None))
        self.miniBtn.setText(QCoreApplication.translate("LabReport", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("LabReport", u"X", None))
        self.pushButton.setText(QCoreApplication.translate("LabReport", u"Add Sample", None))
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

