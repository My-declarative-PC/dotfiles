import os

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:
    import tomli as tomllib  # Для старых версий

# Путь к конфигу
config_path = os.path.expanduser("~/.config/qtile/theme.toml")


def load_config():
    if not os.path.isfile(config_path):
        return {}

    with open(config_path, "rb") as f:
        return tomllib.load(f)


# Загружаем конфиг один раз при импорте
config_data = load_config()

# Удобные шорткаты для переменных
colors = config_data.get("colors", {})
general = config_data.get("general", {})

# Правила для приложений: привязка к группе и автофокус
APP_RULES = {
    "org.wezfurlong.wezterm": {"group": "1", "focus": True},
    "zen": {"group": "2", "focus": True},
    "Nemo": {"group": "3", "focus": True},
    "thunderbird": {"group": "4", "focus": True},
    "vkteams": {"group": "5", "focus": True},
    "dbgate": {"group": "7", "focus": True},
    "org.remmina.Remmina": {"group": "9", "focus": True},
    "obs": {"group": "12", "focus": True},
    "cassette": {"group": "19", "focus": True},
    "anytype": {"group": "20", "focus": True},
}

# Список классов для плавающих окон (Floating)
FLOATING_CLASSES = [
    "Yad",
    "Galculator",
    "Blueberry.py",
    "TelegramDesktop",
    "wezterm_helix",
    "cuneo",
    "Xsane",
    "Pavucontrol",
    "qt5ct",
]
