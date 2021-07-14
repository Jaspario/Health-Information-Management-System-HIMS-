# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClinicalRecord.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ClinicalRecord(object):
    def setupUi(self, ClinicalRecord):
        if not ClinicalRecord.objectName():
            ClinicalRecord.setObjectName(u"ClinicalRecord")
        ClinicalRecord.resize(513, 525)
        self.gridLayout = QGridLayout(ClinicalRecord)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgLayer = QFrame(ClinicalRecord)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setFrameShape(QFrame.StyledPanel)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.bgframe = QFrame(self.bgLayer)
        self.bgframe.setObjectName(u"bgframe")
        self.bgframe.setFrameShape(QFrame.Box)
        self.bgframe.setFrameShadow(QFrame.Raised)
        self.bgframe.setLineWidth(2)
        self.bgframe.setMidLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.bgframe)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_12 = QLabel(self.bgframe)
        self.label_12.setObjectName(u"label_12")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_12)

        self.patientID = QLabel(self.bgframe)
        self.patientID.setObjectName(u"patientID")
        font1 = QFont()
        font1.setPointSize(10)
        self.patientID.setFont(font1)

        self.horizontalLayout_2.addWidget(self.patientID)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.bgframe)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.groupBox.setFont(font2)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.fname = QLabel(self.groupBox)
        self.fname.setObjectName(u"fname")
        sizePolicy1.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.fname.setFont(font3)
        self.fname.setAutoFillBackground(True)
        self.fname.setFrameShape(QFrame.StyledPanel)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.gender = QLabel(self.groupBox)
        self.gender.setObjectName(u"gender")
        self.gender.setFont(font1)
        self.gender.setAutoFillBackground(True)
        self.gender.setFrameShape(QFrame.StyledPanel)

        self.horizontalLayout_5.addWidget(self.gender)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.age = QLabel(self.groupBox)
        self.age.setObjectName(u"age")
        self.age.setFont(font1)
        self.age.setAutoFillBackground(True)
        self.age.setFrameShape(QFrame.StyledPanel)

        self.horizontalLayout_5.addWidget(self.age)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_5)


        self.horizontalLayout.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.lname = QLabel(self.groupBox)
        self.lname.setObjectName(u"lname")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lname.sizePolicy().hasHeightForWidth())
        self.lname.setSizePolicy(sizePolicy2)
        self.lname.setMinimumSize(QSize(100, 0))
        self.lname.setFont(font3)
        self.lname.setAutoFillBackground(True)
        self.lname.setFrameShape(QFrame.StyledPanel)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lname)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pclass = QLabel(self.groupBox)
        self.pclass.setObjectName(u"pclass")
        self.pclass.setFont(font1)
        self.pclass.setAutoFillBackground(True)
        self.pclass.setFrameShape(QFrame.StyledPanel)

        self.horizontalLayout_4.addWidget(self.pclass)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.status = QLabel(self.groupBox)
        self.status.setObjectName(u"status")
        self.status.setFont(font1)
        self.status.setAutoFillBackground(True)
        self.status.setFrameShape(QFrame.StyledPanel)

        self.horizontalLayout_4.addWidget(self.status)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_4)


        self.horizontalLayout.addLayout(self.formLayout_2)


        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)

        self.table = QTableWidget(self.bgframe)
        if (self.table.columnCount() < 7):
            self.table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table.setObjectName(u"table")
        self.table.setFont(font1)
        self.table.setAlternatingRowColors(True)
        self.table.setColumnCount(7)
        self.table.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.table, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.addNewBtn = QPushButton(self.bgframe)
        self.addNewBtn.setObjectName(u"addNewBtn")
        font4 = QFont()
        font4.setFamily(u"Comic Sans MS")
        self.addNewBtn.setFont(font4)

        self.horizontalLayout_3.addWidget(self.addNewBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.closeBtn = QPushButton(self.bgframe)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setFont(font4)

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.bgframe, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 0, 0, 1, 1)


        self.retranslateUi(ClinicalRecord)

        QMetaObject.connectSlotsByName(ClinicalRecord)
    # setupUi

    def retranslateUi(self, ClinicalRecord):
        ClinicalRecord.setWindowTitle(QCoreApplication.translate("ClinicalRecord", u"Clinical Record", None))
        self.label_12.setText(QCoreApplication.translate("ClinicalRecord", u"Patient's ID:", None))
        self.patientID.setText(QCoreApplication.translate("ClinicalRecord", u"000000000", None))
        self.groupBox.setTitle(QCoreApplication.translate("ClinicalRecord", u"Patient's Details:", None))
        self.label_5.setText(QCoreApplication.translate("ClinicalRecord", u"First Name:", None))
        self.fname.setText("")
        self.label_9.setText(QCoreApplication.translate("ClinicalRecord", u"Gender:", None))
        self.gender.setText("")
        self.label_4.setText(QCoreApplication.translate("ClinicalRecord", u"Age:", None))
        self.age.setText("")
        self.label_2.setText(QCoreApplication.translate("ClinicalRecord", u"Last Name:", None))
        self.label_6.setText(QCoreApplication.translate("ClinicalRecord", u"Class:", None))
        self.lname.setText("")
        self.pclass.setText("")
        self.label_10.setText(QCoreApplication.translate("ClinicalRecord", u"Status:", None))
        self.status.setText("")
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ClinicalRecord", u"Date", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ClinicalRecord", u"Doctor", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ClinicalRecord", u"Diagnosis", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ClinicalRecord", u"Action", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ClinicalRecord", u"Test Result", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ClinicalRecord", u"Status", None));
        self.addNewBtn.setText(QCoreApplication.translate("ClinicalRecord", u"Add New Record", None))
        self.closeBtn.setText(QCoreApplication.translate("ClinicalRecord", u"Close", None))
    # retranslateUi

