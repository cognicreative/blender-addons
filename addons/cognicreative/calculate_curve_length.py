import bpy
import mathutils
from mathutils import Vector

category = "CogniCreative"
bl_info = {
    "name": "Curve Length",
    "author": "Gregg Patton",
    "version": (0, 0, 1),
    "blender": (2, 7, 8),
    "location": "Tools > CogniCreative",
    "description": "Blender addons from CogniCreative",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": category}

def get_length(context):

    obj_name_original = context.active_object.name
    bpy.ops.object.duplicate_move()
       
    # the duplicate is active, apply all transforms to get global coordinates
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    
    # convert to mesh
    bpy.ops.object.convert(target='MESH', keep_original=False)
    

    _data = context.active_object.data
    
    edge_length = 0
    for edge in _data.edges:
        vert0 = _data.vertices[edge.vertices[0]].co
        vert1 = _data.vertices[edge.vertices[1]].co
        edge_length += (vert0-vert1).length
    
    # deal with trailing float smear
    edge_length = '{:.6f}'.format(edge_length)
    print(edge_length)
    
    # stick into clipboard
    context.window_manager.clipboard = edge_length
    
    bpy.ops.object.delete()
    context.scene.objects.active = context.scene.objects[obj_name_original]
    context.object.select = True


class ButtonOne(bpy.types.Operator):
    """Defines a button"""
    bl_idname = "scene.dostuff"
    bl_label = "Calc Length"
 
    def execute(self, context):
        get_length(context)
        return{'FINISHED'}  


class OperatorPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Some Utility"
    bl_idname = "OBJECT_PT_somefunction"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object
        row = layout.row()

        # display label and button
        if not obj.type == 'Curve' and context.active_object.select:
            row.label(text="Active object is: " + obj.name)
            self.layout.operator("scene.dostuff", text='Print length to console')



classes = [OperatorPanel, ButtonOne]

def register():
    for i in classes:
        bpy.utils.register_class(i)


def unregister():
    for i in classes:
        bpy.utils.unregister_class(i)


if __name__ == "__main__":
    register()