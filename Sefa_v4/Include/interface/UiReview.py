# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Review.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ReviewNote(object):
    def setupUi(self, ReviewNote):
        if not ReviewNote.objectName():
            ReviewNote.setObjectName(u"ReviewNote")
        ReviewNote.resize(400, 579)
        self.gridLayout = QGridLayout(ReviewNote)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgLayer = QFrame(ReviewNote)
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
        self.verticalLayout_3 = QVBoxLayout(self.bgframe)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.bgframe)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)

        self.horizontalLayout.addWidget(self.label_5)

        self.date = QLabel(self.bgframe)
        self.date.setObjectName(u"date")
        self.date.setAutoFillBackground(True)

        self.horizontalLayout.addWidget(self.date)

        self.label_2 = QLabel(self.bgframe)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.patientID = QLabel(self.bgframe)
        self.patientID.setObjectName(u"patientID")
        font1 = QFont()
        font1.setPointSize(10)
        self.patientID.setFont(font1)
        self.patientID.setAutoFillBackground(True)

        self.horizontalLayout.addWidget(self.patientID)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.bgframe)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.doctor = QLabel(self.bgframe)
        self.doctor.setObjectName(u"doctor")
        self.doctor.setFont(font1)
        self.doctor.setAutoFillBackground(True)
        self.doctor.setFrameShape(QFrame.StyledPanel)

        self.horizontalLayout_2.addWidget(self.doctor)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.bgframe)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.textEdit_2 = QTextEdit(self.bgframe)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.verticalLayout.addWidget(self.textEdit_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.bgframe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.textEdit = QTextEdit(self.bgframe)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labBtn = QPushButton(self.bgframe)
        self.labBtn.setObjectName(u"labBtn")
        font2 = QFont()
        font2.setFamily(u"Comic Sans MS")
        self.labBtn.setFont(font2)

        self.horizontalLayout_3.addWidget(self.labBtn)

        self.pharmBtn = QPushButton(self.bgframe)
        self.pharmBtn.setObjectName(u"pharmBtn")
        self.pharmBtn.setFont(font2)

        self.horizontalLayout_3.addWidget(self.pharmBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.saveBtn = QPushButton(self.bgframe)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setFont(font2)

        self.horizontalLayout_3.addWidget(self.saveBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addWidget(self.bgframe, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 0, 0, 1, 1)


        self.retranslateUi(ReviewNote)

        QMetaObject.connectSlotsByName(ReviewNote)
    # setupUi

    def retranslateUi(self, ReviewNote):
        ReviewNote.setWindowTitle(QCoreApplication.translate("ReviewNote", u"Review Note", None))
        self.label_5.setText(QCoreApplication.translate("ReviewNote", u"Date:", None))
        self.date.setText(QCoreApplication.translate("ReviewNote", u"__________", None))
        self.label_2.setText(QCoreApplication.translate("ReviewNote", u"Patient's ID:", None))
        self.patientID.setText(QCoreApplication.translate("ReviewNote", u"0000000", None))
        self.label_6.setText(QCoreApplication.translate("ReviewNote", u"Reviewed By:", None))
        self.doctor.setText("")
        self.label_4.setText(QCoreApplication.translate("ReviewNote", u"Review Note:", None))
        self.label_3.setText(QCoreApplication.translate("ReviewNote", u"Diagnosis:", None))
        self.labBtn.setText(QCoreApplication.translate("ReviewNote", u"Lab Request", None))
        self.pharmBtn.setText(QCoreApplication.translate("ReviewNote", u"Pharmacy", None))
        self.saveBtn.setText(QCoreApplication.translate("ReviewNote", u"Save", None))
    # retranslateUi

