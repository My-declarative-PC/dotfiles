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

if command -v yq &>/dev/null; then
    eval "$(yq shell-completion bash)"
fi

if command -v docker &>/dev/null; then
    eval "$(docker completion bash)"
fi

if command -v docker &>/dev/null; then
    eval "$(wezterm shell-completion --shell bash)"
fi

if command -v bat &>/dev/null; then
    eval "$(bat --completion bash)"
fi

if command -v sk &>/dev/null; then
    source <(sk --shell bash)
fi

command_not_found_handle() {
    # don't run if not in a container
    if [ ! -e /run/.containerenv ] && [ ! -e /.dockerenv ]; then
        exit 127
    fi

    distrobox-host-exec "${@}"
}
if [ -n "${ZSH_VERSION-}" ]; then
    command_not_found_handler() {
        command_not_found_handle "$@"
    }
fi
