# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_areaalongvector.ui'
#
# Created: Mon Apr 21 22:27:48 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_AreaAlongVector(object):
    def setupUi(self, AreaAlongVector):
        AreaAlongVector.setObjectName(_fromUtf8("AreaAlongVector"))
        AreaAlongVector.resize(411, 367)
        self.buttonBox = QtGui.QDialogButtonBox(AreaAlongVector)
        self.buttonBox.setGeometry(QtCore.QRect(210, 330, 181, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox = QtGui.QGroupBox(AreaAlongVector)
        self.groupBox.setGeometry(QtCore.QRect(9, 0, 391, 111))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.comboBox_forthfield = QtGui.QComboBox(self.groupBox)
        self.comboBox_forthfield.setGeometry(QtCore.QRect(120, 50, 251, 22))
        self.comboBox_forthfield.setObjectName(_fromUtf8("comboBox_forthfield"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox_backfield = QtGui.QComboBox(self.groupBox)
        self.comboBox_backfield.setGeometry(QtCore.QRect(120, 80, 251, 22))
        self.comboBox_backfield.setObjectName(_fromUtf8("comboBox_backfield"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox_inputlayer = QtGui.QComboBox(self.groupBox)
        self.comboBox_inputlayer.setGeometry(QtCore.QRect(120, 20, 251, 22))
        self.comboBox_inputlayer.setObjectName(_fromUtf8("comboBox_inputlayer"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 91, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox_2 = QtGui.QGroupBox(AreaAlongVector)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 391, 121))
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 111, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(210, 20, 91, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(210, 80, 111, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_minvalue = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_minvalue.setGeometry(QtCore.QRect(140, 20, 51, 20))
        self.lineEdit_minvalue.setObjectName(_fromUtf8("lineEdit_minvalue"))
        self.lineEdit_minvaluewidth = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_minvaluewidth.setGeometry(QtCore.QRect(140, 80, 51, 20))
        self.lineEdit_minvaluewidth.setObjectName(_fromUtf8("lineEdit_minvaluewidth"))
        self.lineEdit_maxvaluewidth = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_maxvaluewidth.setGeometry(QtCore.QRect(330, 80, 51, 20))
        self.lineEdit_maxvaluewidth.setObjectName(_fromUtf8("lineEdit_maxvaluewidth"))
        self.lineEdit_maxvalue = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_maxvalue.setGeometry(QtCore.QRect(330, 20, 51, 20))
        self.lineEdit_maxvalue.setObjectName(_fromUtf8("lineEdit_maxvalue"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 50, 91, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(210, 50, 91, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(140, 50, 51, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(330, 50, 51, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.groupBox_3 = QtGui.QGroupBox(AreaAlongVector)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 250, 391, 71))
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 91, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_outputfile = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_outputfile.setGeometry(QtCore.QRect(120, 30, 181, 20))
        self.lineEdit_outputfile.setObjectName(_fromUtf8("lineEdit_outputfile"))
        self.pushButtonBrowseOutput = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonBrowseOutput.setGeometry(QtCore.QRect(310, 30, 75, 23))
        self.pushButtonBrowseOutput.setObjectName(_fromUtf8("pushButtonBrowseOutput"))
        self.pushButton_help = QtGui.QPushButton(AreaAlongVector)
        self.pushButton_help.setGeometry(QtCore.QRect(20, 330, 75, 21))
        self.pushButton_help.setObjectName(_fromUtf8("pushButton_help"))

        self.retranslateUi(AreaAlongVector)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AreaAlongVector.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AreaAlongVector.reject)
        QtCore.QMetaObject.connectSlotsByName(AreaAlongVector)

    def retranslateUi(self, AreaAlongVector):
        AreaAlongVector.setWindowTitle(_translate("AreaAlongVector", "AreaAlongVector", None))
        self.groupBox.setTitle(_translate("AreaAlongVector", "Input", None))
        self.label.setText(_translate("AreaAlongVector", "Input layer :", None))
        self.label_3.setText(_translate("AreaAlongVector", "Forth field (right) :", None))
        self.label_4.setText(_translate("AreaAlongVector", "Back field (left) :", None))
        self.groupBox_2.setTitle(_translate("AreaAlongVector", "Parameters", None))
        self.label_5.setText(_translate("AreaAlongVector", "Minimum limit : ", None))
        self.label_6.setText(_translate("AreaAlongVector", "Minimum limit width : ", None))
        self.label_7.setText(_translate("AreaAlongVector", "Maximum limit : ", None))
        self.label_8.setText(_translate("AreaAlongVector", "Maximum limit width : ", None))
        self.label_9.setText(_translate("AreaAlongVector", "Minimum value : ", None))
        self.label_10.setText(_translate("AreaAlongVector", "Maximum value : ", None))
        self.label_11.setText(_translate("AreaAlongVector", "0", None))
        self.label_12.setText(_translate("AreaAlongVector", "0", None))
        self.groupBox_3.setTitle(_translate("AreaAlongVector", "Output", None))
        self.label_2.setText(_translate("AreaAlongVector", "Output shape file :", None))
        self.pushButtonBrowseOutput.setText(_translate("AreaAlongVector", "Browse ...", None))
        self.pushButton_help.setText(_translate("AreaAlongVector", "Help", None))

