from PyQt4.QtCore import Qt
from PyQt4.QtGui import QItemDelegate,QComboBox

class ComboBoxDelegate(QItemDelegate):

    def __init__(self, items_list,parent=None):
        super(ComboBoxDelegate, self).__init__(parent)
        self.items_list = items_list


    def changeFormula(self, index):
        pass

    def createEditor(self, parent, option, index):
        '''
        Important, otherwise an editor is created if the user clicks in this cell.
        '''
        if index.isValid():
            editor=QComboBox(parent)
            for item in self.items_list:
                editor.addItem(str(item))

        editor.currentIndexChanged.connect(self.changeFormula)
        return editor


    def setEditorData(self, editor, index):

        text = index.model().data(index, Qt.EditRole).toString()
        pos = editor.findText(text)
        if pos == -1:
            pos = 0
        editor.setCurrentIndex(pos)

    def setModelData(self, editor, model, index):
        value = editor.currentText()
        model.setData(index, value)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
