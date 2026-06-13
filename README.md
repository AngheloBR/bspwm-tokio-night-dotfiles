# Tokyo Night Dotfiles

```
   ████████╗ ██████╗ ██╗  ██╗██╗   ██╗ ██████╗
   ╚══██╔══╝██╔═══██╗██║ ██╔╝╚██╗ ██╔╝██╔═══██╗
      ██║   ██║   ██║█████╔╝  ╚████╔╝ ██║   ██║
      ██║   ██║   ██║██╔═██╗   ╚██╔╝  ██║   ██║
      ██║   ╚██████╔╝██║  ██╗   ██║   ╚██████╔╝
      ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝
```

Configuración completa de **bspwm** con tema **Tokyo Night**, animaciones suaves y colores dinámicos tipo **Material You** (pywal).

**Styx**

---

## ⚡ Requisitos

- **SO:** Arch Linux / CachyOS (basado en Arch)
- **WM:** bspwm + sxhkd
- **Terminal:** Ghostty (opcional, usa Alacritty si prefieres)
- **AUR helper:** `yay` o `paru` (recomendado)

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/AngheloBR/bspwm-tokio-night-dotfiles
cd bspwm-tokio-night-dotfiles
```

### 2. Ejecutar instalador

```bash
chmod +x install.sh
./install.sh
```

El instalador:
- Muestra el banner de **Styx**
- Detecta e instala dependencias faltantes (bspwm, polybar, picom, dunst, rofi, etc.)
- Te pregunta si quieres instalar `picom-ibhagwan-git` (animaciones extra) y `pywal`
- Hace respaldo automático de tus configuraciones actuales en `~/.config/backup-dotfiles-*`
- Copia todas las configuraciones a `~/.config/`
- Instala scripts en `~/.local/bin/`
- Te muestra los atajos de teclado al finalizar

### 3. Recargar bspwm

```bash
Super + Escape
```

O cierra sesión y vuelve a entrar.

---

## 🧪 Probar en VM

Perfecto para testear antes de aplicar en una PC nueva:

```bash
# En la VM, instalar bspwm y dependencias
sudo pacman -S bspwm sxhkd polybar picom dunst rofi feh

# Clonar y ejecutar
git clone https://github.com/AngheloBR/bspwm-tokio-night-dotfiles
cd bspwm-tokio-night-dotfiles
./install.sh
```

---

## 🖥️ Vista previa de componentes

| Componente | Archivo | Descripción |
|---|---|---|
| **bspwm** | `config/bspwm/bspwmrc` | Bordes Tokyo Night, gaps 8px, esquinas redondeadas |
| **sxhkd** | `config/sxhkd/sxhkdrc` | Atajos vim (hjkl), multimedia, rofi, power menu |
| **polybar** | `config/polybar/config.ini` | Barra con workspaces, fecha, audio, red, batería, power |
| **picom** | `config/picom/picom.conf` | Sombra, blur dual_kawase, fade, corner-radius 12px |
| **dunst** | `config/dunst/dunstrc` | Notificaciones con esquinas redondeadas 12px |
| **rofi** | `config/rofi/config.rasi` | Lanzador con tema Tokyo Night, esquinas 12px |
| **ghostty** | `config/ghostty/config` | Terminal con paleta Tokyo Night, opacidad 0.92 |
| **GTK** | `config/gtk-3.0/settings.ini` | Tema Tokyonight-Dark-BL + Papirus-Dark |

---

## 🎨 Colores Tokyo Night

| Color | Hex | Uso |
|---|---|---|
| Fondo | `#1a1b26` | bg principal |
| Superficie | `#24283b` | paneles, barras |
| Azul | `#7aa2f7` | acento principal, borde activo |
| Púrpura | `#bb9af7` | acento secundario, presel |
| Verde | `#9ece6a` | volumen, batería llena |
| Rojo | `#f7768e` | urgente, errores |
| Amarillo | `#e0af68` | batería cargando |
| Cian | `#7dcfff` | red, fecha |
| Texto | `#c0caf5` | fg principal |
| Inactivo | `#3b4261` | bordes inactivos |

---

## 🎯 Atajos de teclado

| Atajo | Acción |
|---|---|
| `Super + Enter` | Ghostty (terminal) |
| `Super + D` | Rofi (lanzador de apps) |
| `Super + Shift + D` | Rofi (run) |
| `Super + W` | Rofi (ventanas) |
| `Super + Shift + W` | Firefox |
| `Super + Escape` | Lock screen (betterlockscreen) |

## Navegación de ventanas

| Atajo | Acción |
|---|---|
| `Super + h/j/k/l` | Navegar ventanas (izq/abajo/arriba/der) |
| `Super + Shift + h/j/k/l` | Mover ventana |
| `Super + Ctrl + h/j/k/l` | Preseleccionar dirección |
| `Super + Ctrl + Shift + h/j/k/l` | Cancelar preselección |

## Escritorios

| Atajo | Acción |
|---|---|
| `Super + 1-0` | Ir al escritorio N |
| `Super + Shift + 1-0` | Mover ventana al escritorio N |
| `Super + Tab` | Último escritorio |

## Ventanas

| Atajo | Acción |
|---|---|
| `Super + Q` | Cerrar ventana |
| `Super + M` | Fullscreen |
| `Super + F` | Floating |
| `Super + T` | Tiled |
| `Super + Space` | Alternar floating |

## Multimedia

| Atajo | Acción |
|---|---|
| `XF86AudioRaiseVolume` | Subir volumen 5% |
| `XF86AudioLowerVolume` | Bajar volumen 5% |
| `XF86AudioMute` | Silenciar |
| `Print` | Flameshot GUI |
| `Shift + Print` | Flameshot full |
| `Super + Ctrl + W` | Wallpaper aleatorio (pywal) |

---

## 🖼️ Wallpaper dinámico (Material You)

```bash
# Wallpaper aleatorio
change-wallpaper -r ~/Pictures/Wallpapers

# Siguiente wallpaper
change-wallpaper -n

# Wallpaper específico
change-wallpaper ~/Pictures/Wallpapers/mi-wallpaper.jpg
```

El script `change-wallpaper`:
1. Toma el wallpaper
2. Genera paleta de colores con `pywal` (Material You)
3. Actualiza el fondo con `feh`
4. Actualiza Firefox colors si usas `pywalfox`

Los colores se regeneran automáticamente desde `~/.cache/wal/colors`.

---

## ⚙️ Animaciones extra

El `picom.conf` incluye sombras, blur y fade por defecto.

Para animaciones más avanzadas (zoom al abrir/cerrar ventanas):

```bash
# Instalar fork de picom con animaciones
./scripts/install-picom-animations.sh

# Descomentar en ~/.config/picom/picom.conf:
#   animations = true
#   animation-for-open-window = "zoom"
#   animation-for-close-window = "zoom"
```

---

## 📁 Estructura del proyecto

```
bspwm-tokio-night-dotfiles/
├── install.sh                    # Instalador con banner Styx
├── config/
│   ├── bspwm/bspwmrc             # Configuración de bspwm
│   ├── sxhkd/sxhkdrc             # Atajos de teclado
│   ├── polybar/
│   │   ├── config.ini            # Barra de estado
│   │   └── launch.sh             # Script de inicio
│   ├── picom/picom.conf          # Compositor + animaciones
│   ├── dunst/dunstrc             # Notificaciones
│   ├── rofi/config.rasi          # App launcher
│   ├── ghostty/config            # Terminal
│   └── gtk-3.0/settings.ini      # Tema GTK
├── themes/
│   └── colors-tokyo-night.sh     # Paleta de colores
├── scripts/
│   ├── change-wallpaper.sh       # Wallpaper + pywal
│   └── install-picom-animations.sh
└── README.md
```

---

## 🔧 Personalización

1. **Colores:** Edita `~/.config/themes/colors-tokyo-night.sh`
2. **Atajos:** Edita `~/.config/sxhkd/sxhkdrc`
3. **Barra:** Edita `~/.config/polybar/config.ini`
4. **Animaciones:** Edita `~/.config/picom/picom.conf`
5. **Wallpapers:** Pon imágenes en `~/Pictures/Wallpapers/`

---

**Styx**
