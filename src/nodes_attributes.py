"""Attributes of Nodes from Toon Boom Harmony"""

__all__ = ["Hue_Saturation_Attributtes","Colour_Card_Attributtes"]



def Hue_Saturation_Attributtes() -> None:
    """## Hue Saturation Node

    **Tipo de Nodo:** COLOR_CARD

    Keyword| Keyword | Type | Sub-attributes |
    |---------|------|-----------------|
    | MasterRangeColor | Attribute |  |
    | GreenRangeColor | Attribute |  |
    | RedRangeColor | Attribute |  |
    | BlueRangeColor | Attribute |  |
    | CyanRangeColor | Attribute |  |
    | MagentaRangeColor | Attribute |  |
    | YellowColorizeEnableRangeColor | BoolAttr |  |
    | ColorizeHsl | Attribute | ColorizeHsl.HUE (DoubleAttr)<br>ColorizeHsl.SATURATION (DoubleAttr)<br>ColorizeHsl.LIGHTNESS (DoubleAttr) |
    | ResetRed | Attribute |  |
    | ResetGreen | Attribute |  |
    | ResetBlue | Attribute |  |
    | ResetCyan | Attribute |  |
    | ResetYellow | Attribute |  |
    | INVERT_MATTE_PORT | BoolAttr |  |
    """
    pass

def Colour_Card_Attributtes() -> None:
    """## Colour Card Node

    **Tipo de Nodo:** COLOR_CARD

    Keyword| Keyword | Type | Sub-attributes |
    |---------|------|-----------------|
    | DEPTH | IntAttr |  |
    | OFFSET_Z | DoubleAttr |  |
    | COLOR | ColorAttr | COLOR.RED (IntAttr)<br>COLOR.GREEN (IntAttr)<br>COLOR.BLUE (IntAttr)<br>COLOR.ALPHA (IntAttr)<br>COLOR.PREFERRED_UI (EnumAttr)<br> |
    | INVERT_MATTE_PORT | Attribute |  |

    """
    pass
