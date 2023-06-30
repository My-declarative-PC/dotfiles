{ config, pkgs, ... }:

{
  programs.fish = {
    enable = true;
    shellAliases = { mkdir = "mkdir -p"; };
    interactiveShellInit = ''
      set -Ux FZF_DEFAULT_OPTS "--color=fg:#f8f8f2,bg:#282a36,hl:#bd93f9 --color=fg+:#f8f8f2,bg+:#44475a,hl+:#bd93f9 --color=info:#ffb86c,prompt:#50fa7b,pointer:#ff79c6 --color=marker:#ff79c6,spinner:#ffb86c,header:#6272a4"
      ${pkgs.any-nix-shell}/bin/any-nix-shell fish --info-right | source
    '';
    functions = {
      fish_greeting = { body = "clear; pfetch"; };
      mkcd = { body = "mkdir -p $argv[1]; and cd $argv[1]"; };
    };
  };
}
