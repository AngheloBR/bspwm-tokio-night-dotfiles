#!/usr/bin/env bash

# ============================================================
#   ████████╗ ██████╗ ██╗  ██╗██╗   ██╗ ██████╗
#   ╚══██╔══╝██╔═══██╗██║ ██╔╝╚██╗ ██╔╝██╔═══██╗
#      ██║   ██║   ██║█████╔╝  ╚████╔╝ ██║   ██║
#      ██║   ██║   ██║██╔═██╗   ╚██╔╝  ██║   ██║
#      ██║   ╚██████╔╝██║  ██╗   ██║   ╚██████╔╝
#      ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝
# ============================================================
#   Tokyo Night Dotfiles
#   bspwm | polybar | picom | dunst | rofi | ghostty
# ============================================================
#   Styx
# ============================================================

set -euo pipefail

DOTFILES_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_DIR="$DOTFILES_DIR/config"
THEMES_DIR="$DOTFILES_DIR/themes"
SCRIPTS_DIR="$DOTFILES_DIR/scripts"
BACKUP_DIR="$HOME/.config/backup-dotfiles-$(date +%Y%m%d-%H%M%S)"

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

# ============================================================
# FUNCIONES
# ============================================================

print_banner() {
  clear
  echo -e "${BLUE}"
  echo '   ████████╗ ██████╗ ██╗  ██╗██╗   ██╗ ██████╗'
  echo '   ╚══██╔══╝██╔═══██╗██║ ██╔╝╚██╗ ██╔╝██╔═══██╗'
  echo '      ██║   ██║   ██║█████╔╝  ╚████╔╝ ██║   ██║'
  echo '      ██║   ██║   ██║██╔═██╗   ╚██╔╝  ██║   ██║'
  echo '      ██║   ╚██████╔╝██║  ██╗   ██║   ╚██████╔╝'
  echo '      ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝'
  echo -e "${NC}"
  echo -e "${PURPLE}  ───────────────────────────────────────────${NC}"
  echo -e "${CYAN}   Tokyo Night Dotfiles - bspwm Edition${NC}"
  echo -e "${PURPLE}  ───────────────────────────────────────────${NC}"
  echo -e "${YELLOW}   Styx${NC}"
  echo -e "${PURPLE}  ───────────────────────────────────────────${NC}"
  echo ""
  echo -e "${GREEN}   Directorio: $DOTFILES_DIR${NC}"
  echo ""
}

log()     { echo -e "${GREEN}[✓]${NC} $1"; }
warn()    { echo -e "${YELLOW}[!]${NC} $1"; }
error()   { echo -e "${RED}[✗]${NC} $1"; }
info()    { echo -e "${CYAN}[i]${NC} $1"; }
section() { echo -e "\n${BLUE}══ $1 ══${NC}\n"; }

check_command() {
  if ! command -v "$1" &>/dev/null; then
    return 1
  fi
  return 0
}

# ============================================================
# INICIO
# ============================================================

print_banner

# Verificar que no se ejecute como root
if [ "$EUID" -eq 0 ]; then
  error "No ejecutes este script como root. Usa tu usuario normal."
  exit 1
fi

section "Verificando dependencias"

PKGS=(
  # Core
  bspwm sxhkd polybar picom dunst rofi
  # Herramientas
  feh brightnessctl playerctl fastfetch
  # Audio
  pipewire pipewire-pulse wireplumber
  # Fuentes
  ttf-jetbrains-mono-nerd noto-fonts ttf-font-awesome
  # Temas
  papirus-icon-theme kvantum
  # Utilidades
  btop flameshot betterlockscreen neovim cava ranger thunar wget
)

AUR_PKGS=()
AUR_HELPER=""

# Detectar AUR helper
if check_command "yay"; then
  AUR_HELPER="yay"
elif check_command "paru"; then
  AUR_HELPER="paru"
fi

MISSING=()
for pkg in "${PKGS[@]}"; do
  if ! pacman -Q "$pkg" &>/dev/null; then
    MISSING+=("$pkg")
  fi
done

