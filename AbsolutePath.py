import os
import sys

#convertir relative path a absolute path para lograr crear un solo archivo .exe
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = getattr(sys, '_MEIPASS', os.getcwd())
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)