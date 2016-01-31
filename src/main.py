__author__ = 'xingjieliu'

import sys

from PyQt4.QtGui import QMainWindow,QApplication, QListView, QListWidgetItem
from PyQt4.QtCore import Qt

from lib.environ import *
from lib.utils import Utils


#sys.path.append('..')
import QtUiFiles.main as MainWindow
from widget import requestRouteWidget, objectionReportWidget, \
    initialRouteWidget, revertRouteWidget, loadRouteWidget, generatePlanWidget

class RootWindow(QMainWindow):
    def __init__(self):
        super(RootWindow, self).__init__()
        self.root = MainWindow.Ui_MainWindow()
        self.root.setupUi(self)
        self.logger = Utils.setupLogger('emgui', os.path.join(LOG_PATH, 'emgui_running.log'))

        self.root.listWidget.setViewMode(QListView.ListMode)
        #self.root.listWidget.setIconSize(QSize(96, 84))
        self.root.listWidget.setMovement(QListView.Static)
        self.root.listWidget.setMaximumWidth(128)
        self.root.listWidget.setSpacing(12)

        self.root.stackedWidget.addWidget(initialRouteWidget.IniReportWidget())
        self.root.stackedWidget.addWidget(requestRouteWidget.ReqReportWidget())
        self.root.stackedWidget.addWidget(loadRouteWidget.LoadRouteWidget())
        self.root.stackedWidget.addWidget(revertRouteWidget.RevertReportWidget())
        self.root.stackedWidget.addWidget(objectionReportWidget.ObjectionReportWidget())
        self.root.stackedWidget.addWidget(generatePlanWidget.PlanGenerateWidget())

        self.setWindowTitle("EMGui")

        self.createIcons()
        self.root.listWidget.setCurrentRow(0)

    def changePage(self, current, previous):
        if not current:
            current = previous

        self.root.stackedWidget.setCurrentIndex(self.root.listWidget.row(current))

    def createIcons(self):
        initialButton = QListWidgetItem(self.root.listWidget)
        #initialButton.setIcon(QIcon(':/images/config.png'))
        initialButton.setText("Initial Route")
        initialButton.setTextAlignment(Qt.AlignHCenter)
        initialButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        requestButton = QListWidgetItem(self.root.listWidget)
        #requestButton.setIcon(QIcon(':/images/update.png'))
        requestButton.setText("Request Route")
        requestButton.setTextAlignment(Qt.AlignHCenter)
        requestButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        LoadButton = QListWidgetItem(self.root.listWidget)
        #LoadButton.setIcon(QIcon(':/images/query.png'))
        LoadButton.setText("Load Route")
        LoadButton.setTextAlignment(Qt.AlignHCenter)
        LoadButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        RevertButton = QListWidgetItem(self.root.listWidget)
        #RevertButton.setIcon(QIcon(':/images/query.png'))
        RevertButton.setText("Revert Route")
        RevertButton.setTextAlignment(Qt.AlignHCenter)
        RevertButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        ObjectionButton = QListWidgetItem(self.root.listWidget)
        #ObjectionButton.setIcon(QIcon(':/images/query.png'))
        ObjectionButton.setText("Objection Route")
        ObjectionButton.setTextAlignment(Qt.AlignHCenter)
        ObjectionButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        planButton = QListWidgetItem(self.root.listWidget)
        #planButton.setIcon(QIcon(':/images/query.png'))
        planButton.setText("Plan Generator")
        planButton.setTextAlignment(Qt.AlignHCenter)
        planButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        self.root.listWidget.currentItemChanged.connect(self.changePage)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RootWindow()
    window.show()
    sys.exit(app.exec_())
    pass
