from catppuccin import PALETTE
from libqtile import bar, widget
from libqtile.config import Screen
from .utils import general

theme_name = general.get("theme", "mocha").lower()
flavor = getattr(PALETTE, theme_name, PALETTE.mocha)
font = general.get("font", "FiraCode Nerd Font")
fontsize = general.get("fontsize", 12)
padding = 5

colors = {
    "bg": flavor.colors.base.hex,
    "fg": flavor.colors.text.hex,
    "active": flavor.colors.mauve.hex,
    "inactive": flavor.colors.text.hex,
    "urgent": flavor.colors.red.hex,
    "focus_bg": flavor.colors.mauve.hex,
    "scond_bg": flavor.colors.teal.hex,
    "lihgt_bg": flavor.colors.surface0.hex,
    "chord": flavor.colors.peach.hex,
}

primary_widgets = {
    "font": font,
    "padding": padding,
    "foreground": colors["fg"],
    "background": colors["lihgt_bg"],
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
            widget.CurrentLayout(
                **primary_widgets,
                mode="icon",
            ),
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
            widget.TaskList(
                font=font,
                padding=padding,
                border=colors["lihgt_bg"],
                urgent_alert_method="border",
                highlight_method="block",
                unfocused_border=colors["bg"],
                urgent_border=colors["urgent"],
                rounded=False,
                txt_floating=" ",
                txt_maximized=" ",
                txt_minimized=" ",
            ),
        ]
        if is_primary:
            widgets.extend(
                [
                    widget.DF(
                        **primary_widgets,
                        visible_on_warn=False,
                        partition="/",
                        warn_color=colors["urgent"],
                        warn_space=10,
                        format=" {uf}{m}|{r:.0f}%",
                    ),
                    widget.DF(
                        **primary_widgets,
                        visible_on_warn=False,
                        partition="/home",
                        warn_color=colors["urgent"],
                        warn_space=10,
                        format=" {uf}{m}|{r:.0f}%",
                    ),
                    spacer,
                    widget.CPU(
                        **primary_widgets,
                        measure_mem="G",
                        format=" {load_percent}%",
                        update_interval=5,
                    ),
                    spacer,
                    widget.Memory(
                        **primary_widgets,
                        measure_mem="G",
                        format="{MemUsed: .1f}{mm}/{MemTotal:.0f}{mm}",
                    ),
                    spacer,
                    widget.KeyboardLayout(
                        **primary_widgets,
                        display_map={"us": "🇺🇸", "ru phonetic_winkeys": "🇷🇺"},
                    ),
                    spacer,
                    widget.Spacer(
                        length=5,
                        background=colors["lihgt_bg"],
                    ),
                    widget.Volume(
                        font=font,
                        foreground=colors["fg"],
                        background=colors["lihgt_bg"],
                        emoji=True,
                        emoji_list=[" ", " ", " ", " "],
                    ),
                    widget.Volume(
                        font=font,
                        foreground=colors["fg"],
                        background=colors["lihgt_bg"],
                        emoji=False,
                        unmute_format="{volume}%",
                        mute_format="",
                    ),
                    widget.Spacer(
                        length=5,
                        background=colors["lihgt_bg"],
                    ),
                    spacer,
                    widget.Clock(
                        **primary_widgets,
                        format="%d.%m %H:%M",
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
