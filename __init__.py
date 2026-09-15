import bpy, os

def register():
    folder = os.path.dirname(__file__)
    libs = bpy.context.preferences.filepaths.asset_libraries
    if "CArtz VFX Effects" not in libs:
        libs.new(name="CArtz VFX Effects", directory=folder)

def unregister():
    libs = bpy.context.preferences.filepaths.asset_libraries
    if "CArtz VFX Effects" in libs:
        libs.remove(libs["CArtz VFX Effects"])
