# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PharmRequest.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PharmRequest(object):
    def setupUi(self, PharmRequest):
        if not PharmRequest.objectName():
            PharmRequest.setObjectName(u"PharmRequest")
        PharmRequest.resize(411, 544)
        self.verticalLayout = QVBoxLayout(PharmRequest)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bgLayer = QFrame(PharmRequest)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setFrameShape(QFrame.StyledPanel)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bgLayer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bgframe = QFrame(self.bgLayer)
        self.bgframe.setObjectName(u"bgframe")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bgframe.sizePolicy().hasHeightForWidth())
        self.bgframe.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.bgframe.setFont(font)
        self.bgframe.setFrameShape(QFrame.Box)
        self.bgframe.setFrameShadow(QFrame.Raised)
        self.bgframe.setLineWidth(2)
        self.bgframe.setMidLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.bgframe)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.bgframe)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.date = QLabel(self.bgframe)
        self.date.setObjectName(u"date")
        font2 = QFont()
        font2.setPointSize(10)
        self.date.setFont(font2)

        self.horizontalLayout_3.addWidget(self.date)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.pharmList = QTableWidget(self.bgframe)
        if (self.pharmList.columnCount() < 2):
            self.pharmList.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.pharmList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.pharmList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.pharmList.rowCount() < 20):
            self.pharmList.setRowCount(20)
        self.pharmList.setObjectName(u"pharmList")
        self.pharmList.setFont(font2)
        self.pharmList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.pharmList.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.pharmList.setAlternatingRowColors(True)
        self.pharmList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pharmList.setRowCount(20)
        self.pharmList.setColumnCount(2)
        self.pharmList.horizontalHeader().setCascadingSectionResizes(True)
        self.pharmList.horizontalHeader().setMinimumSectionSize(8)
        self.pharmList.horizontalHeader().setDefaultSectionSize(149)
        self.pharmList.horizontalHeader().setStretchLastSection(True)
        self.pharmList.verticalHeader().setDefaultSectionSize(21)
        self.pharmList.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_3.addWidget(self.pharmList)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sendBtn = QPushButton(self.bgframe)
        self.sendBtn.setObjectName(u"sendBtn")
        self.sendBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.sendBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.bgframe)


        self.verticalLayout.addWidget(self.bgLayer)


        self.retranslateUi(PharmRequest)

        QMetaObject.connectSlotsByName(PharmRequest)
    # setupUi

    def retranslateUi(self, PharmRequest):
        PharmRequest.setWindowTitle(QCoreApplication.translate("PharmRequest", u"Prescription Form", None))
        self.label_3.setText(QCoreApplication.translate("PharmRequest", u"Date:", None))
        self.date.setText(QCoreApplication.translate("PharmRequest", u"10-3-2021", None))
        ___qtablewidgetitem = self.pharmList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PharmRequest", u"List", None));
        ___qtablewidgetitem1 = self.pharmList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PharmRequest", u"Dosage", None));
#if QT_CONFIG(tooltip)
        self.sendBtn.setToolTip(QCoreApplication.translate("PharmRequest", u"<html><head/><body><p>Click to send prescription to Pharmacy</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sendBtn.setText(QCoreApplication.translate("PharmRequest", u"Send Prescription", None))
    # retranslateUi

