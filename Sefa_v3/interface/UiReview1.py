# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Review1.ui'
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
        Review.resize(469, 593)
        Review.setMouseTracking(True)
        Review.setTabletTracking(True)
        Review.setFocusPolicy(Qt.StrongFocus)
        Review.setAutoFillBackground(True)
        Review.setModal(True)
        self.gridLayout = QGridLayout(Review)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgflayer = QFrame(Review)
        self.bgflayer.setObjectName(u"bgflayer")
        self.bgflayer.setFrameShape(QFrame.StyledPanel)
        self.bgflayer.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.bgflayer)
        self.gridLayout_3.setSpacing(9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(13, 13, 13, 13)
        self.bgframe = QFrame(self.bgflayer)
        self.bgframe.setObjectName(u"bgframe")
        self.bgframe.setAutoFillBackground(True)
        self.bgframe.setFrameShape(QFrame.Box)
        self.bgframe.setFrameShadow(QFrame.Raised)
        self.bgframe.setLineWidth(2)
        self.bgframe.setMidLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.bgframe)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.bgframe)
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

        self.doctor = QLabel(self.bgframe)
        self.doctor.setObjectName(u"doctor")
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(8)
        self.doctor.setFont(font1)
        self.doctor.setMargin(7)

        self.horizontalLayout.addWidget(self.doctor)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.bgframe)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.reviewNote = QTextEdit(self.bgframe)
        self.reviewNote.setObjectName(u"reviewNote")
        self.reviewNote.setFont(font1)
        self.reviewNote.setAutoFormatting(QTextEdit.AutoAll)
        self.reviewNote.setLineWrapColumnOrWidth(0)

        self.verticalLayout_2.addWidget(self.reviewNote)

        self.label = QLabel(self.bgframe)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.dlist = QListWidget(self.bgframe)
        self.dlist.setObjectName(u"dlist")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dlist.sizePolicy().hasHeightForWidth())
        self.dlist.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.dlist)

        self.label_3 = QLabel(self.bgframe)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.plist = QListWidget(self.bgframe)
        self.plist.setObjectName(u"plist")

        self.verticalLayout_2.addWidget(self.plist)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.bgframe)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.lineEdit_2 = QLineEdit(self.bgframe)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.labBtn = QPushButton(self.bgframe)
        self.labBtn.setObjectName(u"labBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labBtn.sizePolicy().hasHeightForWidth())
        self.labBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.labBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.bgframe)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.lineEdit = QLineEdit(self.bgframe)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.pharmBtn = QPushButton(self.bgframe)
        self.pharmBtn.setObjectName(u"pharmBtn")
        sizePolicy2.setHeightForWidth(self.pharmBtn.sizePolicy().hasHeightForWidth())
        self.pharmBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.pharmBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cancelBtn = QPushButton(self.bgframe)
        self.cancelBtn.setObjectName(u"cancelBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy3)
        self.cancelBtn.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_3.addWidget(self.cancelBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.saveBtn = QPushButton(self.bgframe)
        self.saveBtn.setObjectName(u"saveBtn")
        sizePolicy3.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy3)
        self.saveBtn.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_3.addWidget(self.saveBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout_3.addWidget(self.bgframe, 1, 0, 1, 1)

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
        sizePolicy1.setHeightForWidth(self.bgflbl.sizePolicy().hasHeightForWidth())
        self.bgflbl.setSizePolicy(sizePolicy1)
        self.bgflbl.setFrameShape(QFrame.NoFrame)
        self.bgflbl.setMidLineWidth(1)
        self.bgflbl.setWordWrap(True)
        self.bgflbl.setMargin(7)

        self.gridLayout_13.addWidget(self.bgflbl, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_13, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.bgflayer, 1, 0, 1, 1)


        self.retranslateUi(Review)

        QMetaObject.connectSlotsByName(Review)
    # setupUi

    def retranslateUi(self, Review):
        Review.setWindowTitle(QCoreApplication.translate("Review", u"Patient's Review", None))
        self.label_4.setText(QCoreApplication.translate("Review", u"Reviewed By: ", None))
        self.doctor.setText(QCoreApplication.translate("Review", u"Dr. Ahmadu Bello", None))
        self.label_2.setText(QCoreApplication.translate("Review", u"Review Note", None))
        self.reviewNote.setDocumentTitle("")
        self.reviewNote.setHtml(QCoreApplication.translate("Review", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Tahoma','Tahoma'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Tahoma'; font-size:7pt;\"><br /></p></body></html>", None))
        self.reviewNote.setPlaceholderText(QCoreApplication.translate("Review", u"Hello Doctor! You can let us know what your reveiws are on this patient by typing them here...", None))
        self.label.setText(QCoreApplication.translate("Review", u"Diagnosis", None))
#if QT_CONFIG(tooltip)
        self.dlist.setToolTip(QCoreApplication.translate("Review", u"<html><head/><body><p>Displays Diagnosis entered</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Review", u"Prescriptions", None))
#if QT_CONFIG(tooltip)
        self.plist.setToolTip(QCoreApplication.translate("Review", u"<html><head/><body><p>Displays prescriptions entered</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Review", u"Diagnosis:   ", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Review", u"Input your diagnosis here; Press return key after each entry", None))
#if QT_CONFIG(tooltip)
        self.labBtn.setToolTip(QCoreApplication.translate("Review", u"<html><head/><body><p>Create and send Lab requests</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labBtn.setText(QCoreApplication.translate("Review", u"Lab Request", None))
        self.label_6.setText(QCoreApplication.translate("Review", u"Prescription:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Review", u"Make prescriptions here; Press the return key after each entry", None))
#if QT_CONFIG(tooltip)
        self.pharmBtn.setToolTip(QCoreApplication.translate("Review", u"<html><head/><body><p>Create and send request to pharmacy</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pharmBtn.setText(QCoreApplication.translate("Review", u"Pharmacy", None))
        self.cancelBtn.setText(QCoreApplication.translate("Review", u"Cancel", None))
        self.saveBtn.setText(QCoreApplication.translate("Review", u"Sign", None))
        self.logo.setText("")
        self.exitBtn.setText(QCoreApplication.translate("Review", u"X", None))
        self.bgflbl.setText(QCoreApplication.translate("Review", u"Patient's Review", None))
    # retranslateUi

