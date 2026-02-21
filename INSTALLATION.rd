# Installation and Download Guide

## 1) Download the correct files

You need these files from this repository:

- `gui_symlink_generator.py`
- `install.sh`
- `README.md` (optional, for usage notes)

### Option A: Clone with Git (recommended)

```bash
git clone <REPOSITORY_URL>
cd symlink-generator-for-3D
```

### Option B: Download ZIP

1. Download the repository ZIP from your Git host.
2. Extract it.
3. Open a terminal in the extracted `symlink-generator-for-3D` folder.
4. Confirm the required files exist:

```bash
ls gui_symlink_generator.py install.sh
```

## 2) Install

Run:

```bash
bash install.sh
```

This installs:

- App script to: `~/.local/share/symlink-generator-3d/gui_symlink_generator.py`
- Launcher command to: `~/.local/bin/symlink-generator-3d`

## 3) Add launcher to PATH (if needed)

If your shell cannot find `symlink-generator-3d`, run:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

To make it permanent, add that line to `~/.bashrc` or your shell profile.

## 4) Run the app

```bash
symlink-generator-3d
```

## 5) Run without installing (optional)

```bash
python3 gui_symlink_generator.py
```
