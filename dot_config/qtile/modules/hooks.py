import os
import subprocess
from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    # Список команд для запуска
    processes = [
        ["picom", "-b"],
        ["autorandr", "--change"],
        "sleep 2 && setxkbmap -layout us,ru -variant qwerty",
        f"sleep 1 && feh --bg-fill {home}/.wallpaper",
        ["/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1"],
    ]

    for p in processes:
        if isinstance(p, list):
            subprocess.Popen(p)
        else:
            # shell=True нужен для обработки && и сложных строк
            subprocess.Popen(p, shell=True)
