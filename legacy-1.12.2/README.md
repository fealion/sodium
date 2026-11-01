# Forge 1.12.2 renderer component

This branch pins a working Sodium-derived renderer for the legacy target:

- Minecraft 1.12.2
- Forge 14.23.5.2860
- Runtime target: Java 8

The renderer source is linked at `renderer/` as a Git submodule. It is
**Relictium**, an unofficial Forge port descended from Vintagium, itself an
unofficial Sodium fork. It is not a direct backport of the current modern
Sodium source tree. The original modern Sodium project remains at the repo
root and is not changed by this legacy component.

## Get the source and build

From the repository root:

```sh
git submodule update --init --recursive
python3 .github/scripts/patch-rfg-settings.py legacy-1.12.2/renderer/settings.gradle
cd legacy-1.12.2/renderer
./gradlew --no-daemon build
```

Use JDK 21 to run the Gradle build and Python 3 for the compatibility patch.
The build uses the Java 8 compilation toolchain. Built jars are written to
`legacy-1.12.2/renderer/build/libs/`.

The patch changes the pinned Relictium build from its unavailable RFG 1.4.1
plugin declaration to published RFG 1.4.2 and adds the GTNH releases
repository. It changes only the checked-out submodule working tree, not its
pinned upstream commit.

## Compatibility notes

Relictium's upstream README lists known incompatibilities with OptiFine,
FarPlaneTwo, LittleTiles, Fluidlogged API (and mods using it, such as
Subaquatic), and ArchitectureCraft. All the Mods 3 6.1.1 has not yet been
tested as a complete pack with this branch. Do not assume every ATM3 mod is
compatible until that regression testing is completed.

## Attribution and licensing

See [UPSTREAMS.md](UPSTREAMS.md). The renderer submodule retains its original
LGPL-3.0 license and attribution notices.
