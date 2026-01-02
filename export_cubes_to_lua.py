bl_info = {
    "name": "Export Cubes To Lua (Defold)",
    "author": "yeqwep",
    "version": (0, 0),
    "blender": (5, 0, 1),
    "location": "View3D > Sidebar",
    "description": "Export cube transforms as a Lua table for Defold",
    "category": "Object",
}

import bpy
import math
from bpy_extras.io_utils import ExportHelper


# ==================================================
# Operator: Handles the actual export process
# ==================================================
class EXPORT_OT_cubes_to_lua(bpy.types.Operator, ExportHelper):
    """
    This operator is executed when the export button is pressed.
    It writes cube transform data into a Lua file.
    """
    bl_idname = "export.cubes_to_lua"
    bl_label = "Export Cubes to Lua (Defold)"

    # File extension enforced by the file dialog
    filename_ext = ".lua"

    def execute(self, context):
        # Open the file selected by the user
        with open(self.filepath, mode="w", encoding="utf-8") as file:

            # Start of Lua table
            file.write("return {\n")

            # Iterate over all objects in the current scene
            for obj in context.scene.objects:

                # Only export mesh objects whose names start with "Cube"
                if obj.type == 'MESH' and obj.name.startswith("Cube"):

                    # Object transforms
                    location = obj.location
                    scale = obj.scale
                    rotation = obj.rotation_euler
                    # Convert rotation from radians to degrees
                    rot_x = math.degrees(rotation.x)
                    rot_y = math.degrees(rotation.y)
                    rot_z = math.degrees(rotation.z)
                    # Write one Lua table entry per object
                    file.write("    {\n")
                    file.write(f"        name = \"{obj.name}\",\n")
                    file.write(
                        "        position = { x = %.3f, y = %.3f, z = %.3f },\n"
                        % (location.x, location.y, location.z)
                    )
                    file.write(
                        "        scale    = { x = %.3f, y = %.3f, z = %.3f },\n"
                        % (scale.x, scale.y, scale.z)
                    )
                    file.write(
                        "        rotation = { x = %.3f, y = %.3f, z = %.3f },\n"
                        % (rot_x, rot_y, rot_z)
                    )
                    file.write("    },\n")

            file.write("}\n")

        # Show a message in Blender's status bar
        self.report({'INFO'}, "Lua export completed successfully")
        return {'FINISHED'}


# ==================================================
# UI Panel: Button shown in the 3D View sidebar
# ==================================================
class EXPORT_PT_cubes_lua_panel(bpy.types.Panel):
    bl_label = "Cube Lua Export (Defold)"
    bl_idname = "EXPORT_PT_cubes_lua_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Export'

    def draw(self, context):
        layout = self.layout
        layout.operator("export.cubes_to_lua")


# ==================================================
# Registration
# ==================================================
def register():
    bpy.utils.register_class(EXPORT_OT_cubes_to_lua)
    bpy.utils.register_class(EXPORT_PT_cubes_lua_panel)


def unregister():
    bpy.utils.unregister_class(EXPORT_PT_cubes_lua_panel)
    bpy.utils.unregister_class(EXPORT_OT_cubes_to_lua)


if __name__ == "__main__":
    register()