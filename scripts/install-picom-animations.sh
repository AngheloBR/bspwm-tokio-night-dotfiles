#!/usr/bin/env bash

# ============================================================
# Instalar picom-ibhagwan-git (animaciones extra)
# ============================================================

set -euo pipefail

AUR_HELPER=""

if command -v yay &>/dev/null; then
  AUR_HELPER="yay"
elif command -v paru &>/dev/null; then
  AUR_HELPER="paru"
else
  echo "No se encontró yay ni paru. Instálalos primero."
  exit 1
fi

echo "Instalando picom-ibhagwan-git con $AUR_HELPER..."
$AUR_HELPER -S --noconfirm picom-ibhagwan-git

echo "Descomenta las líneas de animación en ~/.config/picom/picom.conf"
echo "Busca la sección '# Animaciones (ibhagwan fork)'"
