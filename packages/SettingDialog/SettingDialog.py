from .UI_SettingDialog import Ui_SettingDialog
from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QKeySequence
from packages.config import config, save_config
from packages.utils import error_messagebox


class SettingDialog(QDialog, Ui_SettingDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initialize values
        self.authKeyLineEdit.setText(config.get("authKey", ""))
        self.sourceToTargetKeySequenceEdit.setKeySequence(QKeySequence(config.get("source_target", "")))
        self.targetToSourceKeySequenceEdit.setKeySequence(QKeySequence(config.get("target_source", "")))
        self.sourceLanguageComboBox.setCurrentText(config.get("source", "English"))
        self.targetLanguageComboBox.setCurrentText(config.get("target", "Chinese"))

    def accept(self):
        if self.sourceToTargetKeySequenceEdit.keySequence().toString() != "" \
            and self.sourceToTargetKeySequenceEdit.keySequence().toString() \
                == self.targetToSourceKeySequenceEdit.keySequence().toString():
            error_messagebox("Source-to-Target hotkey and Target-to-Source hotkey should be different.")
            return
        self.save()
        super().accept()

    def save(self):
        config["authKey"] = self.authKeyLineEdit.text()
        config["source_target"] = self.sourceToTargetKeySequenceEdit.keySequence().toString()
        config["target_source"] = self.targetToSourceKeySequenceEdit.keySequence().toString()
        config["source"] = self.sourceLanguageComboBox.currentText()
        config["target"] = self.targetLanguageComboBox.currentText()
        save_config()
