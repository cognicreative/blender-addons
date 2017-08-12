bl_info = {
    "name": "CogniCreative Tools",
    "author": "Gregg Patton",
    "version": (0, 0, 1),
    "blender": (2, 7, 8),
    "location": "Tools > CogniCreative",
    "description": "CogniCreative Tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "CogniCreative"}

import sys
import imp

import bpy
from bpy import utils

class CogniCreative() :
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_context = "objectmode"
    bl_label = "CogniCreative"
    bl_category = bl_label

    def draw(self, context) :
        theCol = self.layout.column(align = True)
        # dragonarmature.draw(theCol, context)
        # theCol.operator("mesh.create_dragon_winglet", text = "Create Dragon Winglet")
        # joints.draw(theCol, context)
        # theCol.operator("armature.reset_bone_scale", text = "Reset Bone Scale")
        # theCol.operator("unregister.cognicreative", text = "Unregister")
        theCol.operator("cc.createsegment", text = "Create Segment")

    #end draw
 
#end CogniCreative

class CogniCreativePanelObject(bpy.types.Panel, CogniCreative) :
    bl_context = "objectmode"

class UnregisterCogniCreative(bpy.types.Operator) :
    bl_idname = "unregister.cognicreative"
    bl_label = "Unregister"
 
    def invoke(self, context, event) :
        unregister()
        return {"FINISHED"}
    
class CC_CreateSegment(bpy.types.Operator) :
    bl_idname = "cc.createsegment"
    bl_label = "Create Segment"
 
    def invoke(self, context, event) :
        print("CreateSegment")
        return {"FINISHED"}
    

def register():
    utils.register_class(CogniCreativePanelObject)
    utils.register_class(CC_CreateSegment)

def unregister():
    utils.unregister_class(CogniCreativePanelObject)
    utils.unregister_class(CC_CreateSegment)


if __name__ == "__main__":
    register()