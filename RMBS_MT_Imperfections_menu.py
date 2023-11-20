import bpy

class SHADER_MT_Imperfections_Menu(bpy.types.Menu):
    bl_label = "Imperfections Menu"
    bl_idname = "SHADER_MT_Imperfections_menu"
    bl_info = "Menu presets"
    
    imperfections = [
        "Impact",
        "Scratch",
        "Scuff",
        "Grunge"
    ]

    masks = [
        "Curvature",
        "Edge Mask",
        "AO noise",
    ]

    uv = [
        "Distord",
        "Top or Bottom",
        "Untiling",
        "Blur",
        "Directional Blur"
    ]

    shaders = [
        "Vitro Art Glass 2",
    ]

    textures = [
        "Polygon",
    ]


    def draw(self, context):
        layout = self.layout
        mr = layout.row(align=True)
        c = mr.column(align=True)
        c.label(text="Imperfections")
        c.separator()
        for k in self.imperfections:
            r = c.row()
            r.operator("shader.load_shaders", text=k).name = k
        
        c = mr.column(align=True)
        c.label(text="Masks")
        c.separator()
        for k in self.masks:
            r = c.row()
            r.operator("shader.load_shaders", text=k).name = k
        
        c = mr.column(align=True)
        c.label(text="UV")
        c.separator()
        for k in self.uv:
            r = c.row()
            r.operator("shader.load_shaders", text=k).name = k
        
        c = mr.column(align=True)
        c.label(text="Shaders")
        c.separator()
        for k in self.shaders:
            r = c.row()
            r.operator("shader.load_shaders", text=k).name = k
        
        c = mr.column(align=True)
        c.label(text="Textures")
        c.separator()
        for k in self.textures:
            r = c.row()
            r.operator("shader.load_shaders", text=k).name = k