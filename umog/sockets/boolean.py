import bpy
from . import UMOGSocket

class BooleanSocket(bpy.types.NodeSocket, UMOGSocket):
    bl_idname = 'BooleanSocketType'
    bl_label = 'Boolean Socket'

    def init(self, context):
        pass

    def draw_color(self, context, node):
        return (0, 0, 1, 0.5)
