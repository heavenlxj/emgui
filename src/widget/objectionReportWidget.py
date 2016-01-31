__author__ = 'xingjieliu'

import sys
import QtUiFiles.objectionReport as objectionReport
from PyQt4.QtGui import QWidget,QApplication,QMessageBox
from lib.utils import *
from dao.object import *
import time


class ObjectionReportWidget(QWidget):
    def __init__(self):
        super(ObjectionReportWidget, self).__init__()
        self.ui = objectionReport.Ui_Form()
        self.ui.setupUi(self)
        self.initialize()

    def initialize(self):
        self.ui.submit_btn.clicked.connect(self.generateXml)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.reload_btn.clicked.connect(self.loadConfig)

    def tableSetting(self):
        self.ui.route_table_widget.setColumnCount(7)
        self.ui.route_table_widget.setRowCount(5)
        self.ui.route_table_widget.setHorizontalHeaderLabels(['Id', 'Latitude', 'Longtitude'])
        self.ui.route_table_widget.setSpan()

    def generateXml(self):
        root = objection_report()
        property = Property()
        root.Property = property

        data_dir = Utils.createDateDir()
        fn_path = abs_lambda(os.path.join(data_dir , 'object.xml'))
        with open(fn_path, 'w') as f:
            f.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
            root.export(f, 1, namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
        msg_box = QMessageBox(QMessageBox.Information, "Success", "Objection Report config file generated successfully")
        msg_box.exec_()

    def loadConfig(self):
        configs, msg = Utils.readGeneralConfigFromXml()
        if configs is not None and len(configs) !=0:
            self.ui.ship_name_edit.setText(configs['ship_name'])
            self.ui.call_sign_edit.setText(configs['call_sign'])
            self.ui.captain_name_edit.setText(configs['captain_name'])
            cur_time = time.strftime('%Y/%m/%d',time.localtime(time.time()))
            self.ui.date_edit.setText(cur_time)
            pass
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", msg)
            msg_box.exec_()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ObjectionReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass