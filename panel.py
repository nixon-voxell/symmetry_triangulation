import bpy
from .operator import SymmetryTriangulation_OT_Triangulate

class SymmetryTriangulation_PT_Panel(bpy.types.Panel):
    bl_idname = "SymmetryTriangulation_PT_Panel"
    bl_label = "Symmetry Triangulation"
    bl_description = "Triangulate faces with more than 3 vertices symmetrically by adding a vertex at the center."
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Symmetry Triangulation"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        scene = context.scene

        prop_SymmetryTri = scene.prop_SymmetryTri

        if (obj != None):
            if obj.data.is_editmode:
                row = layout.row()
                row.prop(prop_SymmetryTri, "selection_only")
                row = layout.row()
                row.operator(
                     SymmetryTriangulation_OT_Triangulate.bl_idname,
                     text="Triangulate"
                )

            else:
                layout.label(text="Enter edit mode to access the features.")
