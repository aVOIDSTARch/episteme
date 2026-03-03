#!/usr/bin/env bash
# List idea topic files in IDEAS_ROOT or ~/ideas/.
# Usage: ./list-topics.sh [ideas_root]
set -e
IDEAS_ROOT="${1:-${IDEAS_ROOT:-$HOME/ideas}}"
if [[ ! -d "$IDEAS_ROOT" ]]; then
  echo "Ideas root not found: $IDEAS_ROOT" >&2
  exit 1
fi
for f in "$IDEAS_ROOT"/*.md; do
  [[ -e "$f" ]] || continue
  name=$(basename "$f" .md)
  # Optional: first # heading as display name
  if head -1 "$f" | grep -q '^# '; then
    title=$(head -1 "$f" | sed 's/^# *//')
    echo "$name|$title"
  else
    echo "$name|$name"
  fi
done
