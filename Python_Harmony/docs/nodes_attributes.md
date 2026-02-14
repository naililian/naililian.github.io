You'll find all the information about nodes attributes.

# Articulation Node

Type: **ArticulationModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | influenceType |
| Main |  | DoubleAttr | influenceFade |
| Main |  | BoolAttr | symmetric |
| Main |  | DoubleAttr | transversalRadius |
| Main |  | DoubleAttr | transversalRadiusRight |
| Main |  | DoubleAttr | longitudinalRadiusBegin |
| Main |  | DoubleAttr | longitudinalRadius |
| Main |  | DoubleAttr | restRadius |
| Main |  | DoubleAttr | restingOrientation |
| Main |  | DoubleAttr | restBias |
| Main |  | DoubleAttr | radius |
| Main |  | DoubleAttr | orientation |
| Main |  | DoubleAttr | bias |


# Auto-Muscle Node

Type: **AutoMuscleModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | enableLeft |
| Main |  | DoubleAttr | leftStart |
| Main |  | DoubleAttr | leftSpan |
| Main |  | DoubleAttr | leftAmplitude |
| Main |  | BoolAttr | enableRight |
| Main |  | BoolAttr | symmetric |
| Main |  | DoubleAttr | rightStart |
| Main |  | DoubleAttr | rightSpan |
| Main |  | DoubleAttr | rightAmplitude |


# Blending Node

Type: **BLEND_MODE_MODULE**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | BLEND_MODE |
| Main |  | EnumAttr | CLAMPING_MODE |
| Main |  | EnumAttr | FLASH_BLEND_MODE |


# Bone Node

Type: **BendyBoneModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | influenceType |
| Main |  | DoubleAttr | influenceFade |
| Main |  | BoolAttr | symmetric |
| Main |  | DoubleAttr | transversalRadius |
| Main |  | DoubleAttr | transversalRadiusRight |
| Main |  | DoubleAttr | longitudinalRadiusBegin |
| Main |  | DoubleAttr | longitudinalRadius |
| Main |  | Pos2DAttr | restOffset |
| Sub | restOffset | BoolAttr | restOffset/SEPARATE |
| Sub | restOffset | DoubleAttr | restOffset.X |
| Sub | restOffset | DoubleAttr | restOffset.Y |
| Main |  | DoubleAttr | restOrientation |
| Main |  | DoubleAttr | restRadius |
| Main |  | DoubleAttr | restBias |
| Main |  | DoubleAttr | restLength |
| Main |  | Pos2DAttr | offset |
| Sub | offset | BoolAttr | offset/SEPARATE |
| Sub | offset | DoubleAttr | offset.X |
| Sub | offset | DoubleAttr | offset.Y |
| Sub | offset | Attribute | offset.2DPOINT |
| Main |  | DoubleAttr | orientation |
| Main |  | DoubleAttr | radius |
| Main |  | DoubleAttr | bias |
| Main |  | DoubleAttr | length |


# Colour-Card Node

Type: **COLOR_CARD**

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


# Composite Node

Type: **COMPOSITE**

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


# Composite-Generic Node

Type: **COMPOSITE_GENERIC**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | COLOR_OPERATION |
| Main |  | EnumAttr | CLAMPING_MODE |
| Main |  | DoubleAttr | INTENSITY_COLOR_RED |
| Main |  | DoubleAttr | INTENSITY_COLOR_BLUE |
| Main |  | DoubleAttr | INTENSITY_COLOR_GREEN |
| Main |  | DoubleAttr | OPACITY |
| Main |  | EnumAttr | ALPHA_OPERATION |
| Main |  | EnumAttr | OUTPUT_Z |
| Main |  | IntAttr | OUTPUT_Z_INPUT_PORT |


# Constraint-Switch Node

Type: **Switch**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | IntAttr | GATENUM |
| Main |  | Pos2DAttr | UIOFFSETPOS |
| Sub | UIOFFSETPOS | BoolAttr | UIOFFSETPOS/SEPARATE |
| Sub | UIOFFSETPOS | DoubleAttr | UIOFFSETPOS.X |
| Sub | UIOFFSETPOS | DoubleAttr | UIOFFSETPOS.Y |
| Main |  | DoubleAttr | UISCALE |


# Curve Node

