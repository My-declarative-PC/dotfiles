from modules.keys import keys, mod
from modules.groups import groups
from modules.layouts import layouts, floating_layout
from modules.screens import init_screens
from libqtile.config import Click, Drag
from libqtile.lazy import lazy as L

# Основные переменные, которые требует Qtile
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"

# Инициализация экранов
screens = init_screens()

# Мышиные привязки (можно тоже вынести в отдельный файл, если их много)
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
