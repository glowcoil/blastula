from ..umog_node import *
from ...engine import types, engine
import bpy

class AndNode(bpy.types.Node, UMOGNode):
    bl_idname = "umog_AndNode"
    bl_label = "And Node"

    def init(self, context):
        self.inputs.new("BooleanSocketType", "a")
        self.inputs.new("BooleanSocketType", "b")
        self.outputs.new("BooleanSocketType", "out")
        super().init(context)

    def get_operation(self, input_types):
        output_types = types.binary_scalar(input_types[0], input_types[1])

        return engine.Operation(
            engine.AND,
            input_types,
            output_types,
            [])

    def update(self):
        pass
