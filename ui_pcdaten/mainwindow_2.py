# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pcdaten\mainwindow_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainwindow_2(object):
    def setupUi(self, mainwindow_2):
        mainwindow_2.setObjectName("mainwindow_2")
        mainwindow_2.resize(400, 209)
        self.gridLayout = QtWidgets.QGridLayout(mainwindow_2)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(mainwindow_2)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.addPC = QtWidgets.QPushButton(self.widget)
        self.addPC.setObjectName("addPC")
        self.gridLayout_2.addWidget(self.addPC, 0, 0, 1, 1)
        self.searchUser = QtWidgets.QPushButton(self.widget)
        self.searchUser.setObjectName("searchUser")
        self.gridLayout_2.addWidget(self.searchUser, 0, 1, 1, 1)
        self.addUser = QtWidgets.QPushButton(self.widget)
        self.addUser.setObjectName("addUser")
        self.gridLayout_2.addWidget(self.addUser, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(mainwindow_2)
        QtCore.QMetaObject.connectSlotsByName(mainwindow_2)

    def retranslateUi(self, mainwindow_2):
        _translate = QtCore.QCoreApplication.translate
        mainwindow_2.setWindowTitle(_translate("mainwindow_2", "Dialog"))
        self.addPC.setText(_translate("mainwindow_2", "PC hinzufuegen"))
        self.searchUser.setText(_translate("mainwindow_2", "Benutzer suchen"))
        self.addUser.setText(_translate("mainwindow_2", "Benutzer hinzufügen"))
        self.pushButton_4.setText(_translate("mainwindow_2", "PC suchen"))
