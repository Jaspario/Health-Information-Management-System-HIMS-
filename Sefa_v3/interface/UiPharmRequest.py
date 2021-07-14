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
        self.bgflayer = QFrame(PharmRequest)
        self.bgflayer.setObjectName(u"bgflayer")
        self.bgflayer.setFrameShape(QFrame.StyledPanel)
        self.bgflayer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bgflayer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo = QLabel(self.bgflayer)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.logo)

        self.label = QLabel(self.bgflayer)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label)

        self.exitBtn = QPushButton(self.bgflayer)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.exitBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.frame = QFrame(self.bgflayer)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.pharmList = QTableWidget(self.frame)
        if (self.pharmList.columnCount() < 2):
            self.pharmList.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.pharmList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.pharmList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.pharmList.rowCount() < 20):
            self.pharmList.setRowCount(20)
        self.pharmList.setObjectName(u"pharmList")
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


        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sendBtn = QPushButton(self.bgflayer)
        self.sendBtn.setObjectName(u"sendBtn")
        self.sendBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.sendBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.bgflayer)


        self.retranslateUi(PharmRequest)

        QMetaObject.connectSlotsByName(PharmRequest)
    # setupUi

    def retranslateUi(self, PharmRequest):
        PharmRequest.setWindowTitle(QCoreApplication.translate("PharmRequest", u"Dialog", None))
        self.logo.setText(QCoreApplication.translate("PharmRequest", u"logo", None))
        self.label.setText(QCoreApplication.translate("PharmRequest", u"Prescription List", None))
#if QT_CONFIG(tooltip)
        self.exitBtn.setToolTip(QCoreApplication.translate("PharmRequest", u"<html><head/><body><p>Click to exit window</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.exitBtn.setText(QCoreApplication.translate("PharmRequest", u"X", None))
        self.label_3.setText(QCoreApplication.translate("PharmRequest", u"Date:", None))
        self.label_2.setText(QCoreApplication.translate("PharmRequest", u"10-3-2021", None))
        ___qtablewidgetitem = self.pharmList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PharmRequest", u"List", None));
        ___qtablewidgetitem1 = self.pharmList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PharmRequest", u"Dosage", None));
#if QT_CONFIG(tooltip)
        self.sendBtn.setToolTip(QCoreApplication.translate("PharmRequest", u"<html><head/><body><p>Click to send prescription to Pharmacy</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sendBtn.setText(QCoreApplication.translate("PharmRequest", u"Send Prescription", None))
    # retranslateUi

