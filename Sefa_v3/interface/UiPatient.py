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
        Patient.resize(734, 505)
        Patient.setMouseTracking(True)
        Patient.setTabletTracking(True)
        Patient.setFocusPolicy(Qt.StrongFocus)
        self.centralwidget = QWidget(Patient)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 2, 0)

        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.bgLayer = QFrame(self.centralwidget)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setFrameShape(QFrame.StyledPanel)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.bgLayer)
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(13, 5, 13, -1)
        self.logo = QLabel(self.bgLayer)
        self.logo.setObjectName(u"logo")

        self.horizontalLayout_7.addWidget(self.logo)

        self.label_4 = QLabel(self.bgLayer)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMargin(5)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.miniBtn = QPushButton(self.bgLayer)
        self.miniBtn.setObjectName(u"miniBtn")

        self.horizontalLayout_7.addWidget(self.miniBtn)

        self.exitBtn = QPushButton(self.bgLayer)
        self.exitBtn.setObjectName(u"exitBtn")

        self.horizontalLayout_7.addWidget(self.exitBtn)


        self.gridLayout_5.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.bgLayer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(13, -1, -1, -1)
        self.bgframe = QFrame(self.frame_2)
        self.bgframe.setObjectName(u"bgframe")
        self.bgframe.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bgframe.sizePolicy().hasHeightForWidth())
        self.bgframe.setSizePolicy(sizePolicy1)
        self.bgframe.setMouseTracking(True)
        self.bgframe.setTabletTracking(True)
        self.bgframe.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.bgframe.setAutoFillBackground(True)
        self.bgframe.setFrameShape(QFrame.Box)
        self.bgframe.setFrameShadow(QFrame.Raised)
        self.bgframe.setLineWidth(2)
        self.bgframe.setMidLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.bgframe)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.bgframe)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.profileBtn = QPushButton(self.groupBox)
        self.profileBtn.setObjectName(u"profileBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.profileBtn.sizePolicy().hasHeightForWidth())
        self.profileBtn.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamily(u"MS UI Gothic")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        font1.setKerning(False)
        self.profileBtn.setFont(font1)
        self.profileBtn.setMouseTracking(True)
        self.profileBtn.setTabletTracking(True)
        self.profileBtn.setAutoFillBackground(True)

        self.horizontalLayout_5.addWidget(self.profileBtn)

        self.clinicBtn = QPushButton(self.groupBox)
        self.clinicBtn.setObjectName(u"clinicBtn")
        sizePolicy2.setHeightForWidth(self.clinicBtn.sizePolicy().hasHeightForWidth())
        self.clinicBtn.setSizePolicy(sizePolicy2)
        self.clinicBtn.setFont(font1)

        self.horizontalLayout_5.addWidget(self.clinicBtn)

        self.pharmacyBtn = QPushButton(self.groupBox)
        self.pharmacyBtn.setObjectName(u"pharmacyBtn")
        sizePolicy2.setHeightForWidth(self.pharmacyBtn.sizePolicy().hasHeightForWidth())
        self.pharmacyBtn.setSizePolicy(sizePolicy2)
        self.pharmacyBtn.setFont(font1)

        self.horizontalLayout_5.addWidget(self.pharmacyBtn)

        self.labBtn = QPushButton(self.groupBox)
        self.labBtn.setObjectName(u"labBtn")
        sizePolicy2.setHeightForWidth(self.labBtn.sizePolicy().hasHeightForWidth())
        self.labBtn.setSizePolicy(sizePolicy2)
        self.labBtn.setFont(font1)

        self.horizontalLayout_5.addWidget(self.labBtn)

        self.accountBtn = QPushButton(self.groupBox)
        self.accountBtn.setObjectName(u"accountBtn")
        sizePolicy2.setHeightForWidth(self.accountBtn.sizePolicy().hasHeightForWidth())
        self.accountBtn.setSizePolicy(sizePolicy2)
        self.accountBtn.setFont(font1)

        self.horizontalLayout_5.addWidget(self.accountBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 4, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.bgframe)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.fullname = QLabel(self.bgframe)
        self.fullname.setObjectName(u"fullname")
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(8)
        self.fullname.setFont(font3)

        self.horizontalLayout_6.addWidget(self.fullname)


        self.gridLayout_3.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bookBtn = QPushButton(self.bgframe)
        self.bookBtn.setObjectName(u"bookBtn")
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(10)
        font4.setKerning(False)
        self.bookBtn.setFont(font4)

        self.horizontalLayout_2.addWidget(self.bookBtn)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.closeBtn = QPushButton(self.bgframe)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setFont(font4)

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout_3.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.label = QLabel(self.bgframe)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setFamily(u"Tahoma")
        font5.setPointSize(12)
        font5.setUnderline(True)
        font5.setKerning(False)
        self.label.setFont(font5)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(2)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 13, -1)
        self.label_2 = QLabel(self.bgframe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_2)

        self.cardNum = QLabel(self.bgframe)
        self.cardNum.setObjectName(u"cardNum")
        sizePolicy3.setHeightForWidth(self.cardNum.sizePolicy().hasHeightForWidth())
        self.cardNum.setSizePolicy(sizePolicy3)
        self.cardNum.setFont(font3)

        self.horizontalLayout_8.addWidget(self.cardNum)


        self.gridLayout_3.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.bgframe, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 1, 0, 1, 2)

        Patient.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Patient)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 734, 16))
        Patient.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Patient)
        self.statusbar.setObjectName(u"statusbar")
        Patient.setStatusBar(self.statusbar)

        self.retranslateUi(Patient)

        QMetaObject.connectSlotsByName(Patient)
    # setupUi

    def retranslateUi(self, Patient):
        Patient.setWindowTitle(QCoreApplication.translate("Patient", u"Patient Portal", None))
        self.logo.setText(QCoreApplication.translate("Patient", u"logo", None))
        self.label_4.setText(QCoreApplication.translate("Patient", u"Patient's Records", None))
        self.miniBtn.setText(QCoreApplication.translate("Patient", u"__", None))
        self.exitBtn.setText(QCoreApplication.translate("Patient", u"X", None))
        self.groupBox.setTitle(QCoreApplication.translate("Patient", u"Activities", None))
