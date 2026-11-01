package net.caffeinemc.mods.sodium.forge;

import net.minecraftforge.fml.relauncher.IFMLLoadingPlugin;
import org.spongepowered.asm.launch.MixinBootstrap;
import org.spongepowered.asm.mixin.MixinEnvironment;
import org.spongepowered.asm.mixin.Mixins;

import java.util.Map;

/**
 * Bootstraps the legacy Forge Mixin environment before game classes load.
 *
 * The renderer mixins are deliberately added in later porting steps. This
 * bootstrap only establishes the Java 8 / LaunchWrapper integration.
 */
@IFMLLoadingPlugin.Name("SodiumForge1122")
@IFMLLoadingPlugin.MCVersion("1.12.2")
@IFMLLoadingPlugin.SortingIndex(-5000)
@IFMLLoadingPlugin.TransformerExclusions({
    "net.caffeinemc.mods.sodium.forge"
})
public final class SodiumCorePlugin implements IFMLLoadingPlugin {
    public SodiumCorePlugin() {
        MixinBootstrap.init();
        MixinEnvironment.getDefaultEnvironment().setObfuscationContext("searge");
        Mixins.addConfiguration("mixins.sodium.json");
    }

    @Override
    public String[] getASMTransformerClass() {
        return new String[0];
    }

    @Override
    public String getModContainerClass() {
        return null;
    }

    @Override
    public String getSetupClass() {
        return null;
    }

    @Override
    public void injectData(Map<String, Object> data) {
        // No environment-specific setup is required at bootstrap time.
    }

    @Override
    public String getAccessTransformerClass() {
        return null;
    }
}
