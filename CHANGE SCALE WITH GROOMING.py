bl_info = {
    "name": "SCALER",
    "author": "Manuja Dilaksitha @ Thina Entertainment",
    "version": (1, 0),
    "blender": (2, 93),
    "description": "Scale the hair particles along with the mesh. So scaling the mesh won't affect the groom",
    "warning": "Ctrl+Z is effective only for limited times in Blender ;)",
    "doc_url": "github.com/Manuja-Dilakshitha",
    "tracker_url": "",
}




import bpy
from bpy import context
from bpy.types import Operator
from bpy.props import BoolProperty


class ChangeScalePanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Change Scale"
    bl_idname = "CHANGE_NAME_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'CHANGE SCALE'

    def draw(self, context):
        
        scene = context.scene
        
        
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Change Scale", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)

        
        row = layout.row()
        row.prop(scene, "my_string_prop")
      
        row = layout.row()
        row.operator('scale.change')
        
        row = layout.row()
        row.label(text = "")
        
        row = layout.row()
        row.label(text = "THINA ENTERTAINMENT", icon="GREASEPENCIL")






########################           FUNCTION              ##############################


class CHANGE_SCALE(bpy.types.Operator):
    
    bl_label = "Change Scale"
    bl_idname = 'scale.change'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        scene = bpy.context.scene
        
        object = bpy.context.active_object
        scale_percentage = float(context.scene.my_string_prop)


        object.scale.x = object.scale.x / scale_percentage
        object.scale.y = object.scale.y / scale_percentage
        object.scale.z = object.scale.z / scale_percentage

        particle_settings = bpy.data.particles['ParticleSettings']

        object.particle_systems['ParticleSystem'].settings = particle_settings

        #particle_settings.child_radius = 0.01
        #particle_settings.kink_amplitude = 0.04


        for ps in object.particle_systems:
            ps.settings.kink_amplitude = ps.settings.kink_amplitude / (scale_percentage)
            ps.settings.child_radius = ps.settings.child_radius / (scale_percentage)
            #ps.settings.hair_length = ps.settings.hair_length / scale_percentage
            
        
        return{'FINISHED'}
            
            
            
            
            
            
##########################           REGISTER              ##############################


def register():
    bpy.types.Scene.my_string_prop = bpy.props.StringProperty \
      (
        name = "Divide By : ",
        description = "Scale division factor",
        default = "0.1"
      )
      
      
    
    bpy.utils.register_class(ChangeScalePanel)
    bpy.utils.register_class(CHANGE_SCALE)




##########################           UNREGISTER              ##############################

def unregister():
    bpy.utils.unregister_class(ChangeScalePanel)
    bpy.utils.unregister_class(CHANGE_SCALE)


if __name__ == "__main__":
    register()
