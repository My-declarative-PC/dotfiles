function fish_greeting
    if command -sq fastfetch
        fastfetch
    end
end

### Aliases
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

function la
    ls -hal $argv
end

function ll
    ls -l $argv
end

### Vatibles
set -x SSH_AUTH_SOCK $XDG_RUNTIME_DIR/ssh-agent.socket

### Initializations
if command -sq starship
    starship init fish | source
end

if command -sq starship
    zoxide init fish | source
end
