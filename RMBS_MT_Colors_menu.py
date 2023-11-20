import bpy
import os




class SHADER_color_Menu(bpy.types.Menu):
    bl_label = "Colors Menu"
    bl_idname = "SHADER_MT_colors_menu"
    bl_info = "Menu color presets"

    metalColors = {
        "Iron": (0.560,0.570,0.580),
        "Silver": (0.972,0.960,0.915),
        "Aluminium": (0.913,0.921,0.925),
        "Gold": (1.000, 0.766, 0.336),
        "Copper": (0.955,0.637,0.538),
        "Chromium": (0.550,0.556,0.554),
        "Nickel": (0.660,0.609,0.526),
        "Titanium": (0.542,0.497,0.449),
        "Cobalt": (0.662,0.655,0.634),
    }

    gemStoneColors = {
        "Ruby": (156/256, 19/256, 30/256),
        "Moonstone": (58/256,465/256,195/256),
        "Lapis Lazuli": (41/256,96/256,156/256),
    }

    def draw(self, context):
        layout = self.layout
        mr = layout.row(align=True)
        c = mr.column(align=True)
        
        c.label(text="Metal")
        c.separator()
        for k in self.metalColors:
            r = c.row()
            r.operator("shader.add_color_operator", text=k).color = self.metalColors[k]
        
        c = mr.column(align=True)
        c.label(text="Gemstone")
        c.separator()
        for k in self.gemStoneColors:
            r = c.row()
            r.operator("shader.add_color_operator", text=k).color = self.gemStoneColors[k]
