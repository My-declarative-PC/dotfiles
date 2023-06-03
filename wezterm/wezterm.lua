local wezterm = require 'wezterm'

return {
    color_scheme = "Dracula (Official)",
    colors = { selection_bg = 'rgba(189 147 249 73%)' },
    font = wezterm.font("JetBrainsMono Nerd Font Mono"),
    tab_bar_at_bottom = true,
    use_fancy_tab_bar = false,
    window_decorations = "RESIZE",
    hide_tab_bar_if_only_one_tab = true,
    pane_focus_follows_mouse = true,
    window_close_confirmation = 'NeverPrompt',
    window_background_opacity = 0.7,

    window_padding = {
        left = 4,
        right = 4,
        top = 4,
        bottom = 4,
    },

    skip_close_confirmation_for_processes_named = {
        'bash',
        'sh',
        'zsh',
        'fish',
        'tmux',
    },
    keys = {
        {
            key = 'w',
            mods = 'CTRL|SHIFT',
            action = wezterm.action.CloseCurrentPane { confirm = false },
        },
        {
	    key = "]",
	    mods = "CTRL|ALT",
	    action = wezterm.action.ActivateTabRelative(1),
	},
        {
	    key = "[",
	    mods = "CTRL|ALT",
	    action = wezterm.action.ActivateTabRelative(-1),
	},
    }
}
