# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MedResult.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MedResult(object):
    def setupUi(self, MedResult):
        if not MedResult.objectName():
            MedResult.setObjectName(u"MedResult")
        MedResult.resize(400, 300)
        self.gridLayout = QGridLayout(MedResult)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgLayer = QFrame(MedResult)
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
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.bgframe)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.date = QLabel(self.bgframe)
        self.date.setObjectName(u"date")
        self.date.setAutoFillBackground(True)

        self.horizontalLayout_2.addWidget(self.date)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.table = QTableWidget(self.bgframe)
        self.table.setObjectName(u"table")

        self.verticalLayout.addWidget(self.table)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.bgframe)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_2.addWidget(self.bgframe, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.bgLayer, 0, 0, 1, 1)


        self.retranslateUi(MedResult)

        QMetaObject.connectSlotsByName(MedResult)
    # setupUi

    def retranslateUi(self, MedResult):
        MedResult.setWindowTitle(QCoreApplication.translate("MedResult", u"Medical Test Result", None))
        self.label_2.setText(QCoreApplication.translate("MedResult", u"Date Recieved:", None))
        self.date.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MedResult", u"<html><head/><body><p>Click to close result</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MedResult", u"Close", None))
    # retranslateUi

