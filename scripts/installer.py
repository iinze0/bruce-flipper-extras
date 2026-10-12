#!/usr/bin/env python3
"""
Cross-platform CLI installer for T-Embed / Bruce / Flipper resources.
Usage:
  python3 scripts/installer.py --target /path/to/mounted/sdcard
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

REPOS = [
    "anonimoKali/Bruce-Themes",
    "Ghoststrats/GhostStrats-Bruce-Themes",
    "sloth632/Bruce-Scripts-Heaven",
    "tebin623/Bruce-Scripts-Heaven",
    "3xp-l01t/Bruce-Firmware-File-Pack",
    "Unknown3613/BruceFlipperScripts",
    "djsime1/awesome-flipperzero",
    "SYOP200/Flipper-Zero-Downloads",
    "DefinetlyNotAI/Full_Flipper_Database",
    "bad-antics/nullsec-flipper-suite",
    "Ringmast4r/RF-Protocol-Database",
    "OG34/flipper-signal-db",
    "Zero-Sploit/FlipperZero-Subghz-DB",
    "UberGuidoZ/Flipper",
    "UberGuidoZ/Flipper-SGDB",
    "MuddledBox/FlipperZeroSub-GHz",
    "SHUR1K-N/Flipper-Zero-Sub-GHz-Jamming-Files",
    "Jhoath994/flipper-zero-au-subghz",
    "kakuzu-f0/Automotive-Sub-Ghz-Collection",
    "kakuzu-f0/Automotive-Sub-Ghz-Playlists",
    "meoker/pagger",
    "retalieight/flipper-touchtunes",
    "MakeTotalSense/Flipper-Concert-bracelets",
    "FlipperDevices/IRDB",
    "Lucaslhm/Flipper-IRDB",
    "I-Am-Jakoby/Flipper-Zero-BadUSB",
    "beigeworm/BadUSB-Files-For-FlipperZero",
    "FalsePhilosopher/BadUSB-Playground",
    "MarkCyber/BadUSB",
    "Mr-Proxy-source/BadUSB-Payloads",
    "SeenKid/flipper-zero-bad-usb",
    "bst04/payloads_flipperZero",
    "Kavitate/FlipperZeroBadUSB",
    "neverfa11ing/FlipperAmiibosNFC",
    "w0lfzk1n/Flipper-Zero-NFC-Trolls",
]

DEST_MAP = {
    "themes": "Themes",
    "apps": "BruceJS",
    "sd_packs": "sd-packs",
    "subghz": "Sub-GHz",
    "ir": "Infrared",
    "badusb": "BadUSB",
    "nfc": "NFC",
    "general": "General",
}

EXT_MAP = {
    "themes": {".json", ".png", ".jpg", ".jpeg", ".bmp", ".webp"},
    "apps": {".js", ".json", ".txt", ".md"},
    "sd_packs": {".zip", ".bin", ".img"},
    "subghz": {".sub", ".bin", ".json", ".txt"},
    "ir": {".ir", ".txt"},
    "badusb": {".txt", ".bin", ".duck", ".ps1", ".sh"},
    "nfc": {".nfc", ".bin", ".txt"},
    "general": {".md", ".txt"},
}

DANGEROUS = ["badusb", "ducky", "jamming", "jam", "payload", "exploit", "subghz"]


def run(cmd, cwd=None):
    print("[run]", " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd, check=False)


def clone_repo(repo, dest):
    url = f"https://github.com/{repo}.git"
    if dest.exists():
        print(f"[skip] {repo} already exists at {dest}")
        return True
    res = run(["git", "clone", "--depth", "1", url, str(dest)])
    return res.returncode == 0


def discover_files(root):
    found = {key: [] for key in EXT_MAP}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        ext = path.suffix.lower()
        for category, exts in EXT_MAP.items():
            if ext in exts:
                found[category].append(path)
                break
    return found


def copy_files(files, target_root, subdir):
    target_dir = target_root / subdir
    target_dir.mkdir(parents=True, exist_ok=True)
    for file_path in files:
        target_file = target_dir / file_path.name
        shutil.copy2(file_path, target_file)
        print(f"copy: {file_path} -> {target_file}")


def main():
    parser = argparse.ArgumentParser(description="T-Embed installer for Bruce / Flipper resources")
    parser.add_argument("--target", "-t", required=True, help="Path to mounted SD card / T-Embed filesystem root")
    parser.add_argument("--external", "-e", default="external", help="Clone directory")
    parser.add_argument("--use-existing-only", action="store_true", help="Do not clone; use current external/ repo clones")
    parser.add_argument("--auto-confirm", action="store_true", help="Skip prompts")
    args = parser.parse_args()

    target_root = Path(args.target)
    if not target_root.exists() or not target_root.is_dir():
        print(f"ERROR: target path does not exist or is not a directory: {target_root}")
        sys.exit(1)

    external_dir = Path(args.external)
    external_dir.mkdir(parents=True, exist_ok=True)

    if not args.use_existing_only:
        for repo in REPOS:
            safe_name = repo.replace("/", "-")
            clone_repo(repo, external_dir / safe_name)

    found = {key: [] for key in EXT_MAP}
    for repo_dir in sorted(external_dir.iterdir()):
        if not repo_dir.is_dir():
            continue
        discovered = discover_files(repo_dir)
        for category, files in discovered.items():
            found[category].extend(files)

    for category, files in found.items():
        if not files:
            continue

        print(f"\nCategory: {category} ({len(files)} files found)")
        dangerous = [f for f in files if any(d in str(f).lower() for d in DANGEROUS)]
        if dangerous:
            print("Potentially dangerous examples:")
            for item in dangerous[:5]:
                print("  -", item)

        if not args.auto_confirm:
            confirm = input(f"Copy {len(files)} files for category '{category}' to /{DEST_MAP.get(category, category)}? [y/N] ").strip().lower()
            if confirm != "y":
                print(f"[skip] category {category}")
                continue

            if dangerous:
                proceed_dangerous = input("Proceed with potentially dangerous files? [y/N] ").strip().lower()
                if proceed_dangerous != "y":
                    files = [f for f in files if f not in dangerous]
                    if not files:
                        print(f"[skip] no safe files left for category {category}")
                        continue

        dest_subdir = DEST_MAP.get(category, category)
        copy_files(files, target_root, dest_subdir)

    print("\nDone. Please eject the SD card safely.")


if __name__ == "__main__":
    main()
