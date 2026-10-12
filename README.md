# bruce-flipper-extras

This repo is a curated, category-sorted collection of Bruce / Flipper-style extras and local installer tooling for a T-Embed device.

It is organized so you can:
- keep a single master catalog of upstream repos
- sort everything by type
- fetch the upstream sources into `external/`
- run a local installer or browser-based web flasher to copy files onto a connected T-Embed / SD card

## What is in here?

- `themes/` — theme pack references and notes
- `apps/` — JS apps and script pack references
- `sd-packs/` — SD card and firmware asset packs
- `subghz/` — regional Sub-GHz collections
- `infrared/` — IRDB and remote packs
- `badusb/` — payload repositories and ducky tools
- `nfc/` — NFC / RFID collections
- `general/` — master indexes and mixed resource packs
- `scripts/installer.py` — cross-platform CLI installer for copying files to the target device
- `webflasher/app.py` — local browser-based installer / flasher
- `docs/source-catalog.md` — sorted repo catalog by category

## Quick start

Install Python deps:

```bash
python3 -m pip install -r requirements.txt
```

Fetch upstream repos (optional):

```bash
chmod +x scripts/fetch_sources.sh
./scripts/fetch_sources.sh
```

Run the CLI installer:

```bash
python3 scripts/installer.py --target /path/to/mounted/sdcard
```

Run the local web flasher:

```bash
python3 webflasher/app.py
```

Then browse to:

```text
http://127.0.0.1:5000
```

## Important safety notes

- Review all files before using them on hardware.
- Only transmit on legal frequencies for your region.
- BadUSB / payload repos require extra caution and should be reviewed carefully before use.
- This repo is intended as a curated index and local installer system. It does not silently mirror every upstream archive into Git history.

## Main repository layout

```text
.
├── README.md
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
│   │   └── main.js
│   └── templates/
│       └── index.html
└── LICENSE
```

## License and redistribution

Many upstream repos have different licensing terms. Before copying or redistributing any third-party files, inspect the source repository’s license and comply with it.

This project is intended for local management and installation of curated community content, not as a blanket redistribution of every upstream payload dump.
