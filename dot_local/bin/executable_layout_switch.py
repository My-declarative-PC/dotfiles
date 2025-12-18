#!/usr/bin/python3

import subprocess
import sys


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
            "--appname",
            "layout switch",
            "Раскладка",
            label,
        ]
    )


def handle_layout_change(arg):
    """Определяет, какую раскладку установить на основе аргумента."""
    if arg == "ru":
        new_layout = set_russian_layout()
    elif arg == "us":
        new_layout = set_english_layout()
    else:
        new_layout = toggle_layout()

    send_notification(new_layout)


def main():
    # Передаем первый аргумент, если он есть, иначе None
    target_arg = sys.argv[1] if len(sys.argv) > 1 else None
    handle_layout_change(target_arg)


if __name__ == "__main__":
    main()
