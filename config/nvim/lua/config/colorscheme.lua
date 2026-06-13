-- ============================================================
-- Neovim colorscheme - Tokyo Night (LazyVim)
-- ============================================================
-- Para usar con LazyVim:
-- 1. Asegúrate de tener instalado el plugin:
--    { "folke/tokyonight.nvim", lazy = false, priority = 1000 }
--
-- 2. Este archivo va en: ~/.config/nvim/lua/config/colorscheme.lua
--
-- 3. LazyVim lo carga automáticamente desde esa ruta.

vim.cmd.colorscheme("tokyonight")

-- Opcional: personalizar colores Tokyo Night
local tokyonight = require("tokyonight")

tokyonight.setup({
  style = "night",           -- "storm", "night", "day"
  transparent = true,        -- Fondo transparente (con picom)
  terminal_colors = true,
  styles = {
    comments = { italic = true },
    keywords = { italic = true },
    functions = {},
    variables = {},
    sidebars = "transparent",
    floats = "transparent",
  },
  day_brightness = 0.3,
  dim_inactive = false,
  lualine_bold = true,
})
