__author__ = 'xingjieliu'

import sys
import time

from PyQt4.QtGui import QWidget,QApplication,QMessageBox
from PyQt4.QtCore import QLocale,Qt

import QtUiFiles.requestRoute as reqReport
from dao.request import *
from lib.environ import *
from lib.utils import Utils
import copy


class ReqReportWidget(QWidget):
    def __init__(self):
        super(ReqReportWidget, self).__init__()
        self.ui = reqReport.Ui_Form()
        self.ui.setupUi(self)
        self.initialize()

    def initialize(self):
        self.loadCountryPorts()
        self.viaListViewLoading()
        self.buttonConnect()

    def viaListViewLoading(self):
        self.ui.via_add_btn.clicked.connect(self.addListItem)
        self.ui.via_remove_btn.clicked.connect(self.removeListItem)
        self.ui.via_up_btn.clicked.connect(self.upListItem)
        self.ui.via_down_btn.clicked.connect(self.downListItem)

    def buttonConnect(self):
        self.ui.submit_btn.clicked.connect(self.generateXml)
        self.ui.submit_btn.clicked.connect(self.updateCountryPortsConfig)
        self.ui.reload_btn.clicked.connect(self.loadConfig)

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

    def updateCountryPortsConfig(self):
        #get origin config
        update_dict = {}
        origin_config = Utils.getCountryPortsMapper()
        for k,v in self.country_ports.iteritems():
            if k not in origin_config.keys():
                update_dict[k]= v
            else:
                temp=[]
                for port in v:
                    if port not in origin_config[k]:
                        temp.append(port)
                if len(temp) !=0:
                    cp = copy.copy(temp)
                    update_dict[k]= cp

        #append the updated country port in the config file
        try:
            file_path = os.path.join(CONF_PATH, 'country_port.csv')
            fp = open(file_path, 'a+')
        except IOError, ex:
            #TODO open error prompt dialog
            return None

        lines = []
        for k,v in update_dict.iteritems():
            for port in v:
                content = port+','+k+'\n'
                lines.append(content)
        fp.writelines(lines)
        fp.close()

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


    def generateXml(self):
        root = request_report()
        property = Property()
        root.Property = property

        #general data
        property.ship_name = self.ui.ship_name_edit.text()
        property.call_sign = self.ui.call_sign_edit.text()
        property.voyage_number = self.ui.voyage_number_edit.text()
        property.date = self.ui.date_edit.text()
        #voyage data departure
        voyage_det = voyage_detail()
        depart = departure()
        arr = arrival()
        depart.departure_date = self.ui.depart_date_edit.text()
        depart.departure_time = self.ui.departure_time_edit.text()
        depart.country = self.ui.departure_country_combo.currentText()
        depart.port = self.ui.departure_port_combo.currentText()
        depart.unlo_code = self.ui.departure_unlo_edit.text()
        depart.terminal = self.ui.departure_terminal_edit.text()
        #voyage data arrival
        arr.arrival_date = self.ui.arrival_date_edit.text()
        arr.arrival_time = self.ui.arrival_time_edit.text()
        arr.country = self.ui.arrival_country_combo.currentText()
        arr.port = self.ui.arrival_port_combo.currentText()
        arr.unlo_code = self.ui.arrival_unlo_edit.text()
        arr.terminal = self.ui.arrival_terminal_edit.text()

        voyage_det.departure=depart
        voyage_det.arrival = arr
        property.voyage_detail = voyage_det

        #add via place
        via_places=[]
        vias = via()
        list_item_count = self.ui.via_listWidget.count()
        for index in range(list_item_count):
            via_places.append(self.ui.via_listWidget.item(index).text())

        vias.place_name = via_places
        property.via = vias

        property.use_dw_route = self.ui.use_dw_route_yes_radio.isChecked()
        property.prefered_route_type = self.ui.prefer_route_type_combo.currentText()
        property.maximum_draft = self.ui.maximum_draft_edit.text()
        property.load_condition = self.ui.load_condition_edit.text()
        property.speed_setting = self.ui.speed_setting_edit.text()
        property.etd = self.ui.etd_edit.text()

        data_dir = Utils.createDataDir()
        fn_path = abs_lambda(os.path.join(data_dir , 'request.xml'))
        with open(fn_path, 'w') as f:
            f.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
            root.export(f, 1, namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')

        msg_box = QMessageBox(QMessageBox.Information, "Success", "Revert Route config file generated successfully")
        msg_box.exec_()


    def loadConfig(self):
        configs, msg = Utils.readGeneralConfigFromXml()
        if configs is not None and len(configs) !=0:
            self.ui.ship_name_edit.setText(configs['ship_name'])
            self.ui.call_sign_edit.setText(configs['call_sign'])
            cur_time = time.strftime('%Y/%m/%d',time.localtime(time.time()))
            self.ui.date_edit.setText(cur_time)
            pass
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", msg)
            msg_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReqReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass