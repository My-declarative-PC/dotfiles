#!/bin/bash

picom -b &
autorandr --change &
/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &
sleep 1 && feh --bg-fill ~/.wallpaper &
sleep 2 && setxkbmap -layout us,ru -variant qwerty &
