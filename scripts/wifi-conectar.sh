#!/usr/bin/env bash
# ============================================================
# wifi-conectar.sh - Selector WiFi con rofi + Tokyo Night
# ============================================================

T_BLUE='\e[38;2;122;162;247m'
T_CYAN='\e[38;2;125;207;255m'
T_GREEN='\e[38;2;158;206;106m'
T_RED='\e[38;2;247;118;142m'
T_ORANGE='\e[38;2;224;175;104m'
T_GRAY='\e[38;2;86;95;137m'
RESET='\e[0m'

ROFI_THEME="${HOME}/.config/rofi/config.rasi"

list_networks() {
  nmcli -t -f SSID,SECURITY device wifi list \
    | grep -v '^:' \
    | awk -F: '!seen[$1]++ {print $1"  ["$2"]"}'
}

notify() {
  notify-send "WiFi" "$1" -i network-wireless
}

# --- MAIN ---
case "${1:-}" in
  -l|--list)
    nmcli --color yes device wifi list
    ;;
  -h|--help)
    echo "Uso: wifi-conectar [SSID PASSWORD]"
    echo "     wifi-conectar        → selector rofi interactivo"
    echo "     wifi-conectar -l     → listar redes"
    exit 0
    ;;
  *)
    if [[ $# -ge 2 ]]; then
      nmcli device wifi connect "$1" password "$2" && \
        echo -e "  ${T_GREEN}󰄬 Conectado a ${T_CYAN}$1${RESET}" && \
        notify "Conectado a $1"
      exit $?
    elif [[ $# -eq 1 ]]; then
      if nmcli -t -f SSID connection show | grep -qx "$1"; then
        nmcli connection up "$1" && \
          echo -e "  ${T_GREEN}󰄬 Conectado a ${T_CYAN}$1${RESET}" && \
          notify "Conectado a $1"
        exit $?
      fi
      echo -e "  ${T_ORANGE}La red $1 requiere contraseña. Usa: wifi-conectar \"$1\" \"contraseña\"${RESET}"
      exit 1
    fi
    ;;
esac

# --- Modo interactivo rofi ---
networks="$(list_networks)"
if [[ -z "$networks" ]]; then
  echo -e "  ${T_ORANGE}󰤭 No se encontraron redes WiFi${RESET}"
  exit 1
fi

selected="$(echo "$networks" | rofi -dmenu -p "󰖩 WiFi" -theme "$ROFI_THEME" | awk '{print $1}')"
[[ -z "$selected" ]] && exit 0

if nmcli -t -f NAME connection show | grep -qx "$selected"; then
  nmcli connection up "$selected" && \
    echo -e "  ${T_GREEN}󰄬 Conectado a ${T_CYAN}$selected${RESET}" && \
    notify "Conectado a $selected"
  exit $?
fi

password="$(rofi -dmenu -password -p "󰛐 Clave para $selected" -theme "$ROFI_THEME")"
[[ -z "$password" ]] && exit 0

nmcli device wifi connect "$selected" password "$password" && \
  echo -e "  ${T_GREEN}󰄬 Conectado a ${T_CYAN}$selected${RESET}" && \
  notify "Conectado a $selected" || \
  echo -e "  ${T_RED}󰑮 Error conectando a ${T_CYAN}$selected${RESET}"