Type: **CurveModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | localReferential |
| Main |  | EnumAttr | influenceType |
| Main |  | DoubleAttr | influenceFade |
| Main |  | BoolAttr | symmetric |
| Main |  | DoubleAttr | transversalRadius |
| Main |  | DoubleAttr | transversalRadiusRight |
| Main |  | DoubleAttr | longitudinalRadiusBegin |
| Main |  | DoubleAttr | longitudinalRadius |
| Main |  | BoolAttr | closePath |
| Main |  | DoubleAttr | restLength0 |
| Main |  | DoubleAttr | restingOrientation0 |
| Main |  | Pos2DAttr | restingOffset |
| Sub | restingOffset | BoolAttr | restingOffset/SEPARATE |
| Sub | restingOffset | DoubleAttr | restingOffset.X |
| Sub | restingOffset | DoubleAttr | restingOffset.Y |
| Main |  | DoubleAttr | restLength1 |
| Main |  | DoubleAttr | restingOrientation1 |
| Main |  | DoubleAttr | Length0 |
| Main |  | DoubleAttr | orientation0 |
| Main |  | Pos2DAttr | offset |
| Sub | offset | BoolAttr | offset/SEPARATE |
| Sub | offset | DoubleAttr | offset.X |
| Sub | offset | DoubleAttr | offset.Y |
| Sub | offset | Attribute | offset.2DPOINT |
| Main |  | DoubleAttr | Length1 |
| Main |  | DoubleAttr | orientation1 |


# Cutter Node

Type: **CUTTER**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERTED |


# Deformation-AutoFold Node

Type: **AutoFoldModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | enable |
| Main |  | DoubleAttr | length |


# Deformation-Fold Node

Type: **FoldModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | enable |
| Main |  | DoubleAttr | t |
| Main |  | DoubleAttr | tBefore |
| Main |  | DoubleAttr | tAfter |
| Main |  | DoubleAttr | angle |
| Main |  | DoubleAttr | length |


# Deformation-Scale Node

Type: **DeformationScaleModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | enableLeft |
| Main |  | DoubleAttr | leftFadeIn |
| Main |  | DoubleAttr | leftFadeOut |
| Main |  | DoubleAttr | leftStart |
| Main |  | DoubleAttr | leftSpan |
| Main |  | DoubleAttr | leftScale0 |
| Main |  | DoubleAttr | leftScale1 |
| Main |  | DoubleAttr | leftHandlePosition0 |
| Main |  | DoubleAttr | leftHandlePosition1 |
| Main |  | DoubleAttr | leftHandleScale0 |
| Main |  | DoubleAttr | leftHandleScale1 |
| Main |  | BoolAttr | enableRight |
| Main |  | BoolAttr | symmetric |
| Main |  | DoubleAttr | rightFadeIn |
| Main |  | DoubleAttr | rightFadeOut |
| Main |  | DoubleAttr | rightStart |
| Main |  | DoubleAttr | rightSpan |
| Main |  | DoubleAttr | rightScale0 |
| Main |  | DoubleAttr | rightScale1 |
| Main |  | DoubleAttr | rightHandlePosition0 |
| Main |  | DoubleAttr | rightHandlePosition1 |
| Main |  | DoubleAttr | rightHandleScale0 |
| Main |  | DoubleAttr | rightHandleScale1 |


# Deformation-Switch Node

Type: **DeformationSwitchModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Attribute | vectorQuality |
| Sub | vectorQuality | EnumAttr | vectorQuality.type |
| Sub | vectorQuality | EnumAttr | vectorQuality.level |
| Main |  | DoubleAttr | fadeExponent |
| Main |  | BoolAttr | fadeInside |
| Main |  | IntAttr | enableDeformation |
| Main |  | IntAttr | chainSelectionReference |


# Deformation-Uniform-Scale Node

Type: **DeformationUniformScaleModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | scale |


# Deformation-Wave Node

Type: **DeformationWaveModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | enableLeft |
| Main |  | DoubleAttr | leftStart |
| Main |  | DoubleAttr | leftSpan |
| Main |  | DoubleAttr | leftOffsetT |
| Main |  | DoubleAttr | leftAmplitude |
| Main |  | DoubleAttr | leftOffset |
| Main |  | DoubleAttr | leftPeriod |
| Main |  | BoolAttr | enableRight |
| Main |  | BoolAttr | symmetric |
| Main |  | DoubleAttr | rightStart |
| Main |  | DoubleAttr | rightSpan |
| Main |  | DoubleAttr | rightOffsetT |
| Main |  | DoubleAttr | rightAmplitude |
| Main |  | DoubleAttr | rightOffset |
| Main |  | DoubleAttr | rightPeriod |


