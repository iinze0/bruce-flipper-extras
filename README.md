# bruce-flipper-extras

This repository is a safe, centralized index and downloader for Bruce / Flipper-style resources. It is intentionally designed to keep one place for links, categories, and local acquisition scripts without committing third-party payload archives directly into Git history.

What this repo includes:
- Bruce themes and UI packs
- JavaScript app packs and community scripts
- SD card / firmware asset packs
- Sub-GHz regional references and large public databases
- IR, BadUSB, and NFC resource indexes
- A simple fetch script that clones selected public repositories into `external/`

Important safety and legal note:
- Review all files before using them on hardware.
- Transmit only on legally permitted frequencies in your region.
- This repo does not include or mirror every payload dump or archive from upstream sources.
- A lot of community collections contain tools, scripts, or payloads that should be reviewed and used with caution.

Recommended placement on SD card:
- Themes: `/Themes/` on FAT32 or LittleFS, depending on your build
- JS scripts: `/BruceJS/<Category>/`
- More general assets: follow the target firmware's SD layout for your specific port

Regional frequency reminder:
- EU / Europe: often 433.92 MHz and 868 MHz
- US / North America: often 315 MHz, 433.92 MHz, and 915 MHz
- AU / NZ: usually 433.92 MHz, with some 915 MHz devices
- Always confirm what is legal where you are before transmitting

## Structure

- `external/` - populated by the downloader script (gitignored)
- `docs/source-catalog.md` - organized catalog of source repos
- `scripts/fetch_sources.sh` - downloads community repos into `external/`

## Quick start

```bash
chmod +x scripts/fetch_sources.sh
./scripts/fetch_sources.sh
```

This will clone the curated sources into `external/` under the repo root.

## Categories covered

### Bruce
- Themes
- JS scripts and app packs
- Bruce-specific SD packs and hubs

### Flipper-style port (Sor3nt)
- `sdcard.zip` / asset packs
- desktop companion utilities
- boot and UI assets

### Sub-GHz by region
- EU / Europe
- US / North America
- Australia / NZ
- large general collections and mixed-region dumps

### Infrared
- universal remote packs
- IR DB sources

### BadUSB
- Duckys and payload libraries

### NFC / RFID
- amiibo and contactless sample collections

## Source catalog

See the detailed index here:
- `docs/source-catalog.md`

## License and usage

This repository is meant to organize references and helper tooling. If a source repository has stricter licensing, review that upstream repo before copying or redistributing files.

Keep this repository focused on indexes, documentation, and local fetch automation unless you specifically intend to mirror and distribute upstream content under compatible terms.
