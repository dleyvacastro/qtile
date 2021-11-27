from typing import List  # noqa: F401
import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from themes import material_ocean as colors
from libqtile.log_utils import logger

# with open("material-ocean.json", 'r') as f:
#    colors = json.load(f)
#    print(colors)

mod = "mod4"
browser = 'brave-browser'
terminal = "konsole -e fish"
font = "UbuntuMono Nerd Font"


def test_funct(qtile):

    try:
        g1 = list(qtile.cmd_groups())
        logger.warning(f'Type of returning: {g1}')
    except:
        logger.warning('exploto')


@hook.subscribe.startup_once
def startup():
    xrandr = 'xrandr --output HDMI-1 --above eDP-1'
    latam_keyboard = 'setxkbmap latam'
    nitrogen = 'nitrogen --restore'
    diodon = '/usr/bin/diodon &'
    picom = 'picom -f &'
    subprocess.run(xrandr, shell=True)
    subprocess.run(latam_keyboard, shell=True)
    subprocess.run(nitrogen, shell=True)
    subprocess.run(diodon, shell=True)
    subprocess.run(picom, shell=True)
    subprocess.run(browser + ' &', shell=True)
    #home = os.path.join(os.path.expanduser('~'), ".config", "qtile")
    #subprocess.call([os.path.join(home, 'autostart.sh')])

    # lazy.spawn('diodon')
    # lazy.spawn('WhatSie')
    # lazy.spawn('Firefox')


def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",  # Icon: nf-oct-triangle_left
        fontsize=37,
        font=font,
        padding=-3
    )


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        font=font,
        text=text,
        padding=3
    )


def MusicPayer(fb='text', bg='dark'):
    events = [
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous',
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause',
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next'
    ]
    return [
        widget.TextBox(
            **base(fb, bg),
            text='玲',
            padding=10,
            font=font,
            fontsize=17,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(events[0])}
        ),
        widget.TextBox(
            **base(fb, bg),
            text='懶',
            padding=10,
            font=font,
            fontsize=17,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(events[1])}
        ),
        widget.TextBox(
            **base(fb, bg),
            text='怜',
            padding=10,
            font=font,
            fontsize=17,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(events[2])}
        ),

    ]


def open_pages(pages: list, browser='brave-browser'):
    return f'{i + " " for i in pages}'


