import bpy

class Properties(bpy.types.PropertyGroup):
    props = bpy.props
    selection_only = props.BoolProperty(
        name = "Selected faces only",
        default = False,
    )
