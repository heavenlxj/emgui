# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'requestRoute.ui'
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
        Form.resize(789, 766)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout_7 = QtGui.QGridLayout(Form)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_6 = QtGui.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_shipName = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_shipName.sizePolicy().hasHeightForWidth())
        self.label_shipName.setSizePolicy(sizePolicy)
        self.label_shipName.setObjectName(_fromUtf8("label_shipName"))
        self.horizontalLayout_3.addWidget(self.label_shipName)
        self.ship_name_edit = QtGui.QLineEdit(self.frame)
        self.ship_name_edit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ship_name_edit.sizePolicy().hasHeightForWidth())
        self.ship_name_edit.setSizePolicy(sizePolicy)
        self.ship_name_edit.setObjectName(_fromUtf8("ship_name_edit"))
        self.horizontalLayout_3.addWidget(self.ship_name_edit)
        self.label_callSign = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_callSign.sizePolicy().hasHeightForWidth())
        self.label_callSign.setSizePolicy(sizePolicy)
        self.label_callSign.setObjectName(_fromUtf8("label_callSign"))
        self.horizontalLayout_3.addWidget(self.label_callSign)
        self.call_sign_edit = QtGui.QLineEdit(self.frame)
        self.call_sign_edit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.call_sign_edit.sizePolicy().hasHeightForWidth())
        self.call_sign_edit.setSizePolicy(sizePolicy)
        self.call_sign_edit.setObjectName(_fromUtf8("call_sign_edit"))
        self.horizontalLayout_3.addWidget(self.call_sign_edit)
        self.label_date = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date.sizePolicy().hasHeightForWidth())
        self.label_date.setSizePolicy(sizePolicy)
        self.label_date.setObjectName(_fromUtf8("label_date"))
        self.horizontalLayout_3.addWidget(self.label_date)
        self.date_edit = QtGui.QLineEdit(self.frame)
        self.date_edit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_edit.sizePolicy().hasHeightForWidth())
        self.date_edit.setSizePolicy(sizePolicy)
        self.date_edit.setObjectName(_fromUtf8("date_edit"))
        self.horizontalLayout_3.addWidget(self.date_edit)
        self.label_voyageNumber = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_voyageNumber.sizePolicy().hasHeightForWidth())
        self.label_voyageNumber.setSizePolicy(sizePolicy)
        self.label_voyageNumber.setObjectName(_fromUtf8("label_voyageNumber"))
        self.horizontalLayout_3.addWidget(self.label_voyageNumber)
        self.voyage_number_edit = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voyage_number_edit.sizePolicy().hasHeightForWidth())
        self.voyage_number_edit.setSizePolicy(sizePolicy)
        self.voyage_number_edit.setObjectName(_fromUtf8("voyage_number_edit"))
        self.horizontalLayout_3.addWidget(self.voyage_number_edit)
        self.gridLayout_6.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.arrival_date_edit = QtGui.QDateEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arrival_date_edit.sizePolicy().hasHeightForWidth())
        self.arrival_date_edit.setSizePolicy(sizePolicy)
        self.arrival_date_edit.setCalendarPopup(True)
        self.arrival_date_edit.setObjectName(_fromUtf8("arrival_date_edit"))
        self.horizontalLayout_8.addWidget(self.arrival_date_edit)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_8.addWidget(self.label_9)
        self.arrival_time_edit = QtGui.QTimeEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arrival_time_edit.sizePolicy().hasHeightForWidth())
        self.arrival_time_edit.setSizePolicy(sizePolicy)
        self.arrival_time_edit.setCalendarPopup(True)
        self.arrival_time_edit.setObjectName(_fromUtf8("arrival_time_edit"))
        self.horizontalLayout_8.addWidget(self.arrival_time_edit)
        self.label_16 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_8.addWidget(self.label_16)
        self.arrival_unlo_edit = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arrival_unlo_edit.sizePolicy().hasHeightForWidth())
        self.arrival_unlo_edit.setSizePolicy(sizePolicy)
        self.arrival_unlo_edit.setObjectName(_fromUtf8("arrival_unlo_edit"))
        self.horizontalLayout_8.addWidget(self.arrival_unlo_edit)
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_8.addWidget(self.label_17)
        self.arrival_terminal_edit = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arrival_terminal_edit.sizePolicy().hasHeightForWidth())
        self.arrival_terminal_edit.setSizePolicy(sizePolicy)
        self.arrival_terminal_edit.setObjectName(_fromUtf8("arrival_terminal_edit"))
        self.horizontalLayout_8.addWidget(self.arrival_terminal_edit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_9.addWidget(self.label_14)
        self.arrival_country_combo = QtGui.QComboBox(self.groupBox_3)
        self.arrival_country_combo.setEditable(True)
        self.arrival_country_combo.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.arrival_country_combo.setObjectName(_fromUtf8("arrival_country_combo"))
        self.horizontalLayout_9.addWidget(self.arrival_country_combo)
        self.label_15 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_9.addWidget(self.label_15)
        self.arrival_port_combo = QtGui.QComboBox(self.groupBox_3)
        self.arrival_port_combo.setEditable(True)
        self.arrival_port_combo.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.arrival_port_combo.setObjectName(_fromUtf8("arrival_port_combo"))
        self.horizontalLayout_9.addWidget(self.arrival_port_combo)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.gridLayout_5.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.via_name_edit = QtGui.QLineEdit(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.via_name_edit.sizePolicy().hasHeightForWidth())
        self.via_name_edit.setSizePolicy(sizePolicy)
        self.via_name_edit.setObjectName(_fromUtf8("via_name_edit"))
        self.verticalLayout.addWidget(self.via_name_edit)
        self.via_listWidget = QtGui.QListWidget(self.groupBox_4)
        self.via_listWidget.setObjectName(_fromUtf8("via_listWidget"))
        self.verticalLayout.addWidget(self.via_listWidget)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.via_add_btn = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.via_add_btn.sizePolicy().hasHeightForWidth())
        self.via_add_btn.setSizePolicy(sizePolicy)
        self.via_add_btn.setObjectName(_fromUtf8("via_add_btn"))
        self.verticalLayout_2.addWidget(self.via_add_btn)
        self.via_remove_btn = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.via_remove_btn.sizePolicy().hasHeightForWidth())
        self.via_remove_btn.setSizePolicy(sizePolicy)
        self.via_remove_btn.setObjectName(_fromUtf8("via_remove_btn"))
        self.verticalLayout_2.addWidget(self.via_remove_btn)
        self.via_up_btn = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.via_up_btn.sizePolicy().hasHeightForWidth())
        self.via_up_btn.setSizePolicy(sizePolicy)
        self.via_up_btn.setObjectName(_fromUtf8("via_up_btn"))
        self.verticalLayout_2.addWidget(self.via_up_btn)
        self.via_down_btn = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.via_down_btn.sizePolicy().hasHeightForWidth())
        self.via_down_btn.setSizePolicy(sizePolicy)
        self.via_down_btn.setObjectName(_fromUtf8("via_down_btn"))
        self.verticalLayout_2.addWidget(self.via_down_btn)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.groupBox)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_question = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_question.sizePolicy().hasHeightForWidth())
        self.label_question.setSizePolicy(sizePolicy)
        self.label_question.setObjectName(_fromUtf8("label_question"))
        self.horizontalLayout_4.addWidget(self.label_question)
        self.use_dw_route_yes_radio = QtGui.QRadioButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.use_dw_route_yes_radio.sizePolicy().hasHeightForWidth())
        self.use_dw_route_yes_radio.setSizePolicy(sizePolicy)
        self.use_dw_route_yes_radio.setObjectName(_fromUtf8("use_dw_route_yes_radio"))
        self.horizontalLayout_4.addWidget(self.use_dw_route_yes_radio)
        self.use_dw_route_no_radio = QtGui.QRadioButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.use_dw_route_no_radio.sizePolicy().hasHeightForWidth())
        self.use_dw_route_no_radio.setSizePolicy(sizePolicy)
        self.use_dw_route_no_radio.setObjectName(_fromUtf8("use_dw_route_no_radio"))
        self.horizontalLayout_4.addWidget(self.use_dw_route_no_radio)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.prefer_route_type_combo = QtGui.QComboBox(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefer_route_type_combo.sizePolicy().hasHeightForWidth())
        self.prefer_route_type_combo.setSizePolicy(sizePolicy)
        self.prefer_route_type_combo.setObjectName(_fromUtf8("prefer_route_type_combo"))
        self.prefer_route_type_combo.addItem(_fromUtf8(""))
        self.prefer_route_type_combo.addItem(_fromUtf8(""))
        self.prefer_route_type_combo.addItem(_fromUtf8(""))
        self.prefer_route_type_combo.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.prefer_route_type_combo)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_maxDraft = QtGui.QLabel(self.frame_2)
        self.label_maxDraft.setObjectName(_fromUtf8("label_maxDraft"))
        self.horizontalLayout_5.addWidget(self.label_maxDraft)
        self.maximum_draft_edit = QtGui.QLineEdit(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maximum_draft_edit.sizePolicy().hasHeightForWidth())
        self.maximum_draft_edit.setSizePolicy(sizePolicy)
        self.maximum_draft_edit.setObjectName(_fromUtf8("maximum_draft_edit"))
        self.horizontalLayout_5.addWidget(self.maximum_draft_edit)
        self.label_loadCondition = QtGui.QLabel(self.frame_2)
        self.label_loadCondition.setObjectName(_fromUtf8("label_loadCondition"))
        self.horizontalLayout_5.addWidget(self.label_loadCondition)
        self.load_condition_edit = QtGui.QLineEdit(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_condition_edit.sizePolicy().hasHeightForWidth())
        self.load_condition_edit.setSizePolicy(sizePolicy)
        self.load_condition_edit.setObjectName(_fromUtf8("load_condition_edit"))
        self.horizontalLayout_5.addWidget(self.load_condition_edit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_speedSetting = QtGui.QLabel(self.frame_2)
        self.label_speedSetting.setObjectName(_fromUtf8("label_speedSetting"))
        self.horizontalLayout_11.addWidget(self.label_speedSetting)
        self.speed_setting_edit = QtGui.QLineEdit(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_setting_edit.sizePolicy().hasHeightForWidth())
        self.speed_setting_edit.setSizePolicy(sizePolicy)
        self.speed_setting_edit.setObjectName(_fromUtf8("speed_setting_edit"))
        self.horizontalLayout_11.addWidget(self.speed_setting_edit)
        self.label_etd = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_etd.sizePolicy().hasHeightForWidth())
        self.label_etd.setSizePolicy(sizePolicy)
        self.label_etd.setObjectName(_fromUtf8("label_etd"))
        self.horizontalLayout_11.addWidget(self.label_etd)
        self.etd_edit = QtGui.QLineEdit(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.etd_edit.sizePolicy().hasHeightForWidth())
        self.etd_edit.setSizePolicy(sizePolicy)
        self.etd_edit.setObjectName(_fromUtf8("etd_edit"))
        self.horizontalLayout_11.addWidget(self.etd_edit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.gridLayout_5.addWidget(self.frame_2, 3, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.depart_date_edit = QtGui.QDateEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.depart_date_edit.sizePolicy().hasHeightForWidth())
        self.depart_date_edit.setSizePolicy(sizePolicy)
        self.depart_date_edit.setCalendarPopup(True)
        self.depart_date_edit.setObjectName(_fromUtf8("depart_date_edit"))
        self.horizontalLayout_6.addWidget(self.depart_date_edit)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        self.departure_time_edit = QtGui.QTimeEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.departure_time_edit.sizePolicy().hasHeightForWidth())
        self.departure_time_edit.setSizePolicy(sizePolicy)
        self.departure_time_edit.setCalendarPopup(True)
        self.departure_time_edit.setObjectName(_fromUtf8("departure_time_edit"))
        self.horizontalLayout_6.addWidget(self.departure_time_edit)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_6.addWidget(self.label_12)
        self.departure_unlo_edit = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.departure_unlo_edit.sizePolicy().hasHeightForWidth())
        self.departure_unlo_edit.setSizePolicy(sizePolicy)
        self.departure_unlo_edit.setObjectName(_fromUtf8("departure_unlo_edit"))
        self.horizontalLayout_6.addWidget(self.departure_unlo_edit)
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_6.addWidget(self.label_13)
        self.departure_terminal_edit = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.departure_terminal_edit.sizePolicy().hasHeightForWidth())
        self.departure_terminal_edit.setSizePolicy(sizePolicy)
        self.departure_terminal_edit.setObjectName(_fromUtf8("departure_terminal_edit"))
        self.horizontalLayout_6.addWidget(self.departure_terminal_edit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_7.addWidget(self.label_10)
        self.departure_country_combo = QtGui.QComboBox(self.groupBox_2)
        self.departure_country_combo.setEditable(True)
        self.departure_country_combo.setMaxVisibleItems(15)
        self.departure_country_combo.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.departure_country_combo.setObjectName(_fromUtf8("departure_country_combo"))
        self.horizontalLayout_7.addWidget(self.departure_country_combo)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_7.addWidget(self.label_11)
        self.departure_port_combo = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.departure_port_combo.sizePolicy().hasHeightForWidth())
        self.departure_port_combo.setSizePolicy(sizePolicy)
        self.departure_port_combo.setEditable(True)
        self.departure_port_combo.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.departure_port_combo.setObjectName(_fromUtf8("departure_port_combo"))
        self.horizontalLayout_7.addWidget(self.departure_port_combo)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.gridLayout_5.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.reload_btn = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reload_btn.sizePolicy().hasHeightForWidth())
        self.reload_btn.setSizePolicy(sizePolicy)
        self.reload_btn.setObjectName(_fromUtf8("reload_btn"))
        self.horizontalLayout_2.addWidget(self.reload_btn)
        self.submit_btn = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_btn.sizePolicy().hasHeightForWidth())
        self.submit_btn.setSizePolicy(sizePolicy)
        self.submit_btn.setObjectName(_fromUtf8("submit_btn"))
        self.horizontalLayout_2.addWidget(self.submit_btn)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.label_shipName.setBuddy(self.ship_name_edit)
        self.label_callSign.setBuddy(self.call_sign_edit)
        self.label_date.setBuddy(self.date_edit)
        self.label_voyageNumber.setBuddy(self.voyage_number_edit)
        self.label_8.setBuddy(self.arrival_date_edit)
        self.label_9.setBuddy(self.arrival_time_edit)
        self.label_16.setBuddy(self.arrival_unlo_edit)
        self.label_17.setBuddy(self.arrival_terminal_edit)
        self.label_14.setBuddy(self.arrival_country_combo)
        self.label_15.setBuddy(self.arrival_port_combo)
        self.label.setBuddy(self.prefer_route_type_combo)
        self.label_maxDraft.setBuddy(self.maximum_draft_edit)
        self.label_loadCondition.setBuddy(self.load_condition_edit)
        self.label_speedSetting.setBuddy(self.speed_setting_edit)
        self.label_etd.setBuddy(self.etd_edit)
        self.label_6.setBuddy(self.depart_date_edit)
        self.label_7.setBuddy(self.departure_time_edit)
        self.label_12.setBuddy(self.departure_unlo_edit)
        self.label_13.setBuddy(self.departure_terminal_edit)
        self.label_10.setBuddy(self.departure_country_combo)
        self.label_11.setBuddy(self.departure_port_combo)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.ship_name_edit, self.call_sign_edit)
        Form.setTabOrder(self.call_sign_edit, self.date_edit)
        Form.setTabOrder(self.date_edit, self.voyage_number_edit)
        Form.setTabOrder(self.voyage_number_edit, self.depart_date_edit)
        Form.setTabOrder(self.depart_date_edit, self.departure_time_edit)
        Form.setTabOrder(self.departure_time_edit, self.departure_terminal_edit)
        Form.setTabOrder(self.departure_terminal_edit, self.departure_country_combo)
        Form.setTabOrder(self.departure_country_combo, self.departure_port_combo)
        Form.setTabOrder(self.departure_port_combo, self.arrival_date_edit)
        Form.setTabOrder(self.arrival_date_edit, self.arrival_time_edit)
        Form.setTabOrder(self.arrival_time_edit, self.arrival_unlo_edit)
        Form.setTabOrder(self.arrival_unlo_edit, self.arrival_terminal_edit)
        Form.setTabOrder(self.arrival_terminal_edit, self.arrival_country_combo)
        Form.setTabOrder(self.arrival_country_combo, self.arrival_port_combo)
        Form.setTabOrder(self.arrival_port_combo, self.via_name_edit)
        Form.setTabOrder(self.via_name_edit, self.via_add_btn)
        Form.setTabOrder(self.via_add_btn, self.via_remove_btn)
        Form.setTabOrder(self.via_remove_btn, self.via_up_btn)
        Form.setTabOrder(self.via_up_btn, self.via_down_btn)
        Form.setTabOrder(self.via_down_btn, self.use_dw_route_yes_radio)
        Form.setTabOrder(self.use_dw_route_yes_radio, self.use_dw_route_no_radio)
        Form.setTabOrder(self.use_dw_route_no_radio, self.prefer_route_type_combo)
        Form.setTabOrder(self.prefer_route_type_combo, self.maximum_draft_edit)
        Form.setTabOrder(self.maximum_draft_edit, self.load_condition_edit)
        Form.setTabOrder(self.load_condition_edit, self.speed_setting_edit)
        Form.setTabOrder(self.speed_setting_edit, self.etd_edit)
        Form.setTabOrder(self.etd_edit, self.reload_btn)
        Form.setTabOrder(self.reload_btn, self.submit_btn)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Request Route", None))
        self.label_shipName.setText(_translate("Form", "Ship Name", None))
        self.label_callSign.setText(_translate("Form", "Call Sign", None))
        self.label_date.setText(_translate("Form", "Date", None))
        self.label_voyageNumber.setText(_translate("Form", "Voyage Number", None))
        self.groupBox.setTitle(_translate("Form", "Voyage Detail", None))
        self.groupBox_3.setTitle(_translate("Form", "Arrival", None))
        self.label_8.setText(_translate("Form", "Arrival Date", None))
        self.arrival_date_edit.setDisplayFormat(_translate("Form", "yyyy/MM/dd", None))
        self.label_9.setText(_translate("Form", "Arrival Time", None))
        self.label_16.setText(_translate("Form", "UNLO Code", None))
        self.label_17.setText(_translate("Form", "Terminal", None))
        self.label_14.setText(_translate("Form", "Arrival Country", None))
        self.label_15.setText(_translate("Form", "Arrival Port", None))
        self.groupBox_4.setTitle(_translate("Form", "Via", None))
        self.via_add_btn.setText(_translate("Form", "Add", None))
        self.via_remove_btn.setText(_translate("Form", "Remove", None))
        self.via_up_btn.setText(_translate("Form", "Up", None))
        self.via_down_btn.setText(_translate("Form", "Down", None))
        self.label_question.setText(_translate("Form", "Use DW route when passing channel or TSS if applicable?", None))
        self.use_dw_route_yes_radio.setText(_translate("Form", "Yes", None))
        self.use_dw_route_no_radio.setText(_translate("Form", "No", None))
        self.label.setText(_translate("Form", "Prefered Route Type", None))
        self.prefer_route_type_combo.setItemText(0, _translate("Form", "Most economical route", None))
        self.prefer_route_type_combo.setItemText(1, _translate("Form", "Most frequently ued route", None))
        self.prefer_route_type_combo.setItemText(2, _translate("Form", "Most recently used route", None))
        self.prefer_route_type_combo.setItemText(3, _translate("Form", "Anti piracy route", None))
        self.label_maxDraft.setText(_translate("Form", "Maximum Draft", None))
        self.label_loadCondition.setText(_translate("Form", "Load Condition", None))
        self.label_speedSetting.setText(_translate("Form", "Speed Setting", None))
        self.label_etd.setText(_translate("Form", "ETD           ", None))
        self.groupBox_2.setTitle(_translate("Form", "Departure", None))
        self.label_6.setText(_translate("Form", "Departure Date", None))
        self.depart_date_edit.setDisplayFormat(_translate("Form", "yyyy/MM/dd", None))
        self.label_7.setText(_translate("Form", "Departure Time", None))
        self.label_12.setText(_translate("Form", "UNLO Code", None))
        self.label_13.setText(_translate("Form", "Terminal", None))
        self.label_10.setText(_translate("Form", "Departure Country", None))
        self.label_11.setText(_translate("Form", "Departure Port", None))
        self.reload_btn.setText(_translate("Form", "Reload", None))
        self.submit_btn.setText(_translate("Form", "Submit", None))

