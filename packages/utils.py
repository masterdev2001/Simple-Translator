from PyQt6.QtWidgets import QMessageBox
from packages.config import config
from win10toast import ToastNotifier
import requests

toast = ToastNotifier()


def notify(title: str, message: str):
    toast.show_toast(
        title,
        message,
        duration=1,
        threaded=True,
    )


def error_messagebox(message: str):
    """
    Displaying the error message box
    :param message: message to display
    """
    messagebox = QMessageBox()
    messagebox.critical(None, "Error", message)


def translate(text: str, target: str):
    """
    translate given text to target language
    :param text: text to translate
    :param target: target language
    :return: translated text
    """
    url = "https://microsoft-translator-text.p.rapidapi.com/translate"

    querystring = {"to[0]": target, "api-version": "3.0", "profanityAction": "NoAction", "textType": "plain"}

    payload = [{"Text": text}]
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": config.get("authKey", ""),
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers, params=querystring, verify=False)
    if response.status_code == 200:
        data = response.json()
        return data[0]["translations"][0]["text"]
    else:
        if response.status_code == 403 and response.json()["message"] == "You are not subscribed to this API.":
            notify(f"Status: {response.status_code}", "Auth Key is not valid")
        else:
            notify(f"Status: {response.status_code}", response.text)
        return None
