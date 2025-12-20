#!/bin/bash

picom -b &
/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &
sleep 2 && setxkbmap -layout us,ru -variant qwerty &
