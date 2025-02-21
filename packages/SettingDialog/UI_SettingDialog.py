# Form implementation generated from reading ui file '.\SettingDialog.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from .SingleKeySequenceEdit import SingleKeySequenceEdit


class Ui_SettingDialog(object):
    def setupUi(self, SettingDialog):
        SettingDialog.setObjectName("SettingDialog")
        SettingDialog.resize(513, 200)
        font = QtGui.QFont()
        font.setPointSize(12)
        SettingDialog.setFont(font)
        self.formLayout = QtWidgets.QFormLayout(SettingDialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=SettingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.authKeyLineEdit = QtWidgets.QLineEdit(parent=SettingDialog)
        self.authKeyLineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.authKeyLineEdit.setObjectName("authKeyLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.authKeyLineEdit)
        self.label_4 = QtWidgets.QLabel(parent=SettingDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.sourceToTargetKeySequenceEdit = SingleKeySequenceEdit(parent=SettingDialog)
        self.sourceToTargetKeySequenceEdit.setObjectName("sourceToTargetKeySequenceEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sourceToTargetKeySequenceEdit)
        self.label_5 = QtWidgets.QLabel(parent=SettingDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.targetToSourceKeySequenceEdit = SingleKeySequenceEdit(parent=SettingDialog)
        self.targetToSourceKeySequenceEdit.setObjectName("targetToSourceKeySequenceEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.targetToSourceKeySequenceEdit)
        self.label_6 = QtWidgets.QLabel(parent=SettingDialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.sourceLanguageComboBox = QtWidgets.QComboBox(parent=SettingDialog)
        self.sourceLanguageComboBox.setObjectName("sourceLanguageComboBox")
        self.sourceLanguageComboBox.addItem("")
        self.sourceLanguageComboBox.addItem("")
        self.sourceLanguageComboBox.addItem("")
        self.sourceLanguageComboBox.addItem("")
        self.sourceLanguageComboBox.addItem("")
        self.sourceLanguageComboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sourceLanguageComboBox)
        self.label_7 = QtWidgets.QLabel(parent=SettingDialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.targetLanguageComboBox = QtWidgets.QComboBox(parent=SettingDialog)
        self.targetLanguageComboBox.setObjectName("targetLanguageComboBox")
        self.targetLanguageComboBox.addItem("")
        self.targetLanguageComboBox.addItem("")
        self.targetLanguageComboBox.addItem("")
        self.targetLanguageComboBox.addItem("")
        self.targetLanguageComboBox.addItem("")
        self.targetLanguageComboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.targetLanguageComboBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=SettingDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.buttonBox)

        self.retranslateUi(SettingDialog)
        self.buttonBox.accepted.connect(SettingDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(SettingDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SettingDialog)

    def retranslateUi(self, SettingDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingDialog.setWindowTitle(_translate("SettingDialog", "Dialog"))
        self.label.setText(_translate("SettingDialog", "Auth Key:"))
        self.label_4.setText(_translate("SettingDialog", "Source-Target:"))
        self.label_5.setText(_translate("SettingDialog", "Target-Source:"))
        self.label_6.setText(_translate("SettingDialog", "Source Language:"))
        self.sourceLanguageComboBox.setItemText(0, _translate("SettingDialog", "English"))
        self.sourceLanguageComboBox.setItemText(1, _translate("SettingDialog", "Chinese"))
        self.sourceLanguageComboBox.setItemText(2, _translate("SettingDialog", "Japanese"))
        self.sourceLanguageComboBox.setItemText(3, _translate("SettingDialog", "Russian"))
        self.sourceLanguageComboBox.setItemText(4, _translate("SettingDialog", "French"))
        self.sourceLanguageComboBox.setItemText(5, _translate("SettingDialog", "German"))
        self.label_7.setText(_translate("SettingDialog", "Target Language:"))
        self.targetLanguageComboBox.setItemText(0, _translate("SettingDialog", "English"))
        self.targetLanguageComboBox.setItemText(1, _translate("SettingDialog", "Chinese"))
        self.targetLanguageComboBox.setItemText(2, _translate("SettingDialog", "Japanese"))
        self.targetLanguageComboBox.setItemText(3, _translate("SettingDialog", "Russian"))
        self.targetLanguageComboBox.setItemText(4, _translate("SettingDialog", "French"))
        self.targetLanguageComboBox.setItemText(5, _translate("SettingDialog", "German"))
