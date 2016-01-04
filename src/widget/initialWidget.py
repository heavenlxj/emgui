__author__ = 'xingjieliu'

import sys
sys.path.append('../..')
import re
import QtUiFiles.initialReport as iniReport
from dao.initital import *

from PyQt4.QtGui import QWidget,QApplication
from lxml import etree as et


class IniReportWidget(QWidget):

    def __init__(self):
        super(IniReportWidget, self).__init__()
        self.ui = iniReport.Ui_Form()
        self.ui.setupUi(self)
        self.initialize()


    def initialize(self):
        self.ship_name =""
        #self.ui.shipNameEdit.textChanged(self.ship_name)

        self.ui.submitButton.clicked.connect(self.generateXml)
    def printT(self):
        self.ship_name = self.ui.shipNameEdit.text()
        self.portRegistry = self.ui.portRegistryEdit.text()
        self.email = self.ui.emailEdit.text()
        # self.ui.emailEdit.setValidator()
        # QRegExpValidator()
        print 'PRINT ship name=%s' % self.ship_name
        print 'PRINT REGISTRY name=%s' % self.portRegistry
        print 'PRINT email name=%s' % self.email

    def setTableProperty(self):
        pass


    def testTable(self):
        rows= self.ui.meTableWidget.rowCount()
        columns = self.ui.meTableWidget.columnCount()
        print 'rows=%s' % rows
        print 'columns=%s' % columns
        for i in range(rows):
            print self.ui.meTableWidget.item(i,0).text()

        print self.ui.meTableWidget.item(0,1).text()
        print self.ui.meTableWidget.item(1,1).text()



    def setText(self, text):
        self.ship_name = text

    def generateXml(self):
        root = initial_report()
        property = Property()
        me_particular = ME_Particular()
        me_table = ME_Table()
        property.ship_name = self.ui.shipNameEdit.text()
        property.call_sign = self.ui.callSignEdit.text()
        property.imo_number = self.ui.imoNumberEdit.text()
        property.port_registry = self.ui.portRegistryEdit.text()
        property.company_name = self.ui.companyNameEdit.text()
        property.class_society = self.ui.classSocietyEdit.text()
        property.email = self.ui.emailEdit.text()
        property.telphone = self.ui.telEdit.text()
        property.fax = self.ui.faxEdit.text()
        property.ship_type = self.ui.shipTypeComboBox.currentText()
        property.international_gross_tonnage = self.ui.igtEdit.text()
        property.international_net_tonnage = self.ui.intEdit.text()
        property.loa = self.ui.loaEdit.text()
        property.lbp = self.ui.lbpEdit.text()
        property.breadth_moulded = self.ui.breadthMouldedEdit.text()
        property.depth_moulded = self.ui.depthMouldedEdit.text()
        property.ecdis_maker = self.ui.ecdisMakerEdit.text()
        property.model = self.ui.depthMouldedEdit.text()
        property.maintain_paper_chart = self.ui.yesRadioBtn.isChecked()

        me_particular.ME_Table = me_table

        cells=[]
        pattern='[./\s]'
        for i in range(self.ui.meTableWidget.rowCount()):
            horirental_name = self.ui.meTableWidget.horizontalHeaderItem(i).text()
            repl_h_name = re.sub(pattern, '_', str(horirental_name))
            for j in range(self.ui.meTableWidget.columnCount()):
                column_name = self.ui.meTableWidget.verticalHeaderItem(j).text()
                repl_c_name = re.sub(pattern, '_', str(column_name))
                cells.append(cell(repl_c_name, repl_h_name, self.ui.meTableWidget.item(i,j).text()))

        me_table.cell = cells
        me_particular.ME_Brand = 'me_brand_test'
        me_particular.ME_Maker = 'me_model_test'

        property.ME_Particular = me_particular
        root.Property = property
        f= open(r'd:\test.xml', 'w')
        f.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
        root.export(f, 1, namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
        print 'generate xml successfully'

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IniReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass