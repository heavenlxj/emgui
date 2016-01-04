__author__ = 'xingjieliu'

import sys
sys.path.append('../..')

import QtUiFiles.objectionReport as objectionReport
from PyQt4.QtGui import QWidget,QApplication


class ObjectionReportWidget(QWidget):
    def __init__(self):
        super(ObjectionReportWidget, self).__init__()
        self.ui = objectionReport.Ui_Form()
        self.ui.setupUi(self)

    def initialize(self):
        pass

    def tableSetting(self):
        self.ui.route_table_widget.setColumnCount(7)
        self.ui.route_table_widget.setRowCount(5)
        self.ui.route_table_widget.setHorizontalHeaderLabels(['Id', 'Latitude', 'Longtitude'])
        self.ui.route_table_widget.setSpan()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ObjectionReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass