import os
import subprocess

from libqtile import backend, hook

from .utils import APP_RULES

home = os.path.expanduser("~")


@hook.subscribe.client_managed
def auto_focus_on_match(client: backend.base.Window):
    wm_classes = client.get_wm_class()
    if not wm_classes:
        return

    for wm_class in wm_classes:
        rule = APP_RULES.get(wm_class)
        if not rule:
            continue

        if not rule.get("focus"):
            return

        group_name = rule.get("group")
        if not group_name:
            return

        qtile = client.qtile
        group = qtile.groups_map.get(group_name)

        if group:
            group.toscreen()
        return


@hook.subscribe.startup_once
def autostart_once():
    subprocess.Popen([home + "/.config/qtile/autostart_once.sh"])


@hook.subscribe.startup
def autostart():
    subprocess.Popen([home + "/.config/qtile/autostart.sh"])
