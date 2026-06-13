#!/usr/bin/env bash

# ============================================================
# change-wallpaper.sh - Tokyo Night + Material You
# ============================================================
# Cambia el wallpaper y regenera los colores con pywal
# Mantiene la base Tokyo Night pero actualiza acentos dinámicos
# ============================================================

WALLPAPER_DIR="${1:-$HOME/Pictures/Wallpapers}"
CACHE_FILE="$HOME/.cache/wal/wal"

show_help() {
  cat <<EOF
Uso: $(basename "$0") [OPCIÓN] [ARCHIVO|DIRECTORIO]

Opciones:
  -r, --random       Selecciona un wallpaper aleatorio del directorio
  -n, --next         Siguiente wallpaper (aleatorio)
  -p, --previous     Wallpaper anterior
  -c, --current      Muestra el wallpaper actual
  -h, --help         Muestra esta ayuda

Sin argumentos, usa el archivo o directorio especificado.
EOF
  exit 0
}

select_random() {
  if [ -d "$WALLPAPER_DIR" ]; then
    WALLPAPER=$(find "$WALLPAPER_DIR" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" \) | shuf -n1)
    if [ -z "$WALLPAPER" ]; then
      notify-send -u critical "change-wallpaper" "No se encontraron imágenes en $WALLPAPER_DIR"
      exit 1
    fi
  else
    notify-send -u critical "change-wallpaper" "Directorio $WALLPAPER_DIR no existe"
    exit 1
  fi
}

case "${1:-}" in
  -h|--help) show_help ;;
  -r|--random|"")
    select_random
    ;;
  -n|--next)
    select_random
    ;;
  -p|--previous)
    if [ -f "$CACHE_FILE" ]; then
      WALLPAPER=$(cat "$CACHE_FILE")
    else
      select_random
    fi
    ;;
  -c|--current)
    if [ -f "$CACHE_FILE" ]; then
      echo "Wallpaper actual: $(cat "$CACHE_FILE")"
      feh --bg-fill "$(cat "$CACHE_FILE")"
    else
      notify-send -u critical "change-wallpaper" "No hay wallpaper en caché"
    fi
    exit 0
    ;;
  *)
    if [ -f "$1" ]; then
      WALLPAPER="$1"
    elif [ -d "$1" ]; then
      WALLPAPER_DIR="$1"
      select_random
    else
      echo "Archivo o directorio no válido: $1"
      exit 1
    fi
    ;;
esac

# Aplicar wallpaper con pywal (genera colores dinámicos)
wal -i "$WALLPAPER" -n --saturate 0.7

# Establecer wallpaper con feh
feh --bg-fill "$WALLPAPER"

# Actualizar colores en vivo para apps compatibles
pywalfox update 2>/dev/null

# Notificar
notify-send -i "$WALLPAPER" "Tokyo Night + Material You" \
  "Wallpaper actualizado\n$(basename "$WALLPAPER")"
