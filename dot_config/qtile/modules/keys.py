import os

from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy as L
from libqtile.utils import guess_terminal

from .keyboard import set_layout_and_notify
from .utils import general


home = os.path.expanduser("~")
mod = general.get("mod", "mod4")
terminal = general.get("terminal", guess_terminal())
browser = general.get("browser", "firefox")

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", L.layout.left(), desc="Move focus to left"),
    Key([mod], "l", L.layout.right(), desc="Move focus to right"),
    Key([mod], "j", L.layout.down(), desc="Move focus down"),
    Key([mod], "k", L.layout.up(), desc="Move focus up"),
    Key([mod], "space", L.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", L.layout.shuffle_left(), desc="Move window to the left"),
    Key(
        [mod, "shift"],
        "l",
        L.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", L.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", L.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", L.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", L.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", L.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", L.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", L.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod], "Return", L.spawn(terminal), desc="Launch terminal"),
    Key(
        [mod, "shift"],
        "Return",
        L.group["scratchpad"].dropdown_toggle("term"),
        desc="Launch terminal in scratchpad",
    ),
    Key([mod], "w", L.spawn(browser), desc="Launch browser"),
    Key(
        [mod, "shift"],
        "w",
        L.group["scratchpad"].dropdown_toggle("browser"),
        desc="Launch browser in scratchpad",
    ),
    Key([mod], "e", L.spawn("nemo"), desc="Launch file manager"),
    Key(
        [mod, "shift"],
        "e",
        L.group["scratchpad"].dropdown_toggle("files"),
        desc="Launch file manager in scratchpad",
    ),
    Key(
        [mod], "t", L.spawn("flatpak run org.telegram.desktop"), desc="Launch telegram"
    ),
    Key(
        [mod, "shift"],
        "t",
        L.group["scratchpad"].dropdown_toggle("telegram"),
        desc="Launch telegram in scratchpad",
    ),
    Key(
        [mod],
        "g",
        L.spawn("flatpak run be.alexandervanhee.gradia"),
        desc="Launch gradia",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", L.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", L.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        L.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod, "shift"],
        "f",
        L.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "control"], "r", L.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", L.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", L.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Layout Switch
    Key(
        [mod],
        "F3",
        L.function(set_layout_and_notify, layout_code="us"),
        desc="Switch to US layout",
    ),
    Key(
        [mod],
        "F2",
        L.function(set_layout_and_notify),
        desc="Toggle keyboard layout",
    ),
    Key(
        [mod],
        "F1",
        L.function(set_layout_and_notify, layout_code="ru"),
        desc="Switch to RU layout",
    ),
    # Rofi
    Key(
        [mod],
        "d",
        L.spawn("rofi -show drun"),
        desc="Lounch Rofi",
    ),
    KeyChord(
        [mod, "shift"],
        "d",
        [
            Key([], "w", L.spawn("rofi -show window"), desc="Переключить окна"),
            Key(
                [],
                "e",
                L.spawn("rofimoji -f emojis math arrows"),
                desc="Rofi-emiji",
            ),
            Key(
                [],
                "k",
                L.spawn("flatpak run io.github.heidefinnischen.cuneo"),
                desc="calculator",
            ),
            Key([], "b", L.spawn("rofi-bluetooth"), desc="Bluetooth manager"),
            Key([], "n", L.spawn("ronema"), desc="Network manager"),
            Key(
                ["shift"],
                "w",
                L.spawn("~/.local/bin/rofi-weather"),
                desc="Weather",
            ),
            Key(
                [],
                "c",
                L.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard"),
                desc="Clipboard",
            ),
            # Exit key
            Key([], "Escape", L.ungrab_all()),
        ],
        name="Rofi",
    ),
    Key([mod], "period", L.next_screen(), desc="Move focus to next monitor"),
    Key([mod], "comma", L.prev_screen(), desc="Move focus to prev monitor"),
    Key([mod], "Escape", L.spawn(f"{home}/.local/bin/blur-lock"), desc="Lock WM"),
    # Volume
    Key(
        [],
        "XF86AudioRaiseVolume",
        L.spawn(f"{home}/.local/bin/volume_brightness volume_up"),
        desc="Volume up",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        L.spawn(f"{home}/.local/bin/volume_brightness volume_down"),
        desc="Volume down",
    ),
    # Audio control
    Key(
        [],
        "XF86AudioNext",
        L.spawn(f"{home}/.local/bin/volume_brightness next_track"),
        desc="Next track",
    ),
    Key(
        [],
        "XF86AudioPrev",
        L.spawn(f"{home}/.local/bin/volume_brightness prev_track"),
        desc="Prev track",
    ),
    Key(
        [],
        "XF86AudioPlay",
        L.spawn(f"{home}/.local/bin/volume_brightness play_pause"),
        desc="Play/Pause",
    ),
]
