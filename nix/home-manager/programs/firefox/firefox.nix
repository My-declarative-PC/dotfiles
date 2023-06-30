{ config, pkgs, ... }:

let
  nurpkgs = import (builtins.fetchTarball "https://github.com/nix-community/NUR/archive/master.tar.gz") { inherit pkgs; };
in
{
  programs.firefox = {
    enable = true;
    profiles = {
      defualt = {
        id = 0;
        name = "defualt";
        isDefault = true;
        extensions = with nurpkgs.repos.rycee.firefox-addons; [
          stylus
          vimium
          ublock-origin
          tree-style-tab
          dracula-dark-colorscheme
          multi-account-containers
        ];
        userChrome = "
          #TabsToolbar { visibility: collapse !important; }
        ";
        settings = {
          # Hide tabs toolbar
          "browser.tabs.tabmanager.enabled"                     = false;
          "toolkit.legacyUserProfileCustomizations.stylesheets" = true;

          # Hardware video acceleration
          "gfx.webrender.all"          = true;
          "media.ffmpeg.vaapi.enabled" = true;

          # Enable HTTPS-Only Mode
          "dom.security.https_only_mode"              = true;
          "dom.security.https_only_mode_ever_enabled" = true;

          # Privacy settings
          "privacy.donottrackheader.enabled"                  = true;
          "privacy.trackingprotection.enabled"                = true;
          "privacy.partition.network_state.ocsp_cache"        = true;
          "privacy.trackingprotection.socialtracking.enabled" = true;

          # Disable Pocket Integration
          "extensions.pocket.api"                                               = "";
          "extensions.pocket.site"                                              = "";
          "extensions.pocket.enabled"                                           = false;
          "extensions.pocket.showHome"                                          = false;
          "extensions.pocket.oAuthConsumerKey"                                  = "";
          "browser.newtabpage.activity-stream.section.highlights.includePocket" = false;

          # Disable all sorts of telemetry
          "toolkit.telemetry.enabled"                          = false;
          "toolkit.telemetry.unified"                          = false;
          "browser.ping-centre.telemetry"                      = false;
          "toolkit.telemetry.archive.enabled"                  = false;
          "toolkit.telemetry.bhrPing.enabled"                  = false;
          "toolkit.telemetry.updatePing.enabled"               = false;
          "toolkit.telemetry.hybridContent.enabled"            = false;
          "toolkit.telemetry.newProfilePing.enabled"           = false;
          "toolkit.telemetry.reportingpolicy.firstRun"         = false;
          "toolkit.telemetry.firstShutdownPing.enabled"        = false;
          "browser.newtabpage.activity-stream.telemetry"       = false;
          "toolkit.telemetry.shutdownPingSender.enabled"       = false;
          "browser.newtabpage.activity-stream.feeds.telemetry" = false;
        };
      };
    };
  };
}
