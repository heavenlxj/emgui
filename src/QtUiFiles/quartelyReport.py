# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quartelyReport.ui'
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
        Form.resize(1096, 771)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.ship_name_edit = QtGui.QLineEdit(Form)
        self.ship_name_edit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ship_name_edit.sizePolicy().hasHeightForWidth())
        self.ship_name_edit.setSizePolicy(sizePolicy)
        self.ship_name_edit.setObjectName(_fromUtf8("ship_name_edit"))
        self.horizontalLayout.addWidget(self.ship_name_edit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.call_sign_edit = QtGui.QLineEdit(Form)
        self.call_sign_edit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.call_sign_edit.sizePolicy().hasHeightForWidth())
        self.call_sign_edit.setSizePolicy(sizePolicy)
        self.call_sign_edit.setObjectName(_fromUtf8("call_sign_edit"))
        self.horizontalLayout.addWidget(self.call_sign_edit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_3 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.captain_name_edit = QtGui.QLineEdit(Form)
        self.captain_name_edit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.captain_name_edit.sizePolicy().hasHeightForWidth())
        self.captain_name_edit.setSizePolicy(sizePolicy)
        self.captain_name_edit.setObjectName(_fromUtf8("captain_name_edit"))
        self.horizontalLayout.addWidget(self.captain_name_edit)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_4 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.date_edit = QtGui.QLineEdit(Form)
        self.date_edit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_edit.sizePolicy().hasHeightForWidth())
        self.date_edit.setSizePolicy(sizePolicy)
        self.date_edit.setObjectName(_fromUtf8("date_edit"))
        self.horizontalLayout.addWidget(self.date_edit)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.year_combo = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.year_combo.sizePolicy().hasHeightForWidth())
        self.year_combo.setSizePolicy(sizePolicy)
        self.year_combo.setObjectName(_fromUtf8("year_combo"))
        self.horizontalLayout_2.addWidget(self.year_combo)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_6 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.quarter_combo = QtGui.QComboBox(Form)
        self.quarter_combo.setObjectName(_fromUtf8("quarter_combo"))
        self.horizontalLayout_2.addWidget(self.quarter_combo)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.cargo_table_widget = QtGui.QTableWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cargo_table_widget.sizePolicy().hasHeightForWidth())
        self.cargo_table_widget.setSizePolicy(sizePolicy)
        self.cargo_table_widget.setRowCount(15)
        self.cargo_table_widget.setObjectName(_fromUtf8("cargo_table_widget"))
        self.cargo_table_widget.setColumnCount(11)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.cargo_table_widget.setHorizontalHeaderItem(10, item)
        self.cargo_table_widget.horizontalHeader().setDefaultSectionSize(120)
        self.cargo_table_widget.horizontalHeader().setStretchLastSection(True)
        self.cargo_table_widget.verticalHeader().setVisible(False)
        self.cargo_table_widget.verticalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.cargo_table_widget)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tfc_table_widget = QtGui.QTableWidget(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tfc_table_widget.sizePolicy().hasHeightForWidth())
        self.tfc_table_widget.setSizePolicy(sizePolicy)
        self.tfc_table_widget.setObjectName(_fromUtf8("tfc_table_widget"))
        self.tfc_table_widget.setColumnCount(12)
        self.tfc_table_widget.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tfc_table_widget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tfc_table_widget.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tfc_table_widget.setItem(0, 8, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setItem(1, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setItem(1, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setItem(1, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setItem(1, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setItem(1, 8, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setItem(1, 9, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setItem(1, 10, item)
        item = QtGui.QTableWidgetItem()
        self.tfc_table_widget.setItem(1, 11, item)
        self.tfc_table_widget.horizontalHeader().setVisible(False)
        self.tfc_table_widget.verticalHeader().setVisible(False)
        self.tfc_table_widget.verticalHeader().setDefaultSectionSize(50)
        self.tfc_table_widget.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.tfc_table_widget)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.reload_btn = QtGui.QPushButton(Form)
        self.reload_btn.setObjectName(_fromUtf8("reload_btn"))
        self.horizontalLayout_5.addWidget(self.reload_btn)
        self.submit_btn = QtGui.QPushButton(Form)
        self.submit_btn.setObjectName(_fromUtf8("submit_btn"))
        self.horizontalLayout_5.addWidget(self.submit_btn)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Ship Name", None))
        self.label_2.setText(_translate("Form", "Call Sign", None))
        self.label_3.setText(_translate("Form", "Captain Name", None))
        self.label_4.setText(_translate("Form", "Date", None))
        self.label_5.setText(_translate("Form", "Year     ", None))
        self.label_6.setText(_translate("Form", "Quarter   ", None))
        self.pushButton.setText(_translate("Form", "Add New Row", None))
        self.pushButton_2.setText(_translate("Form", "Delete Row", None))
        item = self.cargo_table_widget.verticalHeaderItem(0)
        item.setText(_translate("Form", "新建行", None))
        item = self.cargo_table_widget.verticalHeaderItem(1)
        item.setText(_translate("Form", "新建行", None))
        item = self.cargo_table_widget.verticalHeaderItem(2)
        item.setText(_translate("Form", "新建行", None))
        item = self.cargo_table_widget.verticalHeaderItem(3)
        item.setText(_translate("Form", "新建行", None))
        item = self.cargo_table_widget.verticalHeaderItem(4)
        item.setText(_translate("Form", "新建行", None))
        item = self.cargo_table_widget.verticalHeaderItem(5)
        item.setText(_translate("Form", "新建行", None))
        item = self.cargo_table_widget.verticalHeaderItem(6)
        item.setText(_translate("Form", "新建行", None))
        item = self.cargo_table_widget.verticalHeaderItem(7)
        item.setText(_translate("Form", "新建行", None))
        item = self.cargo_table_widget.verticalHeaderItem(8)
        item.setText(_translate("Form", "新建行", None))
        item = self.cargo_table_widget.verticalHeaderItem(9)
        item.setText(_translate("Form", "新建行", None))
        item = self.cargo_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Cargo", None))
        item = self.cargo_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Cargo Weight", None))
        item = self.cargo_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Distance Travelled", None))
        item = self.cargo_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Distance By \n"
"M/E Revoluation (NM)", None))
        item = self.cargo_table_widget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "M/E Average RPM", None))
        item = self.cargo_table_widget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Average Slip", None))
        item = self.cargo_table_widget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "IFO", None))
        item = self.cargo_table_widget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "LSFO", None))
        item = self.cargo_table_widget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "MDO", None))
        item = self.cargo_table_widget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "LSMDO", None))
        item = self.cargo_table_widget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Performance \n"
