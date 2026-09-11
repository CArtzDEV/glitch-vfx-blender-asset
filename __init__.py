import bpy, os

def register():
    folder = os.path.dirname(__file__)
    libs = bpy.context.preferences.filepaths.asset_libraries
    if "Glitch VFX" not in libs:
        libs.new(name="Glitch VFX", directory=folder)

def unregister():
    libs = bpy.context.preferences.filepaths.asset_libraries
    if "Glitch VFX" in libs:
        libs.remove(libs["Glitch VFX"])
