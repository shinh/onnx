# SPDX-License-Identifier: Apache-2.0

import numpy as np  # type: ignore

import onnx

from ..base import Base
from . import expect


class Relu(Base):
    @staticmethod
    def export() -> None:
        node = onnx.helper.make_node(
            "Relu",
            inputs=["x"],
            outputs=["y"],
        )
        x = np.random.randn(3, 4, 5).astype(np.float32)
        y = np.clip(x, 0, np.inf)

        expect(node, inputs=[x], outputs=[y], name="test_relu")
