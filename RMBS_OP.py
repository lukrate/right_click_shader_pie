import bpy
import os

class UseNodeMaterial(bpy.types.Operator):
    """Use Material Node"""
    bl_idname = "use.nodematerial"
    bl_label = "Use Material Node"

    def execute(self, context):        
        bpy.context.active_object.active_material.use_nodes = True
        return {'FINISHED'}
    
class UseNodeWorld(bpy.types.Operator):
    """Use World Node"""
    bl_idname = "use.nodeworld"
    bl_label = "Use World Node"

    def execute(self, context):
        bpy.context.scene.world.use_nodes = True
        return {'FINISHED'}

class UseNodeComp(bpy.types.Operator):
    """Use Comp Node"""
    bl_idname = "use.nodecomp"
    bl_label = "Use Comp Node"

    def execute(self, context):
        bpy.context.scene.use_nodes = True
        return {'FINISHED'}

class AddMaterial(bpy.types.Operator):
    """Add Shader"""
    bl_idname = "add.material"
    bl_label = "Add Material"

    def execute(self, context):
        if bpy.context.active_object.active_material == None and bpy.context.active_object.active_material_index == 0:
            bpy.ops.object.material_slot_remove()
        activeObject = bpy.context.active_object
        mat = bpy.data.materials.new(name="MaterialName")
        activeObject.data.materials.append(mat)
        bpy.context.active_object.active_material.use_nodes = True
        
        return {'FINISHED'}

class ToggleBackdrop(bpy.types.Operator):
    """Toggle Backdrop"""
    bl_idname = "toggle.backdrop"
    bl_label = "Toggle Backdrop"
    
    def execute(self, context):
        if bpy.context.space_data.show_backdrop == False:
            bpy.context.space_data.show_backdrop = True
        else:
            bpy.context.space_data.show_backdrop = False
        return {'FINISHED'}
    
class AddWorld(bpy.types.Operator):
    """Add World"""
    bl_idname = "add.world"
    bl_label = "Add World"

    def execute(self, context):
        scene = bpy.context.scene
        if len(bpy.data.worlds):
            new_world = bpy.data.worlds.new("New World")
        scene.world = bpy.data.worlds[0]
        bpy.context.scene.world.use_nodes = True
        
        return {'FINISHED'}
    
class SimpleHdri(bpy.types.Operator):
    """Simple HDRI setup"""
    bl_idname = "simple.hdri"
    bl_label = "Simple HDRI"
    
    def execute(self, context):
        #select current world
        world = bpy.context.scene.world
        nodes = world.node_tree.nodes
        links = world.node_tree.links
        #clear all nodes
        nodes.clear()
        #add_node
        world_output = nodes.new(type="ShaderNodeOutputWorld")
        
        background = nodes.new(type="ShaderNodeBackground")
        background.location = -230, 0
        links.new(background.outputs[0], world_output.inputs[0])

        hue_sat = nodes.new(type="ShaderNodeHueSaturation")
        hue_sat.location = -430, 0
        links.new(hue_sat.outputs[0], background.inputs[0])
        
        env_text = nodes.new(type="ShaderNodeTexEnvironment")
        env_text.location = -750, 0
        links.new(env_text.outputs[0], hue_sat.inputs[4])
        
        mapping = nodes.new(type="ShaderNodeMapping")
        mapping.location = -950, 0
        links.new(mapping.outputs[0], env_text.inputs[0])
        
        tex_coord = nodes.new(type="ShaderNodeTexCoord")
        tex_coord.location = -1150, 0
        links.new(tex_coord.outputs[0], mapping.inputs[0])        
        
        return {'FINISHED'}

class SetOriginToSelection(bpy.types.Operator):
    bl_label = "Origin to selection"
    bl_idname = "wm.set_origin_to_selection"
    
    clear_position: bpy.props.BoolProperty(name="Center to world origin")
    
    def execute(self, context):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                
                cursorPos = context.scene.cursor.location.xyz
            
                bpy.ops.view3d.snap_cursor_to_selected()
                bpy.ops.object.editmode_toggle()
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
                if self.clear_position:
                    bpy.ops.object.location_clear(clear_delta=False)
                    
                bpy.ops.object.editmode_toggle()

                context.scene.cursor.location.xyz = cursorPos

        
        return { "FINISHED" }

class SHADER_OT_Load_shaders(bpy.types.Operator):
    bl_idname="shader.load_shaders"
    bl_label="Load Shader"
    
    "NAME OF SUBOJECT"
    name: bpy.props.StringProperty(name="Import Shader and add to node")

    def execute(self, context):
        
        try:
            bpy.data.node_groups[self.name]
        except:
            script_file = os.path.realpath(__file__)
            _ = os.sep
            dir = os.path.dirname(script_file) + "/BlenderFiles/"
            fileName = "presets.blend"

            bpy.ops.wm.append(filepath=_+fileName+_+'NodeTree'+_,
                    directory=os.path.join(dir, fileName+_+"NodeTree"+_),
                    filename=self.name)

        bpy.ops.node.add_node(type="ShaderNodeGroup", use_transform=True, settings=[{"name":"node_tree", "value":f"bpy.data.node_groups['{self.name}']"}])
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')


        return { "FINISHED" }

