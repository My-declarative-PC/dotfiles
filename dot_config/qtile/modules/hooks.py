import os
import subprocess
from libqtile import hook


@hook.subscribe.startup_once
def autostart_once():
    home = os.path.expanduser("~")
    subprocess.Popen([home + "/.config/qtile/autostart_once.sh"])


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser("~")
    subprocess.Popen([home + "/.config/qtile/autostart.sh"])
