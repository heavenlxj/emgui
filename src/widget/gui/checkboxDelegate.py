from PyQt4.QtCore import Qt
from PyQt4.QtGui import QItemDelegate, QCheckBox

class CheckBoxDelegate(QItemDelegate):

    def __init__(self, parent = None):
        super(CheckBoxDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        '''
        Important, otherwise an editor is created if the user clicks in this cell.
        '''
        editor=QCheckBox(parent)
        return editor


    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole).toString()

        if value=="Yes":
            editor.setCheckState(Qt.Checked)
        else:
            editor.setCheckState(Qt.Unchecked)


    def setModelData(self, editor, model, index):
        if editor.checkState() == Qt.Checked:
            value = 'Yes'
        else:
            value ='No'
        model.setData(index,value)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
