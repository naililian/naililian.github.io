"""Node attribute documentation models.

Use these classes and docstrings so mkdocstrings can render a clear
API-style reference for node attributes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

__all__ = ["NodeAttribute", "NodeSpec", "color_card_example"]


@dataclass
class NodeAttribute:
	"""Represents a node attribute and its nested subattributes.

	Args:
		name: Full attribute name, e.g. ``ColorizeHsl``.
		type_name: Attribute type, e.g. ``Attribute`` or ``DoubleAttr``.
		path: Full path, e.g. ``Top/HS_Color_A``.
		subattributes: Nested attributes.
	"""

	name: str
	type_name: str
	path: str
	subattributes: List["NodeAttribute"] = field(default_factory=list)


@dataclass
class NodeSpec:
	"""Documentation structure for a node and its attributes.

	Example:
		>>> node = NodeSpec(
		...     name="My_Nodo",
		...     node_type="COLOR_CARD",
		...     attributes=[
		...         NodeAttribute(
		...             name="ColorizeHsl",
		...             type_name="Attribute",
		...             path="Top/HS_Color_A",
		...             subattributes=[
		...                 NodeAttribute(
		...                     name="ColorizeHsl.HUE",
		...                     type_name="DoubleAttr",
		...                     path="Top/HS_Color_A",
		...                 ),
		...                 NodeAttribute(
		...                     name="ColorizeHsl.SATURATION",
		...                     type_name="DoubleAttr",
		...                     path="Top/HS_Color_A",
		...                 ),
		...                 NodeAttribute(
		...                     name="ColorizeHsl.LIGHTNESS",
		...                     type_name="DoubleAttr",
		...                     path="Top/HS_Color_A",
		...                 ),
		...             ],
		...         )
		...     ],
		... )

	Args:
		name: Node name to display.
		node_type: Node type string, e.g. ``COLOR_CARD``.
		attributes: Top-level attributes for the node.
	"""

	name: str
	node_type: str
	attributes: List[NodeAttribute] = field(default_factory=list)


def color_card_example() -> NodeSpec:
	"""Return a sample node spec for documentation.

	This mirrors the structure you described:

	- Attribute: Attribute(Top/HS_Color_A, ColorizeHsl)
	  - Subattributes: DoubleAttr(Top/HS_Color_A, ColorizeHsl.HUE)
	  - Subattributes: DoubleAttr(Top/HS_Color_A, ColorizeHsl.SATURATION)
	  - Subattributes: DoubleAttr(Top/HS_Color_A, ColorizeHsl.LIGHTNESS)
	"""

	return NodeSpec(
		name="My_Nodo",
		node_type="COLOR_CARD",
		attributes=[
			NodeAttribute(
				name="ColorizeHsl",
				type_name="Attribute",
				path="Top/HS_Color_A",
				subattributes=[
					NodeAttribute(
						name="ColorizeHsl.HUE",
						type_name="DoubleAttr",
						path="Top/HS_Color_A",
					),
					NodeAttribute(
						name="ColorizeHsl.SATURATION",
						type_name="DoubleAttr",
						path="Top/HS_Color_A",
					),
					NodeAttribute(
						name="ColorizeHsl.LIGHTNESS",
						type_name="DoubleAttr",
						path="Top/HS_Color_A",
					),
				],
			)
		],
	)
