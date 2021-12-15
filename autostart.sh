#!/usr/bin/env bash
xrandr --output HDMI1 --above eDP1 &
setxkbmap latam &
nm-applet &
cbatticon &
nitrogen --restore
/usr/bin/diodon &
picom -f &
