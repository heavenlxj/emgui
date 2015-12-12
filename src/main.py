__author__ = 'xingjieliu'

import sys

from PyQt4.QtGui import *

sys.path.append('..')
import QtUiFiles.mainWindow as MainWindow
from src.widget import requestRouteWidget, objectionReportWidget, quartelyReportWidget, initialWidget, shareRouteWidget


class RootWindow(QMainWindow):
    def __init__(self):
        super(RootWindow, self).__init__()
        self.root = MainWindow.Ui_MainWindow()
        self.root.setupUi(self)
        self.iniReport = initialWidget.IniReportWidget()
        self.reqReport = requestRouteWidget.ReqReportWidget()
        self.shareReport = shareRouteWidget.ShareReportWidget()
        self.objectionReport = objectionReportWidget.ObjectionReportWidget()
        self.quartelyReport = quartelyReportWidget.QuartelyReportWidget()
        self.buttonConnect()

    def buttonConnect(self):
        self.root.initialReportBtn.clicked.connect(self.iniReport.show)
        self.root.requestRouteBtn.clicked.connect(self.reqReport.show)
        self.root.shareRouteBtn.clicked.connect(self.shareReport.show)
        self.root.objectionReportBtn.clicked.connect(self.objectionReport.show)
        self.root.quartelyReportBtn.clicked.connect(self.quartelyReport.show)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RootWindow()
    window.show()
    sys.exit(app.exec_())
    pass
