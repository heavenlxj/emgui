from PyQt4.QtCore import Qt
from PyQt4.QtGui import QItemDelegate, QLineEdit
from lib.utils import Utils

class LatitudeDelegate(QItemDelegate):

    def __init__(self, parent = None):
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


    def setModelData(self, editor, model, index):
        value = editor.text()
        if not value.isEmpty():
                pattern='(-?[0-8][0-9][0-5][0-9])((\.[0-9]{1,3})?)'
                temp_value = str(value)
                if Utils.check_state(value, pattern):
                    if temp_value.startswith('-'):
                        orient = 'S'
                    else:
                        orient = 'N'
                    temp_value = temp_value.strip('-')
                    deg = temp_value[:2]
                    min = temp_value[2:]
                    dot_index = temp_value.find('.')
                    if dot_index != -1:
                        float_part = str(temp_value[dot_index+1:])
                        float_len = len(float_part)
                        zero_pad = '0' * (3-float_len)
                    else:
                        zero_pad = '.000'

                    format_value = str.format('{0}-{1} {2}', str(deg), str(min)+zero_pad, orient)
                    model.setData(index, format_value)
                elif Utils.check_state(value, Utils.FORMAT_PATTERN):
                    model.setData(index, value)
                else:
                    model.setData(index, '#VALUE!')
        else:
            model.setData(index,  value)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
