#!/bin/python
import time
import pystray
import subprocess
import schedule
from os import path
from PIL import Image
from lib import load_data
from cli import COURSES
from pystray import MenuItem as i, Menu as m
from threading import Thread

icon_image = Image.open(path.join(path.expanduser('~'), 'workspace', 'unischedule', 'icon.png'))

def do_nothing() -> None:
    pass

def open_webpage(src: str) -> None:
    subprocess.Popen(['xdg-open', src])

def quit_app(icon) -> None:
    icon.stop()

def get_submenu(info: dict[str, str]) -> list[i]:
    allowed = ['website']
    return [ i('Web page', lambda: open_webpage(v))
             for k, v in info.items() if k in allowed ]

data = load_data(COURSES)
items = [ i(d.describe(), m(*get_submenu(d.course))) for d in data.today().entries ]
items_or_default = items if len(items) else [i('(empty)', do_nothing)]

tray = pystray.Icon('Unischedule')
tray.icon = icon_image

def setup(icon):
    icon.menu = (
        *items_or_default,
        m.SEPARATOR,
        i('Quit', quit_app),
    )
    icon.visible = True

def update_icon():
    setup(tray)
    tray.update_menu()

def background_refresh():
    while len(schedule.jobs):
        schedule.run_pending()
        time.sleep(10)

schedule.every().day.at('00:00').do(update_icon)

thread = Thread(target = background_refresh)
thread.daemon = True
thread.start()

tray.run(setup)
