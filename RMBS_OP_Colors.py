import bpy

class SHADER_OT_Add_custom_color(bpy.types.Operator):
    bl_idname = "shader.add_color_operator"
    bl_label = "Add custom color"
    bl_info = "Menu color operator"

    color: bpy.props.FloatVectorProperty(name="color", subtype="COLOR")

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeRGB", use_transform=True)
        newNode = bpy.context.active_object.active_material.node_tree.nodes.active
        #matName = context.active_object.active_material.name
        #RGB = bpy.data.materials[matName].node_tree.nodes.new("ShaderNodeRGB")
        newNode.outputs[0].default_value[0] = self.color[0]
        newNode.outputs[0].default_value[1] = self.color[1]
        newNode.outputs[0].default_value[2] = self.color[2]
        
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')