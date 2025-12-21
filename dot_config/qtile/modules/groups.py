from libqtile.config import Group, Key
from libqtile.lazy import lazy as L
from .keys import keys, mod  # Импортируем список ключей для его модификации

AltKey = "mod1"
groups = []
workspace_keys = "1234567890"


def go_to_group(name, screen_number=0):
    def _inner(qtile):
        group = qtile.groups_map[name]
        group.toscreen(screen_number)
        qtile.to_screen(screen_number)

    return _inner


for i in workspace_keys:
    # --- ГРУППЫ ГЛАВНОГО МОНИТОРА (1-9) ---
    screen_number = 0
    # screen_affinity=0 заставляет группу открываться на 1-м мониторе
    groups.append(Group(name=i, label=i, screen_affinity=screen_number))

    keys.extend(
        [
            # Win + [1-9] -> Переключение на основном мониторе
            Key(
                [mod],
                i,
                L.function(go_to_group(i, screen_number)),
                desc=f"Switch to group {i} (Main Screen)",
            ),
            # Win + Shift + [1-9] -> Перенос окна на группу основного монитора
            Key(
                [mod, "shift"],
                i,
                L.window.togroup(i, switch_group=False),
                desc=f"Move focused window to group {i}",
            ),
        ]
    )

    # --- ГРУППЫ ВТОРОГО МОНИТОРА (11-19) ---
    screen_number = 1
    sec_group_name = str(int(i) + 10)
    # screen_affinity=1 заставляет группу открываться на 2-м мониторе
    groups.append(Group(name=sec_group_name, label=i, screen_affinity=screen_number))

    keys.extend(
        [
            # Win + Alt + [1-9] -> Переключение на группу второго монитора (имя группы "11".."19")
            Key(
                [mod, AltKey],
                i,
                L.function(go_to_group(sec_group_name, screen_number)),
                desc=f"Switch to group {i} (Second Screen)",
            ),
            # Win + Alt + Shift + [1-9] -> Перенос окна на группу второго монитора
            Key(
                [mod, AltKey, "shift"],
                i,
                L.window.togroup(sec_group_name, switch_group=False),
                desc=f"Move focused window to group {sec_group_name} (Second Screen)",
            ),
        ]
    )
