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
    "lihgt_bg": flavor.colors.surface1.hex,
    "chord": flavor.colors.peach.hex,
}

widget_defaults = dict(
    font=font,
    fontsize=fontsize,
)


def init_screens():
    main_groups = [str(i) for i in range(0, 10)]
    sec_groups = [str(i + 10) for i in range(0, 10)]
    spacer = widget.Spacer(
        length=5,
        background=colors["bg"],
    )

    def create_bar(groups, is_primary=False):
        widgets = [
            widget.CurrentLayout(font=font, mode="icon", foreground=colors["fg"]),
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
                font=font,
                chords_colors={
                    "launch": (colors["chord"], colors["bg"]),
                    "Rofi": (colors["chord"], colors["bg"]),
                },
                name_transform=lambda name: name.upper(),
            ),
            widget.WindowName(font=font, foreground=colors["fg"]),
        ]
        if is_primary:
            widgets.extend(
                [
                    widget.KeyboardLayout(
                        font=font,
                        padding=5,
                        display_map={"us": "🇺🇸", "ru phonetic_winkeys": "🇷🇺"},
                        foreground=colors["fg"],
                        background=colors["lihgt_bg"],
                    ),
                    spacer,
                    widget.Clock(
                        font=font,
                        padding=5,
                        format="%d.%m %H:%M",
                        foreground=colors["fg"],
                        background=colors["lihgt_bg"],
                    ),
                    spacer,
                    widget.Systray(),
                    spacer,
                ]
            )

        return bar.Bar(widgets, 26, background=colors["bg"])

    return [
        Screen(top=create_bar(main_groups, is_primary=True)),
        Screen(top=create_bar(sec_groups)),
    ]
