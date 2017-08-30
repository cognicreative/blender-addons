import sys
import imp

import bpy
from bpy import utils

bl_info = {
    "name": "Calculate Curve Length",
    "author": "Gregg Patton",
    "version": (0, 0, 1),
    "blender": (2, 7, 8),
    "location": "Tools > CogniCreative",
    "description": "Calculate length of curve",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "CogniCreative"}

class CalculateCurveLength() :
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_context = "objectmode"
    bl_label = "Calc Curve Len"
    bl_category = bl_label

    def draw(self, context) :
        theCol = self.layout.column(align = True)

        obj = context.object
        # row = self.layout.row()

        theCol.label(text="Active object is: " + obj.name)

        if obj.type == 'CURVE' and context.active_object.select:
           theCol.label(text="Length: " + context.window_manager.clipboard)
           theCol.operator("calclen.perform", text = "Update Length")

    #end draw
 
#end CalculateCurveLength

def get_length(context):

    obj_name_original = context.active_object.name
    bpy.ops.object.duplicate_move()
       
    # the duplicate is active, apply all transforms to get global coordinates
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    
    context.active_object.data.bevel_object = None

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

class CalculateCurveLengthPanelObject(bpy.types.Panel, CalculateCurveLength) :
    bl_context = "objectmode"

class PerformCalculation(bpy.types.Operator) :
    bl_idname = "calclen.perform"
    bl_label = "Calc Length"
 
    def invoke(self, context, event) :
        get_length(context)
        return {"FINISHED"}
    

def register():
    utils.register_class(CalculateCurveLengthPanelObject)
    utils.register_class(PerformCalculation)

def unregister():
    utils.unregister_class(CalculateCurveLengthPanelObject)
    utils.unregister_class(PerformCalculation)


if __name__ == "__main__":
    register()