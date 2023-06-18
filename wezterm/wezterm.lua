local wezterm = require 'wezterm'

return {
    -- Set color
    color_scheme = "Dracula (Official)",
    colors = { selection_bg = 'rgba(189 147 249 73%)' },
    window_background_gradient = { 
        colors = { 'rgba(68 71 90 50%)', 'rgba(40 42 54 80%)', 'rgba(40 42 54 98%)', 'rgba(40 42 54 100%) },
        orientation = { Linear = { angle = -100.0} },
    },
    -- -- -- -- --

    font = wezterm.font("JetBrainsMono Nerd Font Mono"),
    tab_bar_at_bottom = true,
    use_fancy_tab_bar = false,
    window_decorations = "RESIZE",
    hide_tab_bar_if_only_one_tab = true,
    pane_focus_follows_mouse = true,
    window_close_confirmation = 'NeverPrompt',

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
