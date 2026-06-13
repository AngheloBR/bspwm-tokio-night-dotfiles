# ============================================================
# Aliases ZSH - Tokyo Night 
# ============================================================
# Fuente: bspwm-tokio-night-dotfiles/config/zsh/aliases.zsh
# ============================================================

# ─── Colores Tokyo Night para output ───
T_BG='\e[48;2;26;27;38m'
T_FG='\e[38;2;192;202;245m'
T_BLUE='\e[38;2;122;162;247m'
T_CYAN='\e[38;2;125;207;255m'
T_GREEN='\e[38;2;158;206;106m'
T_ORANGE='\e[38;2;224;175;104m'
T_RED='\e[38;2;247;118;142m'
T_PURP='\e[38;2;187;154;247m'
T_GRAY='\e[38;2;86;95;137m'
T_DIM='\e[38;2;54;59;84m'
BOLD='\e[1m'
ITALIC='\e[3m'
RESET='\e[0m'

# ════════════════════════════════════════════════════════════
# 🌐 REDES
# ════════════════════════════════════════════════════════════

# Listar redes WiFi (nmcli)
alias redes="nmcli --color yes device wifi list"

# Conectar WiFi rápida: wifi-conectar "SSID" "password"
wifi-conectar() {
  if [[ $# -eq 0 ]]; then
    echo -e "  ${T_BLUE}╭─${RESET} ${T_PURP}󰖩${RESET} ${T_FG}Uso:${RESET}"
    echo -e "  ${T_BLUE}├─${RESET} ${T_FG}wifi-conectar ${T_CYAN}\"SSID\" \"password\"${RESET}"
    echo -e "  ${T_BLUE}│${RESET}"
    echo -e "  ${T_BLUE}╰─${RESET} ${T_GRAY}O solo escribe ${T_FG}wifi-conectar${T_GRAY} sin args para el selector rofi${RESET}"
    return 1
  fi
  nmcli device wifi connect "$1" password "$2" && \
    echo -e "  ${T_GREEN}󰄬 Conectado a ${T_CYAN}$1${RESET}" || \
    echo -e "  ${T_RED}󰑮 Error al conectar a ${T_CYAN}$1${RESET}"
}

# Selector WiFi interactivo con rofi
wifi() {
  local networks
  networks="$(nmcli -t -f SSID,SECURITY device wifi list | grep -v '^:' | awk -F: '!seen[$1]++ {print $1"  ["$2"]"}')"
  if [[ -z "$networks" ]]; then
    echo -e "  ${T_ORANGE}󰤭 No se encontraron redes WiFi${RESET}"
    return 1
  fi
  local selected
  selected="$(echo "$networks" | rofi -dmenu -p "󰖩 WiFi" -theme ~/.config/rofi/config.rasi 2>/dev/null | awk '{print $1}')"
  [[ -z "$selected" ]] && return

  if nmcli -t -f NAME connection show | grep -qx "$selected"; then
    nmcli connection up "$selected" && \
      echo -e "  ${T_GREEN}󰄬 Conectado a ${T_CYAN}$selected${RESET}"
    return
  fi

  local password
  password="$(rofi -dmenu -password -p "󰛐 Clave" -theme ~/.config/rofi/config.rasi 2>/dev/null)"
  [[ -z "$password" ]] && return

  nmcli device wifi connect "$selected" password "$password" && \
    echo -e "  ${T_GREEN}󰄬 Conectado a ${T_CYAN}$selected${RESET}" || \
    echo -e "  ${T_RED}󰑮 Error conectando a ${T_CYAN}$selected${RESET}"
}

# ════════════════════════════════════════════════════════════
# 📦 SISTEMA
# ════════════════════════════════════════════════════════════

alias cat="bat"

update-programs() {
  pacman -Qqe > "$HOME/Escritorio/Dotfiles/programs.txt" && \
    echo -e "  ${T_GREEN}󰄬 Lista guardada en ~/Escritorio/Dotfiles/programs.txt${RESET}"
}

# ════════════════════════════════════════════════════════════
# 🔌 SERVIDORES / SSH
# ════════════════════════════════════════════════════════════

alias vps='ssh -i ~/.ssh/mi_vps_oracle.key opc@137.131.238.173'
alias server-minecraft='ssh -p 2222 jaren@192.168.100.98'

# ════════════════════════════════════════════════════════════
# ⚡ ENERGÍA
# ════════════════════════════════════════════════════════════

alias modo-ahorro="powerprofilesctl set power-saver && echo -e '  ${T_BLUE} Modo Ahorro activado${RESET}'"
alias modo-normal="powerprofilesctl set balanced && echo -e '  ${T_GREEN} Modo Normal activado${RESET}'"
alias modo-juego="powerprofilesctl set performance && echo -e '  ${T_PURP} Modo Rendimiento activado${RESET}'"

# ════════════════════════════════════════════════════════════
# 🖥️ VIRTUALIZACIÓN (KVM)
# ════════════════════════════════════════════════════════════

alias kvm-on='sudo virsh net-start default'
alias kvm-off='sudo virsh net-destroy default'
alias maquinas-virtuales="sudo virsh list --all"
alias disco-conectado="sudo mount -a"

snapshot() {
  local SCRIPT="$HOME/.local/bin/snapshot-kvm.sh"
  if [[ -x "$SCRIPT" ]]; then
    "$SCRIPT"
  else
    echo -e "  ${T_RED}󰑮 snapshot-kvm.sh no encontrado en ~/.local/bin/${RESET}"
  fi
}

# ════════════════════════════════════════════════════════════
# ⏰ UTILIDADES
# ════════════════════════════════════════════════════════════

alias androidstudio='~/android-studio/bin/studio.sh'
alias gemini='python ~/.local/src/asistente_voz/main.py'
alias opencode="opencode --model ollama/qwen3:8b"

# ════════════════════════════════════════════════════════════
# 🤖 JARVIS
# ════════════════════════════════════════════════════════════

jarvis() {
  local JARVIS_DIR="$HOME/.zona de confort/jarvis"
  cd "$JARVIS_DIR" && .venv/bin/python -m src.cli.main "$@"
}

# ════════════════════════════════════════════════════════════
# 🧹 EXTRA
# ════════════════════════════════════════════════════════════

definicion() {
  curl -s "https://es.wiktionary.org/wiki/$1" | \
    sed -n '/<ol>/,/<\/ol>/p' | sed 's/<[^>]*>//g' | sed '/^$/d' | head -5
}
