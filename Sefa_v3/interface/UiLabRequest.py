# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LabRequest.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LabRequest(object):
    def setupUi(self, LabRequest):
        if not LabRequest.objectName():
            LabRequest.setObjectName(u"LabRequest")
        LabRequest.resize(385, 265)
        self.gridLayout = QGridLayout(LabRequest)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.bgflayer = QFrame(LabRequest)
        self.bgflayer.setObjectName(u"bgflayer")
        self.bgflayer.setFrameShape(QFrame.StyledPanel)
        self.bgflayer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.bgflayer)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 5, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo = QLabel(self.bgflayer)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.logo)

        self.label_7 = QLabel(self.bgflayer)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_7)

        self.exitBtn = QPushButton(self.bgflayer)
        self.exitBtn.setObjectName(u"exitBtn")
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(8)
        self.exitBtn.setFont(font)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.exitBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.bgfFrame = QFrame(self.bgflayer)
        self.bgfFrame.setObjectName(u"bgfFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bgfFrame.sizePolicy().hasHeightForWidth())
        self.bgfFrame.setSizePolicy(sizePolicy2)
        self.bgfFrame.setFrameShape(QFrame.Box)
        self.bgfFrame.setFrameShadow(QFrame.Raised)
        self.bgfFrame.setLineWidth(2)
        self.bgfFrame.setMidLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.bgfFrame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.bgfFrame)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(7)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.bgfFrame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.frame = QFrame(self.bgfFrame)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.specimen = QLineEdit(self.frame)
        self.specimen.setObjectName(u"specimen")
        self.specimen.setFocusPolicy(Qt.ClickFocus)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.specimen)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.diagnosis = QLineEdit(self.frame)
        self.diagnosis.setObjectName(u"diagnosis")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.diagnosis)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.examination = QLineEdit(self.frame)
        self.examination.setObjectName(u"examination")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.examination)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.Pathology = QLineEdit(self.frame)
        self.Pathology.setObjectName(u"Pathology")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.Pathology)


        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sendReqBtn = QPushButton(self.bgfFrame)
        self.sendReqBtn.setObjectName(u"sendReqBtn")
        self.sendReqBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.sendReqBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.bgfFrame)


        self.gridLayout.addWidget(self.bgflayer, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)


        self.retranslateUi(LabRequest)

        QMetaObject.connectSlotsByName(LabRequest)
    # setupUi

    def retranslateUi(self, LabRequest):
        LabRequest.setWindowTitle(QCoreApplication.translate("LabRequest", u"Lab Request Form", None))
        self.logo.setText(QCoreApplication.translate("LabRequest", u"logo", None))
        self.label_7.setText(QCoreApplication.translate("LabRequest", u"Lab  Request Form", None))
        self.exitBtn.setText(QCoreApplication.translate("LabRequest", u"X", None))
        self.label.setText(QCoreApplication.translate("LabRequest", u"Date:", None))
        self.label_3.setText(QCoreApplication.translate("LabRequest", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("LabRequest", u"Name of Specimen:", None))
        self.label_5.setText(QCoreApplication.translate("LabRequest", u"Clinical Diagnosis:", None))
        self.label_9.setText(QCoreApplication.translate("LabRequest", u"Examination:", None))
        self.label_6.setText(QCoreApplication.translate("LabRequest", u"Pathology Number:", None))
        self.sendReqBtn.setText(QCoreApplication.translate("LabRequest", u"Send Request", None))
    # retranslateUi

