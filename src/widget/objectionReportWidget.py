__author__ = 'xingjieliu'

import sys
import QtUiFiles.objectionReport as objectionReport
from PyQt4.QtGui import QWidget,QApplication,QMessageBox
from PyQt4.QtCore import *
from lib.utils import *
from dao.object import *
from gui.latitudeDelegate import LatitudeDelegate
from gui.longtitudeDelegate import LongtitudeDelegate
from gui.readOnlyDelegate import ReadOnlyDelegate
import time
import logging


class ObjectionReportWidget(QWidget):
    def __init__(self):
        super(ObjectionReportWidget, self).__init__()
        self.ui = objectionReport.Ui_Form()
        self.ui.setupUi(self)
        self.logger = logging.getLogger('emgui')
        self.autoloadConfig()
        self.initialize()

    def initialize(self):
        self.ui.submit_btn.clicked.connect(self.generateXml)
        self.ui.reload_btn.clicked.connect(self.autoloadConfig)
        self.ui.textEdit_remark.setDisabled(True)
        self.ui.checkBox_others.toggled.connect(self.enableEdit)
        self.routeTableLoading()

    def enableEdit(self, flag):
        if flag:
            self.ui.textEdit_remark.setEnabled(True)
        else:
            self.ui.textEdit_remark.setDisabled(True)


    def routeTableLoading(self):
        self.ui.add_new_btn.clicked.connect(self.addTableItem)
        self.ui.remove_btn.clicked.connect(self.deleteTableItem)
        self.ui.route_table_widget.setItemDelegateForColumn(0, ReadOnlyDelegate(self))
        self.ui.route_table_widget.setItemDelegateForColumn(1, LatitudeDelegate(self))
        self.ui.route_table_widget.setItemDelegateForColumn(2, LongtitudeDelegate(self))
        self.ui.route_table_widget.itemDoubleClicked.connect(self.reformat)
        self.ui.route_table_widget.setAlternatingRowColors(True)

        for i in range(self.ui.route_table_widget.rowCount()):
            index= self.ui.route_table_widget.model().index(i,0)
            self.ui.route_table_widget.model().setData(index, i+1)
            self.ui.route_table_widget.item(i,0).setTextAlignment(Qt.AlignCenter)

    def addTableItem(self):
        count = self.ui.route_table_widget.rowCount()
        self.ui.route_table_widget.insertRow(count)
        index= self.ui.route_table_widget.model().index(count,0)
        self.ui.route_table_widget.model().setData(index, count+1)
        self.ui.route_table_widget.item(count,0).setTextAlignment(Qt.AlignCenter)


    def deleteTableItem(self):
        row = self.ui.route_table_widget.currentRow()
        self.ui.route_table_widget.removeRow(row)
        for i in range(self.ui.route_table_widget.rowCount()):
            index= self.ui.route_table_widget.model().index(i,0)
            self.ui.route_table_widget.model().setData(index, i+1)
            self.ui.route_table_widget.item(i,0).setTextAlignment(Qt.AlignCenter)

    def reformat(self, item):
        if item.column() == 1 or item.column() == 2:
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

    def generateXml(self):
        root = objection_report()
        property = Property()
        root.Property = property

        property.ship_name = self.ui.ship_name_edit.text()
        property.call_sign = self.ui.call_sign_edit.text()
        property.voyage_number = self.ui.voyage_number_edit.text()
        property.captain_name = self.ui.captain_name_edit.text()
        property.date = self.ui.date_edit.text()
        property.route_id_number = self.ui.route_id_number.text()

        #critial point
        routes_list=[]
        row_count = self.ui.route_table_widget.rowCount()
        for i in range(row_count):
            route_item = route()
            try:
                id = self.ui.route_table_widget.item(i,0).text()
                lat = self.ui.route_table_widget.item(i,1).text()
                long = self.ui.route_table_widget.item(i,2).text()
                route_item.id = str(id)
                route_item.latitude = str(self.convertPoint(lat))
                route_item.longtitude = str(self.convertPoint(long))
                routes_list.append(route_item)
            except AttributeError:
                pass

        rou = routes()
        rou.route = routes_list
        property.routes = rou

        reasons = reason_objection()
        reason_list = []
        self.getCheckText(self.ui.checkBox_ukc,reason_list)
        self.getCheckText(self.ui.checkBox_water_depth,reason_list)
        self.getCheckText(self.ui.checkBox_violate_local,reason_list)
        self.getCheckText(self.ui.checkBox_safety_margin,reason_list)
        self.getCheckText(self.ui.checkBox_ntm_navtex_egc,reason_list)
        self.getCheckText(self.ui.checkBox_heavy_traffic,reason_list)
        if self.ui.checkBox_others.isChecked():
            other_reason = self.ui.textEdit_remark.toPlainText()
            if other_reason != '':
                reason_list.append(other_reason)

        reasons.reason = reason_list
        property.reason_objection = reasons

        data_dir = Utils.createDataDir()
        fn_path = abs_lambda(os.path.join(data_dir , 'object.xml'))
        with open(fn_path, 'w') as f:
            f.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
            root.export(f, 1, namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
        msg_box = QMessageBox(QMessageBox.Information, "Success", "Objection Report config file generated successfully")
        msg_box.exec_()

    def getCheckText(self, ckbox, reason_list):
        if ckbox.isChecked():
            reason_list.append(ckbox.text())

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
            self.logger.error('[Objection Report]:' + msg, exc_info=1)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ObjectionReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass