# Qtile

# Table of Contetents
- [Dependences and Defaults]
    - [Terminal Emulator](#terminal-emulator)
    - [Fonts](#fonts)
        - [VictorMono]
        - [UbuntuMono]
    - [Shell](#shell)
    - [Nitrgoen](#nitrgoen)
    - [LXAppearance](#lxappearance)
    - [Rofi](#rofi)
    -
- [Keys]

# Dependences
Required apps and defaults of my preferences linked by key binds:
## Terminal Emulator
Terminal used: [Konsole](https://konsole.kde.org/) \
Font: Victor Mono Nerd Font \
Colorscheme: Shiny-konsole \
## Fonts
[Nerd Fonts](https://www.nerdfonts.com/#home) are required. Several special symbols are used among the config.
There are two main fonts used:
- [VictorMono](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/VictorMono.zip)
- [UbuntuMono](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/UbuntuMono.zip)
## Shell
Shell used: [Fish](https://fishshell.com/).
## Nitrgoen
Nitrgoen is an app to manage wallpapers. At starting the command ´nitrgoen --restore´ is executed.
## Lxappeareance
[Lxappeareance](https://wiki.lxde.org/es/LXAppearance) is an app to set system themes .
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
