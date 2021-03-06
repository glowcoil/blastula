from ..umog_node import *
from ...engine import types, engine
import bpy

class GetMeshNode(bpy.types.Node, UMOGNode):
    bl_idname = "umog_GetMeshNode"
    bl_label = "Get Mesh Node"

    mesh_name = bpy.props.StringProperty()

    def init(self, context):
        self.outputs.new("MeshSocketType", "out")
        super().init(context)

    def draw_buttons(self, context, layout):
        layout.prop_search(self, "mesh_name", bpy.data, "meshes", icon="MESH_CUBE", text="")

    def get_operation(self, input_types):
        return engine.Operation(
            engine.CONST,
            [types.Mesh()],
            [types.Mesh()],
            [])

    def get_default_value(self, index, argument_type):
        bpy.data.meshes[self.mesh_name].update(calc_tessface=True)
        return bpy.data.meshes[self.mesh_name]

    def update(self):
        pass
