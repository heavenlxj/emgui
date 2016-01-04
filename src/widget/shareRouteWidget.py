__author__ = 'xingjieliu'

import sys
sys.path.append('../..')
from dao.share import *
import QtUiFiles.shareRoute as shareReport
from PyQt4.QtGui import QWidget,QApplication


class ShareReportWidget(QWidget):
    def __init__(self):
        super(ShareReportWidget, self).__init__()
        self.ui = shareReport.Ui_Form()
        self.ui.setupUi(self)

    def initialize(self):
        pass

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
        cells.append(cell('d_slow', 'rpm', 1))
        cells.append(cell('d_slow', 'ballast_slip', 5))
        cells.append(cell('half', 'load_speed', 10))
        cells.append(cell('nav_full', 'load_slip', 99))

        me_table.cell = cells
        me_particular.ME_Brand = 'me_brand_test'
        me_particular.ME_Model = 'me_model_test'

        property.ME_Particular = me_particular
        root.Property = property
        f= open(r'd:\test.xml', 'w')
        f.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
        root.export(f, 1, namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
        print 'generate xml successfully'


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShareReportWidget()
    window.show()
    sys.exit(app.exec_())
    pass