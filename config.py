import json
import locale
import os
import sys
import tempfile


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        full_path = os.path.join(sys._MEIPASS, relative_path)
    else:
        full_path = os.path.join(os.path.abspath("."), relative_path)

    if not os.path.exists(full_path):
        resource_name = os.path.basename(relative_path)
        formatted_message = ("Couldn't find {missing_resource}. Please try reinstalling the application.").format(missing_resource=resource_name)
        raise FileNotFoundError(formatted_message)

    return full_path


def apply_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, indent=4)


def load_settings():
    locale.setlocale(locale.LC_ALL, '')

    default_settings = {
        "WeModPath": os.path.join(os.environ["LOCALAPPDATA"], "WeMod"),
        "showWarning": True,
    }

    try:
        with open(SETTINGS_FILE, "r") as f:
            settings = json.load(f)
    except Exception as e:
        print("加载json文件失败: " + str(e))
        settings = default_settings

    for key, value in default_settings.items():
        settings.setdefault(key, value)

    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

    return settings



setting_path = os.path.join(os.environ["APPDATA"], "WU Settings")
os.makedirs(setting_path, exist_ok=True)

SETTINGS_FILE = os.path.join(setting_path, "settings.json")
VERSION_TEMP_DIR = os.path.join(tempfile.gettempdir(), "WeModVersionTemp", "version")
WEMOD_TEMP_DIR = os.path.join(tempfile.gettempdir(), "WemodTemp", "wemod")

settings = load_settings()

dropDownArrow_path = resource_path("assets/dropdown-black.png").replace("\\", "/")
resourceHacker_path = resource_path("prm/ResourceHacker.exe")
unzip_path = resource_path("prm/7z/7z.exe")
binmay_path = resource_path("prm/binmay.exe")
elevator_path = resource_path("prm/Elevate.exe")

