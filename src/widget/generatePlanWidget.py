__author__ = 'xingjieliu'

import sys
import QtUiFiles.planGenerator as planGenerator
from PyQt4.QtGui import QWidget,QApplication,QFileDialog
from PyQt4.QtCore import Qt,QString,QDir
from lib.utils import *
from gui.comboDelegate import ComboBoxDelegate
from gui.latitudeDelegate import LatitudeDelegate
from gui.longtitudeDelegate import LongtitudeDelegate
from gui.readOnlyDelegate import ReadOnlyDelegate
import xlwt

class PlanGenerateWidget(QWidget):
    def __init__(self):
        super(PlanGenerateWidget, self).__init__()
        self.ui = planGenerator.Ui_Form()
        self.ui.setupUi(self)
        self.combo_items= ['RL', 'GC']
        self.initialize()
        self.logger = logging.getLogger('emgui')

    def initialize(self):
        self.ui.add_row_btn.clicked.connect(self.addTableItem)
        self.ui.export_esv_btn.clicked.connect(self.export)
        self.ui.browse_btn.clicked.connect(self.browse)

        self.ui.calculate_form_table_widget.setItemDelegateForColumn(0, ReadOnlyDelegate(self))
        self.ui.calculate_form_table_widget.setItemDelegateForColumn(1, LatitudeDelegate(self))
        self.ui.calculate_form_table_widget.setItemDelegateForColumn(2, LongtitudeDelegate(self))
        self.ui.calculate_form_table_widget.setItemDelegateForColumn(3, ComboBoxDelegate(self.combo_items,self))
        self.ui.calculate_form_table_widget.setItemDelegateForColumn(4, ReadOnlyDelegate(self))
        self.ui.calculate_form_table_widget.setItemDelegateForColumn(5, ReadOnlyDelegate(self))
        self.ui.calculate_form_table_widget.setItemDelegateForColumn(6, ReadOnlyDelegate(self))
        self.ui.calculate_form_table_widget.itemDoubleClicked.connect(self.reformat)
        self.ui.calculate_form_table_widget.setAlternatingRowColors(True)

        for i in range(self.ui.calculate_form_table_widget.rowCount()):
            index= self.ui.calculate_form_table_widget.model().index(i,0)
            self.ui.calculate_form_table_widget.model().setData(index, i+1)
            self.ui.calculate_form_table_widget.item(i,0).setTextAlignment(Qt.AlignCenter)

            combo_index = self.ui.calculate_form_table_widget.model().index(i,3)
            self.ui.calculate_form_table_widget.model().setData(combo_index, self.combo_items[0])
            self.ui.calculate_form_table_widget.item(i,3).setTextAlignment(Qt.AlignCenter)

        self.ui.calculate_form_table_widget.itemChanged.connect(self.itemChangeTest)

    def addTableItem(self):
        count = self.ui.calculate_form_table_widget.rowCount()
        self.ui.calculate_form_table_widget.insertRow(count)

        index= self.ui.calculate_form_table_widget.model().index(count,0)
        self.ui.calculate_form_table_widget.model().setData(index, count+1)
        self.ui.calculate_form_table_widget.item(count,0).setTextAlignment(Qt.AlignCenter)

        combo_index = self.ui.calculate_form_table_widget.model().index(count,3)
        self.ui.calculate_form_table_widget.model().setData(combo_index, self.combo_items[0])
        self.ui.calculate_form_table_widget.item(count,3).setTextAlignment(Qt.AlignCenter)


    def export(self):
        try:
            path = self.ui.csv_edit.text()
            if path.isEmpty() or path.isNull():
                msg_box = QMessageBox(QMessageBox.Warning, "Warning", 'Empty file name')
                msg_box.exec_()
                return False

            f = xlwt.Workbook()
            sheet = f.add_sheet('sheet1', cell_overwrite_ok=True)
            header = []
            for i in range(self.ui.calculate_form_table_widget.columnCount()):
                header.append(self.ui.calculate_form_table_widget.horizontalHeaderItem(i).text())

            for i in range(len(header)):
                sheet.write(0,i,str(header[i]))

            for m in range(self.ui.calculate_form_table_widget.rowCount()):
                for n in range(self.ui.calculate_form_table_widget.columnCount()):
                    try:
                        value = str(self.ui.calculate_form_table_widget.item(m,n).text())
                    except AttributeError:
                        value = ''

                    sheet.write(m+1,n, value)
            f.save(path)
            msg_box = QMessageBox(QMessageBox.Information, "Success", 'Excel File generated successfully')
            msg_box.exec_()
        except Exception, ex:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", 'Excel File generate failed \n' + str(ex))
            msg_box.exec_()

    def browse(self):
        fn = QFileDialog.getSaveFileName(self, "Open Files",
                DATA_PATH, "Excel Files(*.xls, *.xlsx);;CSV Files(*.csv)")
        if fn:
            abs_fn = os.path.abspath(fn)
            self.ui.csv_edit.setText(abs_fn)

    def itemChangeTest(self, item):
        sender = self.sender()
        all_rows = sender.rowCount()
        cur_row_index = item.row()
        cur_column = item.column()
        cur_row_val = cur_row_index + 1

        if cur_column == 1 or cur_column ==  2:
            #if last row update, skip recalculate, set end for course and distance
            if cur_row_val == all_rows:
                course = 'END'
                distance = 'END'

            else:
                formula_type = sender.item(cur_row_index, 3).text()
                self.updateCurrentAndPrevious(sender, cur_row_index, formula_type, True)
                if cur_row_index !=0:
                    pre_formula_type = sender.item(cur_row_index-1, 3).text()
                    print 'previous formula_type=%s' % pre_formula_type
                    self.updateCurrentAndPrevious(sender, cur_row_index, pre_formula_type, False)

        if cur_column ==3:
            #RL/GC update
            formula_type = item.text()
            self.updateCurrentAndPrevious(sender, cur_row_index, formula_type, True)

    def updateCurrentAndPrevious(self, sender, cur_row_index, formula_type, current_next):
        try:
            #UPDATE CURRENT AND PREVIOUS
            if current_next:
                source_index = cur_row_index
                dest_index = cur_row_index+1
            else:
                source_index = cur_row_index-1
                dest_index = cur_row_index

            s_lat = self.convertRadians(sender.item(source_index, 1).text())
            s_long = self.convertRadians(sender.item(source_index, 2).text())
            d_lat = self.convertRadians(sender.item(dest_index, 1).text())
            d_long = self.convertRadians(sender.item(dest_index,2).text())

            if formula_type == 'GC':
                course = Utils.calCourseGCFormula(s_lat, s_long, d_lat, d_long)
                distance = Utils.calDistanceGCFormula(s_lat,s_long,d_lat,d_long)
            elif formula_type == 'RL':
                course = Utils.calCourseRLFormula(s_lat, s_long, d_lat, d_long)
                distance = Utils.calDistanceRLFormula(s_lat, s_long, d_lat, d_long)

        except AttributeError,ex:
            course = 'END'
            distance = 'END'
            self.logger.error(ex, exc_info=1)

        course_index= sender.model().index(source_index,4)
        sender.model().setData(course_index, course)
        sender.item(source_index,4).setTextAlignment(Qt.AlignCenter)

        distance_index= sender.model().index(source_index,5)
        sender.model().setData(distance_index, distance)
        sender.item(source_index,5).setTextAlignment(Qt.AlignCenter)

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

    def convertRadians(self, text):
        formated = ''
        minus = False
        if not text.isEmpty() and not text.isNull():
            if Utils.checkState(text, Utils.FORMAT_PATTERN):
                orient = text[-1]
                formated = text.replace('-','')[:-2]
                if orient == 'S' or orient == 'W':
                    formated.push_front('-')
                    minus = True

        if formated != '':
            formated = float(formated)
            point = int(abs(formated)/100) + (abs(formated)/100-int(abs(formated)/100))*100/60
            if minus:
                point *= -1
        else:
            point = ''
        return QString(str(point))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlanGenerateWidget()
    window.show()
    sys.exit(app.exec_())
    pass