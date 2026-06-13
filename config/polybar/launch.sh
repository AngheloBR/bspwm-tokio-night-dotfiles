#!/usr/bin/env bash

# ============================================================
# Launch polybar
# ============================================================

killall -q polybar

# Wait until polybar is killed
while pgrep -u "$UID" -x polybar >/dev/null; do sleep 0.5; done

# Launch polybar on all monitors
for m in $(polybar --list-monitors | cut -d":" -f1); do
  MONITOR="$m" polybar --reload main &
done
