# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(312, 358)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 271, 271))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.initialReportBtn = QtGui.QPushButton(self.layoutWidget)
        self.initialReportBtn.setObjectName(_fromUtf8("initialReportBtn"))
        self.verticalLayout.addWidget(self.initialReportBtn)
        self.requestRouteBtn = QtGui.QPushButton(self.layoutWidget)
        self.requestRouteBtn.setObjectName(_fromUtf8("requestRouteBtn"))
        self.verticalLayout.addWidget(self.requestRouteBtn)
        self.loadRouteBtn = QtGui.QPushButton(self.layoutWidget)
        self.loadRouteBtn.setObjectName(_fromUtf8("loadRouteBtn"))
        self.verticalLayout.addWidget(self.loadRouteBtn)
        self.shareRouteBtn = QtGui.QPushButton(self.layoutWidget)
        self.shareRouteBtn.setObjectName(_fromUtf8("shareRouteBtn"))
        self.verticalLayout.addWidget(self.shareRouteBtn)
        self.objectionReportBtn = QtGui.QPushButton(self.layoutWidget)
        self.objectionReportBtn.setObjectName(_fromUtf8("objectionReportBtn"))
        self.verticalLayout.addWidget(self.objectionReportBtn)
        self.fmrBtn = QtGui.QPushButton(self.layoutWidget)
        self.fmrBtn.setObjectName(_fromUtf8("fmrBtn"))
        self.verticalLayout.addWidget(self.fmrBtn)
        self.licenseBtn = QtGui.QPushButton(self.layoutWidget)
        self.licenseBtn.setObjectName(_fromUtf8("licenseBtn"))
        self.verticalLayout.addWidget(self.licenseBtn)
        self.exitBtn = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy)
        self.exitBtn.setDefault(False)
        self.exitBtn.setFlat(False)
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.verticalLayout.addWidget(self.exitBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 312, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.openAction = QtGui.QAction(MainWindow)
        self.openAction.setObjectName(_fromUtf8("openAction"))
        self.menuFile.addAction(self.openAction)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.initialReportBtn, self.requestRouteBtn)
        MainWindow.setTabOrder(self.requestRouteBtn, self.loadRouteBtn)
        MainWindow.setTabOrder(self.loadRouteBtn, self.shareRouteBtn)
        MainWindow.setTabOrder(self.shareRouteBtn, self.objectionReportBtn)
        MainWindow.setTabOrder(self.objectionReportBtn, self.fmrBtn)
        MainWindow.setTabOrder(self.fmrBtn, self.licenseBtn)
        MainWindow.setTabOrder(self.licenseBtn, self.exitBtn)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.initialReportBtn.setText(_translate("MainWindow", "Initial Report", None))
        self.requestRouteBtn.setText(_translate("MainWindow", "Request Route", None))
        self.loadRouteBtn.setText(_translate("MainWindow", "Load Route", None))
        self.shareRouteBtn.setText(_translate("MainWindow", "Share Route", None))
        self.objectionReportBtn.setText(_translate("MainWindow", "Objection Report", None))
        self.fmrBtn.setText(_translate("MainWindow", "Fleet Management Report", None))
        self.licenseBtn.setText(_translate("MainWindow", "License", None))
        self.exitBtn.setText(_translate("MainWindow", "Exit", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.openAction.setText(_translate("MainWindow", "Open", None))
        self.openAction.setToolTip(_translate("MainWindow", "Open File", None))

