{ config, pkgs, ... }:

{
  programs.lazygit = {
    enable = true;
    settings = {
      gui.showIcons = true;
      git.paging = {
        colorArg = "always";
        pager = "${pkgs.delta}/bin/delta --side-by-side --line-numbers --dark --paging=never";
      };
    };
  };
}
