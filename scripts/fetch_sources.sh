#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EXTERNAL_DIR="$ROOT_DIR/external"
mkdir -p "$EXTERNAL_DIR"
cd "$EXTERNAL_DIR"

repos=(
  "anonimoKali/Bruce-Themes"
  "Ghoststrats/GhostStrats-Bruce-Themes"
  "sloth632/Bruce-Scripts-Heaven"
  "tebin623/Bruce-Scripts-Heaven"
  "3xp-l01t/Bruce-Firmware-File-Pack"
  "Unknown3613/BruceFlipperScripts"
  "djsime1/awesome-flipperzero"
  "SYOP200/Flipper-Zero-Downloads"
  "DefinetlyNotAI/Full_Flipper_Database"
  "bad-antics/nullsec-flipper-suite"
  "Ringmast4r/RF-Protocol-Database"
  "OG34/flipper-signal-db"
  "Zero-Sploit/FlipperZero-Subghz-DB"
  "UberGuidoZ/Flipper"
  "UberGuidoZ/Flipper-SGDB"
  "MuddledBox/FlipperZeroSub-GHz"
  "SHUR1K-N/Flipper-Zero-Sub-GHz-Jamming-Files"
  "Jhoath994/flipper-zero-au-subghz"
  "kakuzu-f0/Automotive-Sub-Ghz-Collection"
  "kakuzu-f0/Automotive-Sub-Ghz-Playlists"
  "meoker/pagger"
  "retalieight/flipper-touchtunes"
  "MakeTotalSense/Flipper-Concert-bracelets"
  "FlipperDevices/IRDB"
  "Lucaslhm/Flipper-IRDB"
  "I-Am-Jakoby/Flipper-Zero-BadUSB"
  "beigeworm/BadUSB-Files-For-FlipperZero"
  "FalsePhilosopher/BadUSB-Playground"
  "MarkCyber/BadUSB"
  "Mr-Proxy-source/BadUSB-Payloads"
  "SeenKid/flipper-zero-bad-usb"
  "bst04/payloads_flipperZero"
  "Kavitate/FlipperZeroBadUSB"
  "neverfa11ing/FlipperAmiibosNFC"
  "w0lfzk1n/Flipper-Zero-NFC-Trolls"
)

for repo in "${repos[@]}"; do
  dir="${repo//\//-}"
  if [[ -d "$dir/.git" ]]; then
    echo "[skip] $repo already present at $EXTERNAL_DIR/$dir"
    continue
  fi

  echo "[fetch] cloning $repo"
  git clone --depth 1 "https://github.com/$repo.git" "$dir" || {
    echo "[warn] failed to clone $repo" >&2
  }
done

echo "Done. Upstream repos are stored under $EXTERNAL_DIR"
