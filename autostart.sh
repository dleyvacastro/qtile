#!/usr/bin/env bash
# Display config
xrandr --output HDMI1 --mode 1360x768 --above eDP1 &
# Keboard config: latam
setxkbmap latam &
# Transparency compositor
picom -f &
# Wallpaper
nitrogen --restore
# Systray icons
nm-applet &
cbatticon &
# Startup Apps
/usr/bin/diodon &
kdeconnect-indicator &
