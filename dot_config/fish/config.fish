function fish_greeting
    if command -sq fastfetch
        clear
        fastfetch
    end

    if status is-interactive
        import_bash_env
    end
end

function import_bash_env
    set -l skip_vars PWD SHLVL _ OLDPWD

    bash -c 'source ~/.profile.d/custom_profile.sh && env' | while read -l line
        if string match -q '*=*' -- $line
            set -l kv (string split -m 1 '=' $line)
            if test (count $kv) -eq 2
                if not contains $kv[1] $skip_vars
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
    else
        bash -c lsusb $argv
    end
end

function cat
    if command -sq bat
        bat $argv
    else
        bash -c cat $argv
    end
end

function rg
    if command -sq batgrep
        batgrep $argv
    else
        bash -c rg $argv
    end
end

### ls
function ls
    if command -sq eza
        eza -1 --icons $argv
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

function tree
    if command -sq eza
        ls -T $argv
    else
        bash -c tree $argv
    end
end

#
# Initializations
#
if test -d (brew --prefix)"/share/fish/completions"
    set -p fish_complete_path (brew --prefix)/share/fish/completions
end

if test -d (brew --prefix)"/share/fish/vendor_completions.d"
    set -p fish_complete_path (brew --prefix)/share/fish/vendor_completions.d
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
    atuin init fish | source
end
