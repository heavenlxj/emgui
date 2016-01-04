__author__ = 'xingjieliu'

import sys
sys.path.append('../..')

import QtUiFiles.loadRoute as loadRoute
from PyQt4.QtGui import QWidget,QApplication


class LoadRouteWidget(QWidget):
    def __init__(self):
        super(LoadRouteWidget, self).__init__()
        self.ui = loadRoute.Ui_Form()
        self.ui.setupUi(self)

    def initialize(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadRouteWidget()
    window.show()
    sys.exit(app.exec_())
    pass