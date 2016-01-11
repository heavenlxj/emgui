__author__ = 'xingjieliu'

import sys
sys.path.append('../..')

import QtUiFiles.planGenerator as planGenerator
from PyQt4.QtGui import *

class planGenerateWidget(QWidget):
    def __init__(self):
        super(planGenerateWidget, self).__init__()
        self.ui = planGenerator.Ui_Form()
        self.ui.setupUi(self)
        self.initialize()

    def initialize(self):
        pass


    def test(self):
        print 'hello'

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = planGenerateWidget()
    window.show()
    sys.exit(app.exec_())
    pass