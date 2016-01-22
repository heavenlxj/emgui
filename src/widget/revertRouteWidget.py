__author__ = 'xingjieliu'

import sys
import os
sys.path.append('../..')
import QtUiFiles.revertRoute as revertReport
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from lib.utils import Utils
from dao.revert import *
from gui.checkDelegate import CheckBoxDelegate


class RevertReportWidget(QWidget):
    def __init__(self):
        super(RevertReportWidget, self).__init__()
        self.ui = revertReport.Ui_Form()
        self.ui.setupUi(self)
        self.initialize()


    def initialize(self):
        self.new_add_country_ports={}
        self.ui.attach_ecdis_browse_btn.clicked.connect(self.set_route_file_path)
        self.ui.attach_wp_plan_browse_btn.clicked.connect(self.set_wp_plan_path)

        self.ui.via_add_btn.clicked.connect(self.addListItem)
        self.ui.via_remove_btn.clicked.connect(self.removeListItem)

        self.loadCountryPorts()

        self.ui.submit_btn.clicked.connect(self.generateXml)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.reload_btn.clicked.connect(self.loadConfig)
        self.ui.critial_point_table_widget.setItemDelegate(CheckBoxDelegate())



    def set_calendar(self):
        self.depart_calendar = self.ui.depart_date_edit.text()

    def loadCountryPorts(self):
        self.country_ports = Utils.getCountryPortsMapper()
        if self.country_ports is not None and len(self.country_ports) !=0:
            keys = self.country_ports.keys()
            keys.sort()
            self.ui.departure_country_combo.addItems(keys)
            self.ui.arrival_country_combo.addItems(keys)
            self.ui.departure_country_combo.activated.connect(self.activateDeparturePorts)
            self.ui.arrival_country_combo.activated.connect(self.activateArrvialPorts)
            self.ui.departure_port_combo.activated.connect(self.updateDeparturePorts)
            self.ui.arrival_port_combo.activated.connect(self.updateArrivalPorts)

            departure_calendar = self.ui.depart_date_edit.calendarWidget()
            arrival_calendar = self.ui.arrival_date_edit.calendarWidget()
            departure_calendar.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
            arrival_calendar.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        else:
            msg_box = QMessageBox(QMessageBox.Critical, "Error", "Load Country/Ports from config file failed when start Share Route Dialog")
            msg_box.exec_()

    def updateDeparturePorts(self):
        country_name = unicode(self.ui.departure_country_combo.currentText())
        port_name = unicode(self.ui.departure_port_combo.currentText())
        exist_ports = self.country_ports[country_name]
        if port_name not in exist_ports:
            msg='Found %s not in the departure port list, do you want to add this new port in the list, click Yes if confirmed or ignore this by clicking No' % port_name
            reply = QMessageBox.question(self, "QMessageBox.question()",
                    msg,
                    QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.country_ports[country_name].append(port_name)
                self.ui.departure_port_combo.clear()
                self.ui.departure_port_combo.addItems(self.country_ports[country_name])
                self.ui.departure_port_combo.setEditText(QString(port_name))
            else:
                self.ui.departure_port_combo.clear()
                self.ui.departure_port_combo.addItems(self.country_ports[country_name])

    def updateArrivalPorts(self):
        country_name = unicode(self.ui.arrival_country_combo.currentText())
        port_name = unicode(self.ui.arrival_port_combo.currentText())
        exist_ports = self.country_ports[country_name]
        if port_name not in exist_ports:
            msg='Found %s not in the arrival port list, do you want to add this new port in the list, click Yes if confirmed or ignore this by clicking No' % port_name
            reply = QMessageBox.question(self, "QMessageBox.question()",
                    msg,
                    QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.country_ports[country_name].append(port_name)
                self.ui.arrival_port_combo.clear()
                self.ui.arrival_port_combo.addItems(self.country_ports[country_name])
                self.ui.arrival_port_combo.setEditText(QString(port_name))
            else:
                self.ui.arrival_port_combo.clear()
                self.ui.arrival_port_combo.addItems(self.country_ports[country_name])

    def activateDeparturePorts(self):
        country_name = self.ui.departure_country_combo.currentText()
        country_name = unicode(country_name)
        self.ui.departure_port_combo.clear()
        if not self.country_ports.has_key(country_name):
                msg='Found %s not in the departure country list, do you want to add this new country in the list, click Yes if confirmed or ignore this by clicking No' % country_name
                reply = QMessageBox.question(self, "QMessageBox.question()",
                        msg,
                        QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.country_ports[country_name] = []
                else:
                    keys = self.country_ports.keys()
                    keys.sort()
                    self.ui.departure_country_combo.clear()
                    self.ui.departure_country_combo.addItems(keys)
        else:
            self.ui.departure_port_combo.addItems(self.country_ports[country_name])


    def activateArrvialPorts(self):
        country_name = self.ui.arrival_country_combo.currentText()
        country_name = unicode(country_name)
        self.ui.arrival_port_combo.clear()
        if not self.country_ports.has_key(country_name):
                msg='Found %s not in the arrival country list, do you want to add this new country in the list, click Yes if confirmed or ignore this by clicking No' % country_name
                reply = QMessageBox.question(self, "QMessageBox.question()",
                        msg,
                        QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.country_ports[country_name] = []
                else:
                    keys = self.country_ports.keys()
                    keys.sort()
                    self.ui.arrival_country_combo.clear()
                    self.ui.arrival_country_combo.addItems(keys)
        else:
            self.ui.arrival_port_combo.addItems(self.country_ports[country_name])


    def generateXml(self):
        root = revert_report()
        property = Property()

        #general data
        property.ship_name = self.ui.ship_name_edit.text()
        property.call_sign = self.ui.ship_name_edit.text()
        property.voyage_number = self.ui.voyage_number_edit.text()
        property.captain_name = self.ui.captain_name_edit.text()
        property.date = self.ui.dateEdit.text()
        #voyage data departure
        property.voyage_detail.departure.departure_date = self.ui.depart_date_edit.text()
        property.voyage_detail.departure.departure_time = self.ui.departure_time_edit.text()
        property.voyage_detail.departure.country = self.ui.departure_country_combo.currentText()
        property.voyage_detail.departure.port = self.ui.departure_port_combo.currentText()
        property.voyage_detail.departure.unlo_code = self.ui.depature_unlo_code.text()
        property.voyage_detail.departure.terminal = self.ui.departure_terminal.text()
        #voyage data arrival
        property.voyage_detail.arrival.arrival_date = self.ui.arrival_date_edit.text()
        property.voyage_detail.arrival.arrival_time = self.ui.arrival_time_edit.text()
        property.voyage_detail.arrival.country = self.ui.arrival_country_combo.currentText()
        property.voyage_detail.arrival.port = self.ui.arrival_port_combo.currentText()
        property.voyage_detail.arrival.unlo_code = self.ui.arrival_unlo_code.text()
        property.voyage_detail.arrival.terminal = self.ui.arrival_terminal.text()

        #paper tab
        property.use_critial_point = self.ui.critial_yes_radio.isChecked()
        property.use_dw_route = self.ui.use_dw_route_yes_radio.isChecked()
        property.route_number = self.ui.received_route_number.text()
        property.modify_route = self.ui.modify_route_radio_yes.isChecked()
        property.modify_reason = self.ui.reason_modify_route_combo.currentText()

        #critial point
        points=[]
        row_count = self.ui.critial_point_table_widget.rowCount()
        vertical_count = self.ui.critial_point_table_widget.columnCount()
        for i in row_count:
            point_item = point()
            lat = self.ui.critial_point_table_widget.item(i,0).text()
            long = self.ui.critial_point_table_widget.item(i,1).text()


        #via place


        #TODO Paper chart

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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RevertReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass