#!/bin/bash

wget -qO- https://git.io/papirus-icon-theme-install | DESTDIR="$HOME/.local/share/icons" EXTRA_THEMES="Papirus-Dark" sh
