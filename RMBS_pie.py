import bpy
from bpy.types import Menu

class NODE_EDITOR_PIE(Menu):
    bl_idname = 'pie.shader_selection'
    bl_label = "Node Selection"
    #bl_options = {'REGISTER', 'UNDO'}
    
    

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        
        bxtcsdatatt = bpy.context.space_data.tree_type

        if bxtcsdatatt == 'ShaderNodeTree':
            if bpy.context.space_data.shader_type == 'OBJECT':
                if bpy.context.active_object.type == 'MESH':
                    if hasattr(bpy.context.active_object.active_material, 'name'):
                        if bpy.context.active_object.active_material.use_nodes == False:
                            drawPieUseNodeShader(pie)
                        else:
                            drawPieShader(pie)
                    else:
                        drawPieAddMaterial(pie) 
                elif bpy.context.active_object.type == 'LIGHT':
                    drawPieShaderLight(pie)
                else:
                    drawPieAlertNoObject(pie)
            elif bpy.context.space_data.shader_type == 'WORLD':
                if bpy.context.scene.world is None:
                    drawPieAddWorld(pie)
                else:
                    if bpy.context.scene.world.use_nodes == False:
                        drawPieUseNodeWorld(pie)
                    else:
                        drawPieWorld(pie)
            elif bpy.context.space_data.shader_type == 'LINESTYLE':
                drawPieShaderOnlylist(pie)
            else:
                return
                
        elif bxtcsdatatt == 'TextureNodeTree':
            drawPieTextureNode(pie)
        elif bxtcsdatatt == 'CompositorNodeTree':
            if bpy.context.scene.use_nodes == False:
                drawPieUseNodeComp(pie)
            else:
                drawPieNodeComp(pie)
        
        elif bxtcsdatatt == "GeometryNodeTree":
            drawPieShaderOnlylist(pie)
        
        else:
            return
        return   

def shaderNodeBtn(text, type, row, icon="NONE"):
    row_op=row.operator("node.add_node", text=text, icon=icon)
    row_op.type=type
    row_op.use_transform = True

def drawPieAddMaterial(pie):
    pie.operator("add.material", text="New Material", icon="FILE_TICK")
    return

def drawPieAddWorld(pie):
    pie.operator("add.world", text="New World", icon="FILE_TICK")
    return

def drawPieUseNodeShader(pie):
    pie.operator("use.nodematerial", text="Use Node", icon="FILE_TICK")
    return

def drawPieUseNodeWorld(pie):
    pie.operator("use.nodeworld", text="Use Node", icon="ZOOM_IN")
    return

def drawPieUseNodeComp(pie):
    pie.operator("use.nodecomp", text="Use Node", icon="ZOOM_IN")
    return
    

def drawPieShaderOnlylist(pie):
    box = pie.split().column()
    row = box.row(align=True).box()
    row.menu("NODE_MT_add", text="All Nodes", icon="ZOOM_IN")
    

def drawPieShaderLight(pie):
    box = pie.split().column(align=True)
    row = box.row(align=True).box()
    row.scale_y = 1.5
    shaderNodeBtn("IES", "ShaderNodeTexIES", row)
    
    box = pie.split().column(align=True)
    row = box.row(align=True).box()
    row.scale_y = 1.5
    shaderNodeBtn("Black Body", "ShaderNodeBlackbody", row)

    box = pie.split().column(align=True)
    row = box.row(align=True).box()
    row.menu("NODE_MT_add", text="All Nodes", icon="ZOOM_IN")

