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
        Review.resize(335, 567)
        self.verticalLayout_3 = QVBoxLayout(Review)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bgflayer = QFrame(Review)
        self.bgflayer.setObjectName(u"bgflayer")
        self.bgflayer.setAutoFillBackground(True)
        self.bgflayer.setFrameShape(QFrame.StyledPanel)
        self.bgflayer.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.bgflayer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(9)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(13, 13, 13, 13)
        self.bgfFrame = QFrame(self.bgflayer)
        self.bgfFrame.setObjectName(u"bgfFrame")
        self.bgfFrame.setAutoFillBackground(True)
        self.bgfFrame.setFrameShape(QFrame.Box)
        self.bgfFrame.setFrameShadow(QFrame.Raised)
        self.bgfFrame.setLineWidth(2)
        self.bgfFrame.setMidLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.bgfFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.bgfFrame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setMargin(0)

        self.horizontalLayout.addWidget(self.label_4)

        self.doctor = QLabel(self.bgfFrame)
        self.doctor.setObjectName(u"doctor")
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(8)
        self.doctor.setFont(font1)
        self.doctor.setMargin(7)

        self.horizontalLayout.addWidget(self.doctor)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.bgfFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))

        self.verticalLayout_2.addWidget(self.label_2)

        self.reviewNote = QTextEdit(self.bgfFrame)
        self.reviewNote.setObjectName(u"reviewNote")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.reviewNote.sizePolicy().hasHeightForWidth())
        self.reviewNote.setSizePolicy(sizePolicy1)
        self.reviewNote.setFont(font1)
        self.reviewNote.setAutoFormatting(QTextEdit.AutoAll)
        self.reviewNote.setLineWrapColumnOrWidth(0)

        self.verticalLayout_2.addWidget(self.reviewNote)

        self.label = QLabel(self.bgfFrame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(0, 20))

        self.verticalLayout_2.addWidget(self.label)

        self.dlist = QTextEdit(self.bgfFrame)
        self.dlist.setObjectName(u"dlist")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.dlist.sizePolicy().hasHeightForWidth())
        self.dlist.setSizePolicy(sizePolicy3)
        self.dlist.setMinimumSize(QSize(0, 70))

        self.verticalLayout_2.addWidget(self.dlist)

        self.label_3 = QLabel(self.bgfFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 20))

        self.verticalLayout_2.addWidget(self.label_3)

        self.plist = QTextBrowser(self.bgfFrame)
        self.plist.setObjectName(u"plist")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.plist.sizePolicy().hasHeightForWidth())
        self.plist.setSizePolicy(sizePolicy4)

        self.verticalLayout_2.addWidget(self.plist)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labBtn = QPushButton(self.bgfFrame)
        self.labBtn.setObjectName(u"labBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.labBtn.sizePolicy().hasHeightForWidth())
        self.labBtn.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.labBtn)

        self.pharmBtn = QPushButton(self.bgfFrame)
        self.pharmBtn.setObjectName(u"pharmBtn")
        sizePolicy5.setHeightForWidth(self.pharmBtn.sizePolicy().hasHeightForWidth())
        self.pharmBtn.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.pharmBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.saveBtn = QPushButton(self.bgfFrame)
        self.saveBtn.setObjectName(u"saveBtn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy6)
        self.saveBtn.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_3.addWidget(self.saveBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout_3.addWidget(self.bgfFrame, 1, 0, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.logo = QLabel(self.bgflayer)
        self.logo.setObjectName(u"logo")
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.gridLayout_13.addWidget(self.logo, 0, 0, 1, 1)

        self.exitBtn = QPushButton(self.bgflayer)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMaximumSize(QSize(16777215, 16777215))
        self.exitBtn.setFont(font1)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setMouseTracking(True)
        self.exitBtn.setTabletTracking(True)
        self.exitBtn.setLayoutDirection(Qt.LeftToRight)
        self.exitBtn.setAutoFillBackground(True)
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setFlat(False)

        self.gridLayout_13.addWidget(self.exitBtn, 0, 2, 1, 1)

        self.bgflbl = QLabel(self.bgflayer)
        self.bgflbl.setObjectName(u"bgflbl")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.bgflbl.sizePolicy().hasHeightForWidth())
        self.bgflbl.setSizePolicy(sizePolicy7)
        self.bgflbl.setFont(font1)
        self.bgflbl.setFrameShape(QFrame.NoFrame)
        self.bgflbl.setMidLineWidth(1)
        self.bgflbl.setWordWrap(True)
        self.bgflbl.setMargin(7)

        self.gridLayout_13.addWidget(self.bgflbl, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_13, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.bgflayer)


        self.retranslateUi(Review)

        QMetaObject.connectSlotsByName(Review)
    # setupUi

    def retranslateUi(self, Review):
        Review.setWindowTitle(QCoreApplication.translate("Review", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Review", u"Reviewed By: ", None))
        self.doctor.setText(QCoreApplication.translate("Review", u"Dr. Ahmadu Bello", None))
        self.label_2.setText(QCoreApplication.translate("Review", u"Review Note", None))
#if QT_CONFIG(tooltip)
        self.reviewNote.setToolTip(QCoreApplication.translate("Review", u"<html><head/><body><p>Please insert your review here</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.reviewNote.setDocumentTitle("")
        self.reviewNote.setHtml(QCoreApplication.translate("Review", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Tahoma','Tahoma'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Tahoma'; font-size:7pt;\"><br /></p></body></html>", None))
        self.reviewNote.setPlaceholderText(QCoreApplication.translate("Review", u"Hello Doctor! You can let us know what your reveiws are on this patient by typing them here...", None))
        self.label.setText(QCoreApplication.translate("Review", u"Diagnosis", None))
#if QT_CONFIG(tooltip)
        self.dlist.setToolTip(QCoreApplication.translate("Review", u"<html><head/><body><p>Input your diagnosis here</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Review", u"Prescriptions", None))
#if QT_CONFIG(tooltip)
        self.plist.setToolTip(QCoreApplication.translate("Review", u"<html><head/><body><p>Your prescriptions would appear here</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labBtn.setToolTip(QCoreApplication.translate("Review", u"<html><head/><body><p>Click to create lab request</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labBtn.setText(QCoreApplication.translate("Review", u"Lab Request", None))
#if QT_CONFIG(tooltip)
        self.pharmBtn.setToolTip(QCoreApplication.translate("Review", u"<html><head/><body><p>Click to make prescriptions</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pharmBtn.setText(QCoreApplication.translate("Review", u"Pharmacy", None))
#if QT_CONFIG(tooltip)
        self.saveBtn.setToolTip(QCoreApplication.translate("Review", u"<html><head/><body><p>Click to sign and commit reveiw</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.saveBtn.setText(QCoreApplication.translate("Review", u"Sign", None))
        self.logo.setText("")
#if QT_CONFIG(tooltip)
        self.exitBtn.setToolTip(QCoreApplication.translate("Review", u"<html><head/><body><p>Click to exit app</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.exitBtn.setText(QCoreApplication.translate("Review", u"X", None))
        self.bgflbl.setText(QCoreApplication.translate("Review", u"Patient's Review", None))
    # retranslateUi

