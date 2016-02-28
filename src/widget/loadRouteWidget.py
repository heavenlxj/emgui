__author__ = 'xingjieliu'

import sys

from PyQt4.QtGui import QWidget,QApplication,QMessageBox, QFileDialog,QTableWidgetItem
from PyQt4.QtCore import Qt,QDate,QTime,QString

import QtUiFiles.loadRoute as loadRoute
from gui.latitudeDelegate import LatitudeDelegate
from gui.longtitudeDelegate import LongtitudeDelegate
from lib.environ import *
from lib.utils import Utils,PointType
from dao.load import parse
import logging

class LoadRouteWidget(QWidget):
    def __init__(self):
        super(LoadRouteWidget, self).__init__()
        self.ui = loadRoute.Ui_Form()
        self.ui.setupUi(self)
        self.logger = logging.getLogger('emgui')
        self.initialize()

    def initialize(self):
        #self.loadCountryPorts()
        self.setViaListView()
        self.buttonConnect()
        self.critialPointLoading()


    def buttonConnect(self):

        self.ui.load_btn.clicked.connect(self.readConfigFromXML)
        self.ui.browse_btn.clicked.connect(self.browse_config_file)

    def critialPointLoading(self):
        self.ui.critial_point_add_btn.clicked.connect(self.addTableItem)
        self.ui.critial_point_delete_btn.clicked.connect(self.deleteTableItem)
        self.ui.critial_point_table_widget.setItemDelegateForColumn(0, LatitudeDelegate(self))
        self.ui.critial_point_table_widget.setItemDelegateForColumn(1, LongtitudeDelegate(self))
        self.ui.critial_point_table_widget.itemDoubleClicked.connect(self.reformat)

    def reformat(self, item):
        text = item.text()
        formated = self.convertPoint(text)
        item.setText(formated)

    def convertPoint(self, text):
        formated = ''
        if not text.isEmpty() and not text.isNull():
            if Utils.checkState(text, Utils.FORMAT_PATTERN):
                orient = text[-1]
                formated = text.replace('-','')[:-2]
                if orient == 'S' or orient == 'W':
                    formated.push_front('-')
        return formated

    def addTableItem(self):
        count = self.ui.critial_point_table_widget.rowCount()
        self.ui.critial_point_table_widget.insertRow(count)

    def deleteTableItem(self):
        row = self.ui.critial_point_table_widget.currentRow()
        self.ui.critial_point_table_widget.removeRow(row)


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
            try:
                fh = open(fn)
                parsed_file = parse(fh, silence=True)

                property = parsed_file.Property
                self.ui.depart_date_edit.setDate(QDate.fromString(property.voyage_detail.departure.departure_date, 'yyyy/MM/dd'))
                self.ui.departure_time_edit.setTime(QTime.fromString(property.voyage_detail.departure.departure_time, 'hh:mm:ss'))
                self.ui.departure_unlo_edit.setText(property.voyage_detail.departure.unlo_code)
                self.ui.depature_terminal.setText(property.voyage_detail.departure.terminal)
                self.ui.departure_country_combo.setEditText(property.voyage_detail.departure.country)
                self.ui.departure_port_combo.setEditText(property.voyage_detail.departure.port)

                self.ui.arrival_date_edit.setDate(QDate.fromString(property.voyage_detail.arrival.arrival_date,'yyyy/MM/dd'))
                self.ui.arrival_time_edit.setTime(QTime.fromString(property.voyage_detail.arrival.arrival_time,'hh:mm:ss'))
                self.ui.arrival_unlo_edit.setText(property.voyage_detail.arrival.unlo_code)
                self.ui.arrival_terminal.setText(property.voyage_detail.arrival.terminal)
                self.ui.arrival_country_combo.setEditText(property.voyage_detail.arrival.country)
                self.ui.arrival_port_combo.setEditText(property.voyage_detail.arrival.port)

                if property.use_dw_route:
                    self.ui.use_dw_route_yes_radio.setChecked(True)
                else:
                    self.ui.use_dw_route_no_radio.setChecked(True)

                if property.use_critial_point:
                    self.ui.critial_yes_radio.setChecked(True)
                else:
                    self.ui.critial_no_radio.setChecked(True)

                for index,point in enumerate(property.critial_point.point):
                    try:
                        formated_latitude = Utils.formatPoint(QString(point.latitude), PointType.LATITUDE)
                        latitude = QTableWidgetItem(formated_latitude)
                        latitude.setTextAlignment(Qt.AlignCenter)
                        self.ui.critial_point_table_widget.setItem(index,0, latitude)
                        formated_longtitude = Utils.formatPoint(QString(point.longtitude), PointType.LONGTITUDE)
                        longtitude = QTableWidgetItem(formated_longtitude)
                        longtitude.setTextAlignment(Qt.AlignCenter)
                        self.ui.critial_point_table_widget.setItem(index,1,longtitude)
                    except Exception,ex:
                        self.logger.error(ex, exc_info=1)


                self.ui.via_listWidget.addItems(property.via.place_name)
                self.ui.route_id_number_label.setText(property.route_number)
                self.ui.used_times_label.setText(property.used_times)

                row_count = self.ui.paper_chart_table_widget.rowCount()
                column_count = self.ui.paper_chart_table_widget.columnCount()
                chart_ids = property.paper_chart.chart_id
                if len(chart_ids) > row_count*column_count:
                    #add new row for the paper chart table
                    self.ui.paper_chart_table_widget.insertRow(row_count)

                for index,chart_id in enumerate(property.paper_chart.chart_id):
                    row = index/column_count
                    column = index%column_count
                    chart_item = QTableWidgetItem(chart_id)
                    self.ui.paper_chart_table_widget.setItem(row,column, chart_item)

                self.ui.maximum_draft_edit.setText(property.voyage_data.maximum_draft)
                self.ui.minimum_ukc_edit.setText(property.voyage_data.minimum_ukc)
                load_index = self.ui.load_condition_combo.findText(property.voyage_data.load_condition)
                self.ui.load_condition_combo.setCurrentIndex(load_index)
                self.ui.displacement_edit.setText(property.voyage_data.displacement)
                self.ui.cargo_carried.setText(property.voyage_data.cargo_carried)
                self.ui.average_me_rmp_edit.setText(property.voyage_data.average_me_rmp)
                self.ui.total_distance_edit.setText(property.voyage_data.total_distance)
                self.ui.total_streaming_time_edit.setText(property.voyage_data.total_streaming_time)
                self.ui.average_speed_edit.setText(property.voyage_data.average_speed)
                self.ui.distance_me_revolution_edit.setText(property.voyage_data.me_revolution_distance)
                self.ui.log_distance_edit.setText(property.voyage_data.log_distance)
                self.ui.average_slip_edit.setText(property.voyage_data.average_slip)

                bunker_list = [property.total_bunker_consumption,
                               property.average_bunker_consumption_per_nm,
                               property.voyage_performance_efficiency]

                attr_list = ['ifo', 'mdo', 'lsfo', 'lsmdo']

                for i in range(self.ui.bunker_consume_table.rowCount()):
                    for j in range(self.ui.bunker_consume_table.columnCount()):
                        if hasattr(bunker_list[i], attr_list[j]):
                            item = QTableWidgetItem(getattr(bunker_list[i], attr_list[j]))
                            self.ui.bunker_consume_table.setItem(i,j, item)

                self.logger.info('Load route file %s successfully' % fn)
                msg_box = QMessageBox(QMessageBox.Information, "Succeed", 'Load route file successfuly')
                msg_box.exec_()

            except Exception,ex:
                self.logger.error(ex, exc_info=1)
                msg_box = QMessageBox(QMessageBox.Warning, "Warning", 'Load route file failed. Error occurred: + \n' + str(ex))
                msg_box.exec_()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadRouteWidget()
    window.show()
    sys.exit(app.exec_())
    pass