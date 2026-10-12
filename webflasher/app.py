#!/usr/bin/env python3
"""
Local web flasher for Bruce / Flipper resources.
Run:
  python3 webflasher/app.py
Open: http://127.0.0.1:5000
"""

from flask import Flask, render_template, request, jsonify
from pathlib import Path
import os
import psutil
import shutil

app = Flask(__name__, template_folder="templates", static_folder="static")
EXTERNAL = Path("external")
EXT_MAP = {
    "themes": [".json", ".png", ".jpg", ".jpeg", ".bmp", ".webp"],
    "apps": [".js", ".json", ".txt", ".md"],
    "sd_packs": [".zip", ".bin", ".img"],
    "subghz": [".sub", ".bin", ".json", ".txt"],
    "ir": [".ir", ".txt"],
    "badusb": [".txt", ".bin", ".duck", ".ps1", ".sh"],
    "nfc": [".nfc", ".bin", ".txt"],
    "general": [".md", ".txt"],
}


def scan_external():
    results = {category: [] for category in EXT_MAP}
    if not EXTERNAL.exists():
        return results

    for repo_dir in sorted(EXTERNAL.iterdir()):
        if not repo_dir.is_dir():
            continue
        for file_path in sorted(repo_dir.rglob("*")):
            if not file_path.is_file():
                continue
            ext = file_path.suffix.lower()
            for category, exts in EXT_MAP.items():
                if ext in exts:
                    results[category].append({
                        "path": str(file_path),
                        "repo": repo_dir.name,
                        "name": file_path.name,
                    })
                    break
    return results


def removable_drives():
    out = []
    for part in psutil.disk_partitions(all=False):
        mount = part.mountpoint
        if "/media" in mount or "/Volumes" in mount or (os.name == "nt" and ":" in mount):
            out.append(mount)
    return out


@app.route("/")
def index():
    files = scan_external()
    drives = removable_drives()
    return render_template("index.html", files=files, drives=drives)


@app.route("/api/scan")
def api_scan():
    return jsonify(scan_external())


@app.route("/api/flash", methods=["POST"])
def api_flash():
    data = request.get_json(silent=True) or {}
    target = data.get("target", "")
    selected = data.get("selection", [])

    if not target or not selected:
        return jsonify({"ok": False, "error": "target and selection are required"}), 400

    target_root = Path(target)
    if not target_root.exists() or not target_root.is_dir():
        return jsonify({"ok": False, "error": "Target is not a valid directory"}), 400

    copied = []
    for src in selected:
        src_path = Path(src)
        if not src_path.exists() or not src_path.is_file():
            continue
        dest = target_root / src_path.name
        shutil.copy2(src_path, dest)
        copied.append(str(dest))

    return jsonify({"ok": True, "copied": copied})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
