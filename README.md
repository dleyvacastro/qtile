# Qtile

# Table of Contetents
- [Dependences and Defaults](#dependences)
    - [Terminal Emulator](#terminal-emulator)
    - [Fonts](#fonts)
        - VictorMono
        - UbuntuMono
    - [Shell](#shell)
    - [Nitrgoen](#nitrgoen)
    - [LXAppearance](#lxappearance)
    - [Transparency](#transparency)
    - [Rofi](#rofi)
    - [Dbus](#dbus)
- [Keys](#keys)

# Dependences 
Required apps and defaults of my preferences linked by key binds:
## Terminal Emulator
Terminal used: [Kitty](https://sw.kovidgoyal.net/kitty/) \
Font: Victor Mono Nerd Font \
For colorschemes: [Kitty Themes](https://github.com/dexpota/kitty-themes)
Actual Colorscheme: [Argonaut](https://github.com/dexpota/kitty-themes/blob/master/themes/Argonaut.conf)
**Instalation**: \
- Arch-Based: `sudo pacman -S kitty`
- Debian-Based: `sudo apt install kitty`
## Fonts
[Nerd Fonts](https://www.nerdfonts.com/#home) are required. Several special symbols are used among the config.
There are two main fonts used:
- [VictorMono](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/VictorMono.zip)
- [UbuntuMono](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/UbuntuMono.zip)
## Shell
Shell used: [Fish](https://fishshell.com/).
**Instalation**: \
- Arch-Based: `sudo pacman -S fish`
- Debian-Based: `sudo apt install fish`

## Nitrgoen
Nitrgoen is an app to manage wallpapers. At starting the command ´nitrgoen --restore´ is executed.
**Instalation**: \
- Arch-Based: `sudo pacman -S nitrogen`
- Debian-Based: `sudo apt install nitrogen`

## Lxappeareance
[Lxappeareance](https://wiki.lxde.org/es/LXAppearance) is an app to set system themes .
**Instalation**: \
- Arch-Based: `sudo pacman -S lxappearance`
- Debian-Based: `sudo apt install lxappearance`

## Transparency
Transparency compositor used: [picom](https://github.com/yshui/picom). In some cases is needed to create an empty file named `picom.conf` or set the backend as `xrender`.
**Instalation**: \
- Arch-Based: `sudo pacman -S picom`
- Debian-Based: `sudo apt install picom`

## Rofi
[Rofi](https://github.com/davatorium/rofi) is a menu used to start apps and navegate through workspaces.
Theme: [Material-Ocean](https://github.com/material-ocean/rofi-Theme)
config.rasi:
```rasi
configuration {
    modi: "window,drun,ssh,combi";
    font: "VictorMono Nerd Font 11";
    theme: "material-ocean";
    show-icons: true;
}
```
**Instalation**: \
- Arch-Based: `sudo pacman -S rofi dmenu`
- Debian-Based: `sudo apt install rofi dmenu`
    ```
    mkdir ~/.config/rofi
    wget https://raw.githubusercontent.com/material-ocean/rofi-Theme/master/material-ocean.rasi
    echo "configuration {
    modi: "window,drun,ssh,combi";
    font: "VictorMono Nerd Font 11";
    theme: "material-ocean";
    show-icons: true;
    }" >> config.rasi
    
    ```

## Dbus
In order to set the spotify controls and names in the bar is needed to install an `Mpris2` dependence named `dbus-next`. \
`pip install dbus-next`.

# Keys
| Keys                 | Action                                    |
| -------------------- | ----------------------------------------- |
| mod4+w               | Close window                              |
| mod4+control+q       | Shutdown Qtile                            |
| mod4+mod1+r          | Restart Qtile                             |
| mod4+mod1+q          | Shutdown PC                               |
| mod4+h               | Focus the left window                     |
| mod4+l               | Focus the right window                    |
| mod4+j               | Focus the down window                     |
| mod4+k               | Focus the up window                       |
| mod4+c               | Focus the next window                     |
| mod4+shift+h         | Swap with the left window                 |
| mod4+shift+l         | Swap with the right window                |
| mod4+shift+j         | Swap with the down window                 |
| mod4+shift+k         | Swap with the up window                   |
| mod4+i               | Grow actual window                        |
| mod4+shift+i         | Shink actual window                       |
| mod4+control+h       | Grow left                                 |
| mod4+control+l       | Grow right                                |
| mod4+control+j       | Grow down                                 |
| mod4+control+k       | Grow up                                   |
| mod4+Tab             | Next Layout                               |
| mod4+shift+f         | Toggle Floating                           |
| mod4+o               | Maximize window acording to layout config |
| mod4+shift+space     | Flip windows - Monad                      |
| mod4+n               | Normalize widnow sizes                    |
| mod4+m               | Set actual window to fullscreen           |
| mod4+mod1+j          | Go to screen 1                            |
| mod4+mod1+k          | Go to screen 2                            |
| mod4+space           | Open an app                               |
| control+space        | Show opened apps                          |
| mod4+b               | Browser                                   |
| mod4+shift+e         | Study                                     |
| mod4+shift+a         | Anime                                     |
| control+mod1+t       | Terminal                                  |
| XF86AudioRaiseVolume | Volume Up                                 |
| XF86AudioLowerVolume | Volume Down                               |
| XF86AudioPlay        | Spotify Play/Pause                        |
| XF86AudioNext        | Spotify Next                              |
| XF86AudioPrev        | Spotify Prev                              |
| Print                | Full ScreenShot                           |
| shift+mod4+s         | Section ScreenShot                        |
| mod4+v               | Diodon                                    |
