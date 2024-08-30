#!/bin/bash

git clone https://github.com/tmux-plugins/tpm ~/dotfiles/tmux/plugins/tpm

if ! [ -h ~/.tmux.conf ]; then
    ln -s ~/dotfiles/tmux/tmux.conf ~/.tmux.conf
fi
if ! [ -h ~/.tmux ]; then
    ln -s ~/dotfiles/tmux ~/.tmux
fi
