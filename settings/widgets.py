from libqtile import widget, qtile
from settings.default_globals import font
from settings.themes import material_ocean as colors


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
    return widget.Sep(**base(), linewidth=1, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        font=font,
        text=text,
        padding=3
    )


def workspace():
    return [widget.GroupBox(font=font,
                            **base(bg='dark'),
                            fontsize=16,
                            highlight_method='block',
                            inactive='505050',
                            ),
            widget.CurrentScreen(
        font=font, active_text=" 蘒 ", inactive_text=" 﨡 ", **base(bg='dark')),

        separator(),
        widget.WindowName(
        format='{name}', **base(bg='dark', fg='active'), max_chars=20)]


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


primary_widgets = [
    *workspace(),
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
]
secondary_widgets = [
    *workspace(),
    powerline('color2', 'dark'),
    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
    widget.CurrentLayout(**base(bg='color2'),
                         font=font, padding=5),
    # Icon: nf-mdi-calendar_clock
    powerline('color1', 'color2'),
    icon(bg="color1", fontsize=17, text=' '),

    widget.Clock(**base(bg='color1'),
                 format='%d/%m/%Y - %H:%M ', font=font)

]