# Deformation_Composite Node

Type: **DeformationCompositeModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | outputMatrixOnly |
| Main |  | BoolAttr | outputSelectedOnly |
| Main |  | EnumAttr | outputKinematicChainSelector |
| Main |  | IntAttr | outputKinematicChain |


# Deformation_Root Node

Type: **DeformationRootModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Attribute | deformationQuality |
| Sub | deformationQuality | EnumAttr | deformationQuality.type |
| Sub | deformationQuality | EnumAttr | deformationQuality.level |


# Drawing Node

Type: **READ**

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


# Dynamic-Spring Node

Type: **DynamicSpring**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | BoolAttr | MATCHEXPOSURES |
| Main |  | DoubleAttr | TENSIONX |
| Main |  | DoubleAttr | INERTIAX |
| Main |  | DoubleAttr | TENSIONY |
| Main |  | DoubleAttr | INERTIAY |
| Main |  | DoubleAttr | TENSIONZ |
| Main |  | DoubleAttr | INERTIAZ |
| Main |  | DoubleAttr | TENSIONSCALE |
| Main |  | DoubleAttr | INERTIASCALE |
| Main |  | DoubleAttr | TENSIONSKEW |
| Main |  | DoubleAttr | INERTIASKEW |
| Main |  | DoubleAttr | TENSIONROTATE |
| Main |  | DoubleAttr | INERTIAROTATE |
| Main |  | DoubleAttr | PIGNORE |
| Main |  | TextAttr | PARENTNAME |


# Free-Form-Deformer Node

Type: **FreeFormDeformation**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Attribute | DeformationQuality |
| Sub | DeformationQuality | EnumAttr | DeformationQuality.type |
| Sub | DeformationQuality | EnumAttr | DeformationQuality.level |


# GameBone Node

Type: **GameBoneModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Pos2DAttr | restOffset |
| Sub | restOffset | BoolAttr | restOffset/SEPARATE |
| Sub | restOffset | DoubleAttr | restOffset.X |
| Sub | restOffset | DoubleAttr | restOffset.Y |
| Main |  | DoubleAttr | restOrientation |
| Main |  | DoubleAttr | restRadius |
| Main |  | DoubleAttr | restBias |
| Main |  | DoubleAttr | restLength |
| Main |  | Pos2DAttr | offset |
| Sub | offset | BoolAttr | offset/SEPARATE |
| Sub | offset | DoubleAttr | offset.X |
| Sub | offset | DoubleAttr | offset.Y |
| Sub | offset | Attribute | offset.2DPOINT |
| Main |  | DoubleAttr | orientation |
| Main |  | DoubleAttr | radius |
| Main |  | DoubleAttr | bias |
| Main |  | DoubleAttr | length |


# Glue Node

Type: **GLUE**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | DoubleAttr | BIAS |
| Main |  | DoubleAttr | TENSION |
| Main |  | EnumAttr | TYPE |
| Main |  | BoolAttr | USE_Z |
| Main |  | BoolAttr | A_OVER_B |
| Main |  | BoolAttr | SPREAD_A |


# Highlight Node

Type: **HIGHLIGHT**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | TRUCK_FACTOR |
| Main |  | EnumAttr | BLUR_TYPE |
| Main |  | DoubleAttr | RADIUS |
| Main |  | DoubleAttr | DIRECTIONAL_ANGLE |
| Main |  | DoubleAttr | DIRECTIONAL_FALLOFF_RATE |
| Main |  | BoolAttr | USE_MATTE_COLOR |
| Main |  | BoolAttr | INVERT_MATTE |
| Main |  | ColorAttr | COLOR |
| Sub | COLOR | IntAttr | COLOR.RED |
| Sub | COLOR | IntAttr | COLOR.GREEN |
| Sub | COLOR | IntAttr | COLOR.BLUE |
| Sub | COLOR | IntAttr | COLOR.ALPHA |
| Sub | COLOR | EnumAttr | COLOR.PREFERRED_UI |
| Main |  | BoolAttr | MULTIPLICATIVE |
| Main |  | DoubleAttr | COLOUR_GAIN |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


