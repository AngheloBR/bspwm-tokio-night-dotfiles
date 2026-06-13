// ============================================================
// Firefox user.js - Tokyo Night Config
// ============================================================
// Colocar en: ~/.mozilla/firefox/*.default-release/user.js
// ============================================================

// Activar userChrome.css personalizado
user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);

// Compact mode
user_pref("browser.uidensity", 1);

// Desactivar recomendaciones
user_pref("browser.newtabpage.activity-stream.feeds.section.topstories", false);
user_pref("browser.newtabpage.activity-stream.feeds.snippets", false);
user_pref("browser.newtabpage.activity-stream.section.highlights", false);
user_pref("browser.newtabpage.activity-stream.feeds.topsites", false);

// Smooth scrolling
user_pref("general.smoothScroll", true);
user_pref("general.smoothScroll.mouseWheel.durationMinMS", 200);
user_pref("general.smoothScroll.mouseWheel.durationMaxMS", 400);

// Dark theme for all sites
user_pref("ui.systemUsesDarkTheme", 1);
user_pref("browser.theme.dark-private-windows", true);
user_pref("browser.in-content.dark-mode", true);

// Hardware acceleration
user_pref("layers.acceleration.force-enabled", true);
user_pref("gfx.webrender.all", true);
user_pref("gfx.webrender.enabled", true);
user_pref("media.hardware-video-decoding.enabled", true);

// Telemetry off
user_pref("toolkit.telemetry.enabled", false);
user_pref("toolkit.telemetry.unified", false);
user_pref("datareporting.healthreport.uploadEnabled", false);
user_pref("datareporting.policy.dataSubmissionEnabled", false);

// Pocket off
user_pref("extensions.pocket.enabled", false);

// PiP
user_pref("media.videocontrols.picture-in-picture.enabled", true);
