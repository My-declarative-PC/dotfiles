from modules import hooks

from libqtile.config import Click, Drag
from libqtile.lazy import lazy as L
from modules.groups import groups
from modules.keys import keys, mod
from modules.layouts import floating_layout, layouts
from modules.screens import init_screens

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"

screens = init_screens()

mouse = [
    Drag(
        [mod],
        "Button1",
        L.window.set_position_floating(),
        start=L.window.get_position(),
    ),
    Drag([mod], "Button3", L.window.set_size_floating(), start=L.window.get_size()),
    Click([mod], "Button2", L.window.bring_to_front()),
]
