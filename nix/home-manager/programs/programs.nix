{ config, pkgs, ... }:

{
  imports = [
    ./lsd/lsd.nix
    ./git/git.nix
    ./tmux/tmux.nix
    ./fish/fish.nix
    ./zoxide/zoxide.nix
    ./firefox/firefox.nix
    ./lazygit/lazygit.nix
  ];

  programs = {
    starship.enable = true;
  };
}
