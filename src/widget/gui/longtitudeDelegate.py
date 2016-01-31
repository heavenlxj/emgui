from PyQt4.QtCore import Qt
from PyQt4.QtGui import QItemDelegate, QLineEdit
from lib.utils import Utils


class LongtitudeDelegate(QItemDelegate):

    def __init__(self, parent = None):
        super(LongtitudeDelegate, self).__init__(parent)

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
            pattern='(-?)(([0-9][0-9])|[0-1][0-7][0-9])([0-5][0-9])((\.[0-9]{1,3})?)'
            temp_value = str(value)
            if Utils.checkState(value, pattern):
                if temp_value.startswith('-'):
                    orient = 'W'
                else:
                    orient = 'E'
                temp_value = temp_value.strip('-')
                temp_list = temp_value.split('.')
                part1 = temp_list[0]
                deg=0
                min=0
                zero_pad=''
                if len(part1)==4:
                    deg=part1[:2]
                    min=part1[2:]
                elif len(part1)==5:
                    deg=part1[:3]
                    min=part1[3:]
                if temp_list>1:
                    part2 = temp_list[1]
                    min=min+'.'+part2
                    if len(part2) < 3:
                        zero_pad = '0' * (3-len(part2))
                        min=min+zero_pad
                else:
                    zero_pad = '000'
                    min=min+'.'+zero_pad

                format_value = str.format('{0}-{1} {2}', str(deg), str(min), orient)
                model.setData(index, format_value)
            elif Utils.checkState(value, Utils.FORMAT_PATTERN):
                model.setData(index, value)
            else:
                model.setData(index, '#VALUE!')
        else:
            model.setData(index,  value)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
