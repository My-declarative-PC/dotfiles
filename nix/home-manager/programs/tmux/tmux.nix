{ config, pkgs, ... }:

{
  programs.tmux = {
    enable = true;
    baseIndex = 1;
    clock24 = true;
    shell = "${pkgs.fish}/bin/fish";
    extraConfig = ''set -ag terminal-overrides ",xterm*:Tc"''; # Set true color
    plugins = [ {
      plugin = pkgs.tmuxPlugins.dracula;
      extraConfig = ''
        set -g @dracula-show-powerline true
        set -g @dracula-show-left-icon session
        set -g @dracula-plugins "cpu-usage ram-usage"
      '';
    } ];
  };
}
