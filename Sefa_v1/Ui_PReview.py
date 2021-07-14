# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PReview.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PReview(object):
    def setupUi(self, PReview):
        if not PReview.objectName():
            PReview.setObjectName(u"PReview")
        PReview.resize(636, 864)
        PReview.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(PReview)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bgLayer = QFrame(PReview)
        self.bgLayer.setObjectName(u"bgLayer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bgLayer.sizePolicy().hasHeightForWidth())
        self.bgLayer.setSizePolicy(sizePolicy)
        self.bgLayer.setAutoFillBackground(True)
        self.bgLayer.setFrameShape(QFrame.Box)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.bgLayer.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit = QLineEdit(self.bgLayer)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 5, 1, 1, 1)

        self.textEdit = QTextEdit(self.bgLayer)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.textEdit, 4, 0, 1, 4)

        self.label = QLabel(self.bgLayer)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.bgLayer)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 6, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(400, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 7, 1, 1, 2)

        self.label_3 = QLabel(self.bgLayer)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)

        self.cancel = QPushButton(self.bgLayer)
        self.cancel.setObjectName(u"cancel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cancel.sizePolicy().hasHeightForWidth())
        self.cancel.setSizePolicy(sizePolicy1)
        self.cancel.setMinimumSize(QSize(0, 45))

        self.gridLayout_2.addWidget(self.cancel, 7, 0, 1, 1)

        self.commit_2 = QPushButton(self.bgLayer)
        self.commit_2.setObjectName(u"commit_2")

        self.gridLayout_2.addWidget(self.commit_2, 6, 3, 1, 1)

        self.label_2 = QLabel(self.bgLayer)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.save = QPushButton(self.bgLayer)
        self.save.setObjectName(u"save")
        sizePolicy1.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy1)
        self.save.setMinimumSize(QSize(0, 45))

        self.gridLayout_2.addWidget(self.save, 7, 3, 1, 1)

        self.commit = QPushButton(self.bgLayer)
        self.commit.setObjectName(u"commit")

        self.gridLayout_2.addWidget(self.commit, 5, 3, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 1, 0, 1, 1)

        self.frame = QFrame(PReview)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setContentsMargins(3, 0, 8, 0)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 45))
        self.logo.setMaximumSize(QSize(45, 45))
        self.logo.setPixmap(QPixmap(u"Sefa logo2.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logo)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFrameShape(QFrame.NoFrame)
        self.label_29.setMidLineWidth(1)
        self.label_29.setWordWrap(True)
        self.label_29.setMargin(7)

        self.gridLayout_13.addWidget(self.label_29, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 1, -1)
        self.closeButton = QPushButton(self.frame)
        self.closeButton.setObjectName(u"closeButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy2)
        self.closeButton.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        self.closeButton.setFont(font)
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setMouseTracking(True)
        self.closeButton.setTabletTracking(True)
        self.closeButton.setLayoutDirection(Qt.LeftToRight)
        self.closeButton.setAutoFillBackground(True)
        self.closeButton.setAutoDefault(False)
        self.closeButton.setFlat(False)

        self.horizontalLayout_6.addWidget(self.closeButton)


        self.gridLayout_13.addLayout(self.horizontalLayout_6, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(334, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_13)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(PReview)

        QMetaObject.connectSlotsByName(PReview)
    # setupUi

    def retranslateUi(self, PReview):
        PReview.setWindowTitle(QCoreApplication.translate("PReview", u"Review", None))
        self.label.setText(QCoreApplication.translate("PReview", u"Diagnosis", None))
        self.label_3.setText(QCoreApplication.translate("PReview", u"Prescription", None))
        self.cancel.setText(QCoreApplication.translate("PReview", u"Cancel", None))
        self.commit_2.setText(QCoreApplication.translate("PReview", u"Commit", None))
        self.label_2.setText(QCoreApplication.translate("PReview", u"Review Note", None))
        self.save.setText(QCoreApplication.translate("PReview", u"Save", None))
        self.commit.setText(QCoreApplication.translate("PReview", u"Commit", None))
        self.logo.setText("")
        self.label_29.setText(QCoreApplication.translate("PReview", u"Doctor's Review", None))
        self.closeButton.setText(QCoreApplication.translate("PReview", u"X", None))
    # retranslateUi

