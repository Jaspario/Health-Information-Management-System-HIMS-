# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Patient.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Patient(object):
    def setupUi(self, Patient):
        if not Patient.objectName():
            Patient.setObjectName(u"Patient")
        Patient.resize(715, 379)
        self.gridLayout = QGridLayout(Patient)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgLayer = QFrame(Patient)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setMouseTracking(True)
        self.bgLayer.setTabletTracking(True)
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
        self.groupBox = QGroupBox(self.bgframe)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.patientID = QLabel(self.groupBox)
        self.patientID.setObjectName(u"patientID")
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.patientID.setFont(font1)

        self.horizontalLayout.addWidget(self.patientID)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.fullname = QLabel(self.groupBox)
        self.fullname.setObjectName(u"fullname")
        self.fullname.setFont(font1)

        self.horizontalLayout_4.addWidget(self.fullname)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.profileBtn = QPushButton(self.frame)
        self.profileBtn.setObjectName(u"profileBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.profileBtn.sizePolicy().hasHeightForWidth())
        self.profileBtn.setSizePolicy(sizePolicy3)
        self.profileBtn.setFont(font1)
        self.profileBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.profileBtn.setMouseTracking(True)
        self.profileBtn.setTabletTracking(True)

        self.horizontalLayout_2.addWidget(self.profileBtn)

        self.clinicalBtn = QPushButton(self.frame)
        self.clinicalBtn.setObjectName(u"clinicalBtn")
        sizePolicy3.setHeightForWidth(self.clinicalBtn.sizePolicy().hasHeightForWidth())
        self.clinicalBtn.setSizePolicy(sizePolicy3)
        self.clinicalBtn.setFont(font1)
        self.clinicalBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.clinicalBtn.setMouseTracking(True)
        self.clinicalBtn.setTabletTracking(True)

        self.horizontalLayout_2.addWidget(self.clinicalBtn)

        self.labBtn = QPushButton(self.frame)
        self.labBtn.setObjectName(u"labBtn")
        sizePolicy3.setHeightForWidth(self.labBtn.sizePolicy().hasHeightForWidth())
        self.labBtn.setSizePolicy(sizePolicy3)
        self.labBtn.setFont(font1)
        self.labBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.labBtn.setMouseTracking(True)
        self.labBtn.setTabletTracking(True)

        self.horizontalLayout_2.addWidget(self.labBtn)

        self.pharmacyBtn = QPushButton(self.frame)
        self.pharmacyBtn.setObjectName(u"pharmacyBtn")
        sizePolicy3.setHeightForWidth(self.pharmacyBtn.sizePolicy().hasHeightForWidth())
        self.pharmacyBtn.setSizePolicy(sizePolicy3)
        self.pharmacyBtn.setFont(font1)
        self.pharmacyBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pharmacyBtn.setMouseTracking(True)
        self.pharmacyBtn.setTabletTracking(True)

        self.horizontalLayout_2.addWidget(self.pharmacyBtn)

        self.accountBtn = QPushButton(self.frame)
        self.accountBtn.setObjectName(u"accountBtn")
        sizePolicy3.setHeightForWidth(self.accountBtn.sizePolicy().hasHeightForWidth())
        self.accountBtn.setSizePolicy(sizePolicy3)
        self.accountBtn.setFont(font1)
        self.accountBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.accountBtn.setMouseTracking(True)
        self.accountBtn.setTabletTracking(True)

        self.horizontalLayout_2.addWidget(self.accountBtn)


        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bookBtn = QPushButton(self.groupBox)
        self.bookBtn.setObjectName(u"bookBtn")
        self.bookBtn.setFont(font1)
        self.bookBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bookBtn.setMouseTracking(True)
        self.bookBtn.setTabletTracking(True)

        self.horizontalLayout_3.addWidget(self.bookBtn)

        self.closeBtn = QPushButton(self.groupBox)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setFont(font1)
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeBtn.setMouseTracking(True)
        self.closeBtn.setTabletTracking(True)

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout_3.addWidget(self.groupBox, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.bgframe, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 0, 0, 1, 1)


        self.retranslateUi(Patient)

        QMetaObject.connectSlotsByName(Patient)
    # setupUi

    def retranslateUi(self, Patient):
        Patient.setWindowTitle(QCoreApplication.translate("Patient", u"Patient", None))
        self.groupBox.setTitle(QCoreApplication.translate("Patient", u"Patient's Record", None))
        self.label_2.setText(QCoreApplication.translate("Patient", u"Patient's ID:", None))
        self.patientID.setText(QCoreApplication.translate("Patient", u"00000000", None))
        self.label_3.setText(QCoreApplication.translate("Patient", u"Name:", None))
        self.fullname.setText("")
        self.profileBtn.setText(QCoreApplication.translate("Patient", u"Profile", None))
        self.clinicalBtn.setText(QCoreApplication.translate("Patient", u"Clinical", None))
        self.labBtn.setText(QCoreApplication.translate("Patient", u"Lab", None))
        self.pharmacyBtn.setText(QCoreApplication.translate("Patient", u"Pharmacy", None))
        self.accountBtn.setText(QCoreApplication.translate("Patient", u"Account", None))
        self.bookBtn.setText(QCoreApplication.translate("Patient", u"Book Appointment", None))
        self.closeBtn.setText(QCoreApplication.translate("Patient", u"Close Record", None))
    # retranslateUi

