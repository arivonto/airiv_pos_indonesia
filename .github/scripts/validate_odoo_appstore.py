#!/usr/bin/env python3
"""Validate an AIRIV Odoo Apps Store repository.

This check intentionally uses only the Python standard library so it can run
on GitHub Actions free runners without credentials or paid services.
"""

from __future__ import annotations

import ast
import csv
import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


REQUIRED_MANIFEST_KEYS = {
    "name",
    "version",
    "summary",
    "description",
    "author",
    "website",
    "license",
    "depends",
    "data",
    "installable",
}

REQUIRED_DESCRIPTION_FILES = (
    "static/description/icon.png",
    "static/description/banner.png",
    "static/description/index.html",
)

FORBIDDEN_NAMES = {"__pycache__", ".DS_Store"}
FORBIDDEN_SUFFIXES = {".pyc", ".pyo"}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def warn(message: str) -> None:
    print(f"WARNING: {message}")


def read_manifest(path: Path) -> dict:
    try:
        value = ast.literal_eval(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - expose exact manifest parse error.
        fail(f"{path} is not a valid Python literal manifest: {exc}")
    if not isinstance(value, dict):
        fail(f"{path} must evaluate to a dictionary")
    return value


def find_module_dir(repo_root: Path) -> Path:
    repo_name = repo_root.name
    preferred = repo_root / repo_name / "__manifest__.py"
    if preferred.exists():
        return preferred.parent

    candidates = sorted(
        p.parent
        for p in repo_root.glob("*/__manifest__.py")
        if ".git" not in p.parts and ".github" not in p.parts
    )
    if len(candidates) == 1:
        warn(f"module directory is {candidates[0].name}, not repo name {repo_name}")
        return candidates[0]
    if not candidates:
        fail("no module folder with __manifest__.py found at repository root")
    fail("multiple module folders found: " + ", ".join(p.name for p in candidates))


def validate_manifest(module_dir: Path) -> dict:
    manifest_path = module_dir / "__manifest__.py"
    manifest = read_manifest(manifest_path)
    missing = sorted(REQUIRED_MANIFEST_KEYS - set(manifest))
    if missing:
        fail(f"{manifest_path} missing keys: {', '.join(missing)}")

    version = str(manifest.get("version", ""))
    if not version.startswith("18.0."):
        fail(f"{manifest_path} version must start with 18.0., got {version!r}")

    if manifest.get("installable") is not True:
        fail(f"{manifest_path} must set installable=True")

    depends = manifest.get("depends")
    if not isinstance(depends, list) or not depends:
        fail(f"{manifest_path} depends must be a non-empty list")

    data = manifest.get("data", [])
    if not isinstance(data, list):
        fail(f"{manifest_path} data must be a list")
    for rel_path in data:
        if not isinstance(rel_path, str):
            fail(f"{manifest_path} data entry must be a string: {rel_path!r}")
        if not (module_dir / rel_path).exists():
            fail(f"{manifest_path} references missing data file: {rel_path}")

    for key in ("price", "currency"):
        if key not in manifest:
            warn(f"{manifest_path} has no {key!r}; paid/free state may be unclear")

    return manifest


def validate_static_description(module_dir: Path) -> None:
    for rel_path in REQUIRED_DESCRIPTION_FILES:
        path = module_dir / rel_path
        if not path.exists():
            fail(f"missing Apps Store asset: {path}")
        if path.stat().st_size == 0:
            fail(f"empty Apps Store asset: {path}")


def validate_xml_and_csv(module_dir: Path) -> None:
    for path in module_dir.rglob("*.xml"):
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            fail(f"invalid XML {path}: {exc}")

    for path in module_dir.rglob("*.csv"):
        try:
            with path.open(newline="", encoding="utf-8") as handle:
                list(csv.reader(handle))
        except Exception as exc:  # noqa: BLE001 - expose CSV parse/open issue.
            fail(f"invalid CSV {path}: {exc}")


def validate_clean_tree(repo_root: Path) -> None:
    root_manifest = repo_root / "__manifest__.py"
    if root_manifest.exists():
        warn("root-level __manifest__.py found; Odoo Apps expects one module folder at repository root")

    for dirpath, dirnames, filenames in os.walk(repo_root):
        path = Path(dirpath)
        if ".git" in path.parts:
            continue
        for dirname in list(dirnames):
            if dirname in FORBIDDEN_NAMES:
                fail(f"forbidden directory found: {path / dirname}")
        for filename in filenames:
            file_path = path / filename
            if filename in FORBIDDEN_NAMES or file_path.suffix in FORBIDDEN_SUFFIXES:
                fail(f"forbidden file found: {file_path}")


def main() -> int:
    repo_root = Path.cwd()
    branch = os.environ.get("GITHUB_REF_NAME")
    if branch and branch != "18.0":
        warn(f"workflow branch is {branch!r}; Odoo Apps registered branch should be '18.0'")

    module_dir = find_module_dir(repo_root)
    print(f"Validating module: {module_dir.name}")
    manifest = validate_manifest(module_dir)
    validate_static_description(module_dir)
    validate_xml_and_csv(module_dir)
    validate_clean_tree(repo_root)
    print(f"OK: {manifest['name']} ({manifest['version']}) is Apps Store audit-ready")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
