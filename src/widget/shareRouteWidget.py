__author__ = 'xingjieliu'

import sys
sys.path.append('../..')

import QtUiFiles.shareRoute as shareReport
from PyQt4.QtGui import QWidget,QApplication


class ShareReportWidget(QWidget):
    def __init__(self):
        super(ShareReportWidget, self).__init__()
        self.ui = shareReport.Ui_Form()
        self.ui.setupUi(self)

    def initialize(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShareReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass