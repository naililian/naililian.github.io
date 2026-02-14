# Colour-Card

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | DEPTH |
| Main |  | DoubleAttr | OFFSET_Z |
| Main |  | ColorAttr | COLOR |
| Sub | COLOR | IntAttr | COLOR.RED |
| Sub | COLOR | IntAttr | COLOR.GREEN |
| Sub | COLOR | IntAttr | COLOR.BLUE |
| Sub | COLOR | IntAttr | COLOR.ALPHA |
| Sub | COLOR | EnumAttr | COLOR.PREFERRED_UI |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


# Composite

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | COMPOSITE_MODE |
| Main |  | BoolAttr | FLATTEN_OUTPUT |
| Main |  | BoolAttr | FLATTEN_VECTOR |
| Main |  | BoolAttr | COMPOSITE_2D |
| Main |  | BoolAttr | COMPOSITE_3D |
| Main |  | EnumAttr | OUTPUT_Z |
| Main |  | IntAttr | OUTPUT_Z_INPUT_PORT |
| Main |  | BoolAttr | APPLY_FOCUS |
| Main |  | DoubleAttr | MULTIPLIER |
| Main |  | TextAttr | TVG_PALETTE |
| Main |  | BoolAttr | MERGE_VECTOR |


# Drawing

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | ENABLE_3D |
| Main |  | BoolAttr | FACE_CAMERA |
| Main |  | EnumAttr | CAMERA_ALIGNMENT |
| Main |  | Pos3DAttr | OFFSET |
| Sub | OFFSET | BoolAttr | OFFSET/SEPARATE |
| Sub | OFFSET | DoubleAttr | OFFSET.X |
| Sub | OFFSET | DoubleAttr | OFFSET.Y |
| Sub | OFFSET | DoubleAttr | OFFSET.Z |
| Sub | OFFSET | Attribute | OFFSET.3DPATH |
| Main |  | Attribute | SCALE |
| Sub | SCALE | BoolAttr | SCALE/SEPARATE |
| Sub | SCALE | BoolAttr | SCALE/IN_FIELDS |
| Sub | SCALE | DoubleAttr | SCALE.XY |
| Sub | SCALE | DoubleAttr | SCALE.X |
| Sub | SCALE | DoubleAttr | SCALE.Y |
| Sub | SCALE | DoubleAttr | SCALE.Z |
| Main |  | Attribute | ROTATION |
| Sub | ROTATION | BoolAttr | ROTATION/SEPARATE |
| Sub | ROTATION | DoubleAttr | ROTATION.ANGLEX |
| Sub | ROTATION | DoubleAttr | ROTATION.ANGLEY |
| Sub | ROTATION | DoubleAttr | ROTATION.ANGLEZ |
| Sub | ROTATION | Attribute | ROTATION.QUATERNIONPATH |
| Main |  | Attribute | ANGLE |
| Main |  | DoubleAttr | SKEW |
| Main |  | Pos3DAttr | PIVOT |
| Sub | PIVOT | BoolAttr | PIVOT/SEPARATE |
| Sub | PIVOT | DoubleAttr | PIVOT.X |
| Sub | PIVOT | DoubleAttr | PIVOT.Y |
| Sub | PIVOT | DoubleAttr | PIVOT.Z |
| Main |  | Pos3DAttr | SPLINE_OFFSET |
| Sub | SPLINE_OFFSET | BoolAttr | SPLINE_OFFSET/SEPARATE |
| Sub | SPLINE_OFFSET | DoubleAttr | SPLINE_OFFSET.X |
| Sub | SPLINE_OFFSET | DoubleAttr | SPLINE_OFFSET.Y |
| Sub | SPLINE_OFFSET | DoubleAttr | SPLINE_OFFSET.Z |
| Main |  | BoolAttr | IGNORE_PARENT_PEG_SCALING |
| Main |  | BoolAttr | DISABLE_FIELD_RENDERING |
| Main |  | IntAttr | DEPTH |
| Main |  | BoolAttr | ENABLE_MIN_MAX_ANGLE |
| Main |  | DoubleAttr | MIN_ANGLE |
| Main |  | DoubleAttr | MAX_ANGLE |
| Main |  | BoolAttr | NAIL_FOR_CHILDREN |
| Main |  | BoolAttr | IK_HOLD_ORIENTATION |
| Main |  | BoolAttr | IK_HOLD_X |
| Main |  | BoolAttr | IK_HOLD_Y |
| Main |  | BoolAttr | IK_EXCLUDED |
| Main |  | BoolAttr | IK_CAN_ROTATE |
| Main |  | BoolAttr | IK_CAN_TRANSLATE_X |
| Main |  | BoolAttr | IK_CAN_TRANSLATE_Y |
| Main |  | DoubleAttr | IK_BONE_X |
| Main |  | DoubleAttr | IK_BONE_Y |
| Main |  | DoubleAttr | IK_STIFFNESS |
| Main |  | DrawingAttr | DRAWING |
| Sub | DRAWING | BoolAttr | DRAWING/ELEMENT_MODE |
| Sub | DRAWING | ElementAttr | DRAWING/ELEMENT |
| Sub | DRAWING | Attribute | DRAWING.CUSTOM_NAME |
| Main |  | BoolAttr | READ_OVERLAY |
| Main |  | BoolAttr | READ_LINE_ART |
| Main |  | BoolAttr | READ_COLOR_ART |
| Main |  | BoolAttr | READ_UNDERLAY |
| Main |  | EnumAttr | OVERLAY_ART_DRAWING_MODE |
| Main |  | EnumAttr | LINE_ART_DRAWING_MODE |
| Main |  | EnumAttr | COLOR_ART_DRAWING_MODE |
| Main |  | EnumAttr | UNDERLAY_ART_DRAWING_MODE |
| Main |  | BoolAttr | PENCIL_LINE_DEFORMATION_PRESERVE_THICKNESS |
| Main |  | EnumAttr | PENCIL_LINE_DEFORMATION_QUALITY |
| Main |  | IntAttr | PENCIL_LINE_DEFORMATION_SMOOTH |
| Main |  | DoubleAttr | PENCIL_LINE_DEFORMATION_FIT_ERROR |
| Main |  | BoolAttr | READ_COLOR |
| Main |  | BoolAttr | READ_TRANSPARENCY |
| Main |  | EnumAttr | COLOR_TRANSFORMATION |
| Main |  | TextAttr | COLOR_SPACE |
| Main |  | EnumAttr | APPLY_MATTE_TO_COLOR |
| Main |  | BoolAttr | ENABLE_LINE_TEXTURE |
| Main |  | EnumAttr | ANTIALIASING_QUALITY |
| Main |  | DoubleAttr | ANTIALIASING_EXPONENT |
| Main |  | DoubleAttr | OPACITY |
| Main |  | EnumAttr | TEXTURE_FILTER |
| Main |  | BoolAttr | ADJUST_PENCIL_THICKNESS |
| Main |  | BoolAttr | NORMAL_LINE_ART_THICKNESS |
| Main |  | EnumAttr | ZOOM_INDEPENDENT_LINE_ART_THICKNESS |
| Main |  | DoubleAttr | MULT_LINE_ART_THICKNESS |
| Main |  | DoubleAttr | ADD_LINE_ART_THICKNESS |
| Main |  | DoubleAttr | MIN_LINE_ART_THICKNESS |
| Main |  | DoubleAttr | MAX_LINE_ART_THICKNESS |
| Main |  | EnumAttr | USE_DRAWING_PIVOT |
| Main |  | BoolAttr | FLIP_HOR |
| Main |  | BoolAttr | FLIP_VERT |
| Main |  | BoolAttr | TURN_BEFORE_ALIGNMENT |
| Main |  | BoolAttr | NO_CLIPPING |
| Main |  | IntAttr | X_CLIP_FACTOR |
| Main |  | IntAttr | Y_CLIP_FACTOR |
| Main |  | EnumAttr | ALIGNMENT_RULE |
| Main |  | DoubleAttr | MORPHING_VELO |
| Main |  | BoolAttr | CAN_ANIMATE |
| Main |  | BoolAttr | TILE_HORIZONTAL |
| Main |  | BoolAttr | TILE_VERTICAL |
| Main |  | DoubleAttr | FRAMERATE |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


# Peg

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | ENABLE_3D |
| Main |  | BoolAttr | FACE_CAMERA |
| Main |  | EnumAttr | CAMERA_ALIGNMENT |
| Main |  | Pos3DAttr | POSITION |
| Sub | POSITION | BoolAttr | POSITION/SEPARATE |
| Sub | POSITION | DoubleAttr | POSITION.X |
| Sub | POSITION | DoubleAttr | POSITION.Y |
| Sub | POSITION | DoubleAttr | POSITION.Z |
| Sub | POSITION | Attribute | POSITION.3DPATH |
| Main |  | Attribute | SCALE |
| Sub | SCALE | BoolAttr | SCALE/SEPARATE |
| Sub | SCALE | BoolAttr | SCALE/IN_FIELDS |
| Sub | SCALE | DoubleAttr | SCALE.XY |
| Sub | SCALE | DoubleAttr | SCALE.X |
| Sub | SCALE | DoubleAttr | SCALE.Y |
| Sub | SCALE | DoubleAttr | SCALE.Z |
| Main |  | Attribute | ROTATION |
| Sub | ROTATION | BoolAttr | ROTATION/SEPARATE |
| Sub | ROTATION | DoubleAttr | ROTATION.ANGLEX |
| Sub | ROTATION | DoubleAttr | ROTATION.ANGLEY |
| Sub | ROTATION | DoubleAttr | ROTATION.ANGLEZ |
| Sub | ROTATION | Attribute | ROTATION.QUATERNIONPATH |
| Main |  | Attribute | ANGLE |
| Main |  | DoubleAttr | SKEW |
| Main |  | Pos3DAttr | PIVOT |
| Sub | PIVOT | BoolAttr | PIVOT/SEPARATE |
| Sub | PIVOT | DoubleAttr | PIVOT.X |
| Sub | PIVOT | DoubleAttr | PIVOT.Y |
| Sub | PIVOT | DoubleAttr | PIVOT.Z |
| Main |  | Pos3DAttr | SPLINE_OFFSET |
| Sub | SPLINE_OFFSET | BoolAttr | SPLINE_OFFSET/SEPARATE |
| Sub | SPLINE_OFFSET | DoubleAttr | SPLINE_OFFSET.X |
| Sub | SPLINE_OFFSET | DoubleAttr | SPLINE_OFFSET.Y |
| Sub | SPLINE_OFFSET | DoubleAttr | SPLINE_OFFSET.Z |
| Main |  | BoolAttr | IGNORE_PARENT_PEG_SCALING |
| Main |  | BoolAttr | DISABLE_FIELD_RENDERING |
| Main |  | IntAttr | DEPTH |
| Main |  | BoolAttr | ENABLE_MIN_MAX_ANGLE |
| Main |  | DoubleAttr | MIN_ANGLE |
| Main |  | DoubleAttr | MAX_ANGLE |
| Main |  | BoolAttr | NAIL_FOR_CHILDREN |
| Main |  | BoolAttr | IK_HOLD_ORIENTATION |
| Main |  | BoolAttr | IK_HOLD_X |
| Main |  | BoolAttr | IK_HOLD_Y |
| Main |  | BoolAttr | IK_EXCLUDED |
| Main |  | BoolAttr | IK_CAN_ROTATE |
| Main |  | BoolAttr | IK_CAN_TRANSLATE_X |
| Main |  | BoolAttr | IK_CAN_TRANSLATE_Y |
| Main |  | DoubleAttr | IK_BONE_X |
| Main |  | DoubleAttr | IK_BONE_Y |
| Main |  | DoubleAttr | IK_STIFFNESS |
| Main |  | BoolAttr | GROUP_AT_NETWORK_BUILDING |
| Main |  | BoolAttr | ADD_COMPOSITE_TO_GROUP |


# Write

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | EXPORT_TO_MOVIE |
| Main |  | TextAttr | DRAWING_NAME |
| Main |  | TextAttr | MOVIE_PATH |
| Main |  | TextAttr | MOVIE_FORMAT |
| Main |  | TextAttr | MOVIE_AUDIO |
| Main |  | TextAttr | MOVIE_VIDEO |
| Main |  | TextAttr | MOVIE_VIDEOAUDIO |
| Main |  | IntAttr | LEADING_ZEROS |
| Main |  | IntAttr | START |
| Main |  | TextAttr | DRAWING_TYPE |
| Main |  | Attribute | ENABLING |
| Sub | ENABLING | EnumAttr | ENABLING.FILTER |
| Sub | ENABLING | TextAttr | ENABLING.FILTER_NAME |
| Sub | ENABLING | IntAttr | ENABLING.FILTER_RES_X |
| Sub | ENABLING | IntAttr | ENABLING.FILTER_RES_Y |
| Main |  | BoolAttr | SCRIPT_MOVIE |
| Main |  | TextAttr | SCRIPT_EDITOR |
| Main |  | TextAttr | COLOR_SPACE |
| Main |  | EnumAttr | COMPOSITE_PARTITIONING |
| Main |  | DoubleAttr | Z_PARTITION_RANGE |
| Main |  | BoolAttr | CLEAN_UP_PARTITION_FOLDERS |

