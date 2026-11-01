package net.caffeinemc.mods.sodium.forge;

import net.minecraftforge.fml.common.Mod;

/**
 * Minimal Forge 1.12.2 bootstrap.
 *
 * The legacy renderer is intentionally not enabled yet. Replacing the 1.12.2
 * chunk renderer safely requires compatibility work for Forge render hooks,
 * OptiFine-style integrations, TESRs and modded block renderers.
 */
@Mod(
    modid = SodiumForge1122.MOD_ID,
    name = SodiumForge1122.NAME,
    version = SodiumForge1122.VERSION,
    acceptedMinecraftVersions = "[1.12.2]"
)
public final class SodiumForge1122 {
    public static final String MOD_ID = "sodium";
    public static final String NAME = "Sodium (Forge 1.12.2)";
    public static final String VERSION = "0.1.0-1.12.2";
}
