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


class Ui_Review(object):
    def setupUi(self, Review):
        if not Review.objectName():
            Review.setObjectName(u"Review")
        Review.setWindowModality(Qt.ApplicationModal)
        Review.resize(472, 687)
        Review.setMouseTracking(True)
        Review.setTabletTracking(True)
        Review.setFocusPolicy(Qt.StrongFocus)
        Review.setAutoFillBackground(True)
        Review.setModal(True)
        self.gridLayout = QGridLayout(Review)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bgLayer = QFrame(Review)
        self.bgLayer.setObjectName(u"bgLayer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bgLayer.sizePolicy().hasHeightForWidth())
        self.bgLayer.setSizePolicy(sizePolicy)
        self.bgLayer.setAutoFillBackground(True)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setLineWidth(2)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.bgLayer)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 7, 0, 1, 1)

        self.label_3 = QLabel(self.bgLayer)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 8, 0, 1, 1)

        self.reviewNote = QTextEdit(self.bgLayer)
        self.reviewNote.setObjectName(u"reviewNote")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.reviewNote.sizePolicy().hasHeightForWidth())
        self.reviewNote.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(9)
        self.reviewNote.setFont(font)

        self.gridLayout_2.addWidget(self.reviewNote, 4, 0, 1, 4)

        self.diagnosisDisplay = QTextBrowser(self.bgLayer)
        self.diagnosisDisplay.setObjectName(u"diagnosisDisplay")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.diagnosisDisplay.sizePolicy().hasHeightForWidth())
        self.diagnosisDisplay.setSizePolicy(sizePolicy2)
        self.diagnosisDisplay.setFont(font)

        self.gridLayout_2.addWidget(self.diagnosisDisplay, 5, 0, 1, 4)

        self.labBtn = QPushButton(self.bgLayer)
        self.labBtn.setObjectName(u"labBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labBtn.sizePolicy().hasHeightForWidth())
        self.labBtn.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.labBtn, 7, 3, 1, 1)

        self.cancelBtn = QPushButton(self.bgLayer)
        self.cancelBtn.setObjectName(u"cancelBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy4)
        self.cancelBtn.setMinimumSize(QSize(0, 35))

        self.gridLayout_2.addWidget(self.cancelBtn, 9, 0, 1, 1)

        self.label_2 = QLabel(self.bgLayer)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.diagnosis = QLineEdit(self.bgLayer)
        self.diagnosis.setObjectName(u"diagnosis")
        self.diagnosis.setTabletTracking(True)

        self.gridLayout_2.addWidget(self.diagnosis, 7, 1, 1, 1)

        self.prescriptionDisplay = QTextBrowser(self.bgLayer)
        self.prescriptionDisplay.setObjectName(u"prescriptionDisplay")
        sizePolicy2.setHeightForWidth(self.prescriptionDisplay.sizePolicy().hasHeightForWidth())
        self.prescriptionDisplay.setSizePolicy(sizePolicy2)
        self.prescriptionDisplay.setFont(font)
        self.prescriptionDisplay.setLineWidth(2)

        self.gridLayout_2.addWidget(self.prescriptionDisplay, 6, 0, 1, 4)

        self.saveBtn = QPushButton(self.bgLayer)
        self.saveBtn.setObjectName(u"saveBtn")
        sizePolicy4.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy4)
        self.saveBtn.setMinimumSize(QSize(0, 35))

        self.gridLayout_2.addWidget(self.saveBtn, 9, 3, 1, 1)

        self.prescription = QLineEdit(self.bgLayer)
        self.prescription.setObjectName(u"prescription")

        self.gridLayout_2.addWidget(self.prescription, 8, 1, 1, 1)

        self.pharmBtn = QPushButton(self.bgLayer)
        self.pharmBtn.setObjectName(u"pharmBtn")

        self.gridLayout_2.addWidget(self.pharmBtn, 8, 3, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 2, 0, 1, 1)

        self.frame = QFrame(Review)
        self.frame.setObjectName(u"frame")
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setContentsMargins(3, 0, 8, 0)
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 45))
        self.logo.setMaximumSize(QSize(45, 45))
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.gridLayout_13.addWidget(self.logo, 0, 0, 1, 1)

        self.exitBtn = QPushButton(self.frame)
        self.exitBtn.setObjectName(u"exitBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy5)
        self.exitBtn.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(12)
        self.exitBtn.setFont(font1)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setMouseTracking(True)
        self.exitBtn.setTabletTracking(True)
        self.exitBtn.setLayoutDirection(Qt.LeftToRight)
        self.exitBtn.setAutoFillBackground(True)
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setFlat(False)

        self.gridLayout_13.addWidget(self.exitBtn, 0, 2, 1, 1)

        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFrameShape(QFrame.NoFrame)
        self.label_29.setMidLineWidth(1)
        self.label_29.setWordWrap(True)
        self.label_29.setMargin(7)

        self.gridLayout_13.addWidget(self.label_29, 0, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_13)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(Review)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setMargin(7)

        self.horizontalLayout.addWidget(self.label_4)

        self.doctor = QLabel(Review)
        self.doctor.setObjectName(u"doctor")
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(8)
        self.doctor.setFont(font3)
        self.doctor.setMargin(7)

        self.horizontalLayout.addWidget(self.doctor)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(Review)

        QMetaObject.connectSlotsByName(Review)
    # setupUi

    def retranslateUi(self, Review):
        Review.setWindowTitle(QCoreApplication.translate("Review", u"Patient's Review", None))
        self.label.setText(QCoreApplication.translate("Review", u"Diagnosis", None))
        self.label_3.setText(QCoreApplication.translate("Review", u"Prescription", None))
        self.reviewNote.setHtml(QCoreApplication.translate("Review", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Tahoma','Tahoma'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Tahoma'; font-size:7pt;\"><br /></p></body></html>", None))
        self.reviewNote.setPlaceholderText(QCoreApplication.translate("Review", u"Hello Doctor! You can let us know what your reveiws are on this patient by typing them here...", None))
        self.diagnosisDisplay.setPlaceholderText(QCoreApplication.translate("Review", u"Your diagnosis would appear hear.", None))
        self.labBtn.setText(QCoreApplication.translate("Review", u"Lab Request", None))
        self.cancelBtn.setText(QCoreApplication.translate("Review", u"Cancel", None))
        self.label_2.setText(QCoreApplication.translate("Review", u"Review Note", None))
        self.diagnosis.setPlaceholderText(QCoreApplication.translate("Review", u"Please input your diagnosis here", None))
        self.prescriptionDisplay.setHtml(QCoreApplication.translate("Review", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Tahoma','Tahoma'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Tahoma'; font-size:7pt;\"><br /></p></body></html>", None))
        self.prescriptionDisplay.setPlaceholderText(QCoreApplication.translate("Review", u"Your prescriptions would appear here", None))
        self.saveBtn.setText(QCoreApplication.translate("Review", u"Sign", None))
        self.prescription.setPlaceholderText(QCoreApplication.translate("Review", u"What are your prescriptions? Please input them here", None))
        self.pharmBtn.setText(QCoreApplication.translate("Review", u"Pharmacy", None))
        self.logo.setText("")
        self.exitBtn.setText(QCoreApplication.translate("Review", u"X", None))
        self.label_29.setText(QCoreApplication.translate("Review", u"Patient's Review", None))
        self.label_4.setText(QCoreApplication.translate("Review", u"Reviewed By: ", None))
        self.doctor.setText(QCoreApplication.translate("Review", u"Dr. Ahmadu Bello", None))
    # retranslateUi

