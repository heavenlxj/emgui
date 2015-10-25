__author__ = 'xingjieliu'

from PyQt4.QtGui import *
import sys
sys.path.append('..')
import QtUiFiles.mainWindow as MainWindow
import initialWidget
import requestRouteWidget
import shareRouteWidget
import objectionReportWidget

class RootWindow(QMainWindow):
    def __init__(self):
        super(RootWindow, self).__init__()
        self.root = MainWindow.Ui_MainWindow()
        self.iniReport = initialWidget.IniReportWidget()
        self.reqReport = requestRouteWidget.ReqReportWidget()
        self.shareReport = shareRouteWidget.ShareReportWidget()
        self.objectionReport = objectionReportWidget.ObjectionReportWidget()
        self.root.setupUi(self)
        self.buttonConnect()

    def buttonConnect(self):
        self.root.initialReportBtn.clicked.connect(self.iniReport.show)
        self.root.requestRouteBtn.clicked.connect(self.reqReport.show)
        self.root.shareRouteBtn.clicked.connect(self.shareReport.show)
        self.root.objectionReportBtn.clicked.connect(self.objectionReport.show)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RootWindow()
    window.show()
    try:
        sys.exit(app.exec_())
    except:
        sys.exit(0)
    pass
