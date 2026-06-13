#!/usr/bin/env bash

# ============================================================
# download-wallpapers.sh - Wallpapers Tokyo Night
# ============================================================
# Descarga wallpapers oficiales de Tokyo Night
# ============================================================

set -euo pipefail

DEST="${1:-$HOME/Pictures/Wallpapers}"

echo "Descargando wallpapers Tokyo Night..."
echo "Destino: $DEST"
mkdir -p "$DEST"

# Tokyo Night wallpapers from official sources
# Fuente: https://github.com/tokyonight-wallpapers/tokyonight-wallpapers

BASE_URL="https://raw.githubusercontent.com/tokyonight-wallpapers/tokyonight-wallpapers/main"

WALLPAPERS=(
  "abstract-dark-blue.png"
  "abstract-dark-purple.png"
  "city-dark.png"
  "city-night.png"
  "forest-mountains.png"
  "galaxy.png"
  "japan-street.png"
  "lake-mountains.png"
  "minimal-mountain.png"
  "moon-sunset.png"
  "mountain-lake.png"
  "neon-city.png"
  "ocean-wave.png"
  "retro-wave.png"
  "snow-mountain.png"
  "space-colors.png"
  "starry-night.png"
  "sunset-city.png"
)

COUNT=0
for wp in "${WALLPAPERS[@]}"; do
  URL="$BASE_URL/$wp"
  if wget -q --timeout=10 -O "$DEST/$wp" "$URL" 2>/dev/null; then
    echo "  ✓ $wp"
    COUNT=$((COUNT + 1))
  else
    echo "  ✗ $wp (no disponible)"
  fi
done

echo ""
echo "Descargados $COUNT wallpapers en $DEST"
echo ""
echo "Para usarlos: change-wallpaper -r $DEST"
echo "Para lockscreen: betterlockscreen -u $DEST"
