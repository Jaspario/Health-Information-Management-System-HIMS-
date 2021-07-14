# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(511, 338)
        self.gridLayout = QGridLayout(Home)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgLayer = QFrame(Home)
        self.bgLayer.setObjectName(u"bgLayer")
        font = QFont()
        font.setPointSize(8)
        self.bgLayer.setFont(font)
        self.bgLayer.setFrameShape(QFrame.StyledPanel)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.bgframe = QFrame(self.bgLayer)
        self.bgframe.setObjectName(u"bgframe")
        self.bgframe.setFont(font)
        self.bgframe.setFrameShape(QFrame.Box)
        self.bgframe.setFrameShadow(QFrame.Raised)
        self.bgframe.setLineWidth(2)
        self.bgframe.setMidLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.bgframe)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchBtn = QPushButton(self.bgframe)
        self.searchBtn.setObjectName(u"searchBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(8)
        self.searchBtn.setFont(font1)

        self.horizontalLayout.addWidget(self.searchBtn)

        self.searchField = QLineEdit(self.bgframe)
        self.searchField.setObjectName(u"searchField")
        self.searchField.setFont(font)

        self.horizontalLayout.addWidget(self.searchField)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.search = QLabel(self.bgframe)
        self.search.setObjectName(u"search")
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.search.setFont(font2)
        self.search.setMargin(5)

        self.verticalLayout.addWidget(self.search)

        self.pinfoBox = QGroupBox(self.bgframe)
        self.pinfoBox.setObjectName(u"pinfoBox")
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.pinfoBox.setFont(font3)
        self.pinfoBox.setFlat(False)
        self.pinfoBox.setCheckable(False)
        self.horizontalLayout_2 = QHBoxLayout(self.pinfoBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(4)
        self.label = QLabel(self.pinfoBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.fname = QLabel(self.pinfoBox)
        self.fname.setObjectName(u"fname")
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setWeight(50)
        self.fname.setFont(font4)
        self.fname.setAutoFillBackground(True)
        self.fname.setMargin(5)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.label_3 = QLabel(self.pinfoBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.patientID = QLabel(self.pinfoBox)
        self.patientID.setObjectName(u"patientID")
        self.patientID.setFont(font4)
        self.patientID.setAutoFillBackground(True)
        self.patientID.setMargin(5)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.patientID)

        self.label_5 = QLabel(self.pinfoBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.label_2 = QLabel(self.pinfoBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.gender = QLabel(self.pinfoBox)
        self.gender.setObjectName(u"gender")
        self.gender.setFont(font4)
        self.gender.setAutoFillBackground(True)
        self.gender.setMargin(5)

        self.horizontalLayout_5.addWidget(self.gender)

        self.label_6 = QLabel(self.pinfoBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.age = QLabel(self.pinfoBox)
        self.age.setObjectName(u"age")
        self.age.setFont(font4)
        self.age.setAutoFillBackground(True)
        self.age.setMargin(5)

        self.horizontalLayout_5.addWidget(self.age)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.regDate = QLabel(self.pinfoBox)
        self.regDate.setObjectName(u"regDate")
        self.regDate.setFont(font4)
        self.regDate.setAutoFillBackground(True)
        self.regDate.setMargin(5)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.regDate)


        self.horizontalLayout_2.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(4)
        self.label_7 = QLabel(self.pinfoBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.lname = QLabel(self.pinfoBox)
        self.lname.setObjectName(u"lname")
        self.lname.setFont(font4)
        self.lname.setAutoFillBackground(True)
        self.lname.setMargin(5)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lname)

        self.label_9 = QLabel(self.pinfoBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.label_11 = QLabel(self.pinfoBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.status = QLabel(self.pinfoBox)
        self.status.setObjectName(u"status")
        self.status.setFont(font4)
        self.status.setAutoFillBackground(True)
        self.status.setMargin(5)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.status)

        self.label_10 = QLabel(self.pinfoBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.pclass = QLabel(self.pinfoBox)
        self.pclass.setObjectName(u"pclass")
        self.pclass.setFont(font4)
        self.pclass.setAutoFillBackground(True)
        self.pclass.setMargin(5)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.pclass)

        self.lastCheckup = QLabel(self.pinfoBox)
        self.lastCheckup.setObjectName(u"lastCheckup")
        self.lastCheckup.setFont(font4)
        self.lastCheckup.setAutoFillBackground(True)
        self.lastCheckup.setMargin(5)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lastCheckup)


        self.horizontalLayout_2.addLayout(self.formLayout_2)


        self.verticalLayout.addWidget(self.pinfoBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.viewBtn = QPushButton(self.bgframe)
        self.viewBtn.setObjectName(u"viewBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.viewBtn.sizePolicy().hasHeightForWidth())
        self.viewBtn.setSizePolicy(sizePolicy1)
        self.viewBtn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.viewBtn)

        self.regNewBtn = QPushButton(self.bgframe)
        self.regNewBtn.setObjectName(u"regNewBtn")
        sizePolicy1.setHeightForWidth(self.regNewBtn.sizePolicy().hasHeightForWidth())
        self.regNewBtn.setSizePolicy(sizePolicy1)
        self.regNewBtn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.regNewBtn)

        self.bookBtn = QPushButton(self.bgframe)
        self.bookBtn.setObjectName(u"bookBtn")
        sizePolicy1.setHeightForWidth(self.bookBtn.sizePolicy().hasHeightForWidth())
        self.bookBtn.setSizePolicy(sizePolicy1)
        self.bookBtn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.bookBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sendBtn = QPushButton(self.bgframe)
        self.sendBtn.setObjectName(u"sendBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sendBtn.sizePolicy().hasHeightForWidth())
        self.sendBtn.setSizePolicy(sizePolicy2)
        self.sendBtn.setFont(font1)

        self.horizontalLayout_4.addWidget(self.sendBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.closeBtn = QPushButton(self.bgframe)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setFont(font1)

        self.horizontalLayout_4.addWidget(self.closeBtn)

        self.logOutBtn = QPushButton(self.bgframe)
        self.logOutBtn.setObjectName(u"logOutBtn")
        self.logOutBtn.setFont(font1)

        self.horizontalLayout_4.addWidget(self.logOutBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addWidget(self.bgframe, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.bgLayer)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setFont(font3)
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 0, 0, 1, 1)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Home", None))
        self.searchBtn.setText(QCoreApplication.translate("Home", u"Search", None))
        self.searchField.setPlaceholderText(QCoreApplication.translate("Home", u"Please Insert firstname and lastname or Patient's ID", None))
        self.search.setText(QCoreApplication.translate("Home", u"popupMsg", None))
        self.pinfoBox.setTitle(QCoreApplication.translate("Home", u"Patient's Summary", None))
        self.label.setText(QCoreApplication.translate("Home", u"Firstname:", None))
        self.fname.setText("")
        self.label_3.setText(QCoreApplication.translate("Home", u"Patient's ID:", None))
        self.patientID.setText("")
        self.label_5.setText(QCoreApplication.translate("Home", u"Registration Date:", None))
        self.label_2.setText(QCoreApplication.translate("Home", u"Gender:", None))
        self.gender.setText("")
        self.label_6.setText(QCoreApplication.translate("Home", u"Age:", None))
        self.age.setText("")
        self.regDate.setText("")
        self.label_7.setText(QCoreApplication.translate("Home", u"Lastname:", None))
        self.lname.setText("")
        self.label_9.setText(QCoreApplication.translate("Home", u"Patient's Status:", None))
        self.label_11.setText(QCoreApplication.translate("Home", u"Last Checkup Date:", None))
        self.status.setText("")
        self.label_10.setText(QCoreApplication.translate("Home", u"Class:", None))
        self.pclass.setText("")
        self.lastCheckup.setText("")
        self.viewBtn.setText(QCoreApplication.translate("Home", u"View Record", None))
        self.regNewBtn.setText(QCoreApplication.translate("Home", u"Register New Patient", None))
        self.bookBtn.setText(QCoreApplication.translate("Home", u"Book Appointment", None))
        self.sendBtn.setText(QCoreApplication.translate("Home", u"Send File", None))
        self.closeBtn.setText(QCoreApplication.translate("Home", u"Close Record", None))
        self.logOutBtn.setText(QCoreApplication.translate("Home", u"LogOut", None))
    # retranslateUi

