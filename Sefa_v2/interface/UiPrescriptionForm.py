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
        PrescriptionForm.resize(448, 621)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PrescriptionForm.sizePolicy().hasHeightForWidth())
        PrescriptionForm.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(PrescriptionForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(PrescriptionForm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 2, 0)
        self.logo = QLabel(self.frame_2)
        self.logo.setObjectName(u"logo")

        self.horizontalLayout_4.addWidget(self.logo)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setMargin(6)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.exitBtn = QPushButton(self.frame_2)
        self.exitBtn.setObjectName(u"exitBtn")

        self.horizontalLayout_4.addWidget(self.exitBtn)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.bgLayer = QFrame(PrescriptionForm)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.bgLayer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.bgLayer)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 22, -1, -1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(5)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.fname = QLabel(self.groupBox)
        self.fname.setObjectName(u"fname")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy1)
        self.fname.setFrameShape(QFrame.StyledPanel)
        self.fname.setMargin(2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setMargin(5)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.prescribedBy = QLabel(self.groupBox)
        self.prescribedBy.setObjectName(u"prescribedBy")
        sizePolicy1.setHeightForWidth(self.prescribedBy.sizePolicy().hasHeightForWidth())
        self.prescribedBy.setSizePolicy(sizePolicy1)
        self.prescribedBy.setFrameShape(QFrame.StyledPanel)
        self.prescribedBy.setMargin(2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.prescribedBy)


        self.gridLayout_4.addLayout(self.formLayout, 0, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(5)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.lname = QLabel(self.groupBox)
        self.lname.setObjectName(u"lname")
        sizePolicy1.setHeightForWidth(self.lname.sizePolicy().hasHeightForWidth())
        self.lname.setSizePolicy(sizePolicy1)
        self.lname.setFrameShape(QFrame.StyledPanel)
        self.lname.setMargin(2)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lname)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setMargin(5)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.diagnosis = QLabel(self.groupBox)
        self.diagnosis.setObjectName(u"diagnosis")
        sizePolicy1.setHeightForWidth(self.diagnosis.sizePolicy().hasHeightForWidth())
        self.diagnosis.setSizePolicy(sizePolicy1)
        self.diagnosis.setFrameShape(QFrame.StyledPanel)
        self.diagnosis.setMargin(2)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.diagnosis)


        self.gridLayout_4.addLayout(self.formLayout_2, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 2)

        self.frame_4 = QFrame(self.bgLayer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setFamily(u"Georgia")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.date = QLabel(self.frame_4)
        self.date.setObjectName(u"date")
        font1 = QFont()
        font1.setFamily(u"Georgia")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setWeight(50)
        self.date.setFont(font1)

        self.horizontalLayout_3.addWidget(self.date)


        self.gridLayout_3.addWidget(self.frame_4, 0, 0, 1, 2)

        self.frame_3 = QFrame(self.bgLayer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table = QTableWidget(self.frame_3)
        if (self.table.columnCount() < 2):
            self.table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table.setObjectName(u"table")
        self.table.setColumnCount(2)
        self.table.horizontalHeader().setMinimumSectionSize(28)
        self.table.horizontalHeader().setDefaultSectionSize(120)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.table, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_3, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.dispense = QPushButton(self.bgLayer)
        self.dispense.setObjectName(u"dispense")

        self.horizontalLayout_5.addWidget(self.dispense)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 1, 0, 1, 1)


        self.retranslateUi(PrescriptionForm)

        QMetaObject.connectSlotsByName(PrescriptionForm)
    # setupUi

    def retranslateUi(self, PrescriptionForm):
        PrescriptionForm.setWindowTitle(QCoreApplication.translate("PrescriptionForm", u"PrescriptionForm", None))
        self.logo.setText(QCoreApplication.translate("PrescriptionForm", u"logo", None))
        self.label_4.setText(QCoreApplication.translate("PrescriptionForm", u"Prescription Form", None))
        self.exitBtn.setText(QCoreApplication.translate("PrescriptionForm", u"X", None))
        self.groupBox.setTitle(QCoreApplication.translate("PrescriptionForm", u"Patient's details", None))
        self.label.setText(QCoreApplication.translate("PrescriptionForm", u"First Name:", None))
        self.fname.setText("")
        self.label_6.setText(QCoreApplication.translate("PrescriptionForm", u"Prescribed By:", None))
        self.prescribedBy.setText("")
        self.label_3.setText(QCoreApplication.translate("PrescriptionForm", u"Last Name:", None))
        self.lname.setText("")
        self.label_8.setText(QCoreApplication.translate("PrescriptionForm", u"Diagnosis:", None))
        self.diagnosis.setText("")
        self.label_10.setText(QCoreApplication.translate("PrescriptionForm", u"Date: ", None))
        self.date.setText("")
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PrescriptionForm", u"Instock", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PrescriptionForm", u"Drug Name", None));
        self.dispense.setText(QCoreApplication.translate("PrescriptionForm", u"Dispense", None))
    # retranslateUi

