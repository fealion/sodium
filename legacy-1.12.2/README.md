# Sodium — Forge 1.12.2 port (bootstrap)

This directory is an isolated legacy target for Minecraft 1.12.2 / Forge
14.23.5.2860 / Java 8. It deliberately does not alter the modern Fabric and
NeoForge build at the repository root.

## Current status

This is **only the initial Forge mod bootstrap**. It registers a minimal mod
entry point so the legacy build can be brought up independently. It does not
yet replace chunk rendering, improve frame rates, or claim compatibility with
All the Mods 3.

## Build

Use JDK 8 and Gradle 4.10.3:

```sh
cd legacy-1.12.2
gradle setupDecompWorkspace
gradle build
```

The output JAR is written to `build/libs/`.

## Porting milestones

1. Establish a reproducible ForgeGradle 2.3 / Java 8 build.
2. Add a renderer backend behind a safe opt-in switch; preserve vanilla fallback.
3. Integrate Forge block-layer, chunk rebuild, and render events.
4. Add compatibility adapters for TESRs, custom baked models, and modded renderers.
5. Run a structured regression matrix against ATM3 6.1.1.

Do not install this bootstrap as a performance mod: it currently provides no
renderer replacement.
