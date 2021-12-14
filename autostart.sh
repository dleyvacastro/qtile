#!/usr/bin/env bash
xrandr --output HDMI1 --above eDP1 &
pactl set-sink-volume @DEFAULT_SINK@ 33% &
setxkbmap latam &
nitrogen --restore
/usr/bin/diodon &
picom -f &
brave &