# Image-Switch Node

Type: **ImageSwitch**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | Port_Index |


# Mesh-Warp Node

Type: **BezierMesh**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Attribute | Mesh |
| Sub | Mesh | IntAttr | Mesh.Size |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x0 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x1 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x2 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x3 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x4 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x5 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x6 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x7 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x8 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x9 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x10 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x11 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x12 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x13 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x14 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x15 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x16 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x17 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x18 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x19 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x20 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x21 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x22 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x23 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x24 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x25 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x26 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x27 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x28 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x29 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint0x30 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint1x0 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint1x1 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint1x2 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint1x3 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint1x4 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint1x5 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint1x6 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint1x7 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint1x8 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint1x9 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint1x10 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint2x0 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint2x1 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint2x2 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint2x3 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint2x4 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint2x5 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint2x6 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint2x7 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint2x8 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint2x9 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint2x10 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x0 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x1 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x2 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x3 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x4 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x5 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x6 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x7 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x8 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x9 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x10 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x11 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x12 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x13 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x14 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x15 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x16 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x17 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x18 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x19 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x20 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x21 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x22 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x23 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x24 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x25 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x26 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x27 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x28 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x29 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint3x30 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint4x0 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint4x1 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint4x2 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint4x3 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint4x4 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint4x5 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint4x6 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint4x7 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint4x8 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint4x9 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint4x10 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint5x0 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint5x1 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint5x2 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint5x3 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint5x4 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint5x5 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint5x6 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint5x7 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint5x8 |
| Sub | Mesh | Pos2DAttr | Mesh.MeshPoint5x9 |
| Sub | Mesh | IntAttr | Mesh.Rows |
| Sub | Mesh | IntAttr | Mesh.Columns |
| Main |  | Pos2DAttr | Origin |
| Sub | Origin | BoolAttr | Origin/SEPARATE |
| Sub | Origin | DoubleAttr | Origin.X |
| Sub | Origin | DoubleAttr | Origin.Y |
| Sub | Origin | Attribute | Origin.2DPOINT |
| Main |  | DoubleAttr | Width |
| Main |  | DoubleAttr | Height |
| Main |  | Attribute | DeformationQuality |
| Sub | DeformationQuality | EnumAttr | DeformationQuality.type |
| Sub | DeformationQuality | EnumAttr | DeformationQuality.level |


# Multi-Points-Constraint Node

Type: **PointConstraintMulti**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | EnumAttr | FLATTENTYPE |
| Main |  | BoolAttr | CONVEXHULL |
| Main |  | BoolAttr | ALLOWPERSP |


# OGL-Controller Node

Type: **OglController**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Pos3DAttr | position |
| Sub | position | BoolAttr | position/SEPARATE |
| Sub | position | DoubleAttr | position.X |
| Sub | position | DoubleAttr | position.Y |
| Sub | position | DoubleAttr | position.Z |
| Sub | position | Attribute | position.3DPATH |
| Main |  | EnumAttr | shape |
| Main |  | ColorAttr | color |
| Sub | color | IntAttr | color.RED |
| Sub | color | IntAttr | color.GREEN |
| Sub | color | IntAttr | color.BLUE |
| Sub | color | IntAttr | color.ALPHA |
| Sub | color | EnumAttr | color.PREFERRED_UI |
| Main |  | DoubleAttr | size |
| Main |  | TextAttr | selectionoverride |
| Main |  | Attribute | updateSelOverride |
| Main |  | TextAttr | visibilitycontext |
| Main |  | Attribute | updateVisibilityContext |
| Main |  | BoolAttr | selectionOnly |
| Main |  | BoolAttr | preserveProportions |
| Main |  | BoolAttr | constantSize |
| Main |  | TextAttr | text |
| Main |  | ColorAttr | textcolor |
| Sub | textcolor | IntAttr | textcolor.RED |
| Sub | textcolor | IntAttr | textcolor.GREEN |
| Sub | textcolor | IntAttr | textcolor.BLUE |
| Sub | textcolor | IntAttr | textcolor.ALPHA |
| Sub | textcolor | EnumAttr | textcolor.PREFERRED_UI |
| Main |  | Pos3DAttr | textposition |
| Sub | textposition | BoolAttr | textposition/SEPARATE |
| Sub | textposition | DoubleAttr | textposition.X |
| Sub | textposition | DoubleAttr | textposition.Y |
| Sub | textposition | DoubleAttr | textposition.Z |
| Sub | textposition | Attribute | textposition.3DPATH |
| Main |  | DoubleAttr | textsize |
| Main |  | ColorAttr | textbackgroundcolor |
| Sub | textbackgroundcolor | IntAttr | textbackgroundcolor.RED |
| Sub | textbackgroundcolor | IntAttr | textbackgroundcolor.GREEN |
| Sub | textbackgroundcolor | IntAttr | textbackgroundcolor.BLUE |
| Sub | textbackgroundcolor | IntAttr | textbackgroundcolor.ALPHA |
| Sub | textbackgroundcolor | EnumAttr | textbackgroundcolor.PREFERRED_UI |
| Main |  | BoolAttr | backgroundBox |
| Main |  | IntAttr | font |
| Main |  | BoolAttr | setup |


# Offset Node

Type: **OffsetModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | localReferential |
| Main |  | Pos2DAttr | restingOffset |
| Sub | restingOffset | BoolAttr | restingOffset/SEPARATE |
| Sub | restingOffset | DoubleAttr | restingOffset.X |
| Sub | restingOffset | DoubleAttr | restingOffset.Y |
| Main |  | DoubleAttr | restingOrientation |
| Main |  | Pos2DAttr | offset |
| Sub | offset | BoolAttr | offset/SEPARATE |
| Sub | offset | DoubleAttr | offset.X |
| Sub | offset | DoubleAttr | offset.Y |
| Sub | offset | Attribute | offset.2DPOINT |
| Main |  | DoubleAttr | orientation |


# Peg Node

Type: **PEG**

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


# Point-Kinematic-Output Node

Type: **DeformTransformOut**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | SAMPLE |
| Main |  | Pos2DAttr | PIVOT1 |
| Sub | PIVOT1 | BoolAttr | PIVOT1/SEPARATE |
| Sub | PIVOT1 | DoubleAttr | PIVOT1.X |
| Sub | PIVOT1 | DoubleAttr | PIVOT1.Y |
| Sub | PIVOT1 | Attribute | PIVOT1.2DPOINT |
| Main |  | Pos2DAttr | PIVOT2 |
| Sub | PIVOT2 | BoolAttr | PIVOT2/SEPARATE |
| Sub | PIVOT2 | DoubleAttr | PIVOT2.X |
| Sub | PIVOT2 | DoubleAttr | PIVOT2.Y |
| Sub | PIVOT2 | Attribute | PIVOT2.2DPOINT |
| Main |  | Pos2DAttr | PIVOT3 |
| Sub | PIVOT3 | BoolAttr | PIVOT3/SEPARATE |
| Sub | PIVOT3 | DoubleAttr | PIVOT3.X |
| Sub | PIVOT3 | DoubleAttr | PIVOT3.Y |
| Sub | PIVOT3 | Attribute | PIVOT3.2DPOINT |
| Main |  | DoubleAttr | VOLUME |


# Refract Node

Type: **REFRACT**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | DoubleAttr | INTENSITY |
| Main |  | DoubleAttr | HEIGHT |


# Rigid-Point-Deform Node

Type: **RigidPointDeform**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | DoubleAttr | MINDIST |
| Main |  | DoubleAttr | MAXDIST |


# Shape-Aware-Deformation Node

Type: **ShapeAwareDeformation**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Attribute | DeformationQuality |
| Sub | DeformationQuality | EnumAttr | DeformationQuality.type |
| Sub | DeformationQuality | EnumAttr | DeformationQuality.level |
| Main |  | DoubleAttr | ATTENUATION_EXPONENT |
| Main |  | BoolAttr | USE_OVERLAY_AS_RIGIDITY |
| Main |  | IntAttr | POINTS_TO_CONSIDER |
| Main |  | TextAttr | CAGE_DEFINITIONS |
| Main |  | TextAttr | BONE_DEFINITIONS |


# Static-Transformation Node

