from PyQt4.QtCore import *
from PyQt4.QtGui import *

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
            print 'haha' +value

    def setModelData(self, editor, model, index):
        if isinstance(editor, QCheckBox):
            if editor.checkState() == Qt.Checked:
                value = 'Yes'
            else:
                value ='No'
            model.setData(index,value)
        elif isinstance(editor, QLineEdit):
            model.setData(index, editor.text())

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
