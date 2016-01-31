__author__ = 'xingjieliu'

import re
import sys
import logging

from PyQt4.QtGui import QWidget,QApplication,QMessageBox

import QtUiFiles.initialReport as iniReport
from dao.initital import *
from lib.environ import *
from lib.utils import Utils


class IniReportWidget(QWidget):

    def __init__(self):
        super(IniReportWidget, self).__init__()
        self.ui = iniReport.Ui_Form()
        self.ui.setupUi(self)
        self.logger = logging.getLogger('emgui')
        self.initialize()



    def initialize(self):
        self.ui.submitButton.clicked.connect(self.generateXml)
        self.ui.cancelButton.clicked.connect(self.close)

    def generateXml(self):
        try:
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
            property.ecdis_model = self.ui.depthMouldedEdit.text()
            property.captain_name = self.ui.captain_name_edit.text()
            property.captain_crew_id = self.ui.captain_crew_id_edit.text()
            property.maintain_paper_chart = self.ui.yesRadioBtn.isChecked()

            me_particular.ME_Table = me_table

            cells=[]
            pattern='[./\s]'
            for i in range(self.ui.meTableWidget.rowCount()):
                horirental_name = self.ui.meTableWidget.verticalHeaderItem(i).text()
                repl_h_name = re.sub(pattern, '_', str(horirental_name))
                for j in range(self.ui.meTableWidget.columnCount()):
                    column_name = self.ui.meTableWidget.horizontalHeaderItem(j).text()
                    repl_c_name = re.sub(pattern, '_', str(column_name))
                    cells.append(cell(repl_c_name, repl_h_name, self.ui.meTableWidget.item(i,j).text()))

            me_table.cell = cells
            me_particular.ME_Maker = self.ui.meMakerEdit.text()
            me_particular.ME_Model = self.ui.meModelEdit.text()

            property.ME_Particular = me_particular
            root.Property = property

            data_dir = Utils.createDateDir()
            fn_path = abs_lambda(os.path.join(data_dir , 'initial.xml'))
            with open(fn_path, 'w') as f:
                f.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
                root.export(f, 1, namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')

            msg_box = QMessageBox(QMessageBox.Information, "Success", "Initial Report config file generated successfully")
            msg_box.exec_()
        except Exception,ex:
            self.logger.error('Generate the initial report config file failed')
            self.logger.error(ex)
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", "Initial Report config file generated failed \n" + str(ex))
            msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IniReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass