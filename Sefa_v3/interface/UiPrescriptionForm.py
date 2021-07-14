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
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgflayer = QFrame(PrescriptionForm)
        self.bgflayer.setObjectName(u"bgflayer")
        self.bgflayer.setFrameShape(QFrame.StyledPanel)
        self.bgflayer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.bgflayer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo = QLabel(self.bgflayer)
        self.logo.setObjectName(u"logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.logo)

        self.bgflbl = QLabel(self.bgflayer)
        self.bgflbl.setObjectName(u"bgflbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bgflbl.sizePolicy().hasHeightForWidth())
        self.bgflbl.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamily(u"Georgia")
        font.setPointSize(8)
        self.bgflbl.setFont(font)
        self.bgflbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.bgflbl.setMargin(5)

        self.horizontalLayout_2.addWidget(self.bgflbl)

        self.exitBtn = QPushButton(self.bgflayer)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.exitBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.bgLayer = QFrame(self.bgflayer)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.bgLayer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.dBtn = QPushButton(self.bgLayer)
        self.dBtn.setObjectName(u"dBtn")
        self.dBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.dBtn)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.bgLayer)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Georgia")
        font1.setPointSize(7)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_10.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.date = QLabel(self.bgLayer)
        self.date.setObjectName(u"date")
        font2 = QFont()
        font2.setFamily(u"Georgia")
        font2.setPointSize(7)
        font2.setBold(False)
        font2.setWeight(50)
        self.date.setFont(font2)

        self.horizontalLayout_4.addWidget(self.date)

        self.label_5 = QLabel(self.bgLayer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.cardNum = QLabel(self.bgLayer)
        self.cardNum.setObjectName(u"cardNum")
        sizePolicy1.setHeightForWidth(self.cardNum.sizePolicy().hasHeightForWidth())
        self.cardNum.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamily(u"Georgia")
        font3.setPointSize(7)
        self.cardNum.setFont(font3)

        self.horizontalLayout_4.addWidget(self.cardNum)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.bgLayer)
        self.groupBox.setObjectName(u"groupBox")
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(7)
        font4.setBold(True)
        font4.setWeight(75)
        self.groupBox.setFont(font4)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 22, -1, -1)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(5)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.lname = QLabel(self.groupBox)
        self.lname.setObjectName(u"lname")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lname.sizePolicy().hasHeightForWidth())
        self.lname.setSizePolicy(sizePolicy3)
        font5 = QFont()
        font5.setFamily(u"Tahoma")
        font5.setPointSize(7)
        font5.setBold(False)
        font5.setWeight(50)
        self.lname.setFont(font5)
        self.lname.setFrameShape(QFrame.StyledPanel)
        self.lname.setMargin(5)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lname)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setMargin(5)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.diagnosis = QLabel(self.groupBox)
        self.diagnosis.setObjectName(u"diagnosis")
        sizePolicy3.setHeightForWidth(self.diagnosis.sizePolicy().hasHeightForWidth())
        self.diagnosis.setSizePolicy(sizePolicy3)
        self.diagnosis.setFont(font5)
        self.diagnosis.setFrameShape(QFrame.StyledPanel)
        self.diagnosis.setMargin(5)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.diagnosis)


        self.gridLayout_4.addLayout(self.formLayout_2, 0, 1, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(5)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.fname = QLabel(self.groupBox)
        self.fname.setObjectName(u"fname")
        sizePolicy3.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy3)
        self.fname.setFont(font5)
        self.fname.setFocusPolicy(Qt.ClickFocus)
        self.fname.setFrameShape(QFrame.StyledPanel)
        self.fname.setMargin(5)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setMargin(5)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.prescribedBy = QLabel(self.groupBox)
        self.prescribedBy.setObjectName(u"prescribedBy")
        sizePolicy3.setHeightForWidth(self.prescribedBy.sizePolicy().hasHeightForWidth())
        self.prescribedBy.setSizePolicy(sizePolicy3)
        self.prescribedBy.setFont(font5)
        self.prescribedBy.setFrameShape(QFrame.StyledPanel)
        self.prescribedBy.setMargin(5)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.prescribedBy)


        self.gridLayout_4.addLayout(self.formLayout, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 2)

        self.frame_4 = QFrame(self.bgLayer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_3.addWidget(self.frame_4, 1, 0, 1, 2)

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
        font6 = QFont()
        font6.setFamily(u"Georgia")
        font6.setPointSize(8)
        font6.setBold(True)
        font6.setWeight(75)
        self.table.setFont(font6)
        self.table.setColumnCount(2)
        self.table.horizontalHeader().setMinimumSectionSize(28)
        self.table.horizontalHeader().setDefaultSectionSize(120)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.table, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_3, 4, 0, 1, 1)

        self.label_2 = QLabel(self.bgLayer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.bgLayer)


        self.gridLayout.addWidget(self.bgflayer, 0, 0, 1, 1)


        self.retranslateUi(PrescriptionForm)

        QMetaObject.connectSlotsByName(PrescriptionForm)
    # setupUi

    def retranslateUi(self, PrescriptionForm):
        PrescriptionForm.setWindowTitle(QCoreApplication.translate("PrescriptionForm", u"PrescriptionForm", None))
        self.logo.setText(QCoreApplication.translate("PrescriptionForm", u"logo", None))
        self.bgflbl.setText(QCoreApplication.translate("PrescriptionForm", u"Prescription Form", None))
        self.exitBtn.setText(QCoreApplication.translate("PrescriptionForm", u"X", None))
        self.dBtn.setText(QCoreApplication.translate("PrescriptionForm", u"Dispense", None))
        self.label_10.setText(QCoreApplication.translate("PrescriptionForm", u"Date: ", None))
        self.date.setText("")
        self.label_5.setText(QCoreApplication.translate("PrescriptionForm", u"Patient's Number:", None))
        self.cardNum.setText(QCoreApplication.translate("PrescriptionForm", u"0000000000", None))
        self.groupBox.setTitle(QCoreApplication.translate("PrescriptionForm", u"Patient's details", None))
        self.label_3.setText(QCoreApplication.translate("PrescriptionForm", u"Last Name:", None))
        self.lname.setText("")
        self.label_8.setText(QCoreApplication.translate("PrescriptionForm", u"Diagnosis:", None))
        self.diagnosis.setText("")
        self.label.setText(QCoreApplication.translate("PrescriptionForm", u"First Name:", None))
        self.fname.setText("")
        self.label_6.setText(QCoreApplication.translate("PrescriptionForm", u"Prescribed By:", None))
        self.prescribedBy.setText("")
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PrescriptionForm", u"Instock", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PrescriptionForm", u"Drug Name", None));
        self.label_2.setText(QCoreApplication.translate("PrescriptionForm", u"Prescription", None))
    # retranslateUi