Type: **StaticConstraint**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Attribute | bakeAttr |
| Main |  | Attribute | bakeAttr_all |
| Main |  | BoolAttr | active |
| Main |  | Pos3DAttr | translate |
| Sub | translate | BoolAttr | translate/SEPARATE |
| Sub | translate | DoubleAttr | translate.X |
| Sub | translate | DoubleAttr | translate.Y |
| Sub | translate | DoubleAttr | translate.Z |
| Main |  | Attribute | scale |
| Sub | scale | BoolAttr | scale/SEPARATE |
| Sub | scale | BoolAttr | scale/IN_FIELDS |
| Sub | scale | DoubleAttr | scale.XY |
| Sub | scale | DoubleAttr | scale.X |
| Sub | scale | DoubleAttr | scale.Y |
| Sub | scale | DoubleAttr | scale.Z |
| Main |  | Attribute | rotate |
| Sub | rotate | BoolAttr | rotate/SEPARATE |
| Sub | rotate | DoubleAttr | rotate.ANGLEX |
| Sub | rotate | DoubleAttr | rotate.ANGLEY |
| Sub | rotate | DoubleAttr | rotate.ANGLEZ |
| Main |  | DoubleAttr | skewX |
| Main |  | DoubleAttr | skewY |
| Main |  | DoubleAttr | skewZ |
| Main |  | BoolAttr | inverted |


# Stick Node

Type: **BoneModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | influenceType |
| Main |  | DoubleAttr | influenceFade |
| Main |  | BoolAttr | symmetric |
| Main |  | DoubleAttr | transversalRadius |
| Main |  | DoubleAttr | transversalRadiusRight |
| Main |  | DoubleAttr | longitudinalRadiusBegin |
| Main |  | DoubleAttr | longitudinalRadius |
| Main |  | DoubleAttr | restLength |
| Main |  | DoubleAttr | Length |


# Three-Points-Constraints Node

Type: **PointConstraint3**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | EnumAttr | FLATTENTYPE |
| Main |  | EnumAttr | TRANSFORMTYPE |
| Main |  | EnumAttr | PRIMARYPORT |


# Tone Node

Type: **TONE**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | TRUCK_FACTOR |
| Main |  | EnumAttr | BLUR_TYPE |
| Main |  | DoubleAttr | RADIUS |
| Main |  | DoubleAttr | DIRECTIONAL_ANGLE |
| Main |  | DoubleAttr | DIRECTIONAL_FALLOFF_RATE |
| Main |  | BoolAttr | USE_MATTE_COLOR |
| Main |  | BoolAttr | INVERT_MATTE |
| Main |  | ColorAttr | COLOR |
| Sub | COLOR | IntAttr | COLOR.RED |
| Sub | COLOR | IntAttr | COLOR.GREEN |
| Sub | COLOR | IntAttr | COLOR.BLUE |
| Sub | COLOR | IntAttr | COLOR.ALPHA |
| Sub | COLOR | EnumAttr | COLOR.PREFERRED_UI |
| Main |  | BoolAttr | MULTIPLICATIVE |
| Main |  | DoubleAttr | COLOUR_GAIN |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


# Transformation-Gate Node

Type: **TransformGate**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | IntAttr | TARGET_GATE |
| Main |  | IntAttr | DEFAULT_GATE |


# Transformation-Limit Node

Type: **TransformLimit**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | EnumAttr | SWITCHTYPE |
| Main |  | DoubleAttr | TX |
| Main |  | DoubleAttr | TY |
| Main |  | DoubleAttr | TZ |
| Main |  | DoubleAttr | ROT |
| Main |  | DoubleAttr | SKEW |
| Main |  | DoubleAttr | SX |
| Main |  | DoubleAttr | SY |
| Main |  | BoolAttr | ALLOWFLIP |
| Main |  | BoolAttr | UNIFORMSCALE |
| Main |  | DoubleAttr | PIGNORE |
| Main |  | TextAttr | PARENTNAME |
| Main |  | EnumAttr | FLATTENTYPE |
| Main |  | EnumAttr | SKEWTYPE |
| Main |  | EnumAttr | FLIPAXIS |
| Main |  | Pos2DAttr | POS |
| Sub | POS | BoolAttr | POS/SEPARATE |
| Sub | POS | DoubleAttr | POS.X |
| Sub | POS | DoubleAttr | POS.Y |
| Sub | POS | Attribute | POS.2DPOINT |


