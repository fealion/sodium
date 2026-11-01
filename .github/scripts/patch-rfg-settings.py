#!/usr/bin/env python3
"""Patch Relictium's legacy Gradle plugin resolution in the parent CI checkout.

RetroFuturaGradle's implementation artifact is published to GTNH's releases
repository. The upstream settings only search the public repository and rely
on a plugin marker which may not be mirrored there, so CI adds the releases
repository and maps the plugin ID directly to its implementation module.
"""
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: patch-rfg-settings.py path/to/settings.gradle")

path = Path(sys.argv[1])
if not path.is_file():
    raise SystemExit("settings file not found: " + str(path))

source = path.read_text(encoding="utf-8")

if "https://nexus.gtnewhorizons.com/repository/releases/" not in source:
    needle = "    repositories {\n"
    replacement = """    repositories {
        maven {
            name 'GTNH Releases'
            url 'https://nexus.gtnewhorizons.com/repository/releases/'
        }
"""
    if needle not in source:
        raise SystemExit("could not find pluginManagement repositories block in " + str(path))
    source = source.replace(needle, replacement, 1)

if "useModule(\"com.gtnewhorizons:retrofuturagradle:" not in source:
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
    source = source.replace(needle, replacement, 1)

path.write_text(source, encoding="utf-8")
print("Added GTNH releases repository and direct RFG implementation-module resolution")
