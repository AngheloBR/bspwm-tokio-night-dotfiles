# ============================================================
# ranger colorscheme - Tokyo Night
# ============================================================

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class tokyo_night(ColorScheme):
    def use(self, context):
        fg, bg, attr = default_colors

        # Reset
        if context.reset:
            return default_colors

        # Tokyo Night palette
        bg_main     = 0
        bg_surface  = 0
        bg_hl       = 0
        fg_main     = 7
        fg_dim      = 8
        blue        = 4
        purple      = 5
        cyan        = 6
        green       = 2
        yellow      = 3
        red         = 1
        white       = 7
        black       = 0

        # Normal
        if context.directory:
            fg = blue
            attr |= bold

        elif context.executable and not any((context.media, context.container, context.fifo, context.socket)):
            attr |= bold
            fg = green

        elif context.socket:
            fg = purple

        elif context.fifo or context.device:
            fg = yellow

        elif context.link:
            fg = cyan if context.good else red

        elif context.tag_marker and context.selected:
            bg = blue
            fg = bg_main

        elif context.tag_marker:
            bg = blue
            fg = bg_main

        elif context.selected:
            bg = bg_hl

        elif context.cut:
            fg = red

        else:
            fg = fg_main

        # Scroll
        if context.in_titlebar:
            fg = white
            bg = bg_main

        if context.in_taskview:
            fg = white
            bg = bg_main

        # Titlebar
        if context.in_titlebar and context.selected:
            fg = bg_main
            bg = purple

        # Stats
        if context.in_statusbar:
            if context.loaded:
                fg = green
            elif context.cut:
                fg = red
            else:
                fg = fg_main

        if context.border:
            fg = bg_hl

        return fg, bg, attr