# Transformation-Switch Node

Type: **TransformationSwitch**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DrawingAttr | Drawing |
| Sub | Drawing | BoolAttr | Drawing/ELEMENT_MODE |
| Sub | Drawing | ElementAttr | Drawing/ELEMENT |
| Sub | Drawing | Attribute | Drawing.CUSTOM_NAME |
| Main |  | Attribute | TransformationNames |
| Sub | TransformationNames | IntAttr | TransformationNames.Size |


# Turbulence Node

Type: **Turbulence**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | Fractal_Type |
| Main |  | EnumAttr | Noise_Type |
| Main |  | Attribute | Frequency |
| Sub | Frequency | BoolAttr | Frequency/SEPARATE |
| Sub | Frequency | DoubleAttr | Frequency.xyFrequency |
| Sub | Frequency | DoubleAttr | Frequency.xFrequency |
| Sub | Frequency | DoubleAttr | Frequency.yFrequency |
| Main |  | Attribute | Amount |
| Sub | Amount | BoolAttr | Amount/SEPARATE |
| Sub | Amount | DoubleAttr | Amount.xyAmount |
| Sub | Amount | DoubleAttr | Amount.xAmount |
| Sub | Amount | DoubleAttr | Amount.yAmount |
| Main |  | Attribute | Offset |
| Sub | Offset | BoolAttr | Offset/SEPARATE |
| Sub | Offset | DoubleAttr | Offset.xyOffset |
| Sub | Offset | DoubleAttr | Offset.xOffset |
| Sub | Offset | DoubleAttr | Offset.yOffset |
| Main |  | Attribute | Seed |
| Sub | Seed | BoolAttr | Seed/SEPARATE |
| Sub | Seed | DoubleAttr | Seed.xySeed |
| Sub | Seed | DoubleAttr | Seed.xSeed |
| Sub | Seed | DoubleAttr | Seed.ySeed |
| Main |  | DoubleAttr | Evolution |
| Main |  | DoubleAttr | Evolution_Frequency |
| Main |  | DoubleAttr | Gain |
| Main |  | DoubleAttr | Lacunarity |
| Main |  | DoubleAttr | Octaves |
| Main |  | BoolAttr | Pinning |
| Main |  | Attribute | DeformationQuality |
| Sub | DeformationQuality | EnumAttr | DeformationQuality.type |
| Sub | DeformationQuality | EnumAttr | DeformationQuality.level |


# Two-Points-Constraint Node

Type: **PointConstraint2**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | DoubleAttr | VOLUMEMOD |
| Main |  | DoubleAttr | VOLUMEMAX |
| Main |  | DoubleAttr | VOLUMEMIN |
| Main |  | DoubleAttr | STRETCHMAX |
| Main |  | DoubleAttr | STRETCHMIN |
| Main |  | DoubleAttr | SKEWCONTROL |
| Main |  | DoubleAttr | SMOOTH |
| Main |  | DoubleAttr | BALANCE |
| Main |  | EnumAttr | FLATTENTYPE |
| Main |  | EnumAttr | TRANSFORMTYPE |
| Main |  | EnumAttr | PRIMARYPORT |


# Weighted-Curve Node

Type: **WeightCurve**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | CURVETYPE |
| Main |  | DoubleAttr | ACTIVE |
| Main |  | DoubleAttr | MINDIST |
| Main |  | DoubleAttr | MAXDIST |


# Weighted-Deform Node

Type: **WeightedDeform**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | BLEND |
| Main |  | DoubleAttr | POSTBLEND |
| Main |  | Attribute | DeformationQuality |
| Sub | DeformationQuality | EnumAttr | DeformationQuality.type |
| Sub | DeformationQuality | EnumAttr | DeformationQuality.level |


# Weighted-Drawing Node

Type: **WeightDrawing**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | DoubleAttr | MINDIST |
| Main |  | DoubleAttr | MAXDIST |


# Weighted-Line Node

Type: **WeightLine**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | DoubleAttr | MINDIST |
| Main |  | DoubleAttr | MAXDIST |


# Weighted-Point Node

Type: **WeightPoint**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | DoubleAttr | MINDIST |
| Main |  | DoubleAttr | MAXDIST |


# Write Node

Type: **WRITE**

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

