# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ApptSlip.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ApptSlip(object):
    def setupUi(self, ApptSlip):
        if not ApptSlip.objectName():
            ApptSlip.setObjectName(u"ApptSlip")
        ApptSlip.resize(341, 181)
        self.gridLayout = QGridLayout(ApptSlip)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgLayer = QFrame(ApptSlip)
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
        self.verticalLayout = QVBoxLayout(self.bgframe)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.bgframe)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.patientID = QLabel(self.bgframe)
        self.patientID.setObjectName(u"patientID")

        self.horizontalLayout_4.addWidget(self.patientID)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.bgframe)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.dateEdit = QDateEdit(self.bgframe)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateEdit)

        self.label = QLabel(self.bgframe)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.timeEdit = QTimeEdit(self.bgframe)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.timeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.bgframe)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.doclist = QComboBox(self.bgframe)
        self.doclist.setObjectName(u"doclist")

        self.horizontalLayout_2.addWidget(self.doclist)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.bgframe)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.status = QComboBox(self.bgframe)
        self.status.addItem("")
        self.status.addItem("")
        self.status.setObjectName(u"status")

        self.horizontalLayout_5.addWidget(self.status)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bookBtn = QPushButton(self.bgframe)
        self.bookBtn.setObjectName(u"bookBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bookBtn.sizePolicy().hasHeightForWidth())
        self.bookBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.bookBtn)

        self.cancelBtn = QPushButton(self.bgframe)
        self.cancelBtn.setObjectName(u"cancelBtn")
        sizePolicy2.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.cancelBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addWidget(self.bgframe, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 0, 0, 1, 1)


        self.retranslateUi(ApptSlip)

        QMetaObject.connectSlotsByName(ApptSlip)
    # setupUi

    def retranslateUi(self, ApptSlip):
        ApptSlip.setWindowTitle(QCoreApplication.translate("ApptSlip", u"Appointment Slip", None))
        self.label_5.setText(QCoreApplication.translate("ApptSlip", u"Patient's ID:", None))
        self.patientID.setText(QCoreApplication.translate("ApptSlip", u"000000000", None))
        self.label_2.setText(QCoreApplication.translate("ApptSlip", u"Date:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("ApptSlip", u"d/MMM/yyyy", None))
        self.label.setText(QCoreApplication.translate("ApptSlip", u"Time:", None))
        self.label_3.setText(QCoreApplication.translate("ApptSlip", u"Available Doctor:", None))
        self.label_4.setText(QCoreApplication.translate("ApptSlip", u"Status:", None))
        self.status.setItemText(0, QCoreApplication.translate("ApptSlip", u"In-Patient", None))
        self.status.setItemText(1, QCoreApplication.translate("ApptSlip", u"Out-Patient", None))

        self.bookBtn.setText(QCoreApplication.translate("ApptSlip", u"Book", None))
        self.cancelBtn.setText(QCoreApplication.translate("ApptSlip", u"Cancel", None))
    # retranslateUi

