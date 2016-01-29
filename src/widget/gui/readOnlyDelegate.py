from PyQt4.QtGui import QItemDelegate


class ReadOnlyDelegate(QItemDelegate):

    def __init__(self, parent = None):
        super(ReadOnlyDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        '''
        Important, otherwise an editor is created if the user clicks in this cell.
        '''
        return None
