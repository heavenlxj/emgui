__author__ = 'xingjieliu'

import sys
sys.path.append('../..')
import QtUiFiles.shareRoute as shareReport
from PyQt4.QtGui import *
from lib.utils import Utils
from dao.share import *


class ShareReportWidget(QWidget):
    def __init__(self):
        super(ShareReportWidget, self).__init__()
        self.ui = shareReport.Ui_Form()
        self.ui.setupUi(self)

    def initialize(self):
        pass

    def loadCountryPorts(self):
        self.country_ports = Utils.getCountryPortsMapper()
        if self.country_ports is not None and len(self.country_ports) !=0:
            keys = self.country_ports.keys()
            keys.sort()
            self.ui.departure_country_combo.addItems(keys)
            self.ui.arrival_country_combo.addItems(keys)
            self.ui.departure_country_combo.setEditable(True)
            self.ui.departure_port_combo.setEditable(True)
            self.ui.arrival_country_combo.setEditable(True)
            self.ui.arrival_port_combo.setEditable(True)
            self.ui.departure_country_combo.activated.connect(self.activateDeparturePorts)
            self.ui.arrival_country_combo.activated.connect(self.activateArrvialPorts)
        else:
            #TODO ADD prompt dialog
            msg_box = QMessageBox(QMessageBox.Critical, "Error", "Load Country/Ports from config file failed when start Share Route Dialog")
            msg_box.exec_()
            sys.exit(-1)

    def activateDeparturePorts(self, country_index):
        country_name = self.ui.departure_country_combo.itemText(country_index)
        country_name = unicode(country_name)
        self.ui.departure_port_combo.addItems(self.country_ports[country_name])

    def activateArrvialPorts(self, country_index):
        country_name = self.ui.arrival_country_combo.itemText(country_index)
        country_name = unicode(country_name)
        self.ui.arrival_port_combo.addItems(self.country_ports[country_name])


    def generateXml(self):
        root = share_report()
        property = Property()

        root.Property = property
        f= open(r'd:\test.xml', 'w')
        f.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
        root.export(f, 1, namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
        print 'generate xml successfully'


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShareReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass