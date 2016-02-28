__author__ = 'xingjieliu'

import sys
import time
import datetime
from PyQt4.QtGui import QWidget,QApplication,QMessageBox
from PyQt4.QtCore import Qt
import QtUiFiles.quartelyReport as quartelyReport
from dao.quarter import *
from lib.utils import Utils
from lib.environ import *

class QuartelyReportWidget(QWidget):
    def __init__(self):
        super(QuartelyReportWidget, self).__init__()
        self.ui = quartelyReport.Ui_Form()
        self.ui.setupUi(self)
        self.autoloadConfig()
        self.initialize()


    def initialize(self):
        self.cargoTableInit()
        self.fuelTabelInit()
        self.comboInit()


    def buttonInit(self):
        self.ui.reload_btn.clicked.connect(self.autoloadConfig)
        self.ui.submit_btn.clicked.connect(self.generateXml)

    def comboInit(self):
        self.ui.quarter_combo.addItems(['1st Quarter', '2nd Quarter', '3th Quarter', '4th Quarter'])
        cur_year = datetime.date.today().year
        year_list = []
        for i in range(cur_year, cur_year-50, -1):
            year_list.append(str(i))
        self.ui.year_combo.addItems(year_list)

    def cargoTableInit(self):
        self.ui.cargo_table_widget.setAlternatingRowColors(True)

    def fuelTabelInit(self):
        self.ui.tfc_table_widget.setSpan(0,0,1,4)
        self.ui.tfc_table_widget.setSpan(0,4,1,4)
        self.ui.tfc_table_widget.setSpan(0,8,1,4)

    def autoloadConfig(self):
        configs, msg = Utils.readGeneralConfigFromXml()
        if configs is not None and len(configs) !=0:
            self.ui.ship_name_edit.setText(configs['ship_name'])
            self.ui.call_sign_edit.setText(configs['call_sign'])
            self.ui.captain_name_edit.setText(configs['captain_name'])
            cur_time = time.strftime('%Y/%m/%d',time.localtime(time.time()))
            self.ui.date_edit.setText(cur_time)
            pass
        else:
            self.logger.error('[Request Report]:' + msg, exc_info=1)

    def generateXml(self):
        root = quarterly_report()
        property = Property()
        root.Property = property

        data_dir = Utils.createDataDir()
        fn_path = abs_lambda(os.path.join(data_dir , 'request.xml'))
        with open(fn_path, 'w') as f:
            f.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
            root.export(f, 1, namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')

        msg_box = QMessageBox(QMessageBox.Information, "Success", "Revert Route config file generated successfully")
        msg_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuartelyReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass