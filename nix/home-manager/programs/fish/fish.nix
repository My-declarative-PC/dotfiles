{ config, pkgs, ... }:

{
  programs.fish = {
    enable = true;
    shellAliases = { mkdir = "mkdir -p"; };
    interactiveShellInit = ''
      ${pkgs.any-nix-shell}/bin/any-nix-shell fish --info-right | source
    '';
    functions = {
      fish_greeting = { body = "clear; pfetch"; };
      mkcd = { body = "mkdir -p $argv[1]; and cd $argv[1]"; };
    };
  };
}
