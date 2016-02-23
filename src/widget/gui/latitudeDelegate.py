from PyQt4.QtCore import Qt
from PyQt4.QtGui import QItemDelegate, QLineEdit
from lib.utils import Utils, PointType
import logging

class LatitudeDelegate(QItemDelegate):

    def __init__(self, parent = None):
        self.logger = logging.getLogger('emgui')
        super(LatitudeDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        '''
        Important, otherwise an editor is created if the user clicks in this cell.
        '''
        editor = QLineEdit(parent)
        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole).toString()
        editor.setText(value)
        editor.setAlignment(Qt.AlignCenter)

    def setModelData(self, editor, model, index):
        value = editor.text()
        if not value.isEmpty():
            try:
                format_value = Utils.formatPoint(value, PointType.LATITUDE)
                model.setData(index, format_value)

            except Exception,ex:
                self.logger.error(ex, exc_info=1)

        else:
            model.setData(index,  value)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
