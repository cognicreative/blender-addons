bl_info = {
    "name": "Hello World",
    "author": "Gregg Patton",
    "version": (0, 0, 1),
    "blender": (2, 7, 8),
    "location": "Tools > Hello World",
    "description": "Hello World",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Hello World"}

import sys
import imp

import bpy
from bpy import utils

class HelloWorld() :
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_context = "objectmode"
    bl_label = "Hello World"
    bl_category = bl_label

    def draw(self, context) :
        theCol = self.layout.column(align = True)
        # dragonarmature.draw(theCol, context)
        # theCol.operator("mesh.create_dragon_winglet", text = "Create Dragon Winglet")
        # joints.draw(theCol, context)
        # theCol.operator("armature.reset_bone_scale", text = "Reset Bone Scale")
        theCol.operator("unregister.hello_world", text = "Unregister")

    #end draw
 
#end HelloWorld

class HelloWorldPanelObject(bpy.types.Panel, HelloWorld) :
    bl_context = "objectmode"

class UnregisterHelloWorld(bpy.types.Operator) :
    bl_idname = "unregister.hello_world"
    bl_label = "Unregister"
 
    def invoke(self, context, event) :
        unregister()
        return {"FINISHED"}
    

def register():
    utils.register_class(HelloWorldPanelObject)
    utils.register_class(UnregisterHelloWorld)

def unregister():
    utils.unregister_class(HelloWorldPanelObject)
    utils.unregister_class(UnregisterHelloWorld)


if __name__ == "__main__":
    register()