__author__ = 'xingjieliu'

import sys
sys.path.append('../..')

import QtUiFiles.quartelyReport as quartelyReport
from PyQt4.QtGui import QWidget,QApplication


class QuartelyReportWidget(QWidget):
    def __init__(self):
        super(QuartelyReportWidget, self).__init__()
        self.ui = quartelyReport.Ui_Form()
        self.ui.setupUi(self)

    def initialize(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuartelyReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass
