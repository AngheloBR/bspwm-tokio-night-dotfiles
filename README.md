# Tokyo Night Dotfiles

```
   ████████╗ ██████╗ ██╗  ██╗██╗   ██╗ ██████╗
   ╚══██╔══╝██╔═══██╗██║ ██╔╝╚██╗ ██╔╝██╔═══██╗
      ██║   ██║   ██║█████╔╝  ╚████╔╝ ██║   ██║
      ██║   ██║   ██║██╔═██╗   ╚██╔╝  ██║   ██║
      ██║   ╚██████╔╝██║  ██╗   ██║   ╚██████╔╝
      ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝
```

Configuración completa de **bspwm** con tema **Tokyo Night**, animaciones suaves, colores dinámicos tipo **Material You** (pywal), y componentes esenciales para un flujo de trabajo moderno.

**Styx**

---

## ⚡ Componentes incluidos

| Componente | Archivo | Descripción |
|---|---|---|
| **bspwm** | `config/bspwm/bspwmrc` | Bordes Tokyo Night, gaps, rounded |
| **sxhkd** | `config/sxhkd/sxhkdrc` | Atajos vim + multimedia + power menu |
| **polybar** | `config/polybar/config.ini` | Barra: workspaces, fecha, red, batería |
| **picom** | `config/picom/picom.conf` | Sombra, blur, corner-radius 12px, animaciones |
| **dunst** | `config/dunst/dunstrc` | Notificaciones redondeadas oscuras |
| **rofi** | `config/rofi/config.rasi` | Lanzador Tokyo Night transparente |
| **ghostty** | `config/ghostty/config` | Terminal con paleta Tokyo Night |
| **GTK** | `config/gtk-3.0/settings.ini` | Tema Tokyonight-Dark-BL + Papirus-Dark |
| **Kvantum** | `config/kvantum/kvantum.kvconfig` | Tema Qt Tokyonight-Dark-BL |
| **fastfetch** | `config/fastfetch/config.jsonc` | Banner Tokyo Night + Styx |
| **btop** | `config/btop/themes/tokyo-night.theme` | Monitor del sistema con colores Tokyo Night |
| **betterlockscreen** | `config/betterlockscreen/betterlockscreenrc` | Pantalla de bloqueo Tokyo Night |
| **nvim** | `config/nvim/lua/config/colorscheme.lua` | Hint colorscheme Tokyo Night para LazyVim |
| **zsh/p10k** | `config/zsh/p10k-tokyo-night.zsh` | Powerlevel10k con colores Tokyo Night |

---

## 🚀 Instalación

```bash
git clone https://github.com/AngheloBR/bspwm-tokio-night-dotfiles
cd bspwm-tokio-night-dotfiles
./install.sh
```

El instalador:
- Banner **Styx**
- Detecta e instala dependencias (pacman)
- AUR: pywal, picom-ibhagwan-git, tokyonight-gtk-theme-git (opcional)
- Respalda configs anteriores en `~/.config/backup-dotfiles-*`
- Copia todas las configuraciones
- Configura: p10k, btop theme, Kvantum, fastfetch, betterlockscreen
- Instala scripts en `~/.local/bin/`
- Configura pywalfox (Firefox + Material You) opcional

**Recargar bspwm:** `Super + Escape`

---

## 🖼️ fastfetch banner

Al ejecutar `fastfetch` verás:

```
   ████████╗ ██████╗ ██╗  ██╗██╗   ██╗ ██████╗
   ╚══██╔══╝██╔═══██╗██║ ██╔╝╚██╗ ██╔╝██╔═══██╗
      ██║   ██║   ██║█████╔╝  ╚████╔╝ ██║   ██║
      ██║   ██║   ██║██╔═██╗   ╚██╔╝  ██║   ██║
      ██║   ╚██████╔╝██║  ██╗   ██║   ╚██████╔╝
      ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝

                  Tokyo Night
                     Styx

   anghelo
  󰌢 Lenovo IdeaPad 1 15ALC7
  ...
```

---

## 🎨 Paleta Tokyo Night

| Color | Hex | Uso |
|---|---|---|
| Fondo | `#1a1b26` | bg principal |
| Superficie | `#24283b` | paneles, barras |
| Azul | `#7aa2f7` | acento principal |
| Púrpura | `#bb9af7` | acento secundario |
| Verde | `#9ece6a` | volumen, batería |
| Rojo | `#f7768e` | urgente, errores |
| Amarillo | `#e0af68` | carga, warnings |
| Cian | `#7dcfff` | red, fecha |
| Texto | `#c0caf5` | fg principal |
| Inactivo | `#3b4261` | bordes inactivos |

---

## 🎯 Atajos de teclado

### Generales
| Atajo | Acción |
|---|---|
| `Super + Enter` | Ghostty |
| `Super + D` | Rofi (lanzador) |
| `Super + Shift + D` | Rofi (run) |
| `Super + W` | Rofi (ventanas) |
| `Super + Shift + W` | Firefox |
| `Super + Escape` | Lock screen (betterlockscreen) |

### Navegación bspwm
| Atajo | Acción |
|---|---|
| `Super + h/j/k/l` | Navegar ventanas |
| `Super + Shift + h/j/k/l` | Mover ventana |
| `Super + Ctrl + h/j/k/l` | Preseleccionar dirección |

### Escritorios
| Atajo | Acción |
|---|---|
| `Super + 1-0` | Ir al escritorio N |
| `Super + Shift + 1-0` | Mover ventana al escritorio N |

### Ventanas
| Atajo | Acción |
|---|---|
| `Super + Q` | Cerrar |
| `Super + M` | Fullscreen |
| `Super + F` | Floating |
| `Super + Space` | Alternar floating/tiled |

### Multimedia
| Atajo | Acción |
|---|---|
| `XF86AudioRaiseVolume` | Subir volumen 5% |
| `XF86AudioLowerVolume` | Bajar volumen 5% |
| `XF86AudioMute` | Silenciar |
| `Print` | Flameshot GUI |
| `Super + Ctrl + W` | Wallpaper aleatorio (pywal) |

---

## 🖼️ Wallpaper + Material You

```bash
# Aleatorio
change-wallpaper -r ~/Pictures/Wallpapers

# Específico
change-wallpaper ~/Pictures/Wallpapers/mi-wallpaper.jpg

# Actual (refrescar)
change-wallpaper -c
```

Usa `pywal` para extraer colores y actualizar todo el sistema al vuelo.

---

## 🔥 Firefox + pywalfox

```bash
# Instalar e inicializar
setup-pywalfox

# Después de cambiar wallpaper, actualizar Firefox
pywalfox update
```

---

## 🖥️ Neovim (LazyVim)

El hint de configuración se copia a:
```
~/.config/nvim/lua/config/colorscheme.lua
```

Asegúrate de tener el plugin en tu `~/.config/nvim/lazy-lock.json`:
```lua
{ "folke/tokyonight.nvim", lazy = false, priority = 1000 }
```

---

## 📊 btop

Tema Tokyo Night instalado automáticamente en `~/.config/btop/themes/tokyo-night.theme`.

Selecciónalo en btop: `Esc → Themes → tokyo-night`

---

## 🔒 betterlockscreen

Configuración Tokyo Night instalada. Para generar fondos de bloqueo:

```bash
betterlockscreen -u ~/Pictures/Wallpapers/tokyo-night-wallpaper.jpg
```

Luego bloquea con `Super + Escape`.

---

## 🐚 ZSH + Powerlevel10k

Config Tokyo Night copiada a `~/.p10k.zsh`.

En tu `.zshrc` asegúrate de tener:
```zsh
source ~/.p10k.zsh
```

---

## 📁 Estructura completa

```
bspwm-tokio-night-dotfiles/
├── install.sh
├── README.md
├── config/
│   ├── bspwm/bspwmrc
│   ├── sxhkd/sxhkdrc
│   ├── polybar/{config.ini, launch.sh}
│   ├── picom/picom.conf
│   ├── dunst/dunstrc
│   ├── rofi/config.rasi
│   ├── ghostty/config
│   ├── gtk-3.0/settings.ini
│   ├── fastfetch/config.jsonc
│   ├── betterlockscreen/betterlockscreenrc
│   ├── btop/{btop.conf, themes/tokyo-night.theme}
│   ├── kvantum/kvantum.kvconfig
│   ├── nvim/lua/config/colorscheme.lua
│   └── zsh/p10k-tokyo-night.zsh
├── themes/
│   └── colors-tokyo-night.sh
├── scripts/
│   ├── change-wallpaper.sh
│   ├── setup-pywalfox.sh
│   └── install-picom-animations.sh
└── wallpapers/
```

---

## 🧪 Probar en VM

```bash
git clone https://github.com/AngheloBR/bspwm-tokio-night-dotfiles
cd bspwm-tokio-night-dotfiles
./install.sh
```

Perfecto para testear en una VM antes de aplicar en PC nueva.

---

**Styx**
