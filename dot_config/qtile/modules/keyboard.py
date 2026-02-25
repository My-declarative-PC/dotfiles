#!/usr/bin/python3

import subprocess


def run_command(command):
    """Выполняет команду и возвращает вывод."""
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout.strip()


def set_russian_layout():
    subprocess.run(["setxkbmap", "-layout", "ru,us", "-variant", "phonetic_winkeys,"])
    return "🇷🇺"


def set_english_layout():
    subprocess.run(["setxkbmap", "-layout", "us,ru"])
    return "🇺🇸"


def get_current_layout():
    """Извлекает текущую раскладку из setxkbmap."""
    output = run_command("setxkbmap -query")
    for line in output.splitlines():
        if "layout:" in line:
            # Берем первое значение до запятой (например, 'us,ru' -> 'us')
            layout = line.split(":")[1].strip().split(",")[0]
            return layout
    return "us"


def toggle_layout():
    if get_current_layout() == "us":
        return set_russian_layout()
    else:
        return set_english_layout()


def send_notification(label):
    subprocess.run(
        [
            "dunstify",
            "--icon",
            "keyboard",
            "--urgency",
            "low",
            "--app-name",
            "layout switch",
            "Раскладка",
            label,
        ]
    )


def set_layout_and_notify(qtile, layout_code=None):
    """Определяет, какую раскладку установить на основе аргумента."""
    if layout_code == "ru":
        new_layout = set_russian_layout()
    elif layout_code == "us":
        new_layout = set_english_layout()
    else:
        new_layout = toggle_layout()

    send_notification(new_layout)
