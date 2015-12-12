__author__ = 'xingjieliu'

import sys
sys.path.append('../..')

import QtUiFiles.initialReport as iniReport

from PyQt4.QtGui import *


class IniReportWidget(QWidget):
    def __init__(self):
        super(IniReportWidget, self).__init__()
        self.ui = iniReport.Ui_Form()
        self.ui.setupUi(self)
        self.initialize()


    def initialize(self):
        self.ship_name =""
        #self.ui.shipNameEdit.textChanged(self.ship_name)

        self.ui.submitButton.clicked.connect(self.printT)
    def printT(self):
        self.ship_name = self.ui.shipNameEdit.text()
        self.portRegistry = self.ui.portRegistryEdit.text()
        self.email = self.ui.emailEdit.text()
        # self.ui.emailEdit.setValidator()
        # QRegExpValidator()
        print 'PRINT ship name=%s' % self.ship_name
        print 'PRINT REGISTRY name=%s' % self.portRegistry
        print 'PRINT email name=%s' % self.email

    def setText(self, text):
        self.ship_name = text


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IniReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass