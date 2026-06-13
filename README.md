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
| **Firefox** | `config/firefox/userChrome.css` | macOS style + Tokyo Night |
| **LightDM** | `config/lightdm/` | Pantalla de login macOS Tokyo Night |
| **cava** | `config/cava/config` | Visualizador de audio Tokyo Night |
| **ranger** | `config/ranger/` | File manager terminal con Tokyo Night |
| **wallpapers** | `scripts/download-wallpapers.sh` | Descarga wallpapers oficiales Tokyo Night |
| **auto-wallpaper** | `scripts/auto-wallpaper.sh` | Cambio automático de wallpaper cada N min |
| **Thunar** | `config/Thunar/uca.xml` + `config/gtk-3.0/gtk.css` | File manager GUI con Tokyo Night |
| **lazygit** | `config/lazygit/config.yml` | TUI para git con Tokyo Night |
| **cmus** | `config/cmus/rc` | Reproductor música terminal Tokyo Night |
| **mpv** | `config/mpv/mpv.conf` | Reproductor video con OSD Tokyo Night |
| **yazi** | `config/yazi/{theme.toml, yazi.toml}` | File manager Rust (rápido) Tokyo Night |
| **zathura** | `config/zathura/zathurarc` | Visor PDF minimal Tokyo Night |
| **imv** | `config/imv/config` | Visor imágenes Tokyo Night |
| **cliphist** | `config/cliphist/config.toml` | Clipboard manager + sxhkd binding |
| **wifi** | `scripts/wifi-conectar.sh` + `config/zsh/aliases.zsh` | Selector WiFi con rofi + Tokyo Night |
| **aliases** | `config/zsh/aliases.zsh` | Aliases ZSH mejorados y organizados |

---

## 📦 Stack completo (Full Stack)

```
┌─────────────────────────────────────────────────────┐
│                    TOKYO NIGHT                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  🪟 WINDOW MANAGER                                   │
│  ├── bspwm       → Window manager                    │
│  ├── sxhkd       → Key bindings                      │
│  ├── polybar     → Status bar                        │
│  ├── picom       → Compositor + animaciones          │
│  ├── lightdm     → Display manager (login macOS)     │
│  └── betterlockscreen → Lock screen                  │
│                                                      │
│  📱 APPLICATIONS                                     │
│  ├── ghostty     → Terminal                           │
│  ├── rofi        → App launcher                       │
│  ├── firefox     → Browser (macOS style)              │
│  ├── thunar      → File manager GUI (GTK)             │
│  ├── ranger      → File manager TUI (Python)           │
│  ├── yazi        → File manager TUI (Rust, rápido)     │
│  ├── nvim        → Editor (LazyVim + Tokyo Night)     │
│  ├── cava        → Audio visualizer                   │
│  ├── fastfetch   → System info                        │
│  ├── btop        → System monitor                     │
│  ├── flameshot   → Screenshots                        │
│  ├── dunst       → Notifications                      │
│  ├── lazygit     → TUI git                             │
│  ├── cmus        → Música terminal                     │
│  ├── mpv         → Video player                        │
│  ├── zathura     → Visor PDF                           │
│  └── imv         → Visor imágenes                      │
│                                                      │
│  🎨 THEMING                                          │
│  ├── pywal       → Dynamic colors (Material You)      │
│  ├── pywalfox    → Firefox colors                     │
│  ├── Tokyo Night → GTK theme                          │
│  ├── Kvantum     → Qt theme                           │
│  ├── Papirus-Dark → Icon theme                        │
│  └── JetBrainsMono Nerd Font → Monospace font         │
│                                                      │
│  🐚 SHELL & TOOLS                                     │
│  ├── zsh         → Shell                              │
│  ├── oh-my-zsh   → ZSH framework                      │
│  ├── powerlevel10k → Prompt                           │
│  ├── bat         → Cat with syntax highlight          │
│  ├── playerctl   → Media controls                     │
│  ├── brightnessctl → Brightness                       │
│  ├── pipewire    → Audio                              │
│  ├── feh         → Wallpaper setter                    │
│  └── wget        → Downloads                          │
│                                                      │
│  📜 SCRIPTS                                          │
│  ├── change-wallpaper.sh   → Wallpaper + pywal        │
│  ├── auto-wallpaper.sh     → Auto change N min        │
│  ├── download-wallpapers.sh → Get official wallpapers │
│  ├── setup-pywalfox.sh     → Firefox + pywal          │
│  └── install-picom-animations.sh → Extra animations   │
│                                                      │
└─────────────────────────────────────────────────────┘
```

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

---

## 🌐 Firefox macOS Tokyo Night

Estilo macOS unificado con colores Tokyo Night. Incluye:

- Pestañas compactas estilo macOS con borde redondeado
- Pestaña activa con glow azul (`#7aa2f7`)
- Botones de tráfico macOS (rojo, amarillo, verde)
- Barra de URL con borde sutil y focus glow
- Scrollbar delgado con colores Tokyo Night
- Menús y popups redondeados

### Activar:

```bash
# 1. about:config → toolkit.legacyUserProfileCustomizations.stylesheets = true
# 2. Copiar userChrome.css al perfil:
cp config/firefox/userChrome.css ~/.mozilla/firefox/*.default-release/chrome/
cp config/firefox/userChrome-tokyo-night.css ~/.mozilla/firefox/*.default-release/chrome/
cp config/firefox/user.js ~/.mozilla/firefox/*.default-release/
```

---

## 📂 Thunar (file manager gráfico)

Thunar usa el tema GTK `Tokyonight-Dark-BL` automáticamente. Además incluimos:

- **`config/Thunar/uca.xml`** → Acciones personalizadas:
  - Abrir terminal aquí (Ghostty)
  - Cambiar wallpaper con pywal
  - Copiar ruta al portapapeles
  - Extraer comprimidos
- **`config/gtk-3.0/gtk.css`** → Tweaks específicos para Thunar (sidebar, path bar, statusbar, selecciones)

No requiere activación extra — solo tener `Tokyonight-Dark-BL` en GTK.

---

## ⎇ lazygit (TUI para git)

Interfaz terminal para git. En vez de comandos, ves archivos modificados y operás con teclas.

```bash
lazygit
```

Atajos:
- `<espacio>` → stage/unstage archivos
- `c` → commit
- `P` → push
- `p` → pull
- `?` → ayuda

---

## 🎧 cmus (reproductor música terminal)

Para escuchar música directamente en la terminal con colores Tokyo Night.

```bash
cmus
```

Atajos:
- `5` → lista de reproducción
- `2` → navegar directorios
- `x` → play
- `v` → pausa/reanudar
- `b` → siguiente
- `z` → anterior
- `q` → salir

---

## 🎬 mpv (reproductor video)

Reproductor de video con OSD y subtítulos en colores Tokyo Night.

```bash
mpv video.mp4
```

Config incluida: OSD azul `#7aa2f7`, subtítulos con borde sutil, JetBrainsMono Nerd Font, preajuste GPU.

---

## 📂 yazi (file manager en Rust)

Alternativa a ranger pero en Rust — más rápido, preview nativo de imágenes, videos, PDFs, audios.

```bash
yazi
```

Atajos:
- `hjkl` → navegar
- `~` → mostrar/ocultar ocultos
- `o` → abrir archivo
- `e` → editar con nvim
- `y` → copiar ruta
- `q` → salir

---

## 📄 zathura (visor PDF minimal)

Visor PDF con tema oscuro Tokyo Night y JetBrainsMono.

```bash
zathura documento.pdf
```

Atajos:
- `j/k` → scroll
- `f` → pantalla completa
- `i` → recolor (toggle modo invertido)
- `r` → recargar

---

## 🖼️ imv (visor de imágenes minimal)

Alternativa ultra rápida a feh/sxiv para ver imágenes.

```bash
imv imagen.png
imv *.jpg        # slideshow
```

Atajos:
- `Left/Right` → anterior/siguiente
- `f` → pantalla completa
- `<espacio>` → toggle GIF animado
- `Ctrl+C` → copiar ruta al clipboard

---

## 📋 cliphist (clipboard manager)

Historial del portapapeles con interfaz rofi.

| Tecla | Acción |
|---|---|
| `Super + V` | Abrir historial del clipboard |
| `Super + Shift + V` | Limpiar historial |

Requiere `wl-clipboard` (Wayland). Soporta texto, imágenes y archivos.

---

## 🌐 nm-applet + blueman

Autostart en bspwmrc:
- **nm-applet** → icono de red en la bandeja
- **blueman-applet** → icono de bluetooth en la bandeja

Se inician automáticamente al iniciar bspwm.

---

## 🛜 WiFi interactivo con rofi

Selector de redes WiFi con interfaz gráfica rofi y colores Tokyo Night.

```bash
# Modo interactivo (seleccionás red con rofi)
wifi-conectar

# Modo directo
wifi-conectar "MiRed" "MiClave"

# Listar redes
wifi-conectar -l
```

También incluido como alias/función `wifi()` en `config/zsh/aliases.zsh`.

---

## 🔧 Aliases ZSH

Todos los alias mejorados y organizados en `config/zsh/aliases.zsh`:

| Categoría | Alias/Función | Qué hace |
|---|---|---|
| 🌐 Redes | `redes` | Listar WiFi con nmcli |
| | `wifi-conectar` | Conectar WiFi (directo) |
| | `wifi` | Selector WiFi con rofi |
| 📦 Sistema | `cat` | bat (syntax highlight) |
| | `update-programs` | Guarda lista de paquetes |
| 🔌 Servidores | `vps` | SSH a VPS Oracle |
| | `server-minecraft` | SSH server Minecraft |
| ⚡ Energía | `modo-ahorro/normal/juego` | Perfiles de energía |
| 🖥️ KVM | `kvm-on/off`, `maquinas-virtuales` | Virtualización |
| | `snapshot` | Gestión de snapshots |
| ⏰ Utilidades | `awake`, `gemini`, `opencode`, `jarvis` | Varias |

---

## 💡 Notas extra

- **Obsidian**: Tema Tokyo Night disponible en Ajustes → Apariencia → Temas comunitarios
- **Echo Music**: Reproductor Flutter/Dart. Si tiene tema personalizable, se puede adaptar con los colores de `themes/colors-tokyo-night.sh`

---

## 🔐 LightDM macOS Tokyo Night

Pantalla de login estilo macOS con:

- Fondo borroso (blur)
- Panel centrado con glassmorphism
- Reloj grande con formato HH:MM
- Avatar circular con glow
- Input de contraseña minimalista
- Selector de sesión

### Activar (lightdm-gtk-greeter):

```bash
sudo cp config/lightdm/lightdm-gtk-greeter.conf /etc/lightdm/
```

### Activar (lightdm-webkit2-greeter):

```bash
sudo mkdir -p /usr/share/lightdm-webkit/themes/tokyo-night-macos
sudo cp -r config/lightdm/webkit-theme/* /usr/share/lightdm-webkit/themes/tokyo-night-macos/
sudo nano /etc/lightdm/lightdm-webkit2-greeter.conf
# → webkit-theme = tokyo-night-macos
```

---

## 🎵 cava (visualizador de audio)

```bash
cava
```

Muestra barras con gradiente Tokyo Night: rojo → naranja → amarillo → verde → cian → azul → púrpura.

---

## 📂 ranger (file manager de terminal)

**¿Qué es?** Similar a Thunar pero en terminal. Navegas con teclas (hjkl), tiene preview de imágenes, videos, PDFs, etc.

```bash
ranger
```

Atajos:
- `hjkl` → navegar
- `i` → preview de archivo
- `qh` → mostrar/ocultar archivos ocultos
- `S` → abrir shell en el directorio actual

---

## 🖼️ Wallpapers Tokyo Night

```bash
# Descargar wallpapers oficiales
download-wallpapers ~/Pictures/Wallpapers

# Usar uno como fondo
change-wallpaper -r ~/Pictures/Wallpapers
```

---

## 🔄 Auto-wallpaper

Cambia el wallpaper automáticamente cada N minutos:

```bash
# Cada 15 minutos
auto-wallpaper ~/Pictures/Wallpapers 15

# Cada 30 minutos (default)
auto-wallpaper ~/Pictures/Wallpapers

# Detener
pkill -f auto-wallpaper
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
│   ├── gtk-3.0/{settings.ini, gtk.css}
│   ├── fastfetch/config.jsonc
│   ├── betterlockscreen/betterlockscreenrc
│   ├── btop/{btop.conf, themes/tokyo-night.theme}
│   ├── kvantum/kvantum.kvconfig
│   ├── nvim/lua/config/colorscheme.lua
│   ├── zsh/{p10k-tokyo-night.zsh, aliases.zsh}
│   ├── firefox/{userChrome.css, userChrome-tokyo-night.css, user.js}
│   ├── lightdm/{lightdm-gtk-greeter.conf, lightdm-webkit2-greeter.conf, webkit-theme/}
│   ├── cava/config
│   ├── ranger/{rc.conf, scope.sh, colorschemes/tokyo-night.py}
│   ├── Thunar/uca.xml
│   ├── lazygit/config.yml
│   ├── cmus/rc
│   ├── mpv/mpv.conf
│   ├── yazi/{theme.toml, yazi.toml}
│   ├── zathura/zathurarc
│   ├── imv/config
│   └── cliphist/config.toml
├── themes/
│   └── colors-tokyo-night.sh
├── scripts/
│   ├── change-wallpaper.sh
│   ├── setup-pywalfox.sh
│   ├── install-picom-animations.sh
│   ├── auto-wallpaper.sh
│   ├── download-wallpapers.sh
│   ├── generate-wallpapers.py
│   └── wifi-conectar.sh
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
