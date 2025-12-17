import os
from libqtile import bar, widget
from libqtile.config import Screen
import libqtile.resources
from .utils import colors, general

widget_defaults = dict(
    font=general.get("font", "sans"),
    fontsize=general.get("fontsize", 12),
    padding=3,
)
extension_defaults = widget_defaults.copy()


def init_screens():
    return [
        Screen(
            bottom=bar.Bar(
                [
                    widget.CurrentLayout(),
                    widget.GroupBox(
                        active=colors.get("active", "#ff0000"),
                        inactive=colors.get("inactive", "#aaaaaa"),
                        highlight_method="block",
                        this_current_screen_border=colors.get("focus", "#ff0000"),
                    ),
                    widget.Prompt(),
                    widget.WindowName(foreground=colors.get("fg", "#ffffff")),
                    widget.Chord(
                        chords_colors={
                            "launch": ("#ff0000", "#ffffff"),
                        },
                        name_transform=lambda name: name.upper(),
                    ),
                    widget.Systray(),
                    widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                    widget.QuickExit(),
                ],
                24,
                background=colors.get("panel_bg", "#222222"),
            ),
        ),
    ]