#if QT_CONFIG(tooltip)
        self.profileBtn.setToolTip(QCoreApplication.translate("Patient", u"<html><head/><body><p>Click to view patient's profile</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.profileBtn.setText(QCoreApplication.translate("Patient", u"Profile", None))
#if QT_CONFIG(tooltip)
        self.clinicBtn.setToolTip(QCoreApplication.translate("Patient", u"<html><head/><body><p>Click to access patient's clinical records</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.clinicBtn.setText(QCoreApplication.translate("Patient", u"Clinic", None))
#if QT_CONFIG(tooltip)
        self.pharmacyBtn.setToolTip(QCoreApplication.translate("Patient", u"<html><head/><body><p>Click to access patient's pharmacetical records</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pharmacyBtn.setText(QCoreApplication.translate("Patient", u"Pharmacy", None))
#if QT_CONFIG(tooltip)
        self.labBtn.setToolTip(QCoreApplication.translate("Patient", u"<html><head/><body><p>Click to access patient's laboratory records</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labBtn.setText(QCoreApplication.translate("Patient", u"Lab", None))
#if QT_CONFIG(tooltip)
        self.accountBtn.setToolTip(QCoreApplication.translate("Patient", u"<html><head/><body><p>Click to access patient's accout records</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.accountBtn.setText(QCoreApplication.translate("Patient", u"Account", None))
        self.label_3.setText(QCoreApplication.translate("Patient", u"Patient's Name:", None))
        self.fullname.setText("")
#if QT_CONFIG(tooltip)
        self.bookBtn.setToolTip(QCoreApplication.translate("Patient", u"<html><head/><body><p>Click to create new appointment</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bookBtn.setText(QCoreApplication.translate("Patient", u"Create Appointment", None))
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("Patient", u"<html><head/><body><p>Click to close patient's records</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText(QCoreApplication.translate("Patient", u"Close", None))
        self.label.setText(QCoreApplication.translate("Patient", u"Patient's Records", None))
        self.label_2.setText(QCoreApplication.translate("Patient", u"Card Number: ", None))
        self.cardNum.setText(QCoreApplication.translate("Patient", u"0000000000", None))
    # retranslateUi

