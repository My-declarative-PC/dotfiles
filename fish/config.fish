function fish_greeting
    if command -sq fastfetch
        fastfetch
    end
end

### Aliases
function ls
    if not command -sq lsd
        ls $argv
    end

    lsd $argv
end

function la
    if not command -sq lsd
        ls -hal $argv
    end

    lsd -la $argv
end

function ll
    if not command -sq lsd
        ls -hl $argv
    end

    lsd -l $argv
end

### Vatibles
set -x SSH_AUTH_SOCK $XDG_RUNTIME_DIR/ssh-agent.socket

### Initializations
starship init fish | source
zoxide init fish | source
