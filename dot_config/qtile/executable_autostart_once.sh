#!/bin/bash

dbus-launch /usr/bin/dunst &
greenclip daemon >/dev/null &
kdeconnect-indicator &
mkdir -p /home/$USER/Pictures/Screenshots/ &
nm-applet &
picom -b &
sleep 2 && setxkbmap -layout us,ru -variant qwerty &
/usr/bin/dunst &
/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &
yandex-disk-indicator &
