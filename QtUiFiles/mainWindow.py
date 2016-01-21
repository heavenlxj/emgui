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
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(256, 326)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.initialReportBtn = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.initialReportBtn.sizePolicy().hasHeightForWidth())
        self.initialReportBtn.setSizePolicy(sizePolicy)
        self.initialReportBtn.setObjectName(_fromUtf8("initialReportBtn"))
        self.verticalLayout.addWidget(self.initialReportBtn)
        self.requestRouteBtn = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.requestRouteBtn.sizePolicy().hasHeightForWidth())
        self.requestRouteBtn.setSizePolicy(sizePolicy)
        self.requestRouteBtn.setObjectName(_fromUtf8("requestRouteBtn"))
        self.verticalLayout.addWidget(self.requestRouteBtn)
        self.loadRouteBtn = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadRouteBtn.sizePolicy().hasHeightForWidth())
        self.loadRouteBtn.setSizePolicy(sizePolicy)
        self.loadRouteBtn.setObjectName(_fromUtf8("loadRouteBtn"))
        self.verticalLayout.addWidget(self.loadRouteBtn)
        self.revertRouteBtn = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.revertRouteBtn.sizePolicy().hasHeightForWidth())
        self.revertRouteBtn.setSizePolicy(sizePolicy)
        self.revertRouteBtn.setObjectName(_fromUtf8("revertRouteBtn"))
        self.verticalLayout.addWidget(self.revertRouteBtn)
        self.objectionReportBtn = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.objectionReportBtn.sizePolicy().hasHeightForWidth())
        self.objectionReportBtn.setSizePolicy(sizePolicy)
        self.objectionReportBtn.setObjectName(_fromUtf8("objectionReportBtn"))
        self.verticalLayout.addWidget(self.objectionReportBtn)
        self.planBtn = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.planBtn.sizePolicy().hasHeightForWidth())
        self.planBtn.setSizePolicy(sizePolicy)
        self.planBtn.setObjectName(_fromUtf8("planBtn"))
        self.verticalLayout.addWidget(self.planBtn)
        self.exitBtn = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy)
        self.exitBtn.setDefault(False)
        self.exitBtn.setFlat(False)
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.verticalLayout.addWidget(self.exitBtn)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 256, 23))
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
        MainWindow.setTabOrder(self.loadRouteBtn, self.revertRouteBtn)
        MainWindow.setTabOrder(self.revertRouteBtn, self.objectionReportBtn)
        MainWindow.setTabOrder(self.objectionReportBtn, self.planBtn)
        MainWindow.setTabOrder(self.planBtn, self.exitBtn)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "E-Marine", None))
        self.initialReportBtn.setText(_translate("MainWindow", "Initial Report", None))
        self.requestRouteBtn.setText(_translate("MainWindow", "Request Route", None))
        self.loadRouteBtn.setText(_translate("MainWindow", "Load Route", None))
        self.revertRouteBtn.setText(_translate("MainWindow", "Revert Route", None))
        self.objectionReportBtn.setText(_translate("MainWindow", "Objection Report", None))
        self.planBtn.setText(_translate("MainWindow", "Passage Plan Generator", None))
        self.exitBtn.setText(_translate("MainWindow", "Exit", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.openAction.setText(_translate("MainWindow", "Open", None))
        self.openAction.setToolTip(_translate("MainWindow", "Open File", None))

