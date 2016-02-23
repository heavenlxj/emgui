__author__ = 'xingjieliu'

import sys
import time
import copy

from PyQt4.QtGui import QWidget,QApplication,QMessageBox,QFileDialog

import QtUiFiles.quartelyReport as quartelyReport


class QuartelyReportWidget(QWidget):
    def __init__(self):
        super(QuartelyReportWidget, self).__init__()
        self.ui = quartelyReport.Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuartelyReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass