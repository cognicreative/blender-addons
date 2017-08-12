import bpy

category = "CogniCreative"
bl_info = {
    "name": "Segment Tools",
    "author": "Gregg Patton",
    "version": (0, 0, 1),
    "blender": (2, 7, 8),
    "location": "Tools > CogniCreative",
    "description": "Blender addons from CogniCreative",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": category}


class CC_Segment(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Segment Tools"
    bl_category = category

    def draw(self, context):
        theCol = self.layout.column(align = True)
        theCol.operator("cc_create_segment", text = "Create Segment")

    # end draw

# end CC_Segment

class CC_CreateSegment(bpy.types.Operator) :
    bl_idname = "cc_create_segment"
    bl_label = "Create Segment"
    bl_options = {"UNDO"}
 
    def invoke(self, context, event) :
        print("Hello")
        return

def register():
    utils.register_class(CC_Segment)
    utils.register_class(CC_CreateSegment)
    
def unregister():
    utils.unregister_class(CC_Segment)
    utils.unregister_class(CC_CreateSegment)

if __name__ == "__main__":
    register()
