from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy as L
from .keys import keys, mod
from .utils import APP_RULES

AltKey = "mod1"
groups = []
workspace_keys = "1234567890"


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
                L.window.togroup(group_name, switch_group=False),
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
                [mod, AltKey], i, L.function(go_to_group(sec_group_name, screen_number))
            ),
            Key(
                [mod, AltKey, "shift"],
                i,
                L.window.togroup(sec_group_name, switch_group=False),
                desc=f"Switch to group {i} (Main Screen)",
            ),
        ]
    )
