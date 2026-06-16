function fish_greeting
    if command -sq fastfetch
        clear
        fastfetch
    end

    if status is-interactive
        import_bash_env
    end

    if command -sq atuin; and command -sq rg; and command -sq gum
        if not atuin init fish | rg --quiet '\bbind\b.*\-k'
            gum style \
                --border double \
                --border-foreground 212 \
                --margin "1 2" \
                --padding "1 3" \
                --align center \
                --bold \
                "🎉 Интеграция с atuin теперь генерирует валидный код!" \
                "Можно удалить временный костыль из конфигурации:" \
                "`atuin init fish | sd '(\bbind\b.*)(\-k)' '\$1' | source`"
        end
    end
end

function import_bash_env
    if not command -sq bash
        return
    end

    if not test -f ~/.profile.d/custom_profile.sh
        return
    end

    set -l skip_vars PWD SHLVL _ OLDPWD

    bash -c 'source ~/.profile.d/custom_profile.sh && env' | while read -l line
        if string match -q '*=*' -- $line
            set -l kv (string split -m 1 '=' -- $line)

            if test (count $kv) -eq 2
                if not contains -- $kv[1] $skip_vars
                    set -gx $kv[1] $kv[2]
                end
            end
        end
    end
end

#
# Aliases
#

function lsusb
    if command -sq cyme
        cyme $argv
    else if command -sq lsusb
        command lsusb $argv
    else if command -sq bash
        bash -c 'command lsusb "$@"' bash $argv
    else
        echo "lsusb: command not found" >&2
        return 127
    end
end

function ls
    if command -sq eza
        eza -1 --icons $argv
    else
        command ls $argv
    end
end

function ll
    ls -lh $argv
end

function la
    ll -a $argv
end

function tree
    if command -sq eza
        eza -T $argv
    else if command -sq tree
        command tree $argv
    else
        echo "tree: command not found" >&2
        return 127
    end
end

#
# Initializations
#

set -l brew_bin /home/linuxbrew/.linuxbrew/bin/brew

if test -x $brew_bin
    set -l brew_prefix ($brew_bin --prefix 2>/dev/null)

    if test -n "$brew_prefix"
        if test -d "$brew_prefix/share/fish/completions"
            set -p fish_complete_path "$brew_prefix/share/fish/completions"
        end

        if test -d "$brew_prefix/share/fish/vendor_completions.d"
            set -p fish_complete_path "$brew_prefix/share/fish/vendor_completions.d"
        end
    end
end

if command -sq starship
    starship init fish | source
end

if command -sq zoxide
    zoxide init --cmd cd fish | source
end

if command -sq fzf
    fzf --fish | source
end

if command -sq direnv
    direnv hook fish | source
end

if command -sq atuin
    if command -sq sd
        atuin init fish | sd '(\bbind\b.*)(\-k)' '${1}' | source
    else
        atuin init fish | source
    end
end

if command -sq yq
    yq shell-completion fish | source
end

if command -sq docker
    docker completion fish | source
end

if command -sq wezterm
    wezterm shell-completion --shell fish | source
end

if command -sq bat
    bat --completion fish | source
end

if command -sq sk
    sk --shell fish | source
end