keys = [
    Key([mod, "shift"], "p", lazy.function(test_funct(qtile))),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "c", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Toggle between split and unsplit sides of stack.

    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key(["mod1", "control"], "t", lazy.spawn(
        terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "m", lazy.window.toggle_fullscreen()),

    Key([mod, "mod1"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "mod1"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "space", lazy.spawn('rofi -show drun'),
        desc="Spawn a command using a prompt widget"),
    Key(["control"], "space", lazy.spawn('rofi -show')),

    Key([mod, "mod1"], "j",
        lazy.to_screen(0)),

    Key([mod, "mod1"], "k",
        lazy.to_screen(1)),
    Key([mod], "b", lazy.spawn('brave-browser')),
    # Media
    Key([], "XF86AudioRaiseVolume", lazy.spawn('amixer -q set Master 5%+')),
    Key([], "XF86AudioLowerVolume", lazy.spawn('amixer -q set Master 5%-')),
    Key([], 'XF86AudioPlay', lazy.spawn(
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause'
    )),
    Key([], 'XF86AudioNext', lazy.spawn(
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next'
    )),
    Key([], 'XF86AudioPrev', lazy.spawn(
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous'
    )),
    # ScreenShot
    Key([], "Print", lazy.spawn(
        "scrot '/tmp/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f'"), desc="Full ScreenShot"),
    Key(["shift", mod], "s", lazy.spawn(
        "scrot -s '/tmp/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f && rm $f'"), desc="Selected ScreenShot"),
    Key([mod], "v", lazy.spawn('/usr/bin/diodon'), desc="Calls diodon"),
]

# groups = [Group(i) for i in [
#    "   ", "   ", "  ", "   ", "  ", "   ", "   ", "   ", "   ",
# ]]
g = [
    # Group("   "),
    Group("   ", Match(wm_class=["Firefox", "Brave-browser"])),
    Group("   "),
    Group("   ", Match(
        wm_class=["WhatSie", "discord", "TelegramDesktop"]),
        layout='monadwide'
    ),
    Group("   ", Match(wm_class=["spotify"])),
    Group("   "),
    Group("   ", Match(wm_class=["zoom"]))
]
groups = g + [Group(i) for i in [
    "7", "8", "9",
]]

keys.extend(
    [
        Key([mod, "shift"], "e", lazy.spawn(
            'brave-browser --new-window https://e-aulas.urosario.edu.co/ lofi.cafe https://es.symbolab.com/')),
        Key([mod, "shift"], "a", lazy.spawn(
            'brave-browser --new-window https://www3.animeflv.net/ https://www.mangatigre.com/ https://manganyaa.com/es https://www.youtube.com/'))

    ]
)


for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
# groups = [Group(i) for i in "123456789"]
#
# for i in groups:
#    keys.extend([
#        # mod1 + letter of group = switch to group
#        Key([mod], i.name, lazy.group[i.name].toscreen(),
#            desc="Switch to group {}".format(i.name)),
#
#        # mod1 + shift + letter of group = switch to & move focused window to group
#        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#        #    desc="Switch to & move focused window to group {}".format(i.name)),
#        # Or, use below if you prefer not to switch to that group.
#        # # mod1 + shift + letter of group = move focused window to group
#        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#            desc="move focused window to group {}".format(i.name)),
#    ])

layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 1,
    'margin': 4
}

layouts = [
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_conf),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    # layout.Bsp(**layout_conf),
    # layout.Matrix(**layout_conf),
    # layout.Tile(),

    # layout.TreeTab(
    #    font="Ubuntu",
    #    fontsize=10,
    #    sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
    #    section_fontsize=10,
    #    border_width=2,
    #    bg_color="1c1f24",
    #    active_bg="c678dd",
    #    active_fg="000000",
    #    inactive_bg="a9a1e1",
    #    inactive_fg="1c1f24",
    #    padding_left=0,
    #    padding_x=0,
    #    padding_y=5,
    #    section_top=10,
    #    section_bottom=20,
    #    level_shift=8,
    #    vspace=3,
    #    panel_width=200
    # ),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=font,
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(font=font,
                                **base(bg='dark'),
                                fontsize=16,
                                highlight_method='block',
                                inactive='505050',
                                ),
                widget.CurrentScreen(
                    font=font, active_text=" 蘒 ", inactive_text=" 﨡 ", **base(bg='dark')),


                widget.Prompt(),
                widget.WindowName(
                    max_chars=15, format='{name}', **base(bg='dark', fg='text')),
                powerline('color4', 'dark'),


                widget.PulseVolume(**base(bg='color4'),
                                   padding=5,
                                   fmt='墳 {}',
                                   fontsize=15,
                                   font=font
                                   ),
                *MusicPayer(bg='color4'),
                widget.Mpris2(
                    **base(bg='color4'),
                    font=font,
                    name='spotify',
                    objname="org.mpris.MediaPlayer2.spotify",
                    display_metadata=['xesam:title'],
                    stop_pause_text='',
                    fontsize=15,
                    scroll_wait_intervals=2000
                ),

                # icon(bg="color4", text=' '),
                # widget.Net(
                #    **base(bg='color4'),
                #    font=font,
                #    fontsize=15,
                #    format='Claro Caremonda: {down}↓↑{up}'
                # ),
                powerline('color3', 'color4'),
                # widget.Notify(**base(bg='color3'), font=font, max_chars=20),
                widget.Pomodoro(
                    **base(bg='color3'),
                    padding=17,
                    fontsize=18,
                    font=font, prefix_inactive="",
                    prefix_active="  ",
                    prefix_long_break=" 鬒 ",
                    prefix_paused="  ",
                    prefix_break="  ",
                    color_inactive='#000000',
                    color_active='#000000',
                    color_break='dcfb7f'

                ),

                powerline('color2', 'color3'),
                widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
                widget.CurrentLayout(**base(bg='color2'),
                                     font=font, padding=5),
                # Icon: nf-mdi-calendar_clock
                powerline('color1', 'color2'),
                icon(bg="color1", fontsize=17, text=' '),

                widget.Clock(**base(bg='color1'),
                             format='%d/%m/%Y - %H:%M ', font=font),

                powerline('dark', 'color1'),
                widget.Systray(background=colors['dark'], padding=5),
                widget.QuickExit(default_text=" ⏻ ",
                                 countdown_format='[{}]', background=colors['dark'],
                                 fontsize=15,
                                 font=font
                                 ),
            ],
            24,
        ),
    ),
    Screen(
        top=bar.Bar([
            widget.GroupBox(font=font,
                            **base(bg='dark'),
                            fontsize=16,
                            highlight_method='block'
                            ),

            widget.CurrentScreen(
                    **base(bg='dark'), font=font, active_text=" 蘒 ", inactive_text=" 﨡 "),
            widget.WindowName(
                max_chars=15, format='{name}', **base(bg='dark')),
            powerline('color2', 'dark'),
            widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
            widget.CurrentLayout(**base(bg='color2'),
                                 font=font, padding=5),
            # Icon: nf-mdi-calendar_clock
            powerline('color1', 'color2'),
            icon(bg="color1", fontsize=17, text=' '),

            widget.Clock(**base(bg='color1'),
                         format='%d/%m/%Y - %H:%M ', font=font)

        ], 24)
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
