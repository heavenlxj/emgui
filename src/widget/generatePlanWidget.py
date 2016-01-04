__author__ = 'xingjieliu'

import sys
sys.path.append('../..')

import QtUiFiles.planGenerator as planGenerator
from PyQt4.QtGui import QWidget,QApplication


class planGenerateWidget(QWidget):
    def __init__(self):
        super(planGenerateWidget, self).__init__()
        self.ui = planGenerator.Ui_Form()
        self.ui.setupUi(self)

    def initialize(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = planGenerateWidget()
    window.show()
    sys.exit(app.exec_())
    pass