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
        LabReport.resize(571, 300)
        self.gridLayout = QGridLayout(LabReport)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(LabReport)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.patientID = QLabel(self.frame_2)
        self.patientID.setObjectName(u"patientID")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.patientID.sizePolicy().hasHeightForWidth())
        self.patientID.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.patientID)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.table = QTableWidget(self.frame_2)
        if (self.table.columnCount() < 1):
            self.table.setColumnCount(1)
        self.table.setObjectName(u"table")
        self.table.setColumnCount(1)

        self.verticalLayout.addWidget(self.table)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(LabReport)

        QMetaObject.connectSlotsByName(LabReport)
    # setupUi

    def retranslateUi(self, LabReport):
        LabReport.setWindowTitle(QCoreApplication.translate("LabReport", u"Laboratory Report", None))
        self.label_2.setText(QCoreApplication.translate("LabReport", u"Patient's ID:", None))
        self.patientID.setText(QCoreApplication.translate("LabReport", u"00000000000", None))
    # retranslateUi

