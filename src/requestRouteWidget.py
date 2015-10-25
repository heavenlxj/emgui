__author__ = 'xingjieliu'

import sys
sys.path.append('..')

import QtUiFiles.requestRoute as reqReport
from PyQt4.QtGui import QWidget,QApplication


class ReqReportWidget(QWidget):
    def __init__(self):
        super(ReqReportWidget, self).__init__()
        self.ui = reqReport.Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReqReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass