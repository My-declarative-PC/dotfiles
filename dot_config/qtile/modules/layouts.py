from libqtile import layout
from libqtile.config import Match
from .utils import colors

# Используем цвета из TOML
layouts = [
    layout.Columns(
        margin=6,
        border_focus_stack=[
            colors.get("focus", "#d75f5f"),
            colors.get("unfocus", "#8f3d3d"),
        ],
        border_width=4,
    ),
    layout.Max(margin=3),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ]
)
