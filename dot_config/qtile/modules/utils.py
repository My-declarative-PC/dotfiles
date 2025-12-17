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