def drawPieShader(pie):
    
    #### Color ####
    box = pie.split().column(align=True)
    row = box.row(align=True)
    ##row.label(text="Color", icon="COLOR")
    row = box.row(align=True)
    row.scale_y = 1.5
    shaderNodeBtn("Hue Sat", "ShaderNodeHueSaturation", row)
    shaderNodeBtn("RGB Curve", "ShaderNodeRGBCurve", row)
    row = box.row(align=True)
    shaderNodeBtn("Mix RGB", "ShaderNodeMixRGB", row)
    shaderNodeBtn("Invert", "ShaderNodeInvert", row)

    
    #### Vector ####    
    box = pie.split().column(align=True)
    row = box.row(align=True)
    row.scale_y = 1.5
    shaderNodeBtn("Tex. Coordinate", "ShaderNodeTexCoord", row)
    shaderNodeBtn("Mapping", "ShaderNodeMapping", row)
    row = box.row(align=True)
    row.scale_y = 1
    shaderNodeBtn("Bump", "ShaderNodeBump", row)
    shaderNodeBtn("Normal", "ShaderNodeNormalMap", row)
    shaderNodeBtn("Disp", "ShaderNodeDisplacement", row)


    
    #### INPUTS ####
    box = pie.split().column(align=True)
    row = box.row(align=True)    
    row.scale_y = 1.5
    shaderNodeBtn("Fresnel", "ShaderNodeFresnel", row)
    shaderNodeBtn("RGB", "ShaderNodeRGB", row)
    row.menu("SHADER_MT_colors_menu", text="", icon="PLUS")
    shaderNodeBtn("Geometry", "ShaderNodeNewGeometry", row)

    row = box.row(align=True)
    shaderNodeBtn("AO", "ShaderNodeAmbientOcclusion", row)
    shaderNodeBtn("Layer Weight", "ShaderNodeLayerWeight", row)
    shaderNodeBtn("BEVEL", "ShaderNodeBevel", row)
    shaderNodeBtn("Value", "ShaderNodeValue", row)
    
    #### Textures ####
    box = pie.split().column(align=True)
    row = box.row(align=True)
    row.scale_y = 1.0
    shaderNodeBtn("Checker", "ShaderNodeTexChecker", row)
    shaderNodeBtn("Brick", "ShaderNodeTexBrick", row)
    shaderNodeBtn("Gradient", "ShaderNodeTexGradient", row)
    row = box.row(align=True)
    row.scale_y = 1.5
    shaderNodeBtn("Magic", "ShaderNodeTexMagic", row)
    shaderNodeBtn("Noise", "ShaderNodeTexNoise", row)
    shaderNodeBtn("Voronoi", "ShaderNodeTexVoronoi", row)
    shaderNodeBtn("Musgrave", "ShaderNodeTexMusgrave", row)
    shaderNodeBtn("Wave", "ShaderNodeTexWave", row)

    #### Wrangler ####
    box = pie.split().column()
    row = box.row(align=True)
    #row.label(text="Node Wrangler ", icon="NODETREE")
    row = box.row(align=True)
    row.scale_y = 1.5
    row.operator("node.nw_add_texture", text="Wrangler Coordinate")
    row.operator("node.nw_add_textures_for_principled", text="Textures principled")
    

    ###ALL NODE
    box = pie.split().column(align=True)
    row = box.row(align=True).box()
    row.scale_x = 1.5
    row.scale_y = 1.5
    row.menu("SHADER_MT_Imperfections_menu", text="PRESETS", icon="NONE")
    
    #### Converter ####
    box = pie.split().row(align=True)
    col = box.column(align=True)
    row = col.row(align=True)
    row.scale_y = 1.5
    shaderNodeBtn("Color Ramp", "ShaderNodeValToRGB", row)
    shaderNodeBtn("VecMath", "ShaderNodeVectorMath", row)
    shaderNodeBtn("Math", "ShaderNodeMath", row)
    row = col.row(align=True)
    row.scale_y = 1
    shaderNodeBtn("RGB", "ShaderNodeSeparateRGB", row, icon="FULLSCREEN_ENTER")
    shaderNodeBtn("RGB", "ShaderNodeCombineRGB", row, icon="FULLSCREEN_EXIT")
    shaderNodeBtn("XYZ", "ShaderNodeSeparateXYZ", row, icon="FULLSCREEN_ENTER")
    shaderNodeBtn("XYZ", "ShaderNodeCombineXYZ", row, icon="FULLSCREEN_EXIT")
    
    #### SHADERS ####
    box = pie.split().column()
    c = box.column(align=True)
    c.emboss = "NORMAL"
    c.scale_x = 1.5
    c.scale_y = 1
    c.menu("NODE_MT_add", text="All Nodes", icon="VIEW_ZOOM")
    c.menu("NODE_MT_category_SH_NEW_SHADER", text="Shaders", icon="SHADING_RENDERED")


