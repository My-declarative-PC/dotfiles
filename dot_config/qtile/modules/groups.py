from libqtile.config import DropDown, Group, Key, Match, ScratchPad
from libqtile.lazy import lazy as L
from libqtile.utils import guess_terminal

from .keys import keys, mod
from .utils import APP_RULES, general

AltKey = "mod1"
groups = []
workspace_keys = "1234567890"
terminal = general.get("terminal", guess_terminal())
browser = general.get("browser", "firefox")


def get_matches_for_group(group_name):
    return [
        Match(wm_class=wm_class)
        for wm_class, cfg in APP_RULES.items()
        if cfg.get("group") == group_name
    ]


def go_to_group(name, screen_number=0):
    def _inner(qtile):
        if name in qtile.groups_map:
            group = qtile.groups_map[name]
            group.toscreen(screen_number)
            qtile.to_screen(screen_number)

    return _inner


# ---------- ОСНОВНЫЕ ГРУППЫ ----------
for i in workspace_keys:
    # --- ГРУППЫ ГЛАВНОГО МОНИТОРА (1-10) ---
    screen_number = 0
    group_name = i
    groups.append(
        Group(
            name=group_name,
            label="10" if i == "0" else i,
            screen_affinity=screen_number,
            matches=get_matches_for_group(group_name),
        )
    )

    keys.extend(
        [
            Key(
                [mod],
                i,
                L.function(go_to_group(group_name, screen_number)),
                desc=f"Switch to group {i} (Main Screen)",
            ),
            Key(
                [mod, "shift"],
                i,
                L.window.togroup(group_name),
                desc=f"Switch to group {i} (Main Screen)",
            ),
        ]
    )

    # --- ГРУППЫ ВТОРОГО МОНИТОРА (11-20) ---
    screen_number = 1
    sec_group_name = str(int(i) + 10)
    groups.append(
        Group(
            name=sec_group_name,
            label="10" if i == "0" else i,
            screen_affinity=screen_number,
            matches=get_matches_for_group(sec_group_name),
        )
    )

    keys.extend(
        [
            Key(
                [mod, AltKey],
                i,
                L.function(go_to_group(sec_group_name, screen_number)),
                desc=f"Switch to group {i} (Second Screen)",
            ),
            Key(
                [mod, AltKey, "shift"],
                i,
                L.window.togroup(sec_group_name),
                desc=f"Switch to group {i} (Second Screen)",
            ),
        ]
    )


# ---------- SCRATCHPAD ----------
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                terminal,
                width=0.6,
                height=0.6,
                x=0.2,
                y=0.2,
                opacity=1.0,
            ),
            DropDown(
                "browser",
                browser,
                width=0.9,
                height=0.9,
                x=0.05,
                y=0.05,
            ),
            DropDown(
                "files",
                "nemo",
                width=0.7,
                height=0.7,
                x=0.15,
                y=0.15,
            ),
            DropDown(
                "telegram",
                "flatpak run org.telegram.desktop",
                width=0.5,
                height=0.7,
                x=0.25,
                y=0.15,
            ),
        ],
    )
)
