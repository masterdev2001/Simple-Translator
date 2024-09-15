import pickle
import os

config = {}

LANGUAGE = {
    "English": "en",
    "Chinese": "zh-Hans",
    "Japanese": "ja",
    "Russian": "ru",
    "French": "fr",
    "German": "de"
}


def load_config():
    """
    Load configuration
    """
    if os.path.exists("config.pkl"):
        global config
        with open("config.pkl", "rb") as file:
            config = pickle.load(file)


def save_config():
    """
    Save configuration
    """
    with open("config.pkl", "wb") as file:
        pickle.dump(config, file)


load_config()
