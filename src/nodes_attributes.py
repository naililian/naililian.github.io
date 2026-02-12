"""Referencia estatica de nodos y atributos con tablas."""

__all__ = ["nodo_color_card", "data"]


# Datos estructurados de nodos
NODES_DATA = {
    "Color_Card": {
        "name": "Color_Card",
        "type": "COLOR_CARD",
        "attributes": [
            {
                "keyword": "ColorizeHsl",
                "type": "Attribute",
                "subattributes": [
                    {"keyword": "ColorizeHsl.HUE", "type": "DoubleAttr"},
                    {"keyword": "ColorizeHsl.SATURATION", "type": "DoubleAttr"},
                    {"keyword": "ColorizeHsl.LIGHTNESS", "type": "DoubleAttr"},
                ]
            }
        ]
    }
}


def data(node_type: str) -> dict:
    """Retorna los datos estructurados de un nodo.

    Args:
        node_type: Tipo de nodo (ej: "Color_Card")

    Returns:
        Diccionario con la estructura del nodo.

    Example:
        >>> node_info = data("Color_Card")
        >>> print(node_info["type"])
        COLOR_CARD
    """
    return NODES_DATA.get(node_type, {})


def nodo_color_card() -> None:
    """## Color_Card

    **Tipo de Nodo:** COLOR_CARD

    | Keyword | Type | Sub-attributes |
    |---------|------|-----------------|
    | ColorizeHsl | Attribute | ColorizeHsl.HUE (DoubleAttr)<br>ColorizeHsl.SATURATION (DoubleAttr)<br>ColorizeHsl.LIGHTNESS (DoubleAttr) |
    """
    pass
