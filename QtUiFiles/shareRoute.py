# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shareRoute.ui'
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
        Form.resize(1108, 1087)
        self.gridLayout_4 = QtGui.QGridLayout(Form)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1088, 1067))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_11 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit_5 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout.addWidget(self.lineEdit_5)
        self.gridLayout_11.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.voyageDetailGroupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.voyageDetailGroupBox.setObjectName(_fromUtf8("voyageDetailGroupBox"))
        self.gridLayout_10 = QtGui.QGridLayout(self.voyageDetailGroupBox)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.groupBox = QtGui.QGroupBox(self.voyageDetailGroupBox)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.depart_date_edit = QtGui.QDateEdit(self.groupBox)
        self.depart_date_edit.setCalendarPopup(True)
        self.depart_date_edit.setObjectName(_fromUtf8("depart_date_edit"))
        self.gridLayout.addWidget(self.depart_date_edit, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 1, 2, 1, 1)
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.gridLayout.addWidget(self.lineEdit_10, 1, 5, 1, 1)
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.gridLayout.addWidget(self.lineEdit_11, 1, 7, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 1, 3, 1, 1)
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 1, 6, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 1, 4, 1, 1)
        self.timeEdit_2 = QtGui.QTimeEdit(self.groupBox)
        self.timeEdit_2.setCalendarPopup(True)
        self.timeEdit_2.setObjectName(_fromUtf8("timeEdit_2"))
        self.gridLayout.addWidget(self.timeEdit_2, 0, 3, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.voyageDetailGroupBox)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 1, 2, 1, 1)
        self.lineEdit_12 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.gridLayout_2.addWidget(self.lineEdit_12, 1, 5, 1, 1)
        self.lineEdit_13 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.gridLayout_2.addWidget(self.lineEdit_13, 1, 7, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.gridLayout_2.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.comboBox_4 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.gridLayout_2.addWidget(self.comboBox_4, 1, 3, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 1, 4, 1, 1)
        self.label_17 = QtGui.QLabel(self.groupBox_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 1, 6, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)
        self.arrival_date_edit = QtGui.QDateEdit(self.groupBox_2)
        self.arrival_date_edit.setCalendarPopup(True)
        self.arrival_date_edit.setObjectName(_fromUtf8("arrival_date_edit"))
        self.gridLayout_2.addWidget(self.arrival_date_edit, 0, 1, 1, 1)
        self.timeEdit = QtGui.QTimeEdit(self.groupBox_2)
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.gridLayout_2.addWidget(self.timeEdit, 0, 3, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.scrollArea_2 = QtGui.QScrollArea(self.voyageDetailGroupBox)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 884, 69))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_18 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)
        self.lineEdit_14 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.gridLayout_3.addWidget(self.lineEdit_14, 0, 1, 1, 1)
        self.lineEdit_15 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.gridLayout_3.addWidget(self.lineEdit_15, 0, 2, 1, 1)
        self.lineEdit_16 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.gridLayout_3.addWidget(self.lineEdit_16, 0, 3, 1, 1)
        self.lineEdit_17 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.gridLayout_3.addWidget(self.lineEdit_17, 0, 4, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_3.addWidget(self.pushButton_6, 0, 5, 1, 1)
        self.lineEdit_18 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.gridLayout_3.addWidget(self.lineEdit_18, 1, 1, 1, 1)
        self.lineEdit_19 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.gridLayout_3.addWidget(self.lineEdit_19, 1, 2, 1, 1)
        self.lineEdit_20 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.gridLayout_3.addWidget(self.lineEdit_20, 1, 3, 1, 1)
        self.lineEdit_21 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.gridLayout_3.addWidget(self.lineEdit_21, 1, 4, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_10.addWidget(self.scrollArea_2, 2, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.voyageDetailGroupBox)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_19 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_8.addWidget(self.label_19)
        self.radioButton = QtGui.QRadioButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_8.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_8.addWidget(self.radioButton_2)
        self.gridLayout_9.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_20 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_9.addWidget(self.label_20)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_9.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_4.sizePolicy().hasHeightForWidth())
        self.radioButton_4.setSizePolicy(sizePolicy)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout_9.addWidget(self.radioButton_4)
        self.gridLayout_9.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.scrollArea_3 = QtGui.QScrollArea(self.groupBox_4)
        self.scrollArea_3.setMinimumSize(QtCore.QSize(0, 91))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 377, 99))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.gridLayout_8 = QtGui.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.tableWidget_3 = QtGui.QTableWidget(self.scrollAreaWidgetContents_3)
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.gridLayout_8.addWidget(self.tableWidget_3, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_6.addWidget(self.scrollArea_3, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.verticalLayout.addWidget(self.pushButton_8)
        self.gridLayout_6.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.frame = QtGui.QFrame(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_6.addWidget(self.frame, 0, 2, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.label_22 = QtGui.QLabel(self.groupBox_3)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_9.addWidget(self.label_22, 3, 0, 1, 1)
        self.scrollArea_4 = QtGui.QScrollArea(self.groupBox_3)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName(_fromUtf8("scrollArea_4"))
        self.scrollAreaWidgetContents_4 = QtGui.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 864, 100))
        self.scrollAreaWidgetContents_4.setObjectName(_fromUtf8("scrollAreaWidgetContents_4"))
        self.gridLayout_7 = QtGui.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.tableWidget = QtGui.QTableWidget(self.scrollAreaWidgetContents_4)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_7.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_9.addWidget(self.scrollArea_4, 4, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_3, 3, 0, 1, 1)
        self.gridLayout_11.addWidget(self.voyageDetailGroupBox, 1, 0, 1, 1)
        self.voyageDataGroupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.voyageDataGroupBox.setObjectName(_fromUtf8("voyageDataGroupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.voyageDataGroupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_28 = QtGui.QLabel(self.voyageDataGroupBox)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.horizontalLayout_2.addWidget(self.label_28)
        self.lineEdit_32 = QtGui.QLineEdit(self.voyageDataGroupBox)
        self.lineEdit_32.setObjectName(_fromUtf8("lineEdit_32"))
        self.horizontalLayout_2.addWidget(self.lineEdit_32)
        self.label_29 = QtGui.QLabel(self.voyageDataGroupBox)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.horizontalLayout_2.addWidget(self.label_29)
        self.lineEdit_33 = QtGui.QLineEdit(self.voyageDataGroupBox)
        self.lineEdit_33.setObjectName(_fromUtf8("lineEdit_33"))
        self.horizontalLayout_2.addWidget(self.lineEdit_33)
        self.label_30 = QtGui.QLabel(self.voyageDataGroupBox)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.horizontalLayout_2.addWidget(self.label_30)
        self.lineEdit_34 = QtGui.QLineEdit(self.voyageDataGroupBox)
        self.lineEdit_34.setObjectName(_fromUtf8("lineEdit_34"))
        self.horizontalLayout_2.addWidget(self.lineEdit_34)
        self.label_31 = QtGui.QLabel(self.voyageDataGroupBox)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.horizontalLayout_2.addWidget(self.label_31)
        self.lineEdit_35 = QtGui.QLineEdit(self.voyageDataGroupBox)
        self.lineEdit_35.setObjectName(_fromUtf8("lineEdit_35"))
        self.horizontalLayout_2.addWidget(self.lineEdit_35)
        self.label_27 = QtGui.QLabel(self.voyageDataGroupBox)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.horizontalLayout_2.addWidget(self.label_27)
        self.lineEdit_31 = QtGui.QLineEdit(self.voyageDataGroupBox)
        self.lineEdit_31.setObjectName(_fromUtf8("lineEdit_31"))
        self.horizontalLayout_2.addWidget(self.lineEdit_31)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_24 = QtGui.QLabel(self.voyageDataGroupBox)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_3.addWidget(self.label_24)
        self.lineEdit_28 = QtGui.QLineEdit(self.voyageDataGroupBox)
        self.lineEdit_28.setObjectName(_fromUtf8("lineEdit_28"))
        self.horizontalLayout_3.addWidget(self.lineEdit_28)
        self.label_25 = QtGui.QLabel(self.voyageDataGroupBox)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_3.addWidget(self.label_25)
        self.lineEdit_29 = QtGui.QLineEdit(self.voyageDataGroupBox)
        self.lineEdit_29.setObjectName(_fromUtf8("lineEdit_29"))
        self.horizontalLayout_3.addWidget(self.lineEdit_29)
        self.label_26 = QtGui.QLabel(self.voyageDataGroupBox)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_3.addWidget(self.label_26)
        self.lineEdit_30 = QtGui.QLineEdit(self.voyageDataGroupBox)
        self.lineEdit_30.setObjectName(_fromUtf8("lineEdit_30"))
        self.horizontalLayout_3.addWidget(self.lineEdit_30)
        self.label_32 = QtGui.QLabel(self.voyageDataGroupBox)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayout_3.addWidget(self.label_32)
        self.lineEdit_36 = QtGui.QLineEdit(self.voyageDataGroupBox)
        self.lineEdit_36.setObjectName(_fromUtf8("lineEdit_36"))
        self.horizontalLayout_3.addWidget(self.lineEdit_36)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton = QtGui.QPushButton(self.voyageDataGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.label_33 = QtGui.QLabel(self.voyageDataGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.horizontalLayout_4.addWidget(self.label_33)
        self.lineEdit_37 = QtGui.QLineEdit(self.voyageDataGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_37.sizePolicy().hasHeightForWidth())
        self.lineEdit_37.setSizePolicy(sizePolicy)
        self.lineEdit_37.setObjectName(_fromUtf8("lineEdit_37"))
        self.horizontalLayout_4.addWidget(self.lineEdit_37)
        self.label_34 = QtGui.QLabel(self.voyageDataGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.horizontalLayout_4.addWidget(self.label_34)
        self.lineEdit_38 = QtGui.QLineEdit(self.voyageDataGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_38.sizePolicy().hasHeightForWidth())
        self.lineEdit_38.setSizePolicy(sizePolicy)
        self.lineEdit_38.setObjectName(_fromUtf8("lineEdit_38"))
        self.horizontalLayout_4.addWidget(self.lineEdit_38)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.tableWidget_2 = QtGui.QTableWidget(self.voyageDataGroupBox)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableWidget_2, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_35 = QtGui.QLabel(self.voyageDataGroupBox)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.horizontalLayout_5.addWidget(self.label_35)
        self.lineEdit_39 = QtGui.QLineEdit(self.voyageDataGroupBox)
        self.lineEdit_39.setObjectName(_fromUtf8("lineEdit_39"))
        self.horizontalLayout_5.addWidget(self.lineEdit_39)
        self.pushButton_2 = QtGui.QPushButton(self.voyageDataGroupBox)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_36 = QtGui.QLabel(self.voyageDataGroupBox)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.horizontalLayout_6.addWidget(self.label_36)
        self.lineEdit_40 = QtGui.QLineEdit(self.voyageDataGroupBox)
        self.lineEdit_40.setObjectName(_fromUtf8("lineEdit_40"))
        self.horizontalLayout_6.addWidget(self.lineEdit_40)
        self.pushButton_3 = QtGui.QPushButton(self.voyageDataGroupBox)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.voyageDataGroupBox)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_5.addWidget(self.label_21, 6, 0, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.voyageDataGroupBox)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout_5.addWidget(self.plainTextEdit, 7, 0, 1, 1)
        self.gridLayout_11.addWidget(self.voyageDataGroupBox, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.pushButton_4 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_7.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_7.addWidget(self.pushButton_5)
        self.gridLayout_11.addLayout(self.horizontalLayout_7, 3, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Ship Name", None))
        self.label_2.setText(_translate("Form", "Call Sign", None))
        self.label_3.setText(_translate("Form", "Voyage Number", None))
        self.label_4.setText(_translate("Form", "Captain Name", None))
        self.label_5.setText(_translate("Form", "Date", None))
        self.voyageDetailGroupBox.setTitle(_translate("Form", "Voyage Detail", None))
        self.groupBox.setTitle(_translate("Form", "Departure", None))
        self.label_11.setText(_translate("Form", "Departure Port", None))
        self.label_6.setText(_translate("Form", "Departure Date", None))
        self.label_10.setText(_translate("Form", "Departure Country", None))
        self.label_13.setText(_translate("Form", "Terminal", None))
        self.label_7.setText(_translate("Form", "Departure Time", None))
        self.label_12.setText(_translate("Form", "UNLO Code", None))
        self.groupBox_2.setTitle(_translate("Form", "Arrvial", None))
        self.label_15.setText(_translate("Form", "Arrvial Port", None))
        self.label_14.setText(_translate("Form", "Arrvial Country", None))
        self.label_16.setText(_translate("Form", "UNLO Code", None))
        self.label_17.setText(_translate("Form", "Terminal", None))
        self.label_8.setText(_translate("Form", "Arrvial Time     ", None))
        self.label_9.setText(_translate("Form", "Arrvial Time  ", None))
        self.label_18.setText(_translate("Form", "Via", None))
        self.pushButton_6.setText(_translate("Form", "Add Route", None))
        self.groupBox_3.setTitle(_translate("Form", "Paper Chart", None))
        self.label_19.setText(_translate("Form", "Use DW route when passing channel or TSS if appilicable?", None))
        self.radioButton.setText(_translate("Form", "Yes", None))
        self.radioButton_2.setText(_translate("Form", "No", None))
        self.label_20.setText(_translate("Form", " Is there any critial point that request to pay special attention to?", None))
        self.radioButton_3.setText(_translate("Form", "Yes", None))
        self.radioButton_4.setText(_translate("Form", "No", None))
        self.groupBox_4.setTitle(_translate("Form", "Critial Point", None))
        self.pushButton_7.setText(_translate("Form", "Add", None))
        self.pushButton_8.setText(_translate("Form", "Delete", None))
        self.label_22.setText(_translate("Form", " If it is necessery to waitting for high tide or reduce speed to passing critial point,  please click the button on the right of the point.", None))
        self.voyageDataGroupBox.setTitle(_translate("Form", "Voyage Data", None))
        self.label_28.setText(_translate("Form", "Maximum Draft", None))
        self.label_29.setText(_translate("Form", "Minimum UKC", None))
        self.label_30.setText(_translate("Form", "Load Condition", None))
        self.label_31.setText(_translate("Form", "Displacement", None))
        self.label_27.setText(_translate("Form", "Cargo Shipped", None))
        self.label_24.setText(_translate("Form", "Total Distance", None))
        self.label_25.setText(_translate("Form", "Total Streaming Time", None))
        self.label_26.setText(_translate("Form", "Average Speed", None))
        self.label_32.setText(_translate("Form", "Average Slip", None))
        self.pushButton.setText(_translate("Form", "Calculate", None))
        self.label_33.setText(_translate("Form", "Distance By M/E Revolution", None))
        self.label_34.setText(_translate("Form", "Average M/E RMP", None))
        self.label_35.setText(_translate("Form", "Attach ECDIS Route File", None))
        self.pushButton_2.setText(_translate("Form", "Browse", None))
        self.label_36.setText(_translate("Form", "Attach E-marine WP Plan", None))
        self.pushButton_3.setText(_translate("Form", "Browse", None))
        self.label_21.setText(_translate("Form", "Remark", None))
        self.pushButton_4.setText(_translate("Form", "Submit", None))
        self.pushButton_5.setText(_translate("Form", "Cancel", None))

