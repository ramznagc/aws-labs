#!/usr/bin/env bash
set -euo pipefail

VERSION="${1:-}"

if [[ ! "$VERSION" =~ ^php-v[1-4]$ ]]; then
  echo "Usage: $0 php-v1|php-v2|php-v3|php-v4"
  exit 2
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$ROOT/application-versions/$VERSION"
DIST="$ROOT/dist"

mkdir -p "$DIST"
OUTPUT="$DIST/mysampleapp-source-${VERSION#php-v}.zip"

rm -f "$OUTPUT"

(
  cd "$SOURCE"
  zip -qr "$OUTPUT" .
)

echo "Created: $OUTPUT"
