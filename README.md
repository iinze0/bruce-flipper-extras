# bruce-flipper-extras

A single repo for Bruce / Flipper-style resources, sorted by category and ready to fetch locally.

This repository is organized as a source catalog and downloader utility rather than a direct mirror of third-party payload archives. The goal is to centralize the important repositories in one place, keep the main repo lightweight, and let you pull the actual files into `external/` only when needed.

## Categories

- Bruce themes
- Bruce JS apps and scripts
- SD card / firmware asset packs
- Sub-GHz regional collections
- IR packs
- BadUSB payload libraries
- NFC / RFID collections
- General Flipper / Flipper-style collections

## Folder structure

- `external/` — fetched repos live here locally; this directory is ignored by git
- `docs/source-catalog.md` — sorted source catalog
- `scripts/fetch_sources.sh` — downloads the upstream repos into `external/`
- `README.md` — overview and quick-start

## Quick start

```bash
chmod +x scripts/fetch_sources.sh
./scripts/fetch_sources.sh
```

This will clone the curated upstream repos into `external/` under the repo root.

## Registry of sources

See the full catalog here:

- `docs/source-catalog.md`

## Notes

- Always review files before using them on hardware.
- Use only on frequencies legal in your region.
- This repo is intended to organize, index, and fetch upstream sources. It does not silently mirror or redistribute every upstream archive.
