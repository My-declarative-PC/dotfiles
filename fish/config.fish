function fish_greeting
    if command -sq fastfetch
        fastfetch
    end
end

#
# Aliases
#

### ls
function LS
    bash -c ls $argv
end

function ls
    if not command -sq lsd
        LS $argv
        return
    end

    lsd $argv
end

function ll
    ls -lh $argv
end

function la
    ll -a $argv
end

### cd
function CD
    bash -c cd $argv
end

function cd
    if not command -sq zoxide
        CD $argv
        return
    end

    z $argv
end

#
# Vatibles
#
set -x SSH_AUTH_SOCK $XDG_RUNTIME_DIR/ssh-agent.socket

#
# Initializations
#
if command -sq starship
    starship init fish | source
end

if command -sq zoxide
    zoxide init fish | source
end
