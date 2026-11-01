#!/usr/bin/env python3
"""Patch legacy Relictium Gradle resolution for a reproducible CI build.

The pinned Relictium revision requests RFG 1.4.1, which is not present in the
configured GTNH repositories. RFG 1.4.2 is published there, so the legacy
build uses that compatible patch release and resolves its implementation
artifact directly rather than relying on a plugin marker.
"""
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: patch-rfg-settings.py path/to/settings.gradle")

settings_path = Path(sys.argv[1])
if not settings_path.is_file():
    raise SystemExit("settings file not found: " + str(settings_path))

source = settings_path.read_text(encoding="utf-8")

if "https://nexus.gtnewhorizons.com/repository/releases/" not in source:
    needle = "    repositories {\n"
    replacement = """    repositories {
        maven {
            name 'GTNH Releases'
            url 'https://nexus.gtnewhorizons.com/repository/releases/'
        }
"""
    if needle not in source:
        raise SystemExit("could not find pluginManagement repositories block in " + str(settings_path))
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
        raise SystemExit("could not find pluginManagement block in " + str(settings_path))
    source = source.replace(needle, replacement, 1)

build_path = settings_path.with_name("build.gradle")
if not build_path.is_file():
    raise SystemExit("build file not found: " + str(build_path))

build_source = build_path.read_text(encoding="utf-8")
old_decl = "id 'com.gtnewhorizons.retrofuturagradle' version '1.4.1'"
new_decl = "id 'com.gtnewhorizons.retrofuturagradle' version '1.4.2'"
if old_decl in build_source:
    build_source = build_source.replace(old_decl, new_decl, 1)
elif new_decl not in build_source:
    raise SystemExit("could not find the expected RFG 1.4.1 plugin declaration in " + str(build_path))

settings_path.write_text(source, encoding="utf-8")
build_path.write_text(build_source, encoding="utf-8")
print("Added GTNH releases resolution and pinned the unavailable RFG 1.4.1 to published 1.4.2")
