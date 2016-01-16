__author__ = 'xingjieliu'

import sys
sys.path.append('../..')

import QtUiFiles.loadRoute as loadRoute
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from conf.environ import *
from lib.utils import Utils
from dao.load import *


class LoadRouteWidget(QWidget):
    def __init__(self):
        super(LoadRouteWidget, self).__init__()
        self.ui = loadRoute.Ui_Form()
        self.ui.setupUi(self)
        self.initialize()

    def initialize(self):
        self.loadCountryPorts()
        self.setViaListView()

        self.ui.attach_ecdis_browse_btn.clicked.connect(self.set_route_file_path)
        self.ui.attach_wp_plan_browse_btn.clicked.connect(self.set_wp_plan_path)

    def setViaListView(self):
        self.ui.via_add_btn.clicked.connect(self.addListItem)
        self.ui.via_remove_btn.clicked.connect(self.removeListItem)

    def addListItem(self):
        via_name = self.ui.via_name_edit.text()
        if via_name!='':
            self.ui.via_listWidget.addItem(via_name)
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", 'Empty port name in the blank')
            msg_box.exec_()

    def removeListItem(self):
        selected_item = self.ui.via_listWidget.selectedItems()

        if len(selected_item) !=0:
            for item in selected_item:
                print item
        else:
            print 'No Item selected'

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
            msg_box = QMessageBox(QMessageBox.Critical, "Error", "Load Country/Ports from config file failed when start Load Route Dialog")
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
        root = load_report()
        property = Property()
        root.Property = property
        f= open(r'd:\test.xml', 'w')
        f.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
        root.export(f, 1, namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
        print 'generate xml successfully'

    def set_route_file_path(self):
        fn = QFileDialog.getOpenFileName(self, "Open Files",
                QDir.currentPath(), ".xml(*.xml)")
        abs_fn = os.path.abspath(fn)
        self.ui.attach_ecdis_route_file_edit.setText(abs_fn)

    def set_wp_plan_path(self):
        fn = QFileDialog.getOpenFileName(self, "Open Files",
                QDir.currentPath(), ".xml(*.xml)")
        abs_fn = os.path.abspath(fn)
        self.ui.attach_wp_plan_edit.setText(abs_fn)

    def readConfigFromXML(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadRouteWidget()
    window.show()
    sys.exit(app.exec_())
    pass