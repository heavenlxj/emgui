__author__ = 'xingjieliu'

import sys
sys.path.append('../..')

import QtUiFiles.planGenerator as planGenerator
from PyQt4.QtGui import *
from lib.utils import *

class planGenerateWidget(QWidget):
    def __init__(self):
        super(planGenerateWidget, self).__init__()
        self.ui = planGenerator.Ui_Form()
        self.ui.setupUi(self)
        self.initialize()

    def initialize(self):
        pass

    def loadConfig(self):
        configs, msg = Utils.readGeneralConfigFromXml()
        if configs is not None and len(configs) !=0:
            self.ui.ship_name_edit.setText(configs['ship_name'])
            self.ui.call_sign_edit.setText(configs['call_sign'])
            self.ui.captain_name_edit.setText(configs['captain_name'])
            self.ui.date_edit.setText(configs['date'])
            pass
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", msg)
            msg_box.exec_()


    def test(self):
        print 'hello'

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = planGenerateWidget()
    window.show()
    sys.exit(app.exec_())
    pass