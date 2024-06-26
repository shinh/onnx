# SPDX-License-Identifier: Apache-2.0

import numpy as np  # type: ignore

import onnx

from ..base import Base
from . import expect


class SingleRelu(Base):
    @staticmethod
    def export() -> None:

        node = onnx.helper.make_node("Relu", ["x"], ["y"], name="test")
        graph = onnx.helper.make_graph(
            nodes=[node],
            name="SingleRelu",
            inputs=[
                onnx.helper.make_tensor_value_info("x", onnx.TensorProto.FLOAT, [1, 2])
            ],
            outputs=[
                onnx.helper.make_tensor_value_info("y", onnx.TensorProto.FLOAT, [1, 2])
            ],
        )
        model = onnx.helper.make_model_gen_version(
            graph,
            producer_name="backend-test",
            opset_imports=[onnx.helper.make_opsetid("", 9)],
        )

        x = np.random.randn(1, 2).astype(np.float32)
        y = np.maximum(x, 0)

        expect(model, inputs=[x], outputs=[y], name="test_single_relu_model")
