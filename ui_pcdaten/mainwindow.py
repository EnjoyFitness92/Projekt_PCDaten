# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pcdaten\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PCDaten(object):
    def setupUi(self, PCDaten):
        PCDaten.setObjectName("PCDaten")
        PCDaten.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(PCDaten)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.addUser = QtWidgets.QPushButton(self.centralwidget)
        self.addUser.setObjectName("addUser")
        self.gridLayout.addWidget(self.addUser, 0, 1, 1, 1)
        self.searchUser = QtWidgets.QPushButton(self.centralwidget)
        self.searchUser.setObjectName("searchUser")
        self.gridLayout.addWidget(self.searchUser, 1, 1, 1, 1)
        self.addDevice = QtWidgets.QPushButton(self.centralwidget)
        self.addDevice.setObjectName("addDevice")
        self.gridLayout.addWidget(self.addDevice, 0, 0, 1, 1)
        self.searchDevice = QtWidgets.QPushButton(self.centralwidget)
        self.searchDevice.setObjectName("searchDevice")
        self.gridLayout.addWidget(self.searchDevice, 1, 0, 1, 1)
        PCDaten.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PCDaten)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        PCDaten.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PCDaten)
        self.statusbar.setObjectName("statusbar")
        PCDaten.setStatusBar(self.statusbar)

        self.retranslateUi(PCDaten)
        QtCore.QMetaObject.connectSlotsByName(PCDaten)

    def retranslateUi(self, PCDaten):
        _translate = QtCore.QCoreApplication.translate
        PCDaten.setWindowTitle(_translate("PCDaten", "MainWindow"))
        self.addUser.setText(_translate("PCDaten", "Benutzer hinzufügen"))
        self.searchUser.setText(_translate("PCDaten", "Benutzer suchen"))
        self.addDevice.setText(_translate("PCDaten", "Gerät hinzufügen"))
        self.searchDevice.setText(_translate("PCDaten", "Gerät suchen"))
