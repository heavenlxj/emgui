# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'objectionReport.ui'
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
        Form.resize(836, 711)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
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
        self.label_2 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
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
        self.label_3 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.voyage_number_edit = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voyage_number_edit.sizePolicy().hasHeightForWidth())
        self.voyage_number_edit.setSizePolicy(sizePolicy)
        self.voyage_number_edit.setObjectName(_fromUtf8("voyage_number_edit"))
        self.horizontalLayout.addWidget(self.voyage_number_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.captain_name_edit = QtGui.QLineEdit(Form)
        self.captain_name_edit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.captain_name_edit.sizePolicy().hasHeightForWidth())
        self.captain_name_edit.setSizePolicy(sizePolicy)
        self.captain_name_edit.setObjectName(_fromUtf8("captain_name_edit"))
        self.horizontalLayout_2.addWidget(self.captain_name_edit)
        self.label_6 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.date_edit = QtGui.QLineEdit(Form)
        self.date_edit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_edit.sizePolicy().hasHeightForWidth())
        self.date_edit.setSizePolicy(sizePolicy)
        self.date_edit.setObjectName(_fromUtf8("date_edit"))
        self.horizontalLayout_2.addWidget(self.date_edit)
        self.label_4 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.route_id_number = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.route_id_number.sizePolicy().hasHeightForWidth())
        self.route_id_number.setSizePolicy(sizePolicy)
        self.route_id_number.setObjectName(_fromUtf8("route_id_number"))
        self.horizontalLayout_2.addWidget(self.route_id_number)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.remove_btn = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_btn.sizePolicy().hasHeightForWidth())
        self.remove_btn.setSizePolicy(sizePolicy)
        self.remove_btn.setObjectName(_fromUtf8("remove_btn"))
        self.gridLayout_3.addWidget(self.remove_btn, 2, 1, 1, 1)
        self.add_new_btn = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_new_btn.sizePolicy().hasHeightForWidth())
        self.add_new_btn.setSizePolicy(sizePolicy)
        self.add_new_btn.setObjectName(_fromUtf8("add_new_btn"))
        self.gridLayout_3.addWidget(self.add_new_btn, 1, 1, 1, 1)
        self.route_table_widget = QtGui.QTableWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.route_table_widget.sizePolicy().hasHeightForWidth())
        self.route_table_widget.setSizePolicy(sizePolicy)
        self.route_table_widget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.route_table_widget.setTextElideMode(QtCore.Qt.ElideRight)
        self.route_table_widget.setObjectName(_fromUtf8("route_table_widget"))
        self.route_table_widget.setColumnCount(3)
        self.route_table_widget.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.route_table_widget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.route_table_widget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.route_table_widget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.route_table_widget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.route_table_widget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.route_table_widget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.route_table_widget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.route_table_widget.setHorizontalHeaderItem(2, item)
        self.route_table_widget.horizontalHeader().setCascadingSectionResizes(True)
        self.route_table_widget.horizontalHeader().setDefaultSectionSize(200)
        self.route_table_widget.horizontalHeader().setMinimumSectionSize(100)
        self.route_table_widget.horizontalHeader().setStretchLastSection(True)
        self.route_table_widget.verticalHeader().setVisible(False)
        self.route_table_widget.verticalHeader().setCascadingSectionResizes(True)
        self.route_table_widget.verticalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.route_table_widget, 1, 0, 4, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.checkBox_ukc = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ukc.sizePolicy().hasHeightForWidth())
        self.checkBox_ukc.setSizePolicy(sizePolicy)
        self.checkBox_ukc.setObjectName(_fromUtf8("checkBox_ukc"))
        self.verticalLayout_2.addWidget(self.checkBox_ukc)
        self.checkBox_water_depth = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_water_depth.sizePolicy().hasHeightForWidth())
        self.checkBox_water_depth.setSizePolicy(sizePolicy)
        self.checkBox_water_depth.setObjectName(_fromUtf8("checkBox_water_depth"))
        self.verticalLayout_2.addWidget(self.checkBox_water_depth)
        self.checkBox_violate_local = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_violate_local.sizePolicy().hasHeightForWidth())
        self.checkBox_violate_local.setSizePolicy(sizePolicy)
        self.checkBox_violate_local.setObjectName(_fromUtf8("checkBox_violate_local"))
        self.verticalLayout_2.addWidget(self.checkBox_violate_local)
        self.checkBox_safety_margin = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_safety_margin.sizePolicy().hasHeightForWidth())
        self.checkBox_safety_margin.setSizePolicy(sizePolicy)
        self.checkBox_safety_margin.setObjectName(_fromUtf8("checkBox_safety_margin"))
        self.verticalLayout_2.addWidget(self.checkBox_safety_margin)
        self.checkBox_ntm_navtex_egc = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ntm_navtex_egc.sizePolicy().hasHeightForWidth())
        self.checkBox_ntm_navtex_egc.setSizePolicy(sizePolicy)
        self.checkBox_ntm_navtex_egc.setObjectName(_fromUtf8("checkBox_ntm_navtex_egc"))
        self.verticalLayout_2.addWidget(self.checkBox_ntm_navtex_egc)
        self.checkBox_heavy_traffic = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_heavy_traffic.sizePolicy().hasHeightForWidth())
        self.checkBox_heavy_traffic.setSizePolicy(sizePolicy)
        self.checkBox_heavy_traffic.setObjectName(_fromUtf8("checkBox_heavy_traffic"))
        self.verticalLayout_2.addWidget(self.checkBox_heavy_traffic)
        self.checkBox_others = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_others.sizePolicy().hasHeightForWidth())
        self.checkBox_others.setSizePolicy(sizePolicy)
        self.checkBox_others.setObjectName(_fromUtf8("checkBox_others"))
        self.verticalLayout_2.addWidget(self.checkBox_others)
        self.textEdit_remark = QtGui.QTextEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_remark.sizePolicy().hasHeightForWidth())
        self.textEdit_remark.setSizePolicy(sizePolicy)
        self.textEdit_remark.setObjectName(_fromUtf8("textEdit_remark"))
        self.verticalLayout_2.addWidget(self.textEdit_remark)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.reload_btn = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reload_btn.sizePolicy().hasHeightForWidth())
        self.reload_btn.setSizePolicy(sizePolicy)
        self.reload_btn.setObjectName(_fromUtf8("reload_btn"))
        self.horizontalLayout_3.addWidget(self.reload_btn)
        self.submit_btn = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_btn.sizePolicy().hasHeightForWidth())
        self.submit_btn.setSizePolicy(sizePolicy)
        self.submit_btn.setObjectName(_fromUtf8("submit_btn"))
        self.horizontalLayout_3.addWidget(self.submit_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label.setBuddy(self.ship_name_edit)
        self.label_2.setBuddy(self.call_sign_edit)
        self.label_3.setBuddy(self.voyage_number_edit)
        self.label_5.setBuddy(self.captain_name_edit)
        self.label_6.setBuddy(self.date_edit)
        self.label_4.setBuddy(self.route_id_number)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Objection Report", None))
        self.label.setText(_translate("Form", "Ship Name", None))
        self.label_2.setText(_translate("Form", "Call Sign", None))
        self.label_3.setText(_translate("Form", "Voyage Number", None))
        self.label_5.setText(_translate("Form", "Captain Name", None))
        self.label_6.setText(_translate("Form", "Date", None))
        self.label_4.setText(_translate("Form", "Route\'s ID number", None))
        self.groupBox_2.setTitle(_translate("Form", "Route", None))
        self.remove_btn.setText(_translate("Form", "Remove", None))
        self.add_new_btn.setText(_translate("Form", " Add", None))
        item = self.route_table_widget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.route_table_widget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2", None))
        item = self.route_table_widget.verticalHeaderItem(2)
        item.setText(_translate("Form", "3", None))
        item = self.route_table_widget.verticalHeaderItem(3)
        item.setText(_translate("Form", "4", None))
        item = self.route_table_widget.verticalHeaderItem(4)
        item.setText(_translate("Form", "5", None))
        item = self.route_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Id", None))
        item = self.route_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Latitude", None))
        item = self.route_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Longtitue", None))
        self.label_7.setText(_translate("Form", "Navigation hazard exist along the route at position:", None))
        self.groupBox.setTitle(_translate("Form", "Reason of objection", None))
        self.checkBox_ukc.setText(_translate("Form", "Insufficient UKC", None))
        self.checkBox_water_depth.setText(_translate("Form", "Insufficient water depth", None))
        self.checkBox_violate_local.setText(_translate("Form", "Violate international or local regulation/low", None))
        self.checkBox_safety_margin.setText(_translate("Form", "Insufficient safety margin from navigation hazard", None))
        self.checkBox_ntm_navtex_egc.setText(_translate("Form", "New navigation hazard affected by NTM/Navtex/EGC", None))
        self.checkBox_heavy_traffic.setText(_translate("Form", "Heavy traffic that cause concer", None))
        self.checkBox_others.setText(_translate("Form", "Others", None))
        self.reload_btn.setText(_translate("Form", "Reload", None))
        self.submit_btn.setText(_translate("Form", "Submit", None))

