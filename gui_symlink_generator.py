#!/usr/bin/env python3
"""Simple GUI utility for creating symbolic links."""

from __future__ import annotations

import os
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk


class SymlinkGeneratorApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Symlink Generator")
        self.root.geometry("680x360")
        self.root.minsize(640, 320)

        self.target_path = tk.StringVar()
        self.destination_dir = tk.StringVar()
        self.link_name = tk.StringVar()
        self.status_text = tk.StringVar(value="Choose a target and destination to create a symlink.")

        self._build_ui()

    def _build_ui(self) -> None:
        frame = ttk.Frame(self.root, padding=16)
        frame.grid(row=0, column=0, sticky="nsew")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="Target path:").grid(row=0, column=0, sticky="w", pady=(0, 10))
        ttk.Entry(frame, textvariable=self.target_path).grid(row=0, column=1, sticky="ew", pady=(0, 10), padx=(8, 8))
        ttk.Button(frame, text="Browse…", command=self.pick_target).grid(row=0, column=2, pady=(0, 10))

        ttk.Label(frame, text="Symlink destination folder:").grid(row=1, column=0, sticky="w", pady=(0, 10))
        ttk.Entry(frame, textvariable=self.destination_dir).grid(row=1, column=1, sticky="ew", pady=(0, 10), padx=(8, 8))
        ttk.Button(frame, text="Browse…", command=self.pick_destination).grid(row=1, column=2, pady=(0, 10))

        ttk.Label(frame, text="Symlink name:").grid(row=2, column=0, sticky="w", pady=(0, 10))
        ttk.Entry(frame, textvariable=self.link_name).grid(row=2, column=1, sticky="ew", pady=(0, 10), padx=(8, 8))

        ttk.Button(frame, text="Create symlink", command=self.create_symlink).grid(
            row=3, column=0, columnspan=3, sticky="ew", pady=(4, 14)
        )

        preview = ttk.LabelFrame(frame, text="Preview", padding=10)
        preview.grid(row=4, column=0, columnspan=3, sticky="ew")
        preview.columnconfigure(0, weight=1)

        self.preview_label = ttk.Label(preview, text="", wraplength=620, justify="left")
        self.preview_label.grid(row=0, column=0, sticky="w")

        status = ttk.Label(frame, textvariable=self.status_text, wraplength=640, foreground="#1b5e20")
        status.grid(row=5, column=0, columnspan=3, sticky="w", pady=(12, 0))

        for var in (self.target_path, self.destination_dir, self.link_name):
            var.trace_add("write", self.update_preview)

        self.update_preview()

    def pick_target(self) -> None:
        selected = filedialog.askopenfilename(title="Choose target file")
        if not selected:
            selected = filedialog.askdirectory(title="Choose target folder")
        if selected:
            self.target_path.set(selected)
            if not self.link_name.get().strip():
                self.link_name.set(Path(selected).name)

    def pick_destination(self) -> None:
        selected = filedialog.askdirectory(title="Choose destination folder")
        if selected:
            self.destination_dir.set(selected)

    def update_preview(self, *_: object) -> None:
        link_name = self.link_name.get().strip()
        destination = self.destination_dir.get().strip()
        target = self.target_path.get().strip()

        if destination and link_name:
            link_path = str(Path(destination) / link_name)
        else:
            link_path = "(select destination and name)"

        self.preview_label.config(text=f"Symlink to create:\n  {link_path}  ->  {target or '(select target)'}")

    def create_symlink(self) -> None:
        target = Path(self.target_path.get().strip())
        destination = Path(self.destination_dir.get().strip())
        link_name = self.link_name.get().strip()

        if not target:
            messagebox.showerror("Missing target", "Please choose a target path.")
            return
        if not destination:
            messagebox.showerror("Missing destination", "Please choose a destination folder.")
            return
        if not link_name:
            messagebox.showerror("Missing link name", "Please enter a symlink name.")
            return

        link_path = destination / link_name

        if not target.exists():
            messagebox.showerror("Invalid target", "The selected target does not exist.")
            return
        if not destination.exists() or not destination.is_dir():
            messagebox.showerror("Invalid destination", "The destination must be an existing folder.")
            return
        if link_path.exists() or link_path.is_symlink():
            messagebox.showerror("Already exists", f"{link_path} already exists.")
            return

        try:
            os.symlink(target, link_path, target_is_directory=target.is_dir())
        except OSError as exc:
            messagebox.showerror("Failed", f"Could not create symlink:\n{exc}")
            self.status_text.set("Failed to create symlink.")
            return

        self.status_text.set(f"Created: {link_path} -> {target}")
        messagebox.showinfo("Success", f"Symlink created:\n{link_path} -> {target}")


def main() -> None:
    root = tk.Tk()
    app = SymlinkGeneratorApp(root)
    _ = app
    root.mainloop()


if __name__ == "__main__":
    main()
