# Symlink Generator (GUI)

A simple desktop GUI app to create symbolic links while choosing both:

- the **target path** (file or folder you want to link to), and
- the **symlink location/name** (where the link should be created).

## Install

Run the installer script:

```bash
bash install.sh
```

This installs:

- app file to `~/.local/share/symlink-generator-3d/gui_symlink_generator.py`
- launcher command to `~/.local/bin/symlink-generator-3d`

If `~/.local/bin` is not on your `PATH`, add it:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then launch with:

```bash
symlink-generator-3d
```

## Run without install

```bash
python3 gui_symlink_generator.py
```

## How to use

1. Click **Browse…** next to **Target path** and choose a file or folder.
2. Click **Browse…** next to **Symlink destination folder** and choose where to place the symlink.
3. Enter the **Symlink name**.
4. Click **Create symlink**.

The app shows a live preview before creation.
