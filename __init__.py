# ##### BEGIN GPL LICENSE BLOCK ###############################################
#                                                                             #
#  This program is free software; you can redistribute it and/or              #
#  modify it under the terms of the GNU General Public License                #
#  as published by the Free Software Foundation; either version 2             #
#  of the License, or (at your option) any later version.                     #
#                                                                             #
#  This program is distributed in the hope that it will be useful,            #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
#  GNU General Public License for more details.                               #
#                                                                             #
#  You should have received a copy of the GNU General Public License          #
#  along with this program; if not, write to the Free Software Foundation,    #
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.         #
#                                                                             #
# ##### END GPL LICENSE BLOCK #################################################


bl_info = {
    "name": "Right Clic -- Pie Menu for Nodes",
    "description": "Pie menu on -- Right Clic -- to speed up the workflow in the node editor.",
    "author": "Lukrate, thanks to Wazou and Pistiwique from Blenderlounge for the help",
    "version": (0, 0, 7),
    "blender": (3, 0, 0),
    "location": "NODE_EDITOR",
    "warning": "Need Node Wrangler for all option.",
    "wiki_url": "",
    "category": "Node" }


import bpy
import os

from bl_ui.space_view3d import VIEW3D_MT_edit_mesh_context_menu


from . RMBS_pie import NODE_EDITOR_PIE
from . RMBS_OP import UseNodeMaterial
from . RMBS_OP import UseNodeWorld
from . RMBS_OP import UseNodeComp
from . RMBS_OP import AddMaterial
from . RMBS_OP import ToggleBackdrop
from . RMBS_OP import AddWorld
from . RMBS_OP import SimpleHdri
from . RMBS_OP import SetOriginToSelection
from . RMBS_OP import SHADER_OT_Load_shaders
from . RMBS_OP_Colors import SHADER_OT_Add_custom_color
from . RMBS_MT_Colors_menu import SHADER_color_Menu
from . RMBS_MT_Imperfections_menu import SHADER_MT_Imperfections_Menu

bctx = bpy.context
 

def draw_item(self, context):
    layout = self.layout
    layout.separator()
    layout.operator("wm.set_origin_to_selection")





######################## KEY MAP ######################
        
addon_keymaps = []
def register_keymaps():
    addon = bpy.context.window_manager.keyconfigs.addon
    km = addon.keymaps.new(name="Node Generic", space_type='NODE_EDITOR', region_type='WINDOW')  
    kmi = km.keymap_items.new("wm.call_menu_pie",'RIGHTMOUSE', 'PRESS')
    kmi.properties.name = "pie.shader_selection"
    addon_keymaps.append(km)
 
def unregister_keymaps():
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        for kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()

classes = (
    NODE_EDITOR_PIE,
    UseNodeMaterial,
    UseNodeWorld,
    UseNodeComp,
    AddMaterial,
    ToggleBackdrop,
    AddWorld,
    SimpleHdri,
    SetOriginToSelection,
    SHADER_OT_Add_custom_color,
    SHADER_color_Menu,
    SHADER_MT_Imperfections_Menu,
    SHADER_OT_Load_shaders
)

def register():
    register_keymaps()
    for cls in classes:
        bpy.utils.register_class(cls)
    
    VIEW3D_MT_edit_mesh_context_menu.prepend(draw_item)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    VIEW3D_MT_edit_mesh_context_menu.remove(draw_item)


if __name__ == "__main__":
    register()
    bpy.ops.shader.load_shaders()
    

