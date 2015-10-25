__author__ = 'xingjieliu'

import sys
sys.path.append('..')

import QtUiFiles.initialReport as iniReport
from PyQt4.QtGui import QWidget,QApplication


class IniReportWidget(QWidget):
    def __init__(self):
        super(IniReportWidget, self).__init__()
        self.ui = iniReport.Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IniReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass