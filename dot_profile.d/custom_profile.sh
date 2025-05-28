#!/bin/bash

# PATH
export PATH="$PATH:/var/lib/flatpak/exports/bin"
export PATH="$PATH:$HOME/.local/bin"
export PATH="$PATH:$HOME/.local/share/flatpak/exports/share"
# PATH end

# homebrew
export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"
export MANPATH="/home/linuxbrew/.linuxbrew/share/man:$MANPATH"
export INFOPATH="/home/linuxbrew/.linuxbrew/share/info:$INFOPATH"
# homebrew end

# pnpm
export PNPM_HOME="$HOME/.local/share/pnpm"
case ":$PATH:" in
*":$PNPM_HOME:"*) ;;
*) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end

# GTK
export GTK_USE_PORTAL=1
export FLAVOR="mocha"
export ACCENT="mauve"
export GTK_THEME=catppuccin-$FLAVOR-$ACCENT-standard+default
export ADW_DISABLE_PORTAL=1
export GTK2_RC_FILES=/usr/share/themes/$GTK_THEME
export XCURSOR_THEME=catppuccin-$FLAVOR-$ACCENT-cursors
# GTK end

# fzf
source ~/.profile.d/fzf-theme.sh
export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS: \
--preview \"bat --color=always --style=numbers,changes,plain --line-range=:500 {}\"
"
# fzf end

export EDITOR=hx
export QT_STYLE_OVERRIDE=kvantum
export SSH_AUTH_SOCK=$XDG_RUNTIME_DIR/ssh-agent.socket
export XAUTHORITY=$HOME/.Xauthority
