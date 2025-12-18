from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy as L
from libqtile.utils import guess_terminal
import os

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
    Key([mod], "n", L.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        L.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", L.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", L.spawn(browser), desc="Launch browser"),
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
        [mod],
        "t",
        L.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "control"], "r", L.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", L.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", L.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Layout Switch
    Key(
        [mod],
        "F1",
        L.spawn(home + "/.local/bin/layout_switch.py ru"),
        desc="Switch layout",
    ),
    Key(
        [mod],
        "F2",
        L.spawn(home + "/.local/bin/layout_switch.py"),
        desc="Switch layout",
    ),
    Key(
        [mod],
        "F3",
        L.spawn(home + "/.local/bin/layout_switch.py us"),
        desc="Switch layout",
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
        mode=True,
        name="Rofi",
    ),
]