###############  TEXTURES WORLD PIE  ##############
def drawPieWorld(pie):
    
    box = pie.split().column()
    
    row = box.row(align=True).box()
    row.menu("NODE_MT_add", text="All Nodes", icon="ZOOM_IN")
    
    row_op=pie.operator("node.add_node", text="Sky", icon="LIGHT_SUN")
    row_op.type="ShaderNodeTexSky"
    row_op.use_transform = True
    
    box = pie.split().column()
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Background")
    row_op.type="ShaderNodeBackground"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Volume Scatter")
    row_op.type="ShaderNodeVolumeScatter"
    row_op.use_transform = True
    
    
    pie.operator("simple.hdri", text="Simple hdri", icon="URL")
    
    
    
    
###############  TEXTURES NODES PIE  ##############

def drawPieTextureNode(pie):
    
    ### Color ###
    box = pie.split().column()
    row = box.row(align=True)
    row.label(text="Color", icon="COLOR")
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="MIX RGB")
    row_op.type="TextureNodeMixRGB"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Curve RGB")
    row_op.type="TextureNodeCurveRGB"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="HUE / Sat")
    row_op.type="TextureNodeHueSaturation"
    row_op.use_transform = True
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Invert")
    row_op.type="TextureNodeInvert"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Separate RGB")
    row_op.type="TextureNodeDecompose"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Combine RGB")
    row_op.type="TextureNodeCompose"
    row_op.use_transform = True
    
    
    
    
    
    
    
    ### OUTPUT INPUT
    box = pie.split().column()
    row = box.row(align=True)
    row.label(text="Input/Output", icon="NODETREE")
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Output")
    row_op.type="TextureNodeOutput"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Viewer")
    row_op.type="TextureNodeViewer"
    row_op.use_transform = True
    box.separator()
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="IMG")
    row_op.type="TextureNodeImage"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Texture")
    row_op.type="TextureNodeTexture"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Curve Time")
    row_op.type="TextureNodeCurveTime"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Coordinate")
    row_op.type="TextureNodeCoordinate"
    row_op.use_transform = True
    
    
    ### Textures ####
    box = pie.split().column()
    row = box.row(align=True)
    row.label(text="Textures & pattern", icon="TEXTURE")
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Texture Clouds")
    row_op.type="TextureNodeTexClouds"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Noise")
    row_op.type="TextureNodeTexNoise"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Voronoi")
    row_op.type="TextureNodeTexVoronoi"
    row_op.use_transform = True
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Musgrave")
    row_op.type="TextureNodeTexMusgrave"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Distorded Noises")
    row_op.type="TextureNodeTexDistNoise"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Marble")
    row_op.type="TextureNodeTexMarble"
    row_op.use_transform = True
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Magic")
    row_op.type="TextureNodeTexMagic"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Stucci")
    row_op.type="TextureNodeTexStucci"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Wood")
    row_op.type="TextureNodeTexWood"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Blend")
    row_op.type="TextureNodeTexBlend"
    row_op.use_transform = True
    box.separator()
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Bricks")
    row_op.type="TextureNodeBricks"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Checker")
    row_op.type="TextureNodeChecker"
    row_op.use_transform = True
    
    
    
    ### CONVERTER
    box = pie.split().column()
    row = box.row(align=True)
    row.label(text="Converter", icon="RNssA")
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Color RAMP")
    row_op.type="TextureNodeValToRGB"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Math")
    row_op.type="TextureNodeMath"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="RGB to BW")
    row_op.type="TextureNodeRGBtoBW"
    row_op.use_transform = True
    
    
    ### Distort
    box = pie.split().column()
    row = box.row(align=True)
    row.label(text="Distort", icon="PARTICLE_DATA")
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Translate")
    row_op.type="TextureNodeTranslate"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Scale")
    row_op.type="TextureNodeScale"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Rotate")
    row_op.type="TextureNodeRotate"
    row_op.use_transform = True
    
    
    ### ALL NODE
    box = pie.split().column()
    row = box.row(align=True).box()
    row.menu("NODE_MT_add", text="All Nodes", icon="ZOOM_IN")
   

################ Compositing PIE #####################


def drawPieNodeComp(pie):
    
    #### Filter
    box = pie.split().column()
    row = box.row(align=True)
    row.label(text="Filter", icon="DRIVER")
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Blur")
    row_op.type="CompositorNodeBlur"
    row = box.row(align=True)
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Directional BLur")
    row_op.type="CompositorNodeDBlur"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Glare")
    row_op.type="CompositorNodeGlare"
    row_op.use_transform = True

    ### Input
    box = pie.split().column()
    row = box.row(align=True)
    row.label(text="Input", icon="NODETREE")
    row = box.row(align=True)    
    row_op=row.operator("node.add_node", text="Render Layers")
    row_op.type="CompositorNodeRLayers"
    row_op.use_transform = True
    row = box.row(align=True)    
    row_op=row.operator("node.add_node", text="RGB")
    row_op.type="CompositorNodeRGB"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Value")
    row_op.type="CompositorNodeValue"
    row_op.use_transform = True
    

    ### Distort
    box = pie.split().column()
    row = box.row(align=True)
    row.label(text="Distort", icon="RNDCURVE")
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Transform")
    row_op.type="CompositorNodeTransform"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Scale")
    row_op.type="CompositorNodeScale"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Rotate")
    row_op.type="CompositorNodeRotate"
    row_op.use_transform = True
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Lens Distortion")
    row_op.type="CompositorNodeLensdist"
    row_op.use_transform = True
    

    #### Color
    box = pie.split().column()
    row = box.row(align=True)
    row.label(text="Color", icon="COLOR")
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Alpha Over")
    row_op.type="CompositorNodeAlphaOver"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Mix RGB")
    row_op.type="CompositorNodeMixRGB"
    row_op.use_transform = True
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Curves RGB")
    row_op.type="CompositorNodeCurveRGB"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Color Balance")
    row_op.type="CompositorNodeColorBalance"
    row_op.use_transform = True
    

    #### Converter
    box = pie.split().column()
    row = box.row(align=True)
    row.label(text="Converter", icon="RNA")
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Color Ramp")
    row_op.type="CompositorNodeValToRGB"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Math")
    row_op.type="CompositorNodeMath"
    row_op.use_transform = True
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Set Alpha")
    row_op.type="CompositorNodeSetAlpha"
    row_op.use_transform = True
    
    box = pie.split().column().box()
    row = box.row(align=True)
    if bpy.context.space_data.show_backdrop == False:
        row.operator("toggle.backdrop", text="Backdrop", icon="COLOR_GREEN")
        
    else:
        row.operator("toggle.backdrop", text="Backdrop", icon="COLOR_RED")
    row.menu("NODE_MT_add", text="All Nodes", icon="ZOOM_IN")
    

    ##### Mask
    box = pie.split().column()
    row = box.row(align=True)
    row.label(text="Mask", icon="MOD_MASK")
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Ellipse Mask")
    row_op.type="CompositorNodeEllipseMask"
    row_op.use_transform = True
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Box Mask")
    row_op.type="CompositorNodeBoxMask"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Chroma Key")
    row_op.type="CompositorNodeChromaMatte"
    row_op.use_transform = True

	### Output    
    box = pie.split().column()
    row = box.row(align=True)
    row.label(text="Output", icon="NODETREE")
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="File Output")
    row_op.type="CompositorNodeOutputFile"
    row_op.use_transform = True
    row = box.row(align=True)
    row_op=row.operator("node.add_node", text="Viewer")
    row_op.type="CompositorNodeViewer"
    row_op.use_transform = True
    row_op=row.operator("node.add_node", text="Composite")
    row_op.type="CompositorNodeComposite"
    row_op.use_transform = True