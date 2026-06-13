#!/usr/bin/env bash
# ============================================================
# ranger scope.sh - Preview handler
# ============================================================

set -o noclobber -o noglob -o nounset -o pipefail
IFS=$'\n'

FILE_PATH=""
PREVIEW_WIDTH=1920
PREVIEW_HEIGHT=1080
PREVIEW_OFFSET=0
PREVIEW_LEFT=0

while [ "$#" -gt 0 ]; do
  case "$1" in
    --*) ;;
    *)
      if [ -z "$FILE_PATH" ]; then
        FILE_PATH="$1"
      elif [ "$PREVIEW_WIDTH" -eq 1920 ]; then
        PREVIEW_WIDTH="$1"
      elif [ "$PREVIEW_HEIGHT" -eq 1080 ]; then
        PREVIEW_HEIGHT="$1"
      elif [ "$PREVIEW_OFFSET" -eq 0 ]; then
        PREVIEW_OFFSET="$1"
      else
        PREVIEW_LEFT="$1"
      fi
      ;;
  esac
  shift
done

handle_image() {
    case "${FILE_PATH##*.}" in
      jpg|jpeg|png|gif|ico|svg|webp)
        kitten icat --stdin no --transfer-mode file --place "${PREVIEW_WIDTH}x${PREVIEW_HEIGHT}@${PREVIEW_LEFT}x${PREVIEW_OFFSET}" "$FILE_PATH" < /dev/null > /dev/tty
        exit 1
        ;;
    esac
}

handle_mime() {
  local mimetype="${1}"
  case "${mimetype}" in
    text/*|*/xml|application/json|application/yaml)
      bat --style=numbers --color=always --pager=never "$FILE_PATH" 2>/dev/null || cat "$FILE_PATH"
      exit 1
      ;;
    image/*)
      handle_image
      exit 1
      ;;
    video/*)
      ffmpegthumbnailer -i "$FILE_PATH" -o /tmp/thumb.png -s 0 2>/dev/null || exit 1
      exit 1
      ;;
    audio/*)
      exiftool "$FILE_PATH" 2>/dev/null | head -20
      exit 1
      ;;
    application/pdf)
      pdftotext "$FILE_PATH" - | head -50
      exit 1
      ;;
    application/gzip|application/x-tar|application/zip)
      tar -tzf "$FILE_PATH" 2>/dev/null | head -30 || unzip -l "$FILE_PATH" 2>/dev/null | head -30
      exit 1
      ;;
  esac
}

MIMETYPE="$(file --dereference --brief --mime-type -- "$FILE_PATH" 2>/dev/null)"
handle_mime "${MIMETYPE}"
exit 1
