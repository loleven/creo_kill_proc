# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Data\Development\PycharmProjects\KillCreo\src\gui_kill_creo.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frm_kill_creo(object):
    def setupUi(self, frm_kill_creo):
        frm_kill_creo.setObjectName("frm_kill_creo")
        frm_kill_creo.resize(400, 300)
        frm_kill_creo.setMinimumSize(QtCore.QSize(400, 300))
        frm_kill_creo.setMaximumSize(QtCore.QSize(400, 300))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(frm_kill_creo)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_result = QtWidgets.QListWidget(frm_kill_creo)
        self.list_result.setObjectName("list_result")
        self.verticalLayout.addWidget(self.list_result)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_kill = QtWidgets.QPushButton(frm_kill_creo)
        self.btn_kill.setObjectName("btn_kill")
        self.horizontalLayout.addWidget(self.btn_kill)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(frm_kill_creo)
        QtCore.QMetaObject.connectSlotsByName(frm_kill_creo)

    def retranslateUi(self, frm_kill_creo):
        _translate = QtCore.QCoreApplication.translate
        frm_kill_creo.setWindowTitle(_translate("frm_kill_creo", "Kill Creo"))
        self.btn_kill.setText(_translate("frm_kill_creo", "Kill Creo"))

