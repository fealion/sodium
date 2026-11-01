#!/usr/bin/env python3
"""Patch Relictium's legacy Gradle plugin resolution in the parent CI checkout.

RetroFuturaGradle publishes its implementation artifact to Maven, while the
submodule's plugin DSL can fail to resolve the marker from the public repo.
Map the plugin ID directly to the published implementation coordinates.
"""
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: patch-rfg-settings.py path/to/settings.gradle")

path = Path(sys.argv[1])
if not path.is_file():
    raise SystemExit("settings file not found: " + str(path))

source = path.read_text(encoding="utf-8")
if "useModule(" in source and "com.gtnewhorizons:retrofuturagradle" in source:
    print("RFG plugin resolution is already patched")
    raise SystemExit(0)

needle = "pluginManagement {\n"
replacement = """pluginManagement {
    resolutionStrategy {
        eachPlugin {
            if (requested.id.id == 'com.gtnewhorizons.retrofuturagradle') {
                useModule("com.gtnewhorizons:retrofuturagradle:" + requested.version)
            }
        }
    }
"""
if needle not in source:
    raise SystemExit("could not find pluginManagement block in " + str(path))

path.write_text(source.replace(needle, replacement, 1), encoding="utf-8")
print("Added direct RFG implementation-module resolution")
