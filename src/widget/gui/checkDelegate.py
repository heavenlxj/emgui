from PyQt4.QtCore import Qt
from PyQt4.QtGui import QItemDelegate, QCheckBox, QLineEdit
from lib.utils import Utils

FORMAT_PATTERN = '(([0-9][0-9]|1[0-9][0-9])-[0-9][0-9]\.[0-9][0-9][0-9] (N|S|W|E))'

class CheckBoxDelegate(QItemDelegate):

    def __init__(self, parent = None):
        super(CheckBoxDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        '''
        Important, otherwise an editor is created if the user clicks in this cell.
        '''
        if index.isValid() and index.column()==2:
            editor=QCheckBox(parent)
            return editor
        else:
            editor = QLineEdit(parent)
            return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole).toString()
        if isinstance(editor, QCheckBox):
            if value=="Yes":
                editor.setCheckState(Qt.Checked)
            else:
                editor.setCheckState(Qt.Unchecked)
        elif isinstance(editor, QLineEdit):
            editor.setText(value)


    def setModelData(self, editor, model, index):
        if isinstance(editor, QCheckBox):
            if editor.checkState() == Qt.Checked:
                value = 'Yes'
            else:
                value ='No'
            model.setData(index,value)
        elif isinstance(editor, QLineEdit):
            value = editor.text()

            if not value.isEmpty():
                if index.column() ==0:
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
                    elif Utils.check_state(value, FORMAT_PATTERN):
                        model.setData(index, value)
                    else:
                        model.setData(index, '#VALUE!')
                elif index.column() == 1:
                    pattern='(-?)(([0-9][0-9])|[0-1][0-7][0-9])([0-5][0-9])((\.[0-9]{1,3})?)'
                    temp_value = str(value)
                    if Utils.check_state(value, pattern):
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
                    elif Utils.check_state(value, FORMAT_PATTERN):
                        model.setData(index, value)
                    else:
                        model.setData(index, '#VALUE!')
            else:
                model.setData(index,  value)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
