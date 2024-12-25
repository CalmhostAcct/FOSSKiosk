import webview
import tkinter
from tkinter import simpledialog, messagebox
import sys
import keyboard
import threading
import os
import platform
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def ask_password():
    root = tkinter.Tk()
    root.withdraw()
    password = simpledialog.askstring("Password", "Enter Password to Exit Kiosk")
    if password == config['config']['password']:
        window.destroy()
        sys.exit(0)
    else:
        messagebox.showinfo(title="Password Incorrect", message="The password you entered is incorrect")

def monitor_keys():
    while True:
        if platform.system() == "Windows":
            keyboard.block_key("win")
        if keyboard.is_pressed('ctrl+e'):
            ask_password()

if os.name != 'nt' and os.geteuid() != 0:
    print("Non-sudo launches are not supported. Please run the script with sudo.")
    sys.exit(1)

key_thread = threading.Thread(target=monitor_keys, daemon=True)
key_thread.start()

window = webview.create_window('FOSSKiosk App', config['config']['start_url'], fullscreen=True)
webview.start()