"Effciency", None))
        item = self.tfc_table_widget.verticalHeaderItem(0)
        item.setText(_translate("Form", "新建行", None))
        item = self.tfc_table_widget.verticalHeaderItem(1)
        item.setText(_translate("Form", "新建行", None))
        item = self.tfc_table_widget.verticalHeaderItem(2)
        item.setText(_translate("Form", "新建行", None))
        item = self.tfc_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "新建列", None))
        item = self.tfc_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "新建列", None))
        item = self.tfc_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "新建列", None))
        item = self.tfc_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "新建列", None))
        item = self.tfc_table_widget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "新建列", None))
        item = self.tfc_table_widget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "新建列", None))
        item = self.tfc_table_widget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "新建列", None))
        item = self.tfc_table_widget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "新建列", None))
        item = self.tfc_table_widget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "新建列", None))
        item = self.tfc_table_widget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "新建列", None))
        item = self.tfc_table_widget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "新建列", None))
        item = self.tfc_table_widget.horizontalHeaderItem(11)
        item.setText(_translate("Form", "新建列", None))
        __sortingEnabled = self.tfc_table_widget.isSortingEnabled()
        self.tfc_table_widget.setSortingEnabled(False)
        item = self.tfc_table_widget.item(0, 0)
        item.setText(_translate("Form", "Total Fuel Consumption", None))
        item = self.tfc_table_widget.item(0, 4)
        item.setText(_translate("Form", "Total Fuel Supplied", None))
        item = self.tfc_table_widget.item(0, 8)
        item.setText(_translate("Form", "Total Fuel R.O.B", None))
        item = self.tfc_table_widget.item(1, 0)
        item.setText(_translate("Form", "IFO", None))
        item = self.tfc_table_widget.item(1, 1)
        item.setText(_translate("Form", "LSFO", None))
        item = self.tfc_table_widget.item(1, 2)
        item.setText(_translate("Form", "MDO", None))
        item = self.tfc_table_widget.item(1, 3)
        item.setText(_translate("Form", "LSMDO", None))
        item = self.tfc_table_widget.item(1, 4)
        item.setText(_translate("Form", "IFO", None))
        item = self.tfc_table_widget.item(1, 5)
        item.setText(_translate("Form", "LSFO", None))
        item = self.tfc_table_widget.item(1, 6)
        item.setText(_translate("Form", "MDO", None))
        item = self.tfc_table_widget.item(1, 7)
        item.setText(_translate("Form", "LSMDO", None))
        item = self.tfc_table_widget.item(1, 8)
        item.setText(_translate("Form", "IFO", None))
        item = self.tfc_table_widget.item(1, 9)
        item.setText(_translate("Form", "LSFO", None))
        item = self.tfc_table_widget.item(1, 10)
        item.setText(_translate("Form", "MDO", None))
        item = self.tfc_table_widget.item(1, 11)
        item.setText(_translate("Form", "LSMDO", None))
        self.tfc_table_widget.setSortingEnabled(__sortingEnabled)
        self.reload_btn.setText(_translate("Form", "Reload", None))
        self.submit_btn.setText(_translate("Form", "Submit", None))

