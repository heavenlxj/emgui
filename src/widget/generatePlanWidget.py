__author__ = 'xingjieliu'

import sys
import QtUiFiles.planGenerator as planGenerator
from PyQt4.QtGui import QWidget,QApplication
from PyQt4.QtCore import Qt
from lib.utils import *
from gui.comboDelegate import ComboBoxDelegate
from gui.latitudeDelegate import LatitudeDelegate
from gui.longtitudeDelegate import LongtitudeDelegate
from gui.readOnlyDelegate import ReadOnlyDelegate

class PlanGenerateWidget(QWidget):
    def __init__(self):
        super(PlanGenerateWidget, self).__init__()
        self.ui = planGenerator.Ui_Form()
        self.ui.setupUi(self)
        self.initialize()

    def initialize(self):

        combo_items = ['RL', 'GC']
        self.ui.calculate_form_table_widget.setItemDelegateForColumn(0, ReadOnlyDelegate(self))
        self.ui.calculate_form_table_widget.setItemDelegateForColumn(1, LatitudeDelegate(self))
        self.ui.calculate_form_table_widget.setItemDelegateForColumn(2, LongtitudeDelegate(self))
        self.ui.calculate_form_table_widget.setItemDelegateForColumn(3, ComboBoxDelegate(combo_items,self))
        self.ui.calculate_form_table_widget.setItemDelegateForColumn(4, ReadOnlyDelegate(self))
        self.ui.calculate_form_table_widget.setItemDelegateForColumn(5, ReadOnlyDelegate(self))
        self.ui.calculate_form_table_widget.setItemDelegateForColumn(6, ReadOnlyDelegate(self))
        self.ui.calculate_form_table_widget.setAlternatingRowColors(True)

        for i in range(self.ui.calculate_form_table_widget.rowCount()):
            index= self.ui.calculate_form_table_widget.model().index(i,0)
            self.ui.calculate_form_table_widget.model().setData(index, i+1)
            self.ui.calculate_form_table_widget.item(i,0).setTextAlignment(Qt.AlignCenter)

            combo_index = self.ui.calculate_form_table_widget.model().index(i,3)
            self.ui.calculate_form_table_widget.model().setData(combo_index, combo_items[0])
            self.ui.calculate_form_table_widget.item(i,3).setTextAlignment(Qt.AlignCenter)

        self.ui.calculate_form_table_widget.itemChanged.connect(self.itemChangeTest)

    def itemChangeTest(self, item):
        sender = self.sender()
        all_rows = sender.rowCount()
        cur_row_index = item.row()
        cur_column = item.column()
        cur_row_val = cur_row_index + 1
        print 'All Rows=%s' % sender.rowCount()
        print 'Column=%s' % str(item.column())
        print 'Row= %s' % str(item.row())


        if cur_column == 1 or cur_column ==  2:
            #latitude or longtitude change
            #get GC/RL value
            formula_type = sender.item(cur_row_index, 3).text()
            print 'formula_type=%s' % formula_type

            #if last row update, skip recalculate, set end for course and distance
            if cur_row_val == all_rows:
                course = 'END'
                distance = 'END'

            else:
                s_lat = sender.item(cur_row_index, 1).text()
                s_long = sender.item(cur_row_index, 2).text()

                d_lat = sender.item(cur_row_index+1, 1).text()
                d_long = sender.item(cur_row_index+1,2).text()

                if formula_type == 'GC':
                    course = Utils.calCourseGCFormula()
                    distance = Utils.calDistanceGCFormula()
                elif formula_type == 'RL':
                    course = Utils.calCourseRLFormula()
                    distance = Utils.calDistanceRLFormula()

            course_index= sender.model().index(cur_row_index,4)
            sender.model().setData(course_index, course)

            distance_index= sender.model().index(cur_row_index,5)
            sender.model().setData(distance_index, distance)


        if cur_column ==3:
            #RL/GC update
            print item.text()



    # def loadConfig(self):
    #     configs, msg = Utils.readGeneralConfigFromXml()
    #     if configs is not None and len(configs) !=0:
    #         self.ui.ship_name_edit.setText(configs['ship_name'])
    #         self.ui.call_sign_edit.setText(configs['call_sign'])
    #         self.ui.captain_name_edit.setText(configs['captain_name'])
    #         self.ui.date_edit.setText(configs['date'])
    #         pass
    #     else:
    #         msg_box = QMessageBox(QMessageBox.Warning, "Warning", msg)
    #         msg_box.exec_()


    def test(self):
        print 'hello'

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlanGenerateWidget()
    window.show()
    sys.exit(app.exec_())
    pass