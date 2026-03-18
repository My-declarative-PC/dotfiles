#!/bin/bash

uv python install $(/usr/bin/python3 -V | awk '{print $2}') --default
uv tool install \
    --with catppuccin \
    --with psutil \
    --with pyxdg \
    qtile[widgets] --force

sudo cp ~/.config/qtile/qtile.desktop /usr/share/xsessions/
