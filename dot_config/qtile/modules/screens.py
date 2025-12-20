from catppuccin import PALETTE
from libqtile import bar, widget
from libqtile.config import Screen
from .utils import general

theme_name = general.get("theme", "mocha").lower()
flavor = getattr(PALETTE, theme_name, PALETTE.mocha)
font = general.get("font", "FiraCode Nerd Font")
fontsize = general.get("fontsize", 12)

colors = {
    "bg": flavor.colors.base.hex,
    "fg": flavor.colors.text.hex,
    "active": flavor.colors.mauve.hex,
    "inactive": flavor.colors.text.hex,
    "urgent": flavor.colors.red.hex,
    "focus_bg": flavor.colors.mauve.hex,
    "scond_bg": flavor.colors.teal.hex,
}

widget_defaults = dict(
    font=font,
    fontsize=fontsize,
    padding=3,
)


def init_screens():
    main_groups = [str(i) for i in range(0, 10)]
    sec_groups = [str(i + 10) for i in range(0, 10)]

    def create_bar(groups, is_primary=False):
        widgets = [
            widget.CurrentLayout(foreground=colors["fg"]),
            widget.GroupBox(
                font=f"{font} Bold",
                visible_groups=groups,
                highlight_method="block",
                rounded=False,
                disable_drag=True,
                # colors
                active=colors["active"],
                block_highlight_text_color=colors["bg"],
                inactive=colors["inactive"],
                this_current_screen_border=colors["focus_bg"],
                this_screen_border=colors["scond_bg"],
                urgent_alert_method="block",
                urgent_border=colors["urgent"],
                urgent_text=colors["bg"],
            ),
            widget.Chord(
                chords_colors={
                    "launch": (colors["urgent"], colors["fg"]),
                },
                name_transform=lambda name: name.upper(),
            ),
            widget.WindowName(foreground=colors["fg"]),
        ]
        if is_primary:
            widgets.extend(
                [
                    widget.Systray(),
                    widget.Clock(format="%d.%m.%Y %H:%M", foreground=colors["fg"]),
                ]
            )

        return bar.Bar(widgets, 26, background=colors["bg"])

    return [
        Screen(top=create_bar(main_groups, is_primary=True)),
        Screen(top=create_bar(sec_groups)),
    ]
