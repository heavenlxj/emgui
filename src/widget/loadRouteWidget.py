__author__ = 'xingjieliu'

import sys

from PyQt4.QtGui import QWidget,QApplication,QMessageBox, QFileDialog
from PyQt4.QtCore import QDir,Qt

import QtUiFiles.loadRoute as loadRoute
from lib.environ import *
from lib.utils import Utils
from dao.load import parse


class LoadRouteWidget(QWidget):
    def __init__(self):
        super(LoadRouteWidget, self).__init__()
        self.ui = loadRoute.Ui_Form()
        self.ui.setupUi(self)
        self.initialize()

    def initialize(self):
        #self.loadCountryPorts()
        self.setViaListView()
        self.buttonConnect()


    def buttonConnect(self):
        #self.ui.submit_btn.clicked.connect(self.generateXml)
        #self.ui.submit_btn.clicked.connect(self.updateCountryPortsConfig)
        self.ui.load_btn.clicked.connect(self.readConfigFromXML)
        self.ui.browse_btn.clicked.connect(self.browse_config_file)
        self.ui.attach_ecdis_browse_btn.clicked.connect(self.set_route_file_path)
        self.ui.attach_wp_plan_browse_btn.clicked.connect(self.set_wp_plan_path)


    def setViaListView(self):
        self.ui.via_add_btn.clicked.connect(self.addListItem)
        self.ui.via_remove_btn.clicked.connect(self.removeListItem)
        self.ui.via_up_btn.clicked.connect(self.upListItem)
        self.ui.via_down_btn.clicked.connect(self.downListItem)

    def addListItem(self):
        via_name = self.ui.via_name_edit.text()
        if via_name!='':
            item = self.ui.via_listWidget.findItems(via_name,  Qt.MatchExactly|Qt.MatchRecursive)
            if len(item) !=0:
                #find duplicated item
                msg_box = QMessageBox(QMessageBox.Information, "Info", "%s has already added in the list" % via_name)
                msg_box.exec_()
            else:
                self.ui.via_listWidget.addItem(via_name)
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", 'Empty port name in the blank')
            msg_box.exec_()

    def removeListItem(self):
        selected_item = self.ui.via_listWidget.selectedItems()
        if len(selected_item) !=0:
            if QMessageBox.warning(self, 'Confirm', 'Do you want to delete the selected item?', QMessageBox.Yes | QMessageBox.Cancel) == QMessageBox.Yes:
                for i in selected_item:
                    row = self.ui.via_listWidget.row(i)
                    item = self.ui.via_listWidget.takeItem(row)
                    self.ui.via_listWidget.removeItemWidget(item)
        else:
            QMessageBox.information(self, 'Infomation', 'No item selected, nothing removed', QMessageBox.Ok)

    def upListItem(self):
        index = self.ui.via_listWidget.currentRow()
        if index >0:
            index_new = index-1
            self.ui.via_listWidget.insertItem(index_new, self.ui.via_listWidget.takeItem(self.ui.via_listWidget.currentRow()))
            self.ui.via_listWidget.setCurrentRow(index_new)

    def downListItem(self):
        index = self.ui.via_listWidget.currentRow()
        if index < self.ui.via_listWidget.count():
            index_new = index+1
            self.ui.via_listWidget.insertItem(index_new, self.ui.via_listWidget.takeItem(self.ui.via_listWidget.currentRow()))
            self.ui.via_listWidget.setCurrentRow(index_new)

    def loadCountryPorts(self):
        self.country_ports = Utils.getCountryPortsMapper()
        if self.country_ports is not None and len(self.country_ports) !=0:
            keys = self.country_ports.keys()
            keys.sort()
            self.ui.departure_country_combo.addItems(keys)
            self.ui.arrival_country_combo.addItems(keys)
            self.ui.departure_country_combo.currentIndexChanged.connect(self.activateDeparturePorts)
            self.ui.arrival_country_combo.currentIndexChanged.connect(self.activateArrvialPorts)
        else:
            #TODO ADD prompt dialog
            msg_box = QMessageBox(QMessageBox.Critical, "Error", "Load Country/Ports from config file failed when start Load Route Dialog")
            msg_box.exec_()
            sys.exit(-1)

    def activateDeparturePorts(self, country_index):
        country_name = self.ui.departure_country_combo.itemText(country_index)
        country_name = unicode(country_name)
        self.ui.departure_port_combo.clear()
        self.ui.departure_port_combo.addItems(self.country_ports[country_name])

    def activateArrvialPorts(self, country_index):
        country_name = self.ui.arrival_country_combo.itemText(country_index)
        country_name = unicode(country_name)
        self.ui.arrival_port_combo.clear()
        self.ui.arrival_port_combo.addItems(self.country_ports[country_name])


    # def generateXml(self):
    #     root = load_report()
    #     property = Property()
    #     root.Property = property
    #
    #
    #     data_dir = Utils.createDataDir()
    #     fn_path = abs_lambda(os.path.join(data_dir , 'load.xml'))
    #     with open(fn_path, 'w') as f:
    #         f.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
    #         root.export(f, 1, namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
    #     msg_box = QMessageBox(QMessageBox.Information, "Success", "Load Route config file generated successfully")
    #     msg_box.exec_()

    def set_route_file_path(self):
        fn = QFileDialog.getOpenFileName(self, "Open Files",
                DATA_PATH, ".xml(*.xml)")
        if fn:
            abs_fn = os.path.abspath(fn)
            self.ui.attach_ecdis_route_file_edit.setText(abs_fn)

    def set_wp_plan_path(self):
        fn = QFileDialog.getOpenFileName(self, "Open Files",
                DATA_PATH, ".xml(*.xml)")
        if fn:
            abs_fn = os.path.abspath(fn)
            self.ui.attach_wp_plan_edit.setText(abs_fn)

    def browse_config_file(self):
        fn = QFileDialog.getOpenFileName(self, "Open Files",
                DATA_PATH, ".xml(*.xml)")
        if fn:
            abs_fn = os.path.abspath(fn)
            self.ui.load_route_path_edit.setText(abs_fn)

    def readConfigFromXML(self):
        fn = self.ui.load_route_path_edit.text()
        if not os.path.exists(fn) or fn.isEmpty() or fn.isNull():
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", 'Empty file name or the file path is invalid')
            msg_box.exec_()
            return False
        else:
            fh = open(fn)
            parsed_file = parse(fh)
            pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadRouteWidget()
    window.show()
    sys.exit(app.exec_())
    pass