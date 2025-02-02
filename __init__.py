# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Symmetry Triangulation",
    "author" : "Nixon",
    "description" : "Blender add-on to triangulate faces with more than 3 vertices symmetrically by adding a vertex at the center.",
    "blender" : (4, 3, 2),
    "version" : (1, 0, 0),
    "location" : "View3D",
    "category" : "Generic"
}

import bpy

from .operator import *
from .panel import SymmetryTriangulation_PT_Panel
from .properties import Properties

classes = (
    # operators
    SymmetryTriangulation_OT_Triangulate,

    # panels
    SymmetryTriangulation_PT_Panel,

    # prop_SymmetryTri
    Properties
)

def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.VIEW3D_MT_edit_mesh.append(symmetry_triangulation_menu)
    bpy.types.Scene.prop_SymmetryTri = bpy.props.PointerProperty(type=Properties)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    del bpy.types.Scene.prop_SymmetryTri
