__author__ = 'xingjieliu'

import sys
import time
import copy

from PyQt4.QtGui import QWidget,QApplication,QMessageBox,QFileDialog
from PyQt4.QtCore import QLocale,QDir,Qt

import QtUiFiles.revertRoute as revertReport
from lib.environ import *
from lib.utils import Utils
from dao.revert import *
from gui.checkboxDelegate import CheckBoxDelegate
from gui.latitudeDelegate import LatitudeDelegate
from gui.longtitudeDelegate import LongtitudeDelegate


class RevertReportWidget(QWidget):
    def __init__(self):
        super(RevertReportWidget, self).__init__()
        self.ui = revertReport.Ui_Form()
        self.ui.setupUi(self)
        self.initialize()


    def initialize(self):
        self.loadCountryPorts()
        self.viaListViewLoading()
        self.critialPointLoading()
        self.voyageDataSetting()
        self.bunkerConsumptionLoading()
        self.buttonConnect()

    def buttonConnect(self):
        self.ui.submit_btn.clicked.connect(self.generateXml)
        self.ui.submit_btn.clicked.connect(self.updateCountryPortsConfig)
        self.ui.reload_btn.clicked.connect(self.loadConfig)
        self.ui.attach_ecdis_browse_btn.clicked.connect(self.set_route_file_path)
        self.ui.attach_wp_plan_browse_btn.clicked.connect(self.set_wp_plan_path)

    def critialPointLoading(self):
        self.ui.critial_point_add_btn.clicked.connect(self.addTableItem)
        self.ui.critial_point_delete_btn.clicked.connect(self.deleteTableItem)
        self.ui.critial_point_table_widget.setItemDelegateForColumn(0, LatitudeDelegate(self))
        self.ui.critial_point_table_widget.setItemDelegateForColumn(1, LongtitudeDelegate(self))
        self.ui.critial_point_table_widget.setItemDelegateForColumn(2,CheckBoxDelegate(self))
        self.ui.critial_point_table_widget.itemDoubleClicked.connect(self.reformat)

    def viaListViewLoading(self):
        self.ui.via_add_btn.clicked.connect(self.addListItem)
        self.ui.via_remove_btn.clicked.connect(self.removeListItem)
        self.ui.via_up_btn.clicked.connect(self.upListItem)
        self.ui.via_down_btn.clicked.connect(self.downListItem)

    def reformat(self, item):
        text = item.text()
        formated = self.convertPoint(text)
        item.setText(formated)

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

    def voyageDataSetting(self):
        self.ui.total_distance_edit.editingFinished.connect(self.averageSpeedRecalculate)
        self.ui.total_distance_edit.editingFinished.connect(self.averageBunkerConsumptionRecalculate)
        self.ui.total_distance_edit.editingFinished.connect(self.voyagePerformanceEfficiencyRecalculate)
        self.ui.cargo_carried.editingFinished.connect(self.voyagePerformanceEfficiencyRecalculate)
        self.ui.total_streaming_time_edit.editingFinished.connect(self.averageSpeedRecalculate)
        self.ui.distance_me_revolution_edit.editingFinished.connect(self.averageSlipRecalculate)
        self.ui.log_distance_edit.editingFinished.connect(self.averageSlipRecalculate)

    def averageBunkerConsumptionRecalculate(self):
        self.ui.bunker_consume_table.blockSignals(True)
        total_distance = self.ui.total_distance_edit.text()
        for i in range(self.ui.bunker_consume_table.columnCount()):
            try:
                total_bunker_consume = self.ui.bunker_consume_table.item(0,i).text().toFloat()[0]
            except:
                total_bunker_consume = 0.0
            if not total_distance.isNull() and not total_distance.isEmpty() and total_distance != '0':
                result = float(total_bunker_consume)/float(total_distance)
            else:
                result = ''
            self.ui.bunker_consume_table.item(1,i).setText(str(result))
        self.ui.bunker_consume_table.blockSignals(False)

    def voyagePerformanceEfficiencyRecalculate(self):
        self.ui.bunker_consume_table.blockSignals(True)
        total_distance = self.ui.total_distance_edit.text()
        cargo_carried = self.ui.cargo_carried.text()
        for i in range(self.ui.bunker_consume_table.columnCount()):
            try:
                total_bunker_consume = self.ui.bunker_consume_table.item(0,i).text().toFloat()[0]
            except:
                total_bunker_consume = '0.0'
            if ( not total_distance.isNull() and not total_distance.isEmpty() and total_distance != '0')\
                    and ( not cargo_carried.isNull() and not cargo_carried.isEmpty() and cargo_carried != '0'):
                result = float(total_bunker_consume)/float(total_distance)/float(cargo_carried)
            else:
                result = ''
            self.ui.bunker_consume_table.item(2,i).setText(str(result))
        self.ui.bunker_consume_table.blockSignals(False)

    def averageSpeedRecalculate(self):
        total_distance = self.ui.total_distance_edit.text()
        total_streaming = self.ui.total_streaming_time_edit.text()
        if total_distance != '' and total_streaming != '':
            if total_streaming != '0':
                result = float(total_distance)/float(total_streaming)
                self.ui.average_speed_edit.setText(str(result))
            else:
                self.ui.average_speed_edit.setText('')
        else:
            self.ui.average_speed_edit.setText('')

    def averageSlipRecalculate(self):
        distance_me = self.ui.distance_me_revolution_edit.text()
        log_distance = self.ui.log_distance_edit.text()
        if distance_me != '' and log_distance != '':
            if distance_me != '0':
                distance_me = float(distance_me)
                log_distance = float(log_distance)
                result = distance_me - log_distance
                if result < 0:
                    result = 0
                result = float(result)/float(distance_me)
                self.ui.average_slip_edit.setText(str(result))
            else:
                self.ui.average_slip_edit.setText('')
        else:
            self.ui.average_slip_edit.setText('')

    def bunkerConsumptionLoading(self):
        self.ui.bunker_consume_table.cellChanged.connect(self.bunkerConsumeRecalculate)

    def bunkerConsumeRecalculate(self, i,j):
        self.ui.bunker_consume_table.blockSignals(True)
        value = self.ui.bunker_consume_table.item(i,j).text()
        column = j
        total_distance = self.ui.total_distance_edit.text()
        cargo_carried = self.ui.cargo_carried.text()
        distance_valid = True
        cargo_valid = True
        if total_distance == '' or total_distance == '0':
            distance_valid = False
        if cargo_carried == '' or cargo_carried == '0':
            cargo_valid = False


        if distance_valid:
            if value !='':
                average_bunker_consume = float(value)/float(total_distance)
                self.ui.bunker_consume_table.item(1,column).setText(str(average_bunker_consume))
            else:
                self.ui.bunker_consume_table.item(1,column).setText('0')
        else:
            self.ui.bunker_consume_table.item(1,column).setToolTip('Total Distance Over Ground should not be empty or 0')
            self.ui.bunker_consume_table.item(1,column).setText('N/A')


        if cargo_valid and distance_valid:
            if value !='':
                average_bunker_consume = float(value)/float(total_distance)
                voyage_performance = average_bunker_consume/float(cargo_carried)
                self.ui.bunker_consume_table.item(2,column).setText(str(voyage_performance))
            else:
                self.ui.bunker_consume_table.item(2,column).setText('0')
        else:
            self.ui.bunker_consume_table.item(2,column).setToolTip('Total Distance Over Ground or Cargo Carried should not be empty or 0')
            self.ui.bunker_consume_table.item(2,column).setText('N/A')

        self.ui.bunker_consume_table.blockSignals(False)

    def addTableItem(self):
        count = self.ui.critial_point_table_widget.rowCount()
        self.ui.critial_point_table_widget.insertRow(count)

    def deleteTableItem(self):
        row = self.ui.critial_point_table_widget.currentRow()
        self.ui.critial_point_table_widget.removeRow(row)


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
                # self.ui.departure_port_combo.clear()
                # self.ui.departure_port_combo.addItems(self.country_ports[country_name])
                # self.ui.departure_port_combo.setEditText(QString(port_name))
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
                    #REFRESH arrival country list
                    keys = self.country_ports.keys()
                    keys.sort()
                    self.ui.arrival_country_combo.clear()
                    self.ui.arrival_country_combo.addItems(keys)
                else:
                    keys = self.country_ports.keys()
                    keys.sort()
                    self.ui.departure_country_combo.clear()
                    self.ui.departure_country_combo.addItems(keys)
        else:
            ports = self.country_ports[country_name]
            ports.sort()
            self.ui.departure_port_combo.addItems(ports)


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
                    #REFRESH departure country list
                    keys = self.country_ports.keys()
                    keys.sort()
                    self.ui.departure_country_combo.clear()
                    self.ui.departure_country_combo.addItems(keys)
                else:
                    keys = self.country_ports.keys()
                    keys.sort()
                    self.ui.arrival_country_combo.clear()
                    self.ui.arrival_country_combo.addItems(keys)
        else:
            ports = self.country_ports[country_name]
            ports.sort()
            self.ui.arrival_port_combo.addItems(ports)

    def convertPoint(self, text):
        formated = ''
        if not text.isEmpty() and not text.isNull():
            if Utils.checkState(text, Utils.FORMAT_PATTERN):
                orient = text[-1]
                formated = text.replace('-','')[:-2]
                if orient == 'S' or orient == 'W':
                    formated.push_front('-')
        return formated


    def generateXml(self):
        root = revert_report()
        property = Property()

        #general data
        property.ship_name = self.ui.ship_name_edit.text()
        property.call_sign = self.ui.call_sign_edit.text()
        property.voyage_number = self.ui.voyage_number_edit.text()
        property.captain_name = self.ui.captain_name_edit.text()
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

        #paper tab
        property.use_critial_point = self.ui.critial_yes_radio.isChecked()
        property.use_dw_route = self.ui.use_dw_route_yes_radio.isChecked()
        property.route_number = self.ui.received_route_number.text()
        property.modify_route = self.ui.modify_route_radio_yes.isChecked()
        property.modify_reason = self.ui.reason_modify_route_combo.currentText()

        #critial point
        points=[]
        row_count = self.ui.critial_point_table_widget.rowCount()
        for i in range(row_count):
            point_item = point()
            try:
                lat = self.ui.critial_point_table_widget.item(i,0).text()
                long = self.ui.critial_point_table_widget.item(i,1).text()
                point_item.latitude = str(self.convertPoint(lat))
                point_item.longtitude = str(self.convertPoint(long))

                include_flag = self.ui.critial_point_table_widget.item(i,2).text()
                if include_flag == 'Yes':
                    points.append(point_item)
            except AttributeError:
                pass

        cp = critial_point()
        cp.point = points
        property.critial_point = cp

        #add via place
        via_places=[]
        vias = via()
        list_item_count = self.ui.via_listWidget.count()
        for index in range(list_item_count):
            via_places.append(self.ui.via_listWidget.item(index).text())

        vias.place_name = via_places
        property.via = vias

        property.route_number = self.ui.received_route_number.text()
        property.route_type = self.ui.route_type_combo.currentText()
        property.modify_route = self.ui.modify_route_radio_yes.isChecked()
        property.modify_reason = self.ui.reason_modify_route_combo.currentText()

        #paper chart
        chart = paper_chart()
        chart_items=[]
        for i in range(self.ui.paper_chart_table_widget.rowCount()):
            for j in range(self.ui.paper_chart_table_widget.columnCount()):
                try:
                    chart_items.append(self.ui.paper_chart_table_widget.item(i,j).text())
                except:
                    pass
        property.paper_chart = chart

        voyage_dat = voyage_data()
        voyage_dat.maximum_draft = self.ui.maximum_draft_edit.text()
        voyage_dat.minimum_ukc = self.ui.minimum_ukc_edit.text()
        voyage_dat.load_condition = self.ui.load_condition_combo.currentText()
        voyage_dat.displacement = self.ui.displacement_edit.text()
        voyage_dat.cargo_carried = self.ui.cargo_carried.text()
        voyage_dat.average_me_rmp = self.ui.average_me_rmp_edit.text()
        voyage_dat.total_distance = self.ui.total_distance_edit.text()
        voyage_dat.total_streaming_time = self.ui.total_streaming_time_edit.text()
        voyage_dat.average_speed = self.ui.average_speed_edit.text()
        voyage_dat.me_revolution_distance = self.ui.distance_me_revolution_edit.text()
        voyage_dat.log_distance = self.ui.log_distance_edit.text()
        voyage_dat.average_slip = self.ui.average_slip_edit.text()
        property.voyage_data = voyage_dat

        tbc = total_bunker_consumption()
        abc = average_bunker_consumption_per_nm()
        vpe = voyage_performance_efficiency()
        consume_list = [tbc, abc, vpe]
        for i in range(len(consume_list)):
            for j in range(self.ui.bunker_consume_table.columnCount()):
                column_name = self.ui.bunker_consume_table.horizontalHeaderItem(j).text().toLower()
                if hasattr(consume_list[i], str(column_name)):
                    try:
                        setattr(consume_list[i], str(column_name), self.ui.bunker_consume_table.item(i,j).text())
                    except AttributeError:
                        setattr(consume_list[i], str(column_name), '')

        property.total_bunker_consumption = tbc
        property.average_bunker_consumption_per_nm = abc
        property.voyage_performance_efficiency = vpe

        property.overall_weather_condition = self.ui.overall_condition_combo.currentText()
        property.attach_ecdis_route_file = os.path.basename(str(self.ui.attach_ecdis_route_file_edit.text()))
        property.attach_wp_plan = os.path.basename(str(self.ui.attach_wp_plan_edit.text()))
        property.remark = self.ui.remark_edit.toPlainText()

        root.Property = property
        data_dir = Utils.createDataDir()
        fn_path = abs_lambda(os.path.join(data_dir , 'revert.xml'))
        with open(fn_path, 'w') as f:
            f.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
            root.export(f, 1, namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')

        msg_box = QMessageBox(QMessageBox.Information, "Success", "Revert Route config file generated successfully")
        msg_box.exec_()

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

    def loadConfig(self):
        configs, msg = Utils.readGeneralConfigFromXml()
        if configs is not None and len(configs) !=0:
            self.ui.ship_name_edit.setText(configs['ship_name'])
            self.ui.call_sign_edit.setText(configs['call_sign'])
            self.ui.captain_name_edit.setText(configs['captain_name'])
            cur_time = time.strftime('%Y/%m/%d',time.localtime(time.time()))
            self.ui.date_edit.setText(cur_time)
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", msg)
            msg_box.exec_()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RevertReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass