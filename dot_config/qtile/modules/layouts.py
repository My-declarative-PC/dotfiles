from catppuccin import PALETTE
from libqtile import layout
from libqtile.config import Match

from .utils import general, FLOATING_CLASSES

theme_name = general.get("theme", "mocha").lower()
flavor = getattr(PALETTE, theme_name, PALETTE.mocha)
font = general.get("font", "FiraCode Nerd Font")
fontsize = general.get("fontsize", 12)

# Используем цвета из TOML
layouts = [
    layout.Columns(
        margin=6,
        border_focus=flavor.colors.lavender.hex,
        border_normal=flavor.colors.surface0.hex,
        border_focus_stack=[flavor.colors.mauve.hex, flavor.colors.blue.hex],
        border_width=2,
    ),
    layout.Max(
        margin=3,
        border_focus=flavor.colors.lavender.hex,
        border_normal=flavor.colors.surface0.hex,
        border_width=2,
    ),
]

floating_layout = layout.Floating(
    border_focus=flavor.colors.lavender.hex,
    border_normal=flavor.colors.surface0.hex,
    border_width=4,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
        *[Match(wm_class=cls) for cls in FLOATING_CLASSES],
    ],
)
