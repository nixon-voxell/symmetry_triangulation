import bpy, bmesh
import numpy as np
import mathutils as mt
import math
import json
import os

class SymmetryTriangulation_OT_Triangulate(bpy.types.Operator):
    bl_idname = "symmetry_triangulation.triangulate"
    bl_label = "Symmetry Triangulation"
    bl_description = "Triangulate faces with more than 3 vertices symmetrically by adding a vertex at the center."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = bpy.context.active_object
        mesh = bmesh.from_edit_mesh(obj.data)

        for f in mesh.faces:
            if len(f.verts) > 3:
                co_sum = mt.Vector((0, 0, 0))
                for v in f.verts:
                    co_sum += v.co

                center = co_sum / len(f.verts)
                center_v = mesh.verts.new(center)

                for e in f.edges:
                    v1 = e.verts[0]
                    v2 = e.verts[1]
          
                    mesh.faces.new((v1, v2, center_v))

                bmesh.ops.delete(mesh, geom=[f], context="FACES")

        self.report({"INFO"}, "Symmetry triangulation complete!")
        bmesh.update_edit_mesh(obj.data, destructive=True)

        return {"FINISHED"}

def symmetry_triangulation_menu(self, context):
    self.layout.operator(SymmetryTriangulation_OT_Triangulate.bl_idname)
