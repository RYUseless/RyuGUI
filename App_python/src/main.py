import src.FrontEnd.main_gui as frontend
# import src.BackEnd.shrek as Funny
import src.BackEnd.cipher_utils as Cipher
import os
import PyQt5
from PyQt5 import QtCore, QtWidgets

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

if __name__ == '__main__':
    # Funny.youGotShreked()
    print("\t--- RyuGUI main caller ---")
    # # cipher testing:
    ip_pool = ["PetrovSto#2222", "UltraMagiePlsHesloIdk"]
    # Initialize empty lists to store encrypted and decrypted IPs
    cipher_instance = Cipher.AES_cipher()
    # Encrypt each IP address
    cipher_instance.setter(ip_pool=ip_pool)
    cipher_instance.getter()

    # #Frontend launcher# #
    frontend.run()