if [ ${#MISSING[@]} -gt 0 ]; then
  warn "Paquetes faltantes: ${MISSING[*]}"
  echo ""
  echo -n "¿Instalar con pacman? [S/n]: "
  read -r respuesta
  if [[ "$respuesta" =~ ^[Nn] ]]; then
    warn "Continúa sin instalar dependencias..."
  else
    info "Instalando con pacman..."
    sudo pacman -S --needed --noconfirm "${MISSING[@]}"
    log "Paquetes instalados"
  fi
else
  log "Todas las dependencias base están instaladas"
fi

# pywal (AUR)
if ! check_command "wal"; then
  warn "pywal (python-pywal) no está instalado"
  if [ -n "$AUR_HELPER" ]; then
    echo -n "¿Instalar pywal desde AUR? [S/n]: "
    read -r respuesta
    if [[ ! "$respuesta" =~ ^[Nn] ]]; then
      $AUR_HELPER -S --noconfirm python-pywal
      log "pywal instalado"
    fi
  else
    warn "No hay AUR helper (yay/paru). pywal debe instalarse manualmente"
  fi
else
  log "pywal disponible"
fi

# picom-ibhagwan-git (opcional, animaciones)
if check_command "picom"; then
  echo ""
  echo -n "¿Instalar picom-ibhagwan-git para animaciones extra? [s/N]: "
  read -r respuesta
  if [[ "$respuesta" =~ ^[Ss] ]]; then
    if [ -n "$AUR_HELPER" ]; then
      $AUR_HELPER -S --noconfirm picom-ibhagwan-git
      log "picom-ibhagwan-git instalado (más animaciones)"
    else
      warn "No hay AUR helper. Instala picom-ibhagwan-git manualmente"
    fi
  fi
fi

# ============================================================
# RESPALDO
# ============================================================

section "Respaldo de configuraciones existentes"

BACKUP_DIRS=(
  "$HOME/.config/bspwm"
  "$HOME/.config/sxhkd"
  "$HOME/.config/polybar"
  "$HOME/.config/picom"
  "$HOME/.config/dunst"
  "$HOME/.config/rofi"
  "$HOME/.config/ghostty"
  "$HOME/.config/gtk-3.0"
  "$HOME/.config/fastfetch"
  "$HOME/.config/betterlockscreen"
  "$HOME/.config/btop"
  "$HOME/.config/Kvantum"
  "$HOME/.config/nvim"
  "$HOME/.config/themes"
  "$HOME/.p10k.zsh"
)

for dir in "${BACKUP_DIRS[@]}"; do
  if [ -d "$dir" ] || [ -f "$dir" ]; then
    mkdir -p "$BACKUP_DIR/$dir"
    cp -r "$dir" "$BACKUP_DIR/$dir" 2>/dev/null || true
    warn "Respaldado: $dir → $BACKUP_DIR"
  fi
done

if [ -d "$BACKUP_DIR" ]; then
  log "Respaldos guardados en: $BACKUP_DIR"
else
  info "No había configuraciones previas que respaldar"
fi

# ============================================================
# INSTALAR CONFIGURACIONES
# ============================================================

section "Instalando configuraciones Tokyo Night"

# Asegurar directorios de configuración
mkdir -p "$HOME/.config"
mkdir -p "$HOME/.local/bin"
mkdir -p "$HOME/Pictures/Wallpapers"

# Instalar temas
info "Instalando paleta de colores..."
mkdir -p "$HOME/.config/themes"
cp "$THEMES_DIR/colors-tokyo-night.sh" "$HOME/.config/themes/"
log "Temas instalados en ~/.config/themes/"

# Instalar configuraciones
CONFIG_MAP=(
  "bspwm:bspwm"
  "sxhkd:sxhkd"
  "polybar:polybar"
  "picom:picom"
  "dunst:dunst"
  "rofi:rofi"
  "ghostty:ghostty"
  "gtk-3.0:gtk-3.0"
  "Thunar:Thunar"
  "fastfetch:fastfetch"
  "betterlockscreen:betterlockscreen"
  "btop:btop"
  "kvantum:Kvantum"
  "nvim:nvim"
  "zsh:zsh"
  "firefox:firefox"
  "lightdm:lightdm"
  "cava:cava"
  "ranger:ranger"
  "Thunar:Thunar"
)

for entry in "${CONFIG_MAP[@]}"; do
  src="${CONFIG_DIR}/${entry%%:*}"
  dest="${HOME}/.config/${entry##*:}"
  
  if [ -e "$dest" ]; then
    warn "Eliminando configuración anterior: $dest"
    rm -rf "$dest"
  fi
  
  cp -r "$src" "$dest"
  log "Instalado: $dest"
done

# Hacer ejecutables
chmod +x "$HOME/.config/polybar/launch.sh" 2>/dev/null || true
chmod +x "$HOME/.config/bspwm/bspwmrc" 2>/dev/null || true

# Instalar scripts
info "Instalando scripts..."
cp "$SCRIPTS_DIR/change-wallpaper.sh" "$HOME/.local/bin/change-wallpaper"
chmod +x "$HOME/.local/bin/change-wallpaper"
cp "$SCRIPTS_DIR/setup-pywalfox.sh" "$HOME/.local/bin/setup-pywalfox"
chmod +x "$HOME/.local/bin/setup-pywalfox"
cp "$SCRIPTS_DIR/auto-wallpaper.sh" "$HOME/.local/bin/auto-wallpaper"
chmod +x "$HOME/.local/bin/auto-wallpaper"
cp "$SCRIPTS_DIR/download-wallpapers.sh" "$HOME/.local/bin/download-wallpapers"
chmod +x "$HOME/.local/bin/download-wallpapers"
log "Scripts instalados en ~/.local/bin/"

# ============================================================
# POST-INSTALACIÓN
# ============================================================

section "Post-instalación"

# Establecer GTK theme (si existe)
GTK_THEME="Tokyonight-Dark-BL"
if [ -d "/usr/share/themes/$GTK_THEME" ]; then
  gsettings set org.gnome.desktop.interface gtk-theme "$GTK_THEME" 2>/dev/null || true
  log "GTK theme: $GTK_THEME"
else
  info "GTK theme $GTK_THEME no encontrado en el sistema"
  echo -n "¿Descargar tema Tokyo Night GTK? [S/n]: "
  read -r respuesta
  if [[ ! "$respuesta" =~ ^[Nn] ]]; then
    if [ -n "$AUR_HELPER" ]; then
      $AUR_HELPER -S --noconfirm tokyonight-gtk-theme-git 2>/dev/null || \
      warn "No se pudo instalar el tema GTK. Puedes descargarlo manualmente"
    else
      warn "No hay AUR helper. Instala tokyonight-gtk-theme-git manualmente"
    fi
  fi
fi

# Establecer icon theme
gsettings set org.gnome.desktop.interface icon-theme "Papirus-Dark" 2>/dev/null || true

# Agregar scripts al PATH (zsh)
if ! grep -q 'local/bin' "$HOME/.zshrc" 2>/dev/null; then
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.zshrc"
  log "~/.local/bin agregado al PATH en .zshrc"
fi

# Configurar p10k
P10K_SRC="$HOME/.config/zsh/p10k-tokyo-night.zsh"
P10K_DEST="$HOME/.p10k.zsh"
if [ -f "$P10K_SRC" ] && [ ! -f "$P10K_DEST" ]; then
  cp "$P10K_SRC" "$P10K_DEST"
  log "p10k Tokyo Night configurado (~/.p10k.zsh)"
  echo "Asegúrate de tener en .zshrc:  source ~/.p10k.zsh"
fi

# Instalar btop theme
BTOP_THEME_SRC="$HOME/.config/btop/themes/tokyo-night.theme"
BTOP_THEME_DIR="$HOME/.config/btop/themes"
if [ -f "$BTOP_THEME_SRC" ]; then
  mkdir -p "$BTOP_THEME_DIR"
  log "btop Tokyo Night theme instalado"
fi

# Instalar Kvantum theme
if command -v kvantummanager &>/dev/null; then
  echo -n "¿Aplicar tema Kvantum Tokyonight-Dark-BL? [S/n]: "
  read -r respuesta
  if [[ ! "$respuesta" =~ ^[Nn] ]]; then
    kvantummanager --set Tokyonight-Dark-BL 2>/dev/null || true
    log "Kvantum theme: Tokyonight-Dark-BL"
  fi
fi

# Configurar betterlockscreen
if command -v betterlockscreen &>/dev/null && [ -f "$HOME/.config/betterlockscreen/betterlockscreenrc" ]; then
  log "betterlockscreen configurado (atajo: Super + Escape)"
  echo "  Para generar fondos de bloqueo: betterlockscreen -u ~/Pictures/Wallpapers/wallpaper.jpg"
fi

# Fastfetch
if command -v fastfetch &>/dev/null; then
  log "fastfetch Tokyo Night configurado"
  echo "  Para probar: fastfetch --config ~/.config/fastfetch/config.jsonc"
fi

# Ranger
if command -v ranger &>/dev/null; then
  log "ranger configurado con Tokyo Night"
  echo "  (ranger es un file manager de terminal con previews de imágenes)"
fi

# Cava
if command -v cava &>/dev/null; then
  log "cava Tokyo Night configurado"
  echo "  Para probar: cava"
fi

# Thunar
if command -v thunar &>/dev/null; then
  log "Thunar Tokyo Night configurado"
  echo "  Thunar usa el theme GTK Tokyonight-Dark-BL automáticamente"
  echo "  Acciones personalizadas (uca.xml): abrir terminal, copiar ruta, extraer, wallpaper"
fi

# Firefox
log "Firefox userChrome.css Tokyo Night (macOS style) instalado"
echo "  Para activar:"
echo "  1. about:config → toolkit.legacyUserProfileCustomizations.stylesheets = true"
echo "  2. Copiar config/firefox/userChrome.css a ~/.mozilla/firefox/*.default-release/chrome/"

# LightDM
log "LightDM theme Tokyo Night (macOS style) instalado"
echo "  Para activar lightdm-gtk-greeter:"
echo "    sudo cp config/lightdm/lightdm-gtk-greeter.conf /etc/lightdm/"
echo "  Para activar lightdm-webkit2-greeter:"
echo "    sudo cp -r config/lightdm/webkit-theme /usr/share/lightdm-webkit/themes/tokyo-night-macos"
echo "    y configurar /etc/lightdm/lightdm-webkit2-greeter.conf"

# auto-wallpaper
log "auto-wallpaper script instalado"
echo "  Uso: auto-wallpaper.sh ~/Pictures/Wallpapers 30"

# download-wallpapers
log "download-wallpapers script instalado"
echo "  Uso: download-wallpapers.sh ~/Pictures/Wallpapers"

# Neovim hint
if command -v nvim &>/dev/null; then
  log "Neovim: se copió hint de colorscheme Tokyo Night"
  echo "  Revisa: ~/.config/nvim/lua/config/colorscheme.lua"
  echo "  (Ajusta según tu estructura de LazyVim)"
fi

# pywalfox
echo ""
echo -n "¿Configurar pywalfox (Firefox + colores dinámicos)? [s/N]: "
read -r respuesta
if [[ "$respuesta" =~ ^[Ss] ]]; then
  if command -v pip &>/dev/null; then
    pip install --user pywalfox 2>/dev/null
    pywalfox install 2>/dev/null || warn "pywalfox requiere Firefox abierto para completar la instalación"
    log "pywalfox instalado. Ejecuta 'pywalfox update' para sincronizar colores"
  else
    warn "pip no instalado. Ejecuta: sudo pacman -S python-pip && pip install --user pywalfox"
  fi
fi

# ============================================================
# FINAL
# ============================================================

section "¡Instalación completada!"

echo -e "${CYAN}"
echo "   ████████╗ ██████╗ ██╗  ██╗██╗   ██╗ ██████╗"
echo "   ╚══██╔══╝██╔═══██╗██║ ██╔╝╚██╗ ██╔╝██╔═══██╗"
echo "      ██║   ██║   ██║█████╔╝  ╚████╔╝ ██║   ██║"
echo "      ██║   ██║   ██║██╔═██╗   ╚██╔╝  ██║   ██║"
echo "      ██║   ╚██████╔╝██║  ██╗   ██║   ╚██████╔╝"
echo "      ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝"
echo -e "${NC}"
echo -e "${PURPLE}  ───────────────────────────────────────────${NC}"
echo -e "${YELLOW}   Styx  -  Tokyo Night Dotfiles${NC}"
echo -e "${PURPLE}  ───────────────────────────────────────────${NC}"
echo ""
echo -e "${GREEN}  Tokyo Night bspwm dotfiles instalados correctamente${NC}"
echo ""
echo -e "${YELLOW}  Componentes instalados:${NC}"
echo -e "  ${CYAN}✓${NC} bspwm + sxhkd      ${CYAN}✓${NC} polybar        ${CYAN}✓${NC} picom"
echo -e "  ${CYAN}✓${NC} dunst              ${CYAN}✓${NC} rofi           ${CYAN}✓${NC} ghostty"
echo -e "  ${CYAN}✓${NC} fastfetch          ${CYAN}✓${NC} btop           ${CYAN}✓${NC} lockscreen"
echo -e "  ${CYAN}✓${NC} GTK/Kvantum        ${CYAN}✓${NC} nvim           ${CYAN}✓${NC} zsh/p10k"
echo -e "  ${CYAN}✓${NC} Firefox macOS      ${CYAN}✓${NC} LightDM macOS  ${CYAN}✓${NC} cava"
  echo -e "  ${CYAN}✓${NC} ranger             ${CYAN}✓${NC} auto-wallpaper ${CYAN}✓${NC} pywal+pywalfox"
  echo -e "  ${CYAN}✓${NC} Thunar"
echo ""
echo -e "${YELLOW}  Pasos siguientes:${NC}"
echo ""
echo -e "  1. ${CYAN}Recargar bspwm:${NC}  ${PURPLE}Super + Escape${NC}"
echo -e "     ${YELLOW}O cierra sesión y vuelve a entrar${NC}"
echo ""
echo -e "  2. ${CYAN}Mostrar info del sistema:${NC}  ${PURPLE}fastfetch${NC}"
echo ""
echo -e "  3. ${CYAN}Cambiar wallpaper + colores:${NC}"
echo -e "     ${PURPLE}change-wallpaper -r ~/Pictures/Wallpapers${NC}"
echo ""
echo -e "  4. ${CYAN}Firefox Tokyo Night:${NC}"
echo -e "     Copiar ${PURPLE}config/firefox/userChrome.css${NC} a tu perfil de Firefox"
echo ""
echo -e "  5. ${CYAN}LightDM macOS login:${NC}"
echo -e "     ${PURPLE}sudo cp config/lightdm/lightdm-gtk-greeter.conf /etc/lightdm/${NC}"
echo ""
echo -e "  6. ${CYAN}Descargar wallpapers:${NC}  ${PURPLE}download-wallpapers${NC}"
echo ""
echo -e "  7. ${CYAN}Auto-wallpaper:${NC}  ${PURPLE}auto-wallpaper ~/Pictures/Wallpapers 15${NC}"
echo ""
echo -e "  8. ${CYAN}Pantalla de bloqueo:${NC}  ${PURPLE}Super + Escape${NC}"
echo ""
echo -e "  9. ${CYAN}Atajos clave:${NC}"
echo -e "     ${PURPLE}Super + D${NC}       → Rofi (lanzador)"
echo -e "     ${PURPLE}Super + Enter${NC}    → Ghostty (terminal)"
echo -e "     ${PURPLE}Super + W${NC}        → Rofi (ventanas)"
echo -e "     ${PURPLE}Super + Q${NC}        → Cerrar ventana"
echo -e "     ${PURPLE}Super + [hjkl]${NC}    → Navegar ventanas"
echo ""
echo -e "${GREEN}  ¡Disfruta tu Tokyo Night!${NC}"
echo -e "${CYAN}  Styx${NC}"
echo ""
