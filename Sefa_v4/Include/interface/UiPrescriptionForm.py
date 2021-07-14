# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PrescriptionForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PrescriptionForm(object):
    def setupUi(self, PrescriptionForm):
        if not PrescriptionForm.objectName():
            PrescriptionForm.setObjectName(u"PrescriptionForm")
        PrescriptionForm.resize(442, 266)
        self.gridLayout = QGridLayout(PrescriptionForm)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgLayer = QFrame(PrescriptionForm)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setFrameShape(QFrame.StyledPanel)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.bgLayer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.closeBtn = QPushButton(self.frame)
        self.closeBtn.setObjectName(u"closeBtn")

        self.horizontalLayout.addWidget(self.closeBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.dBtn = QPushButton(self.frame)
        self.dBtn.setObjectName(u"dBtn")

        self.horizontalLayout.addWidget(self.dBtn)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.table = QTableWidget(self.frame)
        self.table.setObjectName(u"table")

        self.gridLayout_3.addWidget(self.table, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.fname = QLabel(self.frame)
        self.fname.setObjectName(u"fname")
        font1 = QFont()
        font1.setPointSize(9)
        self.fname.setFont(font1)

        self.horizontalLayout_2.addWidget(self.fname)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lname = QLabel(self.frame)
        self.lname.setObjectName(u"lname")
        self.lname.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lname)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 0, 0, 1, 1)


        self.retranslateUi(PrescriptionForm)

        QMetaObject.connectSlotsByName(PrescriptionForm)
    # setupUi

    def retranslateUi(self, PrescriptionForm):
        PrescriptionForm.setWindowTitle(QCoreApplication.translate("PrescriptionForm", u"Prescription Form", None))
        self.closeBtn.setText(QCoreApplication.translate("PrescriptionForm", u"Close", None))
        self.dBtn.setText(QCoreApplication.translate("PrescriptionForm", u"Dispense", None))
        self.label_2.setText(QCoreApplication.translate("PrescriptionForm", u"First Name:", None))
        self.fname.setText(QCoreApplication.translate("PrescriptionForm", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("PrescriptionForm", u"Last Name:", None))
        self.lname.setText(QCoreApplication.translate("PrescriptionForm", u"TextLabel", None))
    # retranslateUi

