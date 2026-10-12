# Bruce / Flipper Extras Installation Guide

This guide shows how to install and run the project on macOS, Windows, and Linux.

## Prerequisites

Before starting, make sure you have:

- Python 3.8+
- Git
- A mounted SD card or T-Embed storage device
- A terminal or PowerShell window

For radio-related files, use only on frequencies allowed in your region.

## 1) Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/iinze0/bruce-flipper-extras.git
cd bruce-flipper-extras
```

## 2) Create a virtual environment (recommended)

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Windows (Git Bash)

```bash
python -m venv .venv
source .venv/Scripts/activate
```

## 3) Install dependencies

From the repo root:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

This installs:
- Flask
- psutil

## 4) Fetch upstream repos into external/

This pulls the curated upstream source repos into the local `external/` folder, which is ignored by git.

### macOS / Linux

```bash
chmod +x scripts/fetch_sources.sh
./scripts/fetch_sources.sh
```

### Windows

Use Git Bash or WSL if possible.

```bash
bash scripts/fetch_sources.sh
```

If Git Bash is not available, open the repo in a terminal that has Git on PATH and run the script from the repo root.

## 5) Run the local web flasher (recommended)

```bash
python3 webflasher/app.py
```

Then open in your browser:

```text
http://127.0.0.1:5000
```

### In the web UI

- Select the category you want to copy
- Choose the target mount path for your SD card / T-Embed storage
- Click “Flash selected”
- Confirm before copying anything sensitive

### Common target paths

- macOS: `/Volumes/<CARD_NAME>`
- Linux: `/media/<user>/<CARD_NAME>` or `/mnt/<CARD_NAME>`
- Windows: `E:\` or `F:\`

If the drive is not auto-detected, type the path manually.

## 6) Run the CLI installer directly

If you want a command-line installation instead of the browser UI:

```bash
python3 scripts/installer.py --target /path/to/mounted/sdcard
```

Examples:

### macOS

```bash
python3 scripts/installer.py --target /Volumes/T-EMBED
```

### Linux

```bash
python3 scripts/installer.py --target /media/youruser/T-EMBED
```

### Windows

```powershell
python scripts/installer.py --target E:\
```

### Existing clones only (skip re-cloning)

```bash
python3 scripts/installer.py --target /path/to/mounted/sdcard --use-existing-only
```

### Skip prompts (advanced / risky)

```bash
python3 scripts/installer.py --target /path/to/mounted/sdcard --auto-confirm
```

## 7) Eject the SD card safely

### macOS

Use Finder to eject the device, or:

```bash
diskutil eject /Volumes/<CARD_NAME>
```

### Linux

```bash
sudo umount /media/<user>/<CARD_NAME>
```

### Windows

Use “Safely Remove Hardware” or eject the drive in File Explorer.

## Troubleshooting

### Command not found: python3

- Install Python 3.8+ and make sure it is on PATH.
- On Windows, use `python` instead of `python3`.

### Git not found

Install Git and restart your terminal.

### No removable drive detected by the web UI

Manually enter the mount path instead of relying on auto-detection.

### Copy fails with permission errors

- Make sure the SD card is writable.
- Check that the drive is not mounted read-only.
- On Windows, run the terminal with elevated permissions if needed.

### No files listed in the web app

Run the fetch script first:

```bash
./scripts/fetch_sources.sh
```

or run the installer with cloning enabled.

## Important safety notes

- Review files before copying them to hardware.
- Only transmit on legally permitted frequencies in your region.
- BadUSB, jamming, and payload repos require extra caution and should be reviewed carefully before use.
- Do not copy or distribute third-party content that has unclear or restrictive licensing.

## Repository layout

```text
.
├── README.md
├── INSTALL.md
├── .gitignore
├── requirements.txt
├── docs/
│   └── source-catalog.md
├── themes/
├── apps/
├── sd-packs/
├── subghz/
│   ├── eu/
│   ├── us/
│   ├── au/
│   └── general/
├── infrared/
├── badusb/
├── nfc/
├── general/
├── external/
├── scripts/
│   ├── fetch_sources.sh
│   └── installer.py
├── webflasher/
│   ├── app.py
│   ├── static/
│   └── templates/
└── LICENSE
```

## Quick start summary

```bash
git clone https://github.com/iinze0/bruce-flipper-extras.git
cd bruce-flipper-extras
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
./scripts/fetch_sources.sh
python3 webflasher/app.py
```

Then open:

```text
http://127.0.0.1:5000
```

and select the target mount to install your extras.
