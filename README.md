# FFC (Fuckin Fast Copier)

Copies files/directories from one machine to another using tar + rsync for speed.

## Usage

```bash
python main.py
```

Then enter the source path and destination path (e.g., `user@host:/path`).

## How it works

1. Archives the source directory with `tar`
2. Transfers the archive with `rsync -ah --progress`
3. Extracts the archive at the destination
4. Cleans up temporary tar files

## Requirements

- Python 3
- `tar`, `rsync` on both machines
