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
cd legacy-1.12.2/renderer
./gradlew --no-daemon build
```

Use JDK 21 to run the Gradle build. The CI build downloads/uses the required
Java 8 compilation toolchain. Built jars are written to
`legacy-1.12.2/renderer/build/libs/`.

## Compatibility notes

Relictium's upstream README lists known incompatibilities with OptiFine,
FarPlaneTwo, LittleTiles, Fluidlogged API (and mods using it, such as
Subaquatic), and ArchitectureCraft. All the Mods 3 6.1.1 has not yet been
tested as a complete pack with this branch. Do not assume every ATM3 mod is
compatible until that regression testing is completed.

## Attribution and licensing

See [UPSTREAMS.md](UPSTREAMS.md). The renderer submodule retains its original
LGPL-3.0 license and attribution notices.
