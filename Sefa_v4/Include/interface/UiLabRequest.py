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
        LabRequest.resize(385, 251)
        self.gridLayout = QGridLayout(LabRequest)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.bgLayer = QFrame(LabRequest)
        self.bgLayer.setObjectName(u"bgLayer")
        self.bgLayer.setFrameShape(QFrame.StyledPanel)
        self.bgLayer.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.bgLayer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 5, 10, 10)
        self.bgframe = QFrame(self.bgLayer)
        self.bgframe.setObjectName(u"bgframe")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bgframe.sizePolicy().hasHeightForWidth())
        self.bgframe.setSizePolicy(sizePolicy)
        self.bgframe.setFrameShape(QFrame.Box)
        self.bgframe.setFrameShadow(QFrame.Raised)
        self.bgframe.setLineWidth(2)
        self.bgframe.setMidLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.bgframe)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.bgframe)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.bgframe)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_3.setFont(font1)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setFrameShape(QFrame.StyledPanel)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame = QFrame(self.bgframe)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.specimen = QLineEdit(self.frame)
        self.specimen.setObjectName(u"specimen")
        self.specimen.setFont(font1)
        self.specimen.setFocusPolicy(Qt.ClickFocus)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.specimen)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.diagnosis = QLineEdit(self.frame)
        self.diagnosis.setObjectName(u"diagnosis")
        self.diagnosis.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.diagnosis)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.examination = QLineEdit(self.frame)
        self.examination.setObjectName(u"examination")
        self.examination.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.examination)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.Pathology = QLineEdit(self.frame)
        self.Pathology.setObjectName(u"Pathology")
        self.Pathology.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.Pathology)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sendReqBtn = QPushButton(self.bgframe)
        self.sendReqBtn.setObjectName(u"sendReqBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sendReqBtn.sizePolicy().hasHeightForWidth())
        self.sendReqBtn.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamily(u"Comic Sans MS")
        font2.setPointSize(12)
        self.sendReqBtn.setFont(font2)
        self.sendReqBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.sendReqBtn)

        self.viewResult = QPushButton(self.bgframe)
        self.viewResult.setObjectName(u"viewResult")
        font3 = QFont()
        font3.setFamily(u"Comic Sans MS")
        self.viewResult.setFont(font3)

        self.horizontalLayout_2.addWidget(self.viewResult)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addWidget(self.bgframe, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 1, 1, 1, 1)


        self.retranslateUi(LabRequest)

        QMetaObject.connectSlotsByName(LabRequest)
    # setupUi

    def retranslateUi(self, LabRequest):
        LabRequest.setWindowTitle(QCoreApplication.translate("LabRequest", u"Lab Request Form", None))
        self.label.setText(QCoreApplication.translate("LabRequest", u"Date:", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("LabRequest", u"Name of Specimen:", None))
        self.label_5.setText(QCoreApplication.translate("LabRequest", u"Clinical Diagnosis:", None))
        self.label_9.setText(QCoreApplication.translate("LabRequest", u"Examination:", None))
        self.label_6.setText(QCoreApplication.translate("LabRequest", u"Pathology Number:", None))
#if QT_CONFIG(tooltip)
        self.sendReqBtn.setToolTip(QCoreApplication.translate("LabRequest", u"<html><head/><body><p>Click to request for medical test</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sendReqBtn.setText(QCoreApplication.translate("LabRequest", u"Send Request", None))
#if QT_CONFIG(tooltip)
        self.viewResult.setToolTip(QCoreApplication.translate("LabRequest", u"<html><head/><body><p>Click to view medical test results</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.viewResult.setText(QCoreApplication.translate("LabRequest", u"View Result", None))
    # retranslateUi

