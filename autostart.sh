#!/usr/bin/env bash
xrandr --output HDMI-1 --above eDP-1 &
setxkbmap latam &
/usr/bin/diodon &
picom -f &
