#!/usr/bin/env bash

# ============================================================
# setup-pywalfox.sh - Firefox + pywal (Material You)
# ============================================================
# Integra los colores de pywal en Firefox
# ============================================================

set -euo pipefail

echo "Instalando pywalfox para Firefox..."

# Instalar pywalfox
if ! command -v pywalfox &>/dev/null; then
  if command -v pip &>/dev/null; then
    pip install --user pywalfox
  else
    echo "pip no encontrado. Instala python-pip primero."
    exit 1
  fi
fi

# Inicializar pywalfox
if pgrep -x firefox >/dev/null 2>&1; then
  pywalfox install || warn "pywalfox install requiere Firefox abierto"
else
  warn "Firefox no está abierto. Ejecuta: firefox &"
  warn "Luego ejecuta: pywalfox install"
fi

echo ""
echo "pywalfox instalado."
echo ""
echo "Pasos manuales en Firefox:"
echo "  1. Abre Firefox"
echo "  2. Ve a about:debugging#/runtime/this-firefox"
echo "  3. Haz clic en 'Cargar complemento temporal...'"
echo "  4. Selecciona ~/.mozilla/firefox/*.default-release/pywalfox/extension/manifest.json"
echo ""
echo "Para actualizar colores en Firefox:  pywalfox update"
