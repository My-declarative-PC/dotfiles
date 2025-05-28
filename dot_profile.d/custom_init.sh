#!/bin/bash

if command -v fastfetch &>/dev/null; then
    clear
    fastfetch
fi

#
# Aliases
#

function lsusb {
    if command -v cyme &>/dev/null; then
        cyme "$@"
    else
        lsusb "$@"
    fi
}

function cat {
    if command -v bat &>/dev/null; then
        bat "$@"
    else
        cat "$@"
    fi
}

function rg {
    if command -v batgrep &>/dev/null; then
        batgrep "$@"
    else
        rg "$@"
    fi
}

### ls
function ls {
    if command -v eza &>/dev/null; then
        eza -1 --icons "$@"
    else
        ls "$@"
    fi
}

function ll {
    ls -lh "$@"
}

function la {
    ll -a "$@"
}

function tree {
    if command -v eza &>/dev/null; then
        ls -T "$@"
    else
        tree "$@"
    fi
}

#
# Initializations
#

if command -v starship &>/dev/null; then
    eval "$(starship init bash)"
fi

if command -v zoxide &>/dev/null; then
    eval "$(zoxide init --cmd cd bash)"
fi

if command -v fzf &>/dev/null; then
    eval "$(fzf --bash)"
fi

if command -v direnv &>/dev/null; then
    eval "$(direnv hook bash)"
fi

if command -v atuin &>/dev/null; then
    eval "$(atuin init bash)"
fi
