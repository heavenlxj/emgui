# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'initialReport.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(897, 656)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.shipNameLabel = QtGui.QLabel(self.groupBox)
        self.shipNameLabel.setObjectName(_fromUtf8("shipNameLabel"))
        self.gridLayout.addWidget(self.shipNameLabel, 0, 0, 1, 1)
        self.shipNameEdit = QtGui.QLineEdit(self.groupBox)
        self.shipNameEdit.setObjectName(_fromUtf8("shipNameEdit"))
        self.gridLayout.addWidget(self.shipNameEdit, 0, 1, 1, 1)
        self.callSignLabel = QtGui.QLabel(self.groupBox)
        self.callSignLabel.setObjectName(_fromUtf8("callSignLabel"))
        self.gridLayout.addWidget(self.callSignLabel, 0, 2, 1, 1)
        self.callSignEdit = QtGui.QLineEdit(self.groupBox)
        self.callSignEdit.setObjectName(_fromUtf8("callSignEdit"))
        self.gridLayout.addWidget(self.callSignEdit, 0, 4, 1, 1)
        self.imoNumberLabel = QtGui.QLabel(self.groupBox)
        self.imoNumberLabel.setObjectName(_fromUtf8("imoNumberLabel"))
        self.gridLayout.addWidget(self.imoNumberLabel, 0, 5, 1, 1)
        self.imoNumberEdit = QtGui.QLineEdit(self.groupBox)
        self.imoNumberEdit.setObjectName(_fromUtf8("imoNumberEdit"))
        self.gridLayout.addWidget(self.imoNumberEdit, 0, 6, 1, 1)
        self.portRegistryLabel = QtGui.QLabel(self.groupBox)
        self.portRegistryLabel.setObjectName(_fromUtf8("portRegistryLabel"))
        self.gridLayout.addWidget(self.portRegistryLabel, 1, 0, 1, 1)
        self.portRegistryEdit = QtGui.QLineEdit(self.groupBox)
        self.portRegistryEdit.setObjectName(_fromUtf8("portRegistryEdit"))
        self.gridLayout.addWidget(self.portRegistryEdit, 1, 1, 1, 1)
        self.companyNameLabel = QtGui.QLabel(self.groupBox)
        self.companyNameLabel.setObjectName(_fromUtf8("companyNameLabel"))
        self.gridLayout.addWidget(self.companyNameLabel, 1, 2, 1, 1)
        self.companyNameEdit = QtGui.QLineEdit(self.groupBox)
        self.companyNameEdit.setObjectName(_fromUtf8("companyNameEdit"))
        self.gridLayout.addWidget(self.companyNameEdit, 1, 4, 1, 1)
        self.classSocietyLabel = QtGui.QLabel(self.groupBox)
        self.classSocietyLabel.setObjectName(_fromUtf8("classSocietyLabel"))
        self.gridLayout.addWidget(self.classSocietyLabel, 1, 5, 1, 1)
        self.classSocietyEdit = QtGui.QLineEdit(self.groupBox)
        self.classSocietyEdit.setObjectName(_fromUtf8("classSocietyEdit"))
        self.gridLayout.addWidget(self.classSocietyEdit, 1, 6, 1, 1)
        self.emailLabel = QtGui.QLabel(self.groupBox)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.gridLayout.addWidget(self.emailLabel, 2, 0, 1, 1)
        self.emailEdit = QtGui.QLineEdit(self.groupBox)
        self.emailEdit.setObjectName(_fromUtf8("emailEdit"))
        self.gridLayout.addWidget(self.emailEdit, 2, 1, 1, 1)
        self.telLabel = QtGui.QLabel(self.groupBox)
        self.telLabel.setObjectName(_fromUtf8("telLabel"))
        self.gridLayout.addWidget(self.telLabel, 2, 2, 1, 1)
        self.telEdit = QtGui.QLineEdit(self.groupBox)
        self.telEdit.setObjectName(_fromUtf8("telEdit"))
        self.gridLayout.addWidget(self.telEdit, 2, 4, 1, 1)
        self.taxNumberLabel = QtGui.QLabel(self.groupBox)
        self.taxNumberLabel.setObjectName(_fromUtf8("taxNumberLabel"))
        self.gridLayout.addWidget(self.taxNumberLabel, 2, 5, 1, 1)
        self.faxEdit = QtGui.QLineEdit(self.groupBox)
        self.faxEdit.setObjectName(_fromUtf8("faxEdit"))
        self.gridLayout.addWidget(self.faxEdit, 2, 6, 1, 1)
        self.shipTypeLabel = QtGui.QLabel(self.groupBox)
        self.shipTypeLabel.setObjectName(_fromUtf8("shipTypeLabel"))
        self.gridLayout.addWidget(self.shipTypeLabel, 3, 0, 1, 1)
        self.shipTypeComboBox = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shipTypeComboBox.sizePolicy().hasHeightForWidth())
        self.shipTypeComboBox.setSizePolicy(sizePolicy)
        self.shipTypeComboBox.setMinimumSize(QtCore.QSize(69, 20))
        self.shipTypeComboBox.setObjectName(_fromUtf8("shipTypeComboBox"))
        self.shipTypeComboBox.addItem(_fromUtf8(""))
        self.shipTypeComboBox.addItem(_fromUtf8(""))
        self.shipTypeComboBox.addItem(_fromUtf8(""))
        self.shipTypeComboBox.addItem(_fromUtf8(""))
        self.shipTypeComboBox.addItem(_fromUtf8(""))
        self.shipTypeComboBox.addItem(_fromUtf8(""))
        self.shipTypeComboBox.addItem(_fromUtf8(""))
        self.shipTypeComboBox.addItem(_fromUtf8(""))
        self.shipTypeComboBox.addItem(_fromUtf8(""))
        self.shipTypeComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.shipTypeComboBox, 3, 1, 1, 1)
        self.igtLabel = QtGui.QLabel(self.groupBox)
        self.igtLabel.setLineWidth(0)
        self.igtLabel.setObjectName(_fromUtf8("igtLabel"))
        self.gridLayout.addWidget(self.igtLabel, 3, 2, 1, 2)
        self.igtEdit = QtGui.QLineEdit(self.groupBox)
        self.igtEdit.setEnabled(True)
        self.igtEdit.setObjectName(_fromUtf8("igtEdit"))
        self.gridLayout.addWidget(self.igtEdit, 3, 4, 1, 1)
        self.intLabel = QtGui.QLabel(self.groupBox)
        self.intLabel.setObjectName(_fromUtf8("intLabel"))
        self.gridLayout.addWidget(self.intLabel, 3, 5, 1, 1)
        self.intEdit = QtGui.QLineEdit(self.groupBox)
        self.intEdit.setObjectName(_fromUtf8("intEdit"))
        self.gridLayout.addWidget(self.intEdit, 3, 6, 1, 1)
        self.loaLabel = QtGui.QLabel(self.groupBox)
        self.loaLabel.setObjectName(_fromUtf8("loaLabel"))
        self.gridLayout.addWidget(self.loaLabel, 4, 0, 1, 1)
        self.loaEdit = QtGui.QLineEdit(self.groupBox)
        self.loaEdit.setObjectName(_fromUtf8("loaEdit"))
        self.gridLayout.addWidget(self.loaEdit, 4, 1, 1, 1)
        self.lbpLabel = QtGui.QLabel(self.groupBox)
        self.lbpLabel.setObjectName(_fromUtf8("lbpLabel"))
        self.gridLayout.addWidget(self.lbpLabel, 4, 2, 1, 1)
        self.lbpEdit = QtGui.QLineEdit(self.groupBox)
        self.lbpEdit.setObjectName(_fromUtf8("lbpEdit"))
        self.gridLayout.addWidget(self.lbpEdit, 4, 4, 1, 1)
        self.breadthMouldedLabel = QtGui.QLabel(self.groupBox)
        self.breadthMouldedLabel.setObjectName(_fromUtf8("breadthMouldedLabel"))
        self.gridLayout.addWidget(self.breadthMouldedLabel, 4, 5, 1, 1)
        self.breadthMouldedEdit = QtGui.QLineEdit(self.groupBox)
        self.breadthMouldedEdit.setObjectName(_fromUtf8("breadthMouldedEdit"))
        self.gridLayout.addWidget(self.breadthMouldedEdit, 4, 6, 1, 1)
        self.depthMoulded = QtGui.QLabel(self.groupBox)
        self.depthMoulded.setObjectName(_fromUtf8("depthMoulded"))
        self.gridLayout.addWidget(self.depthMoulded, 5, 0, 1, 1)
        self.depthMouldedEdit = QtGui.QLineEdit(self.groupBox)
        self.depthMouldedEdit.setObjectName(_fromUtf8("depthMouldedEdit"))
        self.gridLayout.addWidget(self.depthMouldedEdit, 5, 1, 1, 1)
        self.ecdisMakerLabel = QtGui.QLabel(self.groupBox)
        self.ecdisMakerLabel.setObjectName(_fromUtf8("ecdisMakerLabel"))
        self.gridLayout.addWidget(self.ecdisMakerLabel, 5, 2, 1, 1)
        self.ecdisMakerEdit = QtGui.QLineEdit(self.groupBox)
        self.ecdisMakerEdit.setObjectName(_fromUtf8("ecdisMakerEdit"))
        self.gridLayout.addWidget(self.ecdisMakerEdit, 5, 4, 1, 1)
        self.modelLabel = QtGui.QLabel(self.groupBox)
        self.modelLabel.setObjectName(_fromUtf8("modelLabel"))
        self.gridLayout.addWidget(self.modelLabel, 5, 5, 1, 1)
        self.modelEdit = QtGui.QLineEdit(self.groupBox)
        self.modelEdit.setObjectName(_fromUtf8("modelEdit"))
        self.gridLayout.addWidget(self.modelEdit, 5, 6, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)
        self.captain_name_edit = QtGui.QLineEdit(self.groupBox)
        self.captain_name_edit.setObjectName(_fromUtf8("captain_name_edit"))
        self.gridLayout.addWidget(self.captain_name_edit, 6, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 6, 2, 1, 1)
        self.captain_crew_id_edit = QtGui.QLineEdit(self.groupBox)
        self.captain_crew_id_edit.setObjectName(_fromUtf8("captain_crew_id_edit"))
        self.gridLayout.addWidget(self.captain_crew_id_edit, 6, 4, 1, 1)
        self.depthMouldedEdit.raise_()
        self.callSignEdit.raise_()
        self.ecdisMakerLabel.raise_()
        self.telLabel.raise_()
        self.modelLabel.raise_()
        self.imoNumberEdit.raise_()
        self.lbpLabel.raise_()
        self.breadthMouldedLabel.raise_()
        self.telEdit.raise_()
        self.companyNameEdit.raise_()
        self.loaLabel.raise_()
        self.companyNameLabel.raise_()
        self.shipTypeLabel.raise_()
        self.classSocietyLabel.raise_()
        self.emailEdit.raise_()
        self.imoNumberLabel.raise_()
        self.modelEdit.raise_()
        self.depthMoulded.raise_()
        self.loaEdit.raise_()
        self.igtLabel.raise_()
        self.ecdisMakerEdit.raise_()
        self.classSocietyEdit.raise_()
        self.lbpEdit.raise_()
        self.emailLabel.raise_()
        self.taxNumberLabel.raise_()
        self.portRegistryLabel.raise_()
        self.shipNameLabel.raise_()
        self.breadthMouldedEdit.raise_()
        self.faxEdit.raise_()
        self.shipTypeComboBox.raise_()
        self.callSignLabel.raise_()
        self.portRegistryEdit.raise_()
        self.shipNameEdit.raise_()
        self.intEdit.raise_()
        self.igtEdit.raise_()
        self.intLabel.raise_()
        self.label.raise_()
        self.captain_name_edit.raise_()
        self.label_2.raise_()
        self.captain_crew_id_edit.raise_()
        self.verticalLayout.addWidget(self.groupBox)
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.questionLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.questionLabel.sizePolicy().hasHeightForWidth())
        self.questionLabel.setSizePolicy(sizePolicy)
        self.questionLabel.setObjectName(_fromUtf8("questionLabel"))
        self.horizontalLayout_2.addWidget(self.questionLabel)
        self.yesRadioBtn = QtGui.QRadioButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yesRadioBtn.sizePolicy().hasHeightForWidth())
        self.yesRadioBtn.setSizePolicy(sizePolicy)
        self.yesRadioBtn.setObjectName(_fromUtf8("yesRadioBtn"))
        self.horizontalLayout_2.addWidget(self.yesRadioBtn)
        self.noRadioBtn = QtGui.QRadioButton(self.widget)
        self.noRadioBtn.setObjectName(_fromUtf8("noRadioBtn"))
        self.horizontalLayout_2.addWidget(self.noRadioBtn)
        self.verticalLayout.addWidget(self.widget)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.meBandLabel = QtGui.QLabel(self.groupBox_2)
        self.meBandLabel.setObjectName(_fromUtf8("meBandLabel"))
        self.gridLayout_2.addWidget(self.meBandLabel, 0, 0, 1, 1)
        self.meModelLabel = QtGui.QLabel(self.groupBox_2)
        self.meModelLabel.setObjectName(_fromUtf8("meModelLabel"))
        self.gridLayout_2.addWidget(self.meModelLabel, 1, 0, 1, 1)
        self.meModelEdit = QtGui.QLineEdit(self.groupBox_2)
        self.meModelEdit.setObjectName(_fromUtf8("meModelEdit"))
        self.gridLayout_2.addWidget(self.meModelEdit, 1, 1, 1, 1)
        self.meMakerEdit = QtGui.QLineEdit(self.groupBox_2)
        self.meMakerEdit.setObjectName(_fromUtf8("meMakerEdit"))
        self.gridLayout_2.addWidget(self.meMakerEdit, 0, 1, 1, 1)
        self.meTableWidget = QtGui.QTableWidget(self.groupBox_2)
        self.meTableWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.meTableWidget.setObjectName(_fromUtf8("meTableWidget"))
        self.meTableWidget.setColumnCount(5)
        self.meTableWidget.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.meTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.meTableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.meTableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.meTableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.meTableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.meTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.meTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.meTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.meTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.meTableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(1, 4, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(2, 3, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(2, 4, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(3, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(3, 3, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(3, 4, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(4, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(4, 3, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.meTableWidget.setItem(4, 4, item)
        self.meTableWidget.horizontalHeader().setVisible(True)
        self.meTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.meTableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.meTableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.meTableWidget.horizontalHeader().setStretchLastSection(True)
        self.meTableWidget.verticalHeader().setVisible(True)
        self.meTableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.meTableWidget.verticalHeader().setDefaultSectionSize(50)
        self.meTableWidget.verticalHeader().setHighlightSections(True)
        self.meTableWidget.verticalHeader().setMinimumSectionSize(50)
        self.meTableWidget.verticalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.meTableWidget, 2, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.submitButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)
        self.submitButton.setCheckable(False)
        self.submitButton.setAutoDefault(False)
        self.submitButton.setDefault(False)
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.horizontalLayout.addWidget(self.submitButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.shipNameLabel.setBuddy(self.shipNameEdit)
        self.callSignLabel.setBuddy(self.callSignEdit)
        self.imoNumberLabel.setBuddy(self.imoNumberEdit)
        self.portRegistryLabel.setBuddy(self.portRegistryEdit)
        self.companyNameLabel.setBuddy(self.companyNameEdit)
        self.classSocietyLabel.setBuddy(self.classSocietyEdit)
        self.emailLabel.setBuddy(self.emailEdit)
        self.telLabel.setBuddy(self.telEdit)
        self.taxNumberLabel.setBuddy(self.faxEdit)
        self.shipTypeLabel.setBuddy(self.shipTypeComboBox)
        self.igtLabel.setBuddy(self.igtEdit)
        self.intLabel.setBuddy(self.intEdit)
        self.loaLabel.setBuddy(self.loaEdit)
        self.lbpLabel.setBuddy(self.lbpEdit)
        self.breadthMouldedLabel.setBuddy(self.breadthMouldedEdit)
        self.depthMoulded.setBuddy(self.depthMouldedEdit)
        self.ecdisMakerLabel.setBuddy(self.ecdisMakerEdit)
        self.modelLabel.setBuddy(self.modelEdit)
        self.label.setBuddy(self.captain_name_edit)
        self.label_2.setBuddy(self.captain_crew_id_edit)
        self.meBandLabel.setBuddy(self.meMakerEdit)
        self.meModelLabel.setBuddy(self.meModelEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.shipNameEdit, self.callSignEdit)
        Form.setTabOrder(self.callSignEdit, self.imoNumberEdit)
        Form.setTabOrder(self.imoNumberEdit, self.portRegistryEdit)
        Form.setTabOrder(self.portRegistryEdit, self.companyNameEdit)
        Form.setTabOrder(self.companyNameEdit, self.classSocietyEdit)
        Form.setTabOrder(self.classSocietyEdit, self.emailEdit)
        Form.setTabOrder(self.emailEdit, self.telEdit)
        Form.setTabOrder(self.telEdit, self.faxEdit)
        Form.setTabOrder(self.faxEdit, self.shipTypeComboBox)
        Form.setTabOrder(self.shipTypeComboBox, self.igtEdit)
        Form.setTabOrder(self.igtEdit, self.intEdit)
        Form.setTabOrder(self.intEdit, self.loaEdit)
        Form.setTabOrder(self.loaEdit, self.lbpEdit)
        Form.setTabOrder(self.lbpEdit, self.breadthMouldedEdit)
        Form.setTabOrder(self.breadthMouldedEdit, self.depthMouldedEdit)
        Form.setTabOrder(self.depthMouldedEdit, self.ecdisMakerEdit)
        Form.setTabOrder(self.ecdisMakerEdit, self.modelEdit)
        Form.setTabOrder(self.modelEdit, self.captain_name_edit)
        Form.setTabOrder(self.captain_name_edit, self.captain_crew_id_edit)
        Form.setTabOrder(self.captain_crew_id_edit, self.yesRadioBtn)
        Form.setTabOrder(self.yesRadioBtn, self.noRadioBtn)
        Form.setTabOrder(self.noRadioBtn, self.meMakerEdit)
        Form.setTabOrder(self.meMakerEdit, self.meModelEdit)
        Form.setTabOrder(self.meModelEdit, self.meTableWidget)
        Form.setTabOrder(self.meTableWidget, self.submitButton)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Initial Report", None))
        self.groupBox.setTitle(_translate("Form", "Initial Report", None))
        self.shipNameLabel.setText(_translate("Form", "Ship Name", None))
        self.callSignLabel.setText(_translate("Form", "Call Sign", None))
        self.imoNumberLabel.setText(_translate("Form", "IMO Number", None))
        self.portRegistryLabel.setText(_translate("Form", "Port of Registry", None))
        self.companyNameLabel.setText(_translate("Form", "Company Name", None))
        self.classSocietyLabel.setText(_translate("Form", "Class Society", None))
        self.emailLabel.setText(_translate("Form", "E-mail Address", None))
        self.telLabel.setText(_translate("Form", "Telephone Number", None))
        self.taxNumberLabel.setText(_translate("Form", "Fax Number", None))
        self.shipTypeLabel.setText(_translate("Form", "Ship Type", None))
        self.shipTypeComboBox.setItemText(0, _translate("Form", "Bulk Carrier", None))
        self.shipTypeComboBox.setItemText(1, _translate("Form", "Chemical Tanker", None))
        self.shipTypeComboBox.setItemText(2, _translate("Form", "Container Ship", None))
        self.shipTypeComboBox.setItemText(3, _translate("Form", "General Cargo", None))
        self.shipTypeComboBox.setItemText(4, _translate("Form", "LNG/LPG", None))
        self.shipTypeComboBox.setItemText(5, _translate("Form", "O.B.O", None))
        self.shipTypeComboBox.setItemText(6, _translate("Form", "Oil Tanker", None))
        self.shipTypeComboBox.setItemText(7, _translate("Form", "Passager Ship", None))
        self.shipTypeComboBox.setItemText(8, _translate("Form", "Roll On/Off", None))
        self.shipTypeComboBox.setItemText(9, _translate("Form", "Other", None))
        self.igtLabel.setText(_translate("Form", "International Gross Tonnage(t)", None))
        self.intLabel.setText(_translate("Form", "International Net Tonnage(t)", None))
        self.loaLabel.setText(_translate("Form", "LOA (m)", None))
        self.lbpLabel.setText(_translate("Form", "LBP (m)", None))
        self.breadthMouldedLabel.setText(_translate("Form", "Breadth Moulded (m)", None))
        self.depthMoulded.setText(_translate("Form", "Depth Moulded (m)", None))
        self.ecdisMakerLabel.setText(_translate("Form", "ECDIS Maker", None))
        self.modelLabel.setText(_translate("Form", "ECDIS Model", None))
        self.label.setText(_translate("Form", "Captain Name", None))
        self.label_2.setText(_translate("Form", "Captain Crew ID", None))
        self.questionLabel.setText(_translate("Form", "Do you maintain paper chart onboard ?", None))
        self.yesRadioBtn.setText(_translate("Form", "Yes", None))
        self.noRadioBtn.setText(_translate("Form", "No", None))
        self.groupBox_2.setTitle(_translate("Form", "M/E Particular", None))
        self.meBandLabel.setText(_translate("Form", "Maker", None))
        self.meModelLabel.setText(_translate("Form", "Model", None))
        item = self.meTableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "D/Slow", None))
        item = self.meTableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "Slow", None))
        item = self.meTableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "Half", None))
        item = self.meTableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "Full", None))
        item = self.meTableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "Nav.Full", None))
        item = self.meTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "RPM", None))
        item = self.meTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Ballast Speed", None))
        item = self.meTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Ballast Slip", None))
        item = self.meTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Load Speed", None))
        item = self.meTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Load Slip", None))
        __sortingEnabled = self.meTableWidget.isSortingEnabled()
        self.meTableWidget.setSortingEnabled(False)
        self.meTableWidget.setSortingEnabled(__sortingEnabled)
        self.submitButton.setText(_translate("Form", "Submit", None))

