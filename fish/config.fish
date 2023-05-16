# vatibles
set -x SSH_AUTH_SOCK $XDG_RUNTIME_DIR/ssh-agent.socket

starship init fish | source
zoxide init fish | source
