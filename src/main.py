__author__ = 'xingjieliu'

import sys

from PyQt4.QtGui import *

sys.path.append('..')
import QtUiFiles.mainWindow as MainWindow
from src.widget import requestRouteWidget, objectionReportWidget, \
    initialWidget, revertRouteWidget, loadRouteWidget, generatePlanWidget

from PyQt4.QtCore import QString


class RootWindow(QMainWindow):
    def __init__(self):
        super(RootWindow, self).__init__()
        self.root = MainWindow.Ui_MainWindow()
        self.root.setupUi(self)
        self.iniReport = initialWidget.IniReportWidget()
        self.reqReport = requestRouteWidget.ReqReportWidget()
        self.loadRoute = loadRouteWidget.LoadRouteWidget()
        self.revertRoute = revertRouteWidget.RevertReportWidget()
        self.objectionReport = objectionReportWidget.ObjectionReportWidget()
        self.planGenerator = generatePlanWidget.planGenerateWidget()
        self.buttonConnect()

    def buttonConnect(self):
        self.root.initialReportBtn.clicked.connect(self.iniReport.show)
        self.root.requestRouteBtn.clicked.connect(self.reqReport.show)
        self.root.loadRouteBtn.clicked.connect(self.loadRoute.show)
        self.root.revertRouteBtn.clicked.connect(self.revertRoute.show)
        self.root.objectionReportBtn.clicked.connect(self.objectionReport.show)
        self.root.planBtn.clicked.connect(self.planGenerator.show)
        self.root.exitBtn.clicked.connect(self.exit)

    def exit(self):
        try:
            window.close()
        except:
            sys.exit(0)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RootWindow()
    window.show()
    sys.exit(app.exec_())
    pass
