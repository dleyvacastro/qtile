#!/usr/bin/env bash
# Display config
xrandr --output HDMI-1 --mode 1360x768 --left-of DP-0 &
# Keboard config: latam
setxkbmap latam &
# Transparency compositor
picom -f &
# Wallpaper
# nitrogen --restore
python ~/.config/apthemes/wall_init.py
# Systray icons
nm-applet &
#cbatticon &
# Theme loader
python ~/.config/apthemes/ap_loader.py
# Startup Apps
/usr/bin/diodon &
#/usr/bin/klipper &
/usr/bin/volctl &
kdeconnect-indicator &
