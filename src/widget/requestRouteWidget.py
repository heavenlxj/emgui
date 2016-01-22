__author__ = 'xingjieliu'

import sys
sys.path.append('../..')

import QtUiFiles.requestRoute as reqReport
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from dao.request import *
from lib.utils import Utils
import time

class ReqReportWidget(QWidget):
    def __init__(self):
        super(ReqReportWidget, self).__init__()
        self.ui = reqReport.Ui_Form()
        self.ui.setupUi(self)
        self.initialize()

    def initialize(self):
        self.loadCountryPorts()
        self.ui.submit_btn.clicked.connect(self.generateXml)
        self.ui.cancel_btn.clicked.connect(self.close)
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
        root = request_report()
        property = Property()
        root.Property = property
        f= open(r'd:\test.xml', 'w')
        f.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
        root.export(f, 1, namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
        print 'generate xml successfully'

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