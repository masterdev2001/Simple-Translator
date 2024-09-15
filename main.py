from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from win32event import CreateMutex
from win32api import GetLastError
from packages.utils import error_messagebox, translate, notify
from packages.config import config, LANGUAGE
from packages.SettingDialog import SettingDialog
import winerror
import keyboard
import time
import pyperclip


def quit_app():
    """
    Quit app
    """
    app.quit()


def translate_selected_text(target: str):
    """
    translate text
    :param target: target language
    """
    if config.get("authKey", "") == "":
        notify("Error", "Auth Key is required.")
        return
    # press Ctrl+X to copy selected text into clipboard
    keyboard.press("Ctrl+X")
    keyboard.release("Ctrl+X")
    time.sleep(1)
    # Get Clipboard data and translate
    data = pyperclip.paste()
    result = translate(data, target)
    # Set Clipboard Data
    if result is not None:
        pyperclip.copy(result)
    # press Ctrl+V to paste translated text
    keyboard.press("Ctrl+V")
    keyboard.release("Ctrl+V")


def show_setting():
    """
    Show setting dialog
    """
    global s2t_hotkey, t2s_hotkey
    if s2t_hotkey:
        keyboard.remove_hotkey(s2t_hotkey)
    if t2s_hotkey:
        keyboard.remove_hotkey(t2s_hotkey)
    dlg = SettingDialog()
    ret = dlg.exec()
    if ret == 1:
        source_target_hotkey = config.get("source_target", "")
        target_source_hotkey = config.get("target_source", "")
        if source_target_hotkey:
            s2t_hotkey = keyboard.add_hotkey(
                source_target_hotkey,
                translate_selected_text,
                (LANGUAGE[config.get("target", "Chinese")], )
            )
        if target_source_hotkey:
            t2s_hotkey = keyboard.add_hotkey(
                target_source_hotkey,
                translate_selected_text,
                (LANGUAGE[config.get("source", "English")], )
            )


if __name__ == "__main__":
    # create app
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)

    # check app is already running or not
    mutex_name = "translator-{b7bed741-3cd2-4b3b-acd1-79f43b8511e3}"
    mutex = CreateMutex(None, False, mutex_name)
    if GetLastError() == winerror.ERROR_ALREADY_EXISTS:
        error_messagebox("Translator app is already running")
        quit_app()

    # create tray icon
    tray = QSystemTrayIcon()
    tray.setIcon(QIcon("resource/translator.png"))
    tray.setToolTip("translator")
    tray.setVisible(True)

    # create quit action
    quit_action = QAction("Quit")
    quit_action.triggered.connect(quit_app)

    # setting action
    setting_action = QAction("Settings")
    setting_action.triggered.connect(show_setting)

    # create context menu for tray icon
    menu = QMenu()
    menu.addAction(quit_action)
    menu.addAction(setting_action)
    tray.setContextMenu(menu)

    # add hotkey
    s2t_hotkey = None
    t2s_hotkey = None
    if config.get("source_target", ""):
        s2t_hotkey = keyboard.add_hotkey(
            config.get("source_target", ""),
            translate_selected_text,
            (LANGUAGE[config.get("target", "Chinese")],)
        )
    if config.get("target_source", ""):
        t2s_hotkey = keyboard.add_hotkey(
            config.get("target_source", ""),
            translate_selected_text,
            (LANGUAGE[config.get("source", "English")],)
        )

    # run app
    app.exec()
