#!/usr/bin/env bash

# ============================================================
# auto-wallpaper.sh - Cambia wallpaper automáticamente
# ============================================================
# Uso: auto-wallpaper.sh [directorio] [minutos]
# Ejemplo: auto-wallpaper.sh ~/Pictures/Wallpapers 15
# ============================================================

set -euo pipefail

WALLPAPER_DIR="${1:-$HOME/Pictures/Wallpapers}"
INTERVAL="${2:-30}"  # minutos

show_help() {
  cat <<EOF
Uso: $(basename "$0") [DIRECTORIO] [INTERVALO_MINUTOS]

Cambia el wallpaper automáticamente cada N minutos usando pywal.

Argumentos:
  DIRECTORIO      Directorio con wallpapers (default: ~/Pictures/Wallpapers)
  INTERVALO       Minutos entre cambios (default: 30)

Ejemplos:
  $(basename "$0")                               # Cada 30min
  $(basename "$0") ~/Wallpapers 15               # Cada 15min
  $(basename "$0") ~/Wallpapers 60               # Cada 1h

Para detener: pkill -f auto-wallpaper
EOF
  exit 0
}

case "${1:-}" in
  -h|--help) show_help ;;
esac

if [ ! -d "$WALLPAPER_DIR" ]; then
  echo "Error: $WALLPAPER_DIR no existe"
  exit 1
fi

WALLPAPERS=()
while IFS= read -r f; do
  WALLPAPERS+=("$f")
done < <(find "$WALLPAPER_DIR" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" \) | sort)

if [ ${#WALLPAPERS[@]} -eq 0 ]; then
  echo "Error: No hay imágenes en $WALLPAPER_DIR"
  exit 1
fi

CURRENT=0
INTERVAL_SEC=$((INTERVAL * 60))

echo "auto-wallpaper iniciado"
echo "  Directorio: $WALLPAPER_DIR"
echo "  Intervalo:  $INTERVAL minutos"
echo "  Wallpapers: ${#WALLPAPERS[@]}"
echo "  PID: $$"
echo ""

while true; do
  WALLPAPER="${WALLPAPERS[$CURRENT]}"

  if command -v wal &>/dev/null; then
    wal -i "$WALLPAPER" -n --saturate 0.7
  fi
  feh --bg-fill "$WALLPAPER"

  NAME=$(basename "$WALLPAPER")
  notify-send -i "$WALLPAPER" "auto-wallpaper" "$NAME ($((CURRENT+1))/${#WALLPAPERS[@]})" 2>/dev/null || true

  CURRENT=$(( (CURRENT + 1) % ${#WALLPAPERS[@]} ))
  sleep "$INTERVAL_SEC"
done
