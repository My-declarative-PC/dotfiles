function fish_greeting
    if command -sq fastfetch
        fastfetch
    end
end

#
# Aliases
#

### ls
function ls
    if command -sq lsd
        lsd $argv
    else
        bash -c ls $argv
    end
end

function ll
    ls -lh $argv
end

function la
    ll -a $argv
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
    zoxide init fish --cmd cd | source
end
