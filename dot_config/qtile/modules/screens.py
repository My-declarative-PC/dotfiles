from libqtile import bar, widget
from libqtile.config import Screen
from .utils import colors, general

widget_defaults = dict(
    font=general.get("font", "sans"),
    fontsize=general.get("fontsize", 12),
    padding=3,
)

extension_defaults = widget_defaults.copy()


def init_screens():
    # Список имен групп для первого монитора: "1", "2"..."9"
    main_groups = [str(i) for i in range(1, 10)]
    # Список имен групп для второго монитора: "11", "12"..."19"
    sec_groups = [str(i + 10) for i in range(1, 10)]

    return [
        Screen(
            top=bar.Bar(
                [
                    widget.CurrentLayout(),
                    widget.GroupBox(
                        visible_groups=main_groups,
                        active=colors.get("active", "#ff0000"),
                        inactive=colors.get("inactive", "#aaaaaa"),
                        highlight_method="block",
                        this_current_screen_border=colors.get("focus", "#ff0000"),
                    ),
                    widget.Chord(
                        chords_colors={
                            "launch": ("#ff0000", "#ffffff"),
                            "Rofi": ("#ffff00", "#ffffff"),
                        },
                        name_transform=lambda name: name.upper(),
                    ),
                    widget.Prompt(),
                    widget.WindowName(foreground=colors.get("fg", "#ffffff")),
                    widget.Systray(),
                    widget.Clock(format="%d.%m.%Y %H:%M"),
                ],
                24,
                background=colors.get("panel_bg", "#222222"),
            ),
        ),
        Screen(
            top=bar.Bar(
                [
                    widget.CurrentLayout(),
                    widget.GroupBox(
                        visible_groups=sec_groups,
                        active=colors.get("active", "#ff0000"),
                        inactive=colors.get("inactive", "#aaaaaa"),
                        highlight_method="block",
                        this_current_screen_border=colors.get("focus", "#ff0000"),
                    ),
                    widget.Chord(
                        chords_colors={
                            "launch": ("#ff0000", "#ffffff"),
                            "Rofi": ("#ffff00", "#ffffff"),
                        },
                        name_transform=lambda name: name.upper(),
                    ),
                    widget.WindowName(foreground=colors.get("fg", "#ffffff")),
                ],
                24,
                background=colors.get("panel_bg", "#222222"),
            ),
        ),
    ]
