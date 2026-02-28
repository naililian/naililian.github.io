# Nodes Attributes

You'll find all the information about nodes attributes.

## 3D-Region Node

Type: **Particle3dRegion**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | shapeType |
| Main |  | DoubleAttr | sizeX |
| Main |  | DoubleAttr | sizeY |
| Main |  | DoubleAttr | sizeZ |
| Main |  | DoubleAttr | outerRadius |
| Main |  | DoubleAttr | innerRadius |


## Ambient-Occlusion Node

Type: **AmbientOcclusion**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | Darkness |
| Main |  | DoubleAttr | ZRange |
| Main |  | DoubleAttr | Bias |
| Main |  | DoubleAttr | Exponent |
| Main |  | DoubleAttr | Gamma |
| Main |  | DoubleAttr | Blur |
| Main |  | DoubleAttr | Postblur |
| Main |  | DoubleAttr | PostblurThreshold |
| Main |  | BoolAttr | UseImageColor |
| Main |  | ColorAttr | Color |
| Sub | Color | IntAttr | Color.RED |
| Sub | Color | IntAttr | Color.GREEN |
| Sub | Color | IntAttr | Color.BLUE |
| Sub | Color | IntAttr | Color.ALPHA |
| Sub | Color | EnumAttr | Color.PREFERRED_UI |
| Main |  | DoubleAttr | ImageColorWeight |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


## Animate-Pencil-Texture Node

Type: **AnimatePencilTexture**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | HoldMode |
| Main |  | IntAttr | HoldValue |
| Main |  | IntAttr | HoldKeyframes |
| Main |  | Attribute | BakeOffsets |
| Main |  | DoubleAttr | Frequency |
| Main |  | IntAttr | Octaves |
| Main |  | DoubleAttr | Multiplier |
| Main |  | DoubleAttr | IncrementalOffset |
| Main |  | DoubleAttr | MaxStart |
| Main |  | DoubleAttr | MinCenter |
| Main |  | DoubleAttr | MaxCenter |
| Main |  | DoubleAttr | MinScaleX |
| Main |  | DoubleAttr | MaxScaleX |
| Main |  | DoubleAttr | MinScaleY |
| Main |  | DoubleAttr | MaxScaleY |
| Main |  | IntAttr | Seed |
| Main |  | EnumAttr | SeedType |


## Animated-Matte-Generator Node

Type: **AnimatedMatteGenerator**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | snapRadius |
| Main |  | BoolAttr | snapOutlinesOnly |
| Main |  | EnumAttr | outputType |
| Main |  | DoubleAttr | outputInterpolation |
| Main |  | ColorAttr | insideColor |
| Sub | insideColor | IntAttr | insideColor.RED |
| Sub | insideColor | IntAttr | insideColor.GREEN |
| Sub | insideColor | IntAttr | insideColor.BLUE |
| Sub | insideColor | IntAttr | insideColor.ALPHA |
| Sub | insideColor | EnumAttr | insideColor.PREFERRED_UI |
| Main |  | ColorAttr | outsideColor |
| Sub | outsideColor | IntAttr | outsideColor.RED |
| Sub | outsideColor | IntAttr | outsideColor.GREEN |
| Sub | outsideColor | IntAttr | outsideColor.BLUE |
| Sub | outsideColor | IntAttr | outsideColor.ALPHA |
| Sub | outsideColor | EnumAttr | outsideColor.PREFERRED_UI |
| Main |  | EnumAttr | interpolationMode |
| Main |  | EnumAttr | colorInterpolation |
| Main |  | EnumAttr | alphaMapping |
| Main |  | IntAttr | colorLUTDomain |
| Main |  | IntAttr | alphaLUTDomain |
| Main |  | DoubleAttr | colorGamma |
| Main |  | DoubleAttr | alphaGamma |
| Main |  | DoubleAttr | colorLUT |
| Main |  | DoubleAttr | alphaLUT |
| Main |  | BoolAttr | snapUnderlay |
| Main |  | BoolAttr | snapColor |
| Main |  | BoolAttr | snapLine |
| Main |  | BoolAttr | snapOverlay |
| Main |  | BoolAttr | useHints |
| Main |  | DoubleAttr | snapRadiusDragHint |
| Main |  | DoubleAttr | snapRadiusGenerateHint |
| Main |  | DoubleAttr | minDistancePregenerateHints |
| Main |  | BoolAttr | snapHintUnderlay |
| Main |  | BoolAttr | snapHintColor |
| Main |  | BoolAttr | snapHintLine |
| Main |  | BoolAttr | snapHintOverlay |
| Main |  | BoolAttr | overlayIsNote |
| Main |  | TextAttr | contourCentres |


## Anti-Flicker Node

Type: **FLICKER_BLUR**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | RADIUS |


## Articulation Node

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


## Auto-Muscle Node

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


## Blending Node

Type: **BLEND_MODE_MODULE**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | BLEND_MODE |
| Main |  | EnumAttr | CLAMPING_MODE |
| Main |  | EnumAttr | FLASH_BLEND_MODE |


## Bloom Node

Type: **Bloom**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | LuminanceThresholdThresh |
| Main |  | BoolAttr | LuminanceThresholdSoften |
| Main |  | DoubleAttr | LuminanceThresholdGamma |
| Main |  | BoolAttr | LuminanceThresholdGrey |
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | BoolAttr | TRUCK_FACTOR |
| Main |  | DoubleAttr | RADIUS |
| Main |  | EnumAttr | QUALITY |
| Main |  | BoolAttr | COMPOSITE_SRC_IMAGE |
| Main |  | EnumAttr | BLEND_MODE |


## Blur Node

Type: **BLUR_RADIAL**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | BoolAttr | TRUCK_FACTOR |
| Main |  | DoubleAttr | RADIUS |
| Main |  | EnumAttr | QUALITY |


## Blur-Box Node

Type: **BOXBLUR-PLUGIN**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | BoolAttr | Truck_Factor |
| Main |  | BoolAttr | Bidirectional |
| Main |  | EnumAttr | Precision |
| Main |  | BoolAttr | Repeat_Edge_Pixels |
| Main |  | BoolAttr | Directional |
| Main |  | DoubleAttr | Angle |
| Main |  | IntAttr | Iterations |
| Main |  | DoubleAttr | Radius |
| Main |  | DoubleAttr | Width |
| Main |  | DoubleAttr | Length |
| Main |  | DoubleAttr | Fall_Off |


## Blur-Directional Node

Type: **BLUR_DIRECTIONAL**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | BoolAttr | TRUCK_FACTOR |
| Main |  | DoubleAttr | FALLOF_RATE |
| Main |  | DoubleAttr | ANGLE |
| Main |  | DoubleAttr | RADIUS |
| Main |  | EnumAttr | DIRECTION_OF_TRAIL |
| Main |  | BoolAttr | IGNORE_ALPHA |
| Main |  | BoolAttr | EXTRA_FINAL_BLUR |


## Blur-Gaussian Node

Type: **GAUSSIANBLUR-PLUGIN**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | BoolAttr | Truck_Factor |
| Main |  | BoolAttr | Bidirectional |
| Main |  | EnumAttr | Precision |
| Main |  | BoolAttr | Repeat_Edge_Pixels |
| Main |  | BoolAttr | Directional |
| Main |  | DoubleAttr | Angle |
| Main |  | IntAttr | Iterations |
| Main |  | DoubleAttr | Blurriness |
| Main |  | DoubleAttr | Vertical |
| Main |  | DoubleAttr | Horizontal |


## Blur-Radial-Zoom Node

Type: **RADIALBLUR-PLUGIN**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | BoolAttr | Truck_Factor |
| Main |  | BoolAttr | Bidirectional |
| Main |  | EnumAttr | Precision |
| Main |  | DoubleAttr | Blurriness |
| Main |  | DoubleAttr | Fall_Off |
| Main |  | DoubleAttr | Spiral |
| Main |  | Pos2DAttr | Focus |
| Sub | Focus | BoolAttr | Focus/SEPARATE |
| Sub | Focus | DoubleAttr | Focus.X |
| Sub | Focus | DoubleAttr | Focus.Y |
| Sub | Focus | Attribute | Focus.2DPOINT |
| Main |  | EnumAttr | Smoothness |
| Main |  | DoubleAttr | Quality |
| Main |  | BoolAttr | Legacy |


## Blur-Variable Node

Type: **BLUR_VARIABLE**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | DoubleAttr | BLACK_RADIUS |
| Main |  | DoubleAttr | WHITE_RADIUS |
| Main |  | EnumAttr | QUALITY |
| Main |  | BoolAttr | KEEP_INSIDE_SOURCE_IMAGE |


## Bokeh-Blur Node

Type: **BOKEH**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | DoubleAttr | Radius |
| Main |  | BoolAttr | Highlights |
| Main |  | DoubleAttr | Highlight_Threshold |
| Main |  | DoubleAttr | Brightness |
| Main |  | DoubleAttr | Fall_Off |
| Main |  | IntAttr | Sides |
| Main |  | DoubleAttr | Roundedness |
| Main |  | DoubleAttr | Indentation |
| Main |  | DoubleAttr | Angle |
| Main |  | DoubleAttr | Sharpness |
| Main |  | BoolAttr | RepeatEdges |
| Main |  | BoolAttr | Truckfactor |
| Main |  | EnumAttr | ShapeType |


## Bone Node

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


## Bounce Node

Type: **ParticleBounce**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | DoubleAttr | friction |
| Main |  | DoubleAttr | resilience |
| Main |  | DoubleAttr | cutoff |


## Brightness-Contrast Node

Type: **BRIGHTNESS_CONTRAST**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | BoolAttr | BRIGHTCONTRAST_LEGACY_BRIGHTNESS |
| Main |  | DoubleAttr | BRIGHTCONTRAST_BRIGHTNESS_ADJUSTMENT |
| Main |  | DoubleAttr | BRIGHTCONTRAST_CONTRAST_ADJUSTMENT |
| Main |  | BoolAttr | BRIGHTCONTRAST_LEGACY_CONTRAST |


## BrightnessContrast Node

Type: **BRIGHTNESS_CONTRAST**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | BoolAttr | BRIGHTCONTRAST_LEGACY_BRIGHTNESS |
| Main |  | DoubleAttr | BRIGHTCONTRAST_BRIGHTNESS_ADJUSTMENT |
| Main |  | DoubleAttr | BRIGHTCONTRAST_CONTRAST_ADJUSTMENT |
| Main |  | BoolAttr | BRIGHTCONTRAST_LEGACY_CONTRAST |


## Burn-In Node

Type: **BurnIn**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | DrawBackgroundBox |
| Main |  | ColorAttr | TextColor |
| Sub | TextColor | IntAttr | TextColor.RED |
| Sub | TextColor | IntAttr | TextColor.GREEN |
| Sub | TextColor | IntAttr | TextColor.BLUE |
| Sub | TextColor | IntAttr | TextColor.ALPHA |
| Sub | TextColor | EnumAttr | TextColor.PREFERRED_UI |
| Main |  | ColorAttr | BackgroundColor |
| Sub | BackgroundColor | IntAttr | BackgroundColor.RED |
| Sub | BackgroundColor | IntAttr | BackgroundColor.GREEN |
| Sub | BackgroundColor | IntAttr | BackgroundColor.BLUE |
| Sub | BackgroundColor | IntAttr | BackgroundColor.ALPHA |
| Sub | BackgroundColor | EnumAttr | BackgroundColor.PREFERRED_UI |
| Main |  | IntAttr | Size |
| Main |  | IntAttr | FrameOffset |
| Main |  | BoolAttr | DrawFrameNumber |
| Main |  | BoolAttr | DrawTimecode |
| Main |  | TextAttr | PrintInfo |
| Main |  | EnumAttr | Alignment |
| Main |  | IntAttr | Font |


## Camera Node

Type: **CAMERA**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Pos3DAttr | OFFSET |
| Sub | OFFSET | BoolAttr | OFFSET/SEPARATE |
| Sub | OFFSET | DoubleAttr | OFFSET.X |
| Sub | OFFSET | DoubleAttr | OFFSET.Y |
| Sub | OFFSET | DoubleAttr | OFFSET.Z |
| Main |  | Pos2DAttr | PIVOT |
| Sub | PIVOT | BoolAttr | PIVOT/SEPARATE |
| Sub | PIVOT | DoubleAttr | PIVOT.X |
| Sub | PIVOT | DoubleAttr | PIVOT.Y |
| Main |  | DoubleAttr | ANGLE |
| Main |  | BoolAttr | OVERRIDE_SCENE_FOV |
| Main |  | DoubleAttr | FOV |
| Main |  | DoubleAttr | NEAR_PLANE |
| Main |  | DoubleAttr | FAR_PLANE |


## Cast-Shadow Node

Type: **CastShadow**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | LightType |
| Main |  | EnumAttr | ShadeType |
| Main |  | DoubleAttr | AngleBias |
| Main |  | DoubleAttr | ShadowDarkness |
| Main |  | DoubleAttr | ShadowLength |
| Main |  | DoubleAttr | ShadowBias |
| Main |  | IntAttr | SampleCount |
| Main |  | DoubleAttr | SampleSize |
| Main |  | IntAttr | SoftCount |
| Main |  | DoubleAttr | SoftSize |
| Main |  | DoubleAttr | SoftWeight |
| Main |  | DoubleAttr | PostBlur |
| Main |  | DoubleAttr | PostBlurThreshold |
| Main |  | DoubleAttr | ShadowNoise |
| Main |  | IntAttr | ExpandSource |
| Main |  | DoubleAttr | ShadowGamma |
| Main |  | IntAttr | AntiAliasBias |
| Main |  | IntAttr | AntiAliasBlend |
| Main |  | IntAttr | AntialiasBlur |
| Main |  | DoubleAttr | Exponent |
| Main |  | ColorAttr | Color |
| Sub | Color | IntAttr | Color.RED |
| Sub | Color | IntAttr | Color.GREEN |
| Sub | Color | IntAttr | Color.BLUE |
| Sub | Color | IntAttr | Color.ALPHA |
| Sub | Color | EnumAttr | Color.PREFERRED_UI |
| Main |  | BoolAttr | UseImageColor |
| Main |  | DoubleAttr | ImageColorWeight |
| Main |  | BoolAttr | UseTruckFactor |
| Main |  | BoolAttr | PolarMethod |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


## Channel-Selector Node

Type: **COLOR_MASK**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | RED |
| Main |  | BoolAttr | GREEN |
| Main |  | BoolAttr | BLUE |
| Main |  | BoolAttr | ALPHA |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


## Channel-Swap Node

Type: **CHANNEL_SWAP**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | RedChannelSelection |
| Main |  | EnumAttr | GreenChannelSelection |
| Main |  | EnumAttr | BlueChannelSelection |
| Main |  | EnumAttr | AlphaChannelSelection |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


## Chroma-Keying Node

Type: **CHROMA_KEYING**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | ColorAttr | COLOR |
| Sub | COLOR | IntAttr | COLOR.RED |
| Sub | COLOR | IntAttr | COLOR.GREEN |
| Sub | COLOR | IntAttr | COLOR.BLUE |
| Sub | COLOR | IntAttr | COLOR.ALPHA |
| Sub | COLOR | EnumAttr | COLOR.PREFERRED_UI |
| Main |  | DoubleAttr | CHROMA_KEY_MINIMUM |
| Main |  | DoubleAttr | CHROMA_KEY_MAXIMUM |
| Main |  | DoubleAttr | CHROMA_KEY_FILTER_INTENSITY |
| Main |  | DoubleAttr | CHROMA_KEY_SAMPLING |
| Main |  | BoolAttr | applyFinalThreshold |
| Main |  | DoubleAttr | finalThreshold |
| Main |  | BoolAttr | cutImage |


## Colour-Art Node

Type: **COLOR_ART**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | FLATTEN |
| Main |  | BoolAttr | APPLY_TO_MATTE_PORTS |
| Main |  | EnumAttr | ANTIALIASING_QUALITY |
| Main |  | DoubleAttr | ANTIALIASING_EXPONENT |


## Colour-Banding Node

Type: **FilterBanding**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | threshold1 |
| Main |  | ColorAttr | colour1 |
| Sub | colour1 | IntAttr | colour1.RED |
| Sub | colour1 | IntAttr | colour1.GREEN |
| Sub | colour1 | IntAttr | colour1.BLUE |
| Sub | colour1 | IntAttr | colour1.ALPHA |
| Sub | colour1 | EnumAttr | colour1.PREFERRED_UI |
| Main |  | DoubleAttr | blur1 |
| Main |  | DoubleAttr | threshold2 |
| Main |  | ColorAttr | colour2 |
| Sub | colour2 | IntAttr | colour2.RED |
| Sub | colour2 | IntAttr | colour2.GREEN |
| Sub | colour2 | IntAttr | colour2.BLUE |
| Sub | colour2 | IntAttr | colour2.ALPHA |
| Sub | colour2 | EnumAttr | colour2.PREFERRED_UI |
| Main |  | DoubleAttr | blur2 |
| Main |  | DoubleAttr | threshold3 |
| Main |  | ColorAttr | colour3 |
| Sub | colour3 | IntAttr | colour3.RED |
| Sub | colour3 | IntAttr | colour3.GREEN |
| Sub | colour3 | IntAttr | colour3.BLUE |
| Sub | colour3 | IntAttr | colour3.ALPHA |
| Sub | colour3 | EnumAttr | colour3.PREFERRED_UI |
| Main |  | DoubleAttr | blur3 |
| Main |  | DoubleAttr | threshold4 |
| Main |  | ColorAttr | colour4 |
| Sub | colour4 | IntAttr | colour4.RED |
| Sub | colour4 | IntAttr | colour4.GREEN |
| Sub | colour4 | IntAttr | colour4.BLUE |
| Sub | colour4 | IntAttr | colour4.ALPHA |
| Sub | colour4 | EnumAttr | colour4.PREFERRED_UI |
| Main |  | DoubleAttr | blur4 |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


## Colour-Card Node

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


## Colour-Curves Node

Type: **COLOR_CURVES**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | clamp |
| Main |  | BoolAttr | extrapolate |
| Main |  | DoubleAttr | clampMin |
| Main |  | DoubleAttr | clampMax |
| Main |  | Attribute | CONTROL_POINT_RED_0 |
| Sub | CONTROL_POINT_RED_0 | Pos2DAttr | CONTROL_POINT_RED_0.CONTROL |
| Sub | CONTROL_POINT_RED_0 | Pos2DAttr | CONTROL_POINT_RED_0.LEFT_HANDLE |
| Sub | CONTROL_POINT_RED_0 | Pos2DAttr | CONTROL_POINT_RED_0.RIGHT_HANDLE |
| Main |  | Attribute | CONTROL_POINT_RED_1 |
| Sub | CONTROL_POINT_RED_1 | Pos2DAttr | CONTROL_POINT_RED_1.CONTROL |
| Sub | CONTROL_POINT_RED_1 | Pos2DAttr | CONTROL_POINT_RED_1.LEFT_HANDLE |
| Sub | CONTROL_POINT_RED_1 | Pos2DAttr | CONTROL_POINT_RED_1.RIGHT_HANDLE |
| Main |  | Attribute | CONTROL_POINT_GREEN_0 |
| Sub | CONTROL_POINT_GREEN_0 | Pos2DAttr | CONTROL_POINT_GREEN_0.CONTROL |
| Sub | CONTROL_POINT_GREEN_0 | Pos2DAttr | CONTROL_POINT_GREEN_0.LEFT_HANDLE |
| Sub | CONTROL_POINT_GREEN_0 | Pos2DAttr | CONTROL_POINT_GREEN_0.RIGHT_HANDLE |
| Main |  | Attribute | CONTROL_POINT_GREEN_1 |
| Sub | CONTROL_POINT_GREEN_1 | Pos2DAttr | CONTROL_POINT_GREEN_1.CONTROL |
| Sub | CONTROL_POINT_GREEN_1 | Pos2DAttr | CONTROL_POINT_GREEN_1.LEFT_HANDLE |
| Sub | CONTROL_POINT_GREEN_1 | Pos2DAttr | CONTROL_POINT_GREEN_1.RIGHT_HANDLE |
| Main |  | Attribute | CONTROL_POINT_BLUE_0 |
| Sub | CONTROL_POINT_BLUE_0 | Pos2DAttr | CONTROL_POINT_BLUE_0.CONTROL |
| Sub | CONTROL_POINT_BLUE_0 | Pos2DAttr | CONTROL_POINT_BLUE_0.LEFT_HANDLE |
| Sub | CONTROL_POINT_BLUE_0 | Pos2DAttr | CONTROL_POINT_BLUE_0.RIGHT_HANDLE |
| Main |  | Attribute | CONTROL_POINT_BLUE_1 |
| Sub | CONTROL_POINT_BLUE_1 | Pos2DAttr | CONTROL_POINT_BLUE_1.CONTROL |
| Sub | CONTROL_POINT_BLUE_1 | Pos2DAttr | CONTROL_POINT_BLUE_1.LEFT_HANDLE |
| Sub | CONTROL_POINT_BLUE_1 | Pos2DAttr | CONTROL_POINT_BLUE_1.RIGHT_HANDLE |
| Main |  | Attribute | CONTROL_POINT_RGB_0 |
| Sub | CONTROL_POINT_RGB_0 | Pos2DAttr | CONTROL_POINT_RGB_0.CONTROL |
| Sub | CONTROL_POINT_RGB_0 | Pos2DAttr | CONTROL_POINT_RGB_0.LEFT_HANDLE |
| Sub | CONTROL_POINT_RGB_0 | Pos2DAttr | CONTROL_POINT_RGB_0.RIGHT_HANDLE |
| Main |  | Attribute | CONTROL_POINT_RGB_1 |
| Sub | CONTROL_POINT_RGB_1 | Pos2DAttr | CONTROL_POINT_RGB_1.CONTROL |
| Sub | CONTROL_POINT_RGB_1 | Pos2DAttr | CONTROL_POINT_RGB_1.LEFT_HANDLE |
| Sub | CONTROL_POINT_RGB_1 | Pos2DAttr | CONTROL_POINT_RGB_1.RIGHT_HANDLE |
| Main |  | Attribute | CONTROL_POINT_ALPHA_0 |
| Sub | CONTROL_POINT_ALPHA_0 | Pos2DAttr | CONTROL_POINT_ALPHA_0.CONTROL |
| Sub | CONTROL_POINT_ALPHA_0 | Pos2DAttr | CONTROL_POINT_ALPHA_0.LEFT_HANDLE |
| Sub | CONTROL_POINT_ALPHA_0 | Pos2DAttr | CONTROL_POINT_ALPHA_0.RIGHT_HANDLE |
| Main |  | Attribute | CONTROL_POINT_ALPHA_1 |
| Sub | CONTROL_POINT_ALPHA_1 | Pos2DAttr | CONTROL_POINT_ALPHA_1.CONTROL |
| Sub | CONTROL_POINT_ALPHA_1 | Pos2DAttr | CONTROL_POINT_ALPHA_1.LEFT_HANDLE |
| Sub | CONTROL_POINT_ALPHA_1 | Pos2DAttr | CONTROL_POINT_ALPHA_1.RIGHT_HANDLE |


## Colour-Fade Node

Type: **COLOR_FADE**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | FadeFactor |
| Main |  | EnumAttr | ColorSpace |
| Main |  | EnumAttr | HueInterpolation |


## Colour-Levels Node

Type: **COLOR_LEVELS**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Attribute | RGB |
| Sub | RGB | DoubleAttr | RGB.INPUT_BLACK |
| Sub | RGB | DoubleAttr | RGB.INPUT_WHITE |
| Sub | RGB | DoubleAttr | RGB.GAMMA |
| Sub | RGB | DoubleAttr | RGB.OUTPUT_BLACK |
| Sub | RGB | DoubleAttr | RGB.OUTPUT_WHITE |
| Main |  | Attribute | RED |
| Sub | RED | DoubleAttr | RED.INPUT_BLACK |
| Sub | RED | DoubleAttr | RED.INPUT_WHITE |
| Sub | RED | DoubleAttr | RED.GAMMA |
| Sub | RED | DoubleAttr | RED.OUTPUT_BLACK |
| Sub | RED | DoubleAttr | RED.OUTPUT_WHITE |
| Main |  | Attribute | GREEN |
| Sub | GREEN | DoubleAttr | GREEN.INPUT_BLACK |
| Sub | GREEN | DoubleAttr | GREEN.INPUT_WHITE |
| Sub | GREEN | DoubleAttr | GREEN.GAMMA |
| Sub | GREEN | DoubleAttr | GREEN.OUTPUT_BLACK |
| Sub | GREEN | DoubleAttr | GREEN.OUTPUT_WHITE |
| Main |  | Attribute | BLUE |
| Sub | BLUE | DoubleAttr | BLUE.INPUT_BLACK |
| Sub | BLUE | DoubleAttr | BLUE.INPUT_WHITE |
| Sub | BLUE | DoubleAttr | BLUE.GAMMA |
| Sub | BLUE | DoubleAttr | BLUE.OUTPUT_BLACK |
| Sub | BLUE | DoubleAttr | BLUE.OUTPUT_WHITE |
| Main |  | Attribute | ALPHA |
| Sub | ALPHA | DoubleAttr | ALPHA.INPUT_BLACK |
| Sub | ALPHA | DoubleAttr | ALPHA.INPUT_WHITE |
| Sub | ALPHA | DoubleAttr | ALPHA.GAMMA |
| Sub | ALPHA | DoubleAttr | ALPHA.OUTPUT_BLACK |
| Sub | ALPHA | DoubleAttr | ALPHA.OUTPUT_WHITE |


## Colour-Scale Node

Type: **COLOR_SCALE**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | RED |
| Main |  | DoubleAttr | GREEN |
| Main |  | DoubleAttr | BLUE |
| Main |  | DoubleAttr | ALPHA |
| Main |  | DoubleAttr | HUE |
| Main |  | DoubleAttr | HUE_OFFSET |
| Main |  | DoubleAttr | SATURATION |
| Main |  | DoubleAttr | VALUE |
| Main |  | BoolAttr | CLAMPNEG |
| Main |  | BoolAttr | PRE_MULTIPLIED_ALPHA |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


## Colour-Selector Node

Type: **TbdColorSelector**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | TextAttr | selectedColors |
| Main |  | BoolAttr | applyToMatte |


## Composite Node

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


## Composite-Generic Node

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


## Constraint-Switch Node

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


## Contrast Node

Type: **CONTRAST**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | MID_POINT |
| Main |  | DoubleAttr | DARK_PIXEL_ADJUSTEMENT |
| Main |  | DoubleAttr | BRIGHT_PIXEL_ADJUSTEMENT |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


## Crop Node

Type: **CROP**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | RES_X |
| Main |  | IntAttr | RES_Y |
| Main |  | DoubleAttr | OFFSET_X |
| Main |  | DoubleAttr | OFFSET_Y |
| Main |  | BoolAttr | DRAW_FRAME |
| Main |  | ColorAttr | FRAME_COLOR |
| Sub | FRAME_COLOR | IntAttr | FRAME_COLOR.RED |
| Sub | FRAME_COLOR | IntAttr | FRAME_COLOR.GREEN |
| Sub | FRAME_COLOR | IntAttr | FRAME_COLOR.BLUE |
| Sub | FRAME_COLOR | IntAttr | FRAME_COLOR.ALPHA |
| Sub | FRAME_COLOR | EnumAttr | FRAME_COLOR.PREFERRED_UI |
| Main |  | Attribute | ENABLING |
| Sub | ENABLING | EnumAttr | ENABLING.FILTER |
| Sub | ENABLING | TextAttr | ENABLING.FILTER_NAME |
| Sub | ENABLING | IntAttr | ENABLING.FILTER_RES_X |
| Sub | ENABLING | IntAttr | ENABLING.FILTER_RES_Y |


## CryptoMatte Node

Type: **CryptoMatte**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | TextAttr | names |


## CryptoMatte-Write Node

Type: **CryptoMatteWrite**

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
| Main |  | TextAttr | INPUT_NAMES |
| Main |  | TextAttr | CRYPTOMATTE_NAME |
| Main |  | IntAttr | CRYPTOMATTE_COUNT |


## Curve Node

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


## Cutter Node

Type: **CUTTER**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERTED |


## Deformation-AutoFold Node

Type: **AutoFoldModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | enable |
| Main |  | DoubleAttr | length |


## Deformation-Fold Node

Type: **FoldModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | enable |
| Main |  | DoubleAttr | t |
| Main |  | DoubleAttr | tBefore |
| Main |  | DoubleAttr | tAfter |
| Main |  | DoubleAttr | angle |
| Main |  | DoubleAttr | length |


## Deformation-Scale Node

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


## Deformation-Switch Node

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


## Deformation-Uniform-Scale Node

Type: **DeformationUniformScaleModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | scale |


## Deformation-Wave Node

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


## Deformation_Composite Node

Type: **DeformationCompositeModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | outputMatrixOnly |
| Main |  | BoolAttr | outputSelectedOnly |
| Main |  | EnumAttr | outputKinematicChainSelector |
| Main |  | IntAttr | outputKinematicChain |


## Deformation_Root Node

Type: **DeformationRootModule**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Attribute | deformationQuality |
| Sub | deformationQuality | EnumAttr | deformationQuality.type |
| Sub | deformationQuality | EnumAttr | deformationQuality.level |


## Dither Node

Type: **DITHER**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | MAGNITUDE |
| Main |  | BoolAttr | CORRELATE |
| Main |  | BoolAttr | RANDOMATFRAME |
| Main |  | IntAttr | SEED |


## Drawing Node

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


## Dynamic-Spring Node

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


## External Node

Type: **EXTERNAL**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | TextAttr | PROGRAM_NAME |
| Main |  | TextAttr | PROGRAM_INPUT |
| Main |  | TextAttr | PROGRAM_INPUT2 |
| Main |  | TextAttr | PROGRAM_OUTPUT |
| Main |  | TextAttr | EXTENSION |
| Main |  | DoubleAttr | PROGRAM_NUM_PARAM |
| Main |  | BoolAttr | PROGRAM_UNIQUEID |
| Main |  | DoubleAttr | PROGRAM_NUM_PARAM_2 |
| Main |  | DoubleAttr | PROGRAM_NUM_PARAM_3 |
| Main |  | DoubleAttr | PROGRAM_NUM_PARAM_4 |
| Main |  | DoubleAttr | PROGRAM_NUM_PARAM_5 |


## Field-Chart Node

Type: **FIELD_CHART**

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
| Main |  | EnumAttr | SIZE |
| Main |  | BoolAttr | OPAQUE |


## Focus Node

Type: **FOCUS_SET**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | MIRROR |
| Main |  | DoubleAttr | RATIO |
| Main |  | Attribute | RADIUS |
| Main |  | EnumAttr | QUALITY |


## Focus-Multiplier Node

Type: **FOCUS_APPLY**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | MULTIPLIER |


## Free-Form-Deformer Node

Type: **FreeFormDeformation**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Attribute | DeformationQuality |
| Sub | DeformationQuality | EnumAttr | DeformationQuality.type |
| Sub | DeformationQuality | EnumAttr | DeformationQuality.level |


## GameBone Node

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


## Gamma Node

Type: **Gamma**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | RGB_GAMMA |
| Main |  | DoubleAttr | RED_GAMMA |
| Main |  | DoubleAttr | GREEN_GAMMA |
| Main |  | DoubleAttr | BLUE_GAMMA |
| Main |  | DoubleAttr | ALPHA_GAMMA |


## Glow Node

Type: **GLOW**

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


## Glue Node

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


## Gradient Node

Type: **GRADIENT-PLUGIN**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | DEPTH |
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | EnumAttr | Type |
| Main |  | Pos2DAttr | 0 |
| Sub | 0 | BoolAttr | 0/SEPARATE |
| Sub | 0 | DoubleAttr | 0.X |
| Sub | 0 | DoubleAttr | 0.Y |
| Sub | 0 | Attribute | 0.2DPOINT |
| Main |  | Pos2DAttr | 1 |
| Sub | 1 | BoolAttr | 1/SEPARATE |
| Sub | 1 | DoubleAttr | 1.X |
| Sub | 1 | DoubleAttr | 1.Y |
| Sub | 1 | Attribute | 1.2DPOINT |
| Main |  | ColorAttr | Color0 |
| Sub | Color0 | IntAttr | Color0.RED |
| Sub | Color0 | IntAttr | Color0.GREEN |
| Sub | Color0 | IntAttr | Color0.BLUE |
| Sub | Color0 | IntAttr | Color0.ALPHA |
| Sub | Color0 | EnumAttr | Color0.PREFERRED_UI |
| Main |  | ColorAttr | Color1 |
| Sub | Color1 | IntAttr | Color1.RED |
| Sub | Color1 | IntAttr | Color1.GREEN |
| Sub | Color1 | IntAttr | Color1.BLUE |
| Sub | Color1 | IntAttr | Color1.ALPHA |
| Sub | Color1 | EnumAttr | Color1.PREFERRED_UI |
| Main |  | DoubleAttr | Offset_Z |


## Grain Node

Type: **GRAIN**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | DoubleAttr | NOISE |
| Main |  | DoubleAttr | SMOOTH |
| Main |  | BoolAttr | RANDOM |
| Main |  | IntAttr | SEED |


## Gravity Node

Type: **ParticleGravity**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | BoolAttr | applyGravity |
| Main |  | DoubleAttr | directionX |
| Main |  | DoubleAttr | directionY |
| Main |  | DoubleAttr | directionZ |
| Main |  | BoolAttr | relativeGravity |
| Main |  | DoubleAttr | relativeMagnitude |
| Main |  | DoubleAttr | relativeGravityEpsilon |
| Main |  | DoubleAttr | relativeGravityMaxRadius |


## Greyscale Node

Type: **COLOR2BW**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | PERCENT |
| Main |  | BoolAttr | MATTE_OUTPUT |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


## Grid Node

Type: **Grid**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | Size |
| Main |  | DoubleAttr | Aspect |
| Main |  | BoolAttr | ShowText |
| Main |  | ColorAttr | GridColor |
| Sub | GridColor | IntAttr | GridColor.RED |
| Sub | GridColor | IntAttr | GridColor.GREEN |
| Sub | GridColor | IntAttr | GridColor.BLUE |
| Sub | GridColor | IntAttr | GridColor.ALPHA |
| Sub | GridColor | EnumAttr | GridColor.PREFERRED_UI |
| Main |  | ColorAttr | BGColor |
| Sub | BGColor | IntAttr | BGColor.RED |
| Sub | BGColor | IntAttr | BGColor.GREEN |
| Sub | BGColor | IntAttr | BGColor.BLUE |
| Sub | BGColor | IntAttr | BGColor.ALPHA |
| Sub | BGColor | EnumAttr | BGColor.PREFERRED_UI |
| Main |  | BoolAttr | Opaque |
| Main |  | BoolAttr | FitVertical |


## Highlight Node

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


## Hold-Timing Node

Type: **HoldTiming**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | HoldMode |
| Main |  | IntAttr | HoldValue |
| Main |  | IntAttr | HoldKeyframes |
| Main |  | Attribute | BakeOffsets |
| Main |  | BoolAttr | PreventSelection |
| Main |  | BoolAttr | HideTimeline |


## Hold-Transformation-Timing Node

Type: **HoldTransformationTiming**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | HoldMode |
| Main |  | IntAttr | HoldValue |
| Main |  | IntAttr | HoldKeyframes |
| Main |  | Attribute | BakeOffsets |
| Main |  | BoolAttr | PreventSelection |
| Main |  | BoolAttr | HideTimeline |


## Hue-Saturation Node

Type: **HUE_SATURATION**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Attribute | MasterRangeColor |
| Sub | MasterRangeColor | DoubleAttr | MasterRangeColor.HUE_SHIFT |
| Sub | MasterRangeColor | DoubleAttr | MasterRangeColor.SATURATION |
| Sub | MasterRangeColor | DoubleAttr | MasterRangeColor.LIGHTNESS |
| Main |  | Attribute | RedRangeColor |
| Sub | RedRangeColor | DoubleAttr | RedRangeColor.HUE_SHIFT |
| Sub | RedRangeColor | DoubleAttr | RedRangeColor.SATURATION |
| Sub | RedRangeColor | DoubleAttr | RedRangeColor.LIGHTNESS |
| Sub | RedRangeColor | DoubleAttr | RedRangeColor.LOW_RANGE |
| Sub | RedRangeColor | DoubleAttr | RedRangeColor.HIGH_RANGE |
| Sub | RedRangeColor | DoubleAttr | RedRangeColor.LOW_FALLOFF |
| Sub | RedRangeColor | DoubleAttr | RedRangeColor.HIGH_FALLOFF |
| Main |  | Attribute | GreenRangeColor |
| Sub | GreenRangeColor | DoubleAttr | GreenRangeColor.HUE_SHIFT |
| Sub | GreenRangeColor | DoubleAttr | GreenRangeColor.SATURATION |
| Sub | GreenRangeColor | DoubleAttr | GreenRangeColor.LIGHTNESS |
| Sub | GreenRangeColor | DoubleAttr | GreenRangeColor.LOW_RANGE |
| Sub | GreenRangeColor | DoubleAttr | GreenRangeColor.HIGH_RANGE |
| Sub | GreenRangeColor | DoubleAttr | GreenRangeColor.LOW_FALLOFF |
| Sub | GreenRangeColor | DoubleAttr | GreenRangeColor.HIGH_FALLOFF |
| Main |  | Attribute | BlueRangeColor |
| Sub | BlueRangeColor | DoubleAttr | BlueRangeColor.HUE_SHIFT |
| Sub | BlueRangeColor | DoubleAttr | BlueRangeColor.SATURATION |
| Sub | BlueRangeColor | DoubleAttr | BlueRangeColor.LIGHTNESS |
| Sub | BlueRangeColor | DoubleAttr | BlueRangeColor.LOW_RANGE |
| Sub | BlueRangeColor | DoubleAttr | BlueRangeColor.HIGH_RANGE |
| Sub | BlueRangeColor | DoubleAttr | BlueRangeColor.LOW_FALLOFF |
| Sub | BlueRangeColor | DoubleAttr | BlueRangeColor.HIGH_FALLOFF |
| Main |  | Attribute | CyanRangeColor |
| Sub | CyanRangeColor | DoubleAttr | CyanRangeColor.HUE_SHIFT |
| Sub | CyanRangeColor | DoubleAttr | CyanRangeColor.SATURATION |
| Sub | CyanRangeColor | DoubleAttr | CyanRangeColor.LIGHTNESS |
| Sub | CyanRangeColor | DoubleAttr | CyanRangeColor.LOW_RANGE |
| Sub | CyanRangeColor | DoubleAttr | CyanRangeColor.HIGH_RANGE |
| Sub | CyanRangeColor | DoubleAttr | CyanRangeColor.LOW_FALLOFF |
| Sub | CyanRangeColor | DoubleAttr | CyanRangeColor.HIGH_FALLOFF |
| Main |  | Attribute | MagentaRangeColor |
| Sub | MagentaRangeColor | DoubleAttr | MagentaRangeColor.HUE_SHIFT |
| Sub | MagentaRangeColor | DoubleAttr | MagentaRangeColor.SATURATION |
| Sub | MagentaRangeColor | DoubleAttr | MagentaRangeColor.LIGHTNESS |
| Sub | MagentaRangeColor | DoubleAttr | MagentaRangeColor.LOW_RANGE |
| Sub | MagentaRangeColor | DoubleAttr | MagentaRangeColor.HIGH_RANGE |
| Sub | MagentaRangeColor | DoubleAttr | MagentaRangeColor.LOW_FALLOFF |
| Sub | MagentaRangeColor | DoubleAttr | MagentaRangeColor.HIGH_FALLOFF |
| Main |  | Attribute | YellowRangeColor |
| Sub | YellowRangeColor | DoubleAttr | YellowRangeColor.HUE_SHIFT |
| Sub | YellowRangeColor | DoubleAttr | YellowRangeColor.SATURATION |
| Sub | YellowRangeColor | DoubleAttr | YellowRangeColor.LIGHTNESS |
| Sub | YellowRangeColor | DoubleAttr | YellowRangeColor.LOW_RANGE |
| Sub | YellowRangeColor | DoubleAttr | YellowRangeColor.HIGH_RANGE |
| Sub | YellowRangeColor | DoubleAttr | YellowRangeColor.LOW_FALLOFF |
| Sub | YellowRangeColor | DoubleAttr | YellowRangeColor.HIGH_FALLOFF |
| Main |  | BoolAttr | ColorizeEnable |
| Main |  | Attribute | ColorizeHsl |
| Sub | ColorizeHsl | DoubleAttr | ColorizeHsl.HUE |
| Sub | ColorizeHsl | DoubleAttr | ColorizeHsl.SATURATION |
| Sub | ColorizeHsl | DoubleAttr | ColorizeHsl.LIGHTNESS |
| Main |  | Attribute | ResetRed |
| Main |  | Attribute | ResetGreen |
| Main |  | Attribute | ResetBlue |
| Main |  | Attribute | ResetCyan |
| Main |  | Attribute | ResetMagenta |
| Main |  | Attribute | ResetYellow |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


## Image-Fracture Node

Type: **ParticleImageEmitter**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | DoubleAttr | ageAtBirth |
| Main |  | DoubleAttr | ageAtBirthStd |
| Main |  | DoubleAttr | mass |
| Main |  | EnumAttr | typeChoosingStrategy |
| Main |  | IntAttr | particleType0 |
| Main |  | IntAttr | particleType1 |
| Main |  | DoubleAttr | particleSize |
| Main |  | BoolAttr | overrideVelocity |
| Main |  | EnumAttr | BLEND_MODE |
| Main |  | DoubleAttr | blendIntensity |
| Main |  | EnumAttr | colouringStrategy |
| Main |  | ColorAttr | particleColour |
| Sub | particleColour | IntAttr | particleColour.RED |
| Sub | particleColour | IntAttr | particleColour.GREEN |
| Sub | particleColour | IntAttr | particleColour.BLUE |
| Sub | particleColour | IntAttr | particleColour.ALPHA |
| Sub | particleColour | EnumAttr | particleColour.PREFERRED_UI |
| Main |  | BoolAttr | alignWithDirection |
| Main |  | BoolAttr | useRotation |
| Main |  | BoolAttr | directionalScale |
| Main |  | DoubleAttr | directionalScaleFactor |
| Main |  | BoolAttr | keepVolume |
| Main |  | EnumAttr | blur |
| Main |  | DoubleAttr | blurIntensity |
| Main |  | DoubleAttr | blurFallof |
| Main |  | BoolAttr | flipWithDirectionX |
| Main |  | BoolAttr | flipWithDirectionY |
| Main |  | EnumAttr | alignWithDirectionAxis |


## Image-Switch Node

Type: **ImageSwitch**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | Port_Index |


## Increase-Opacity Node

Type: **IncreaseOpacity**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | FACTOR |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


## Kill Node

Type: **ParticleKill**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | BoolAttr | handleNaturalDeth |
| Main |  | BoolAttr | killYounger |
| Main |  | IntAttr | killYoungerThan |
| Main |  | BoolAttr | killOlder |
| Main |  | IntAttr | killOlderThan |


## Layer-Selector Node

Type: **LAYER_SELECTOR**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | FLATTEN |
| Main |  | BoolAttr | APPLY_TO_MATTE_PORTS |
| Main |  | EnumAttr | ANTIALIASING_QUALITY |
| Main |  | DoubleAttr | ANTIALIASING_EXPONENT |
| Main |  | BoolAttr | READ_OVERLAY |
| Main |  | BoolAttr | READ_LINEART |
| Main |  | BoolAttr | READ_COLOURART |
| Main |  | BoolAttr | READ_UNDERLAY |


## LensFlare Node

Type: **LensFlare**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | BLEND_MODE |
| Main |  | EnumAttr | CLAMPING_MODE |
| Main |  | EnumAttr | FLASH_BLEND_MODE |
| Main |  | BoolAttr | UseRGBA |
| Main |  | BoolAttr | BrightEnable |
| Main |  | DoubleAttr | Brightness |
| Main |  | ColorAttr | BrightColor |
| Sub | BrightColor | IntAttr | BrightColor.RED |
| Sub | BrightColor | IntAttr | BrightColor.GREEN |
| Sub | BrightColor | IntAttr | BrightColor.BLUE |
| Sub | BrightColor | IntAttr | BrightColor.ALPHA |
| Sub | BrightColor | EnumAttr | BrightColor.PREFERRED_UI |
| Main |  | DoubleAttr | PositionX |
| Main |  | DoubleAttr | PositionY |
| Main |  | DoubleAttr | PositionZ |
| Main |  | EnumAttr | FlareConfig |
| Main |  | BoolAttr | Enable1 |
| Main |  | DoubleAttr | Size1 |
| Main |  | DoubleAttr | Position1 |
| Main |  | IntAttr | Drawing1 |
| Main |  | DoubleAttr | Blur1 |
| Main |  | BoolAttr | Enable2 |
| Main |  | DoubleAttr | Size2 |
| Main |  | DoubleAttr | Position2 |
| Main |  | IntAttr | Drawing2 |
| Main |  | DoubleAttr | Blur2 |
| Main |  | BoolAttr | Enable3 |
| Main |  | DoubleAttr | Size3 |
| Main |  | DoubleAttr | Position3 |
| Main |  | IntAttr | Drawing3 |
| Main |  | DoubleAttr | Blur3 |
| Main |  | BoolAttr | Enable4 |
| Main |  | DoubleAttr | Size4 |
| Main |  | DoubleAttr | Position4 |
| Main |  | IntAttr | Drawing4 |
| Main |  | DoubleAttr | Blur4 |
| Main |  | BoolAttr | Enable5 |
| Main |  | DoubleAttr | Size5 |
| Main |  | DoubleAttr | Position5 |
| Main |  | IntAttr | Drawing5 |
| Main |  | DoubleAttr | Blur5 |
| Main |  | BoolAttr | Enable6 |
| Main |  | DoubleAttr | Size6 |
| Main |  | DoubleAttr | Position6 |
| Main |  | IntAttr | Drawing6 |
| Main |  | DoubleAttr | Blur6 |
| Main |  | BoolAttr | Enable7 |
| Main |  | DoubleAttr | Size7 |
| Main |  | DoubleAttr | Position7 |
| Main |  | IntAttr | Drawing7 |
| Main |  | DoubleAttr | Blur7 |
| Main |  | BoolAttr | Enable8 |
| Main |  | DoubleAttr | Size8 |
| Main |  | DoubleAttr | Position8 |
| Main |  | IntAttr | Drawing8 |
| Main |  | DoubleAttr | Blur8 |
| Main |  | BoolAttr | Enable9 |
| Main |  | DoubleAttr | Size9 |
| Main |  | DoubleAttr | Position9 |
| Main |  | IntAttr | Drawing9 |
| Main |  | DoubleAttr | Blur9 |
| Main |  | BoolAttr | Enable10 |
| Main |  | DoubleAttr | Size10 |
| Main |  | DoubleAttr | Position10 |
| Main |  | IntAttr | Drawing10 |
| Main |  | DoubleAttr | Blur10 |


## Light-Position Node

Type: **LightPosition**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Pos3DAttr | position0 |
| Sub | position0 | BoolAttr | position0/SEPARATE |
| Sub | position0 | DoubleAttr | position0.X |
| Sub | position0 | DoubleAttr | position0.Y |
| Sub | position0 | DoubleAttr | position0.Z |
| Sub | position0 | Attribute | position0.3DPATH |
| Main |  | Pos3DAttr | position1 |
| Sub | position1 | BoolAttr | position1/SEPARATE |
| Sub | position1 | DoubleAttr | position1.X |
| Sub | position1 | DoubleAttr | position1.Y |
| Sub | position1 | DoubleAttr | position1.Z |
| Sub | position1 | Attribute | position1.3DPATH |


## Light-Shader Node

Type: **LightShader**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | LightType |
| Main |  | DoubleAttr | FloodAngle |
| Main |  | DoubleAttr | FloodSharpness |
| Main |  | DoubleAttr | FloodRadius |
| Main |  | DoubleAttr | PointElevation |
| Main |  | DoubleAttr | AngleThreshold |
| Main |  | EnumAttr | ShadeType |
| Main |  | DoubleAttr | Bias |
| Main |  | DoubleAttr | Exponent |
| Main |  | ColorAttr | LightColor |
| Sub | LightColor | IntAttr | LightColor.RED |
| Sub | LightColor | IntAttr | LightColor.GREEN |
| Sub | LightColor | IntAttr | LightColor.BLUE |
| Sub | LightColor | IntAttr | LightColor.ALPHA |
| Sub | LightColor | EnumAttr | LightColor.PREFERRED_UI |
| Main |  | BoolAttr | Flatten |
| Main |  | BoolAttr | UseImageColor |
| Main |  | DoubleAttr | ImageColorWeight |
| Main |  | BoolAttr | AdjustLevel |
| Main |  | DoubleAttr | AdjustedLevel |
| Main |  | DoubleAttr | Scale |
| Main |  | BoolAttr | UseSurface |
| Main |  | DoubleAttr | SpecularTransparency |
| Main |  | DoubleAttr | Specularity |
| Main |  | DoubleAttr | DistanceFalloff |


## Line-Art Node

Type: **LINE_ART**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | FLATTEN |
| Main |  | BoolAttr | APPLY_TO_MATTE_PORTS |
| Main |  | EnumAttr | ANTIALIASING_QUALITY |
| Main |  | DoubleAttr | ANTIALIASING_EXPONENT |


## Loop Node

Type: **Loop**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | LoopRangeStart |
| Main |  | IntAttr | LoopRangeEnd |
| Main |  | IntAttr | LoopOffset |
| Main |  | BoolAttr | LoopOutput |
| Main |  | IntAttr | LoopOutputStart |
| Main |  | IntAttr | LoopOutputEnd |
| Main |  | EnumAttr | ResumeBehaviour |
| Main |  | EnumAttr | CycleMode |
| Main |  | BoolAttr | PreventSelection |
| Main |  | BoolAttr | HideTimeline |


## Loop-Transformation Node

Type: **LoopTransformation**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | LoopRangeStart |
| Main |  | IntAttr | LoopRangeEnd |
| Main |  | IntAttr | LoopOffset |
| Main |  | BoolAttr | LoopOutput |
| Main |  | IntAttr | LoopOutputStart |
| Main |  | IntAttr | LoopOutputEnd |
| Main |  | EnumAttr | ResumeBehaviour |
| Main |  | EnumAttr | CycleModePeg |
| Main |  | BoolAttr | PreventSelection |
| Main |  | BoolAttr | HideTimeline |


## Luminance-Threshold Node

Type: **LuminanceThreshold**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | LuminanceThresholdThresh |
| Main |  | BoolAttr | LuminanceThresholdSoften |
| Main |  | DoubleAttr | LuminanceThresholdGamma |
| Main |  | BoolAttr | LuminanceThresholdGrey |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


## MasterController Node

Type: **MasterController**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | TextAttr | SPECS_EDITOR |
| Main |  | Attribute | SCRIPT_EDITOR |
| Sub | SCRIPT_EDITOR | TextAttr | SCRIPT_EDITOR.FILENAME |
| Sub | SCRIPT_EDITOR | TextAttr | SCRIPT_EDITOR.EDITOR |
| Main |  | Attribute | INIT_SCRIPT |
| Sub | INIT_SCRIPT | TextAttr | INIT_SCRIPT.FILENAME |
| Sub | INIT_SCRIPT | TextAttr | INIT_SCRIPT.EDITOR |
| Main |  | Attribute | CLEANUP_SCRIPT |
| Sub | CLEANUP_SCRIPT | TextAttr | CLEANUP_SCRIPT.FILENAME |
| Sub | CLEANUP_SCRIPT | TextAttr | CLEANUP_SCRIPT.EDITOR |
| Main |  | Attribute | UI_SCRIPT |
| Sub | UI_SCRIPT | TextAttr | UI_SCRIPT.FILENAME |
| Sub | UI_SCRIPT | TextAttr | UI_SCRIPT.EDITOR |
| Main |  | TextAttr | UI_DATA |
| Main |  | TextAttr | FILES |
| Main |  | EnumAttr | SHOW_CONTROLS_MODE |


## Matte-Blur Node

Type: **MATTE_BLUR**

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


## Matte-Resize Node

Type: **MATTE_RESIZE**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | RADIUS |


## Median Node

Type: **MedianFilter**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | DoubleAttr | Radius |
| Main |  | IntAttr | BitDepth |


## Mesh-Warp Node

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


## Motion-Blur Node

Type: **MOTIONBLUR-PLUGIN**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | NB_FRAMES_TRAIL |
| Main |  | IntAttr | SAMPLES |
| Main |  | DoubleAttr | FALLOFF |
| Main |  | BoolAttr | USE_CAMERA_TRANSFORMATION |
| Main |  | BoolAttr | PREROLL_MOTION |


## Motion-Blur-Legacy Node

Type: **MOTION_BLUR**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | NB_FRAMES_TRAIL |
| Main |  | DoubleAttr | SAMPLES |
| Main |  | DoubleAttr | FALLOFF |
| Main |  | DoubleAttr | INTENSITY |
| Main |  | BoolAttr | MIRROR |


## Move-Particles Node

Type: **ParticleMove**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | BoolAttr | moveAge |
| Main |  | BoolAttr | movePosition |
| Main |  | BoolAttr | moveAngle |
| Main |  | BoolAttr | followEachOther |
| Main |  | DoubleAttr | followIntensity |


## Multi-Layer-Write Node

Type: **MultiLayerWrite**

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
| Main |  | TextAttr | INPUT_NAMES |


## Multi-Points-Constraint Node

Type: **PointConstraintMulti**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | EnumAttr | FLATTENTYPE |
| Main |  | BoolAttr | CONVEXHULL |
| Main |  | BoolAttr | ALLOWPERSP |


## Negate Node

Type: **NEGATE**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | COLOR |
| Main |  | BoolAttr | COLOR_ALPHA |
| Main |  | BoolAttr | COLOR_CLAMP_TO_ALPHA |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


## Normal-Map Node

Type: **ComputeNormals**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | TextAttr | ObjectList |
| Main |  | BoolAttr | DepthInBlue |
| Main |  | DoubleAttr | BlurScale |
| Main |  | BoolAttr | ClipBlurredWithGeometry |
| Main |  | DoubleAttr | ElevationScale |
| Main |  | DoubleAttr | ElevationSmoothness |
| Main |  | BoolAttr | GenerateNormals |
| Main |  | EnumAttr | NormalQuality |
| Main |  | BoolAttr | UseTruckFactor |
| Main |  | TextAttr | ColorInformation |


## Normal-Map-Converter Node

Type: **NormalFloat**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | ConversionType |
| Main |  | DoubleAttr | Offset |
| Main |  | DoubleAttr | Length |
| Main |  | BoolAttr | InvertRed |
| Main |  | BoolAttr | InvertGreen |
| Main |  | BoolAttr | InvertBlue |


## Note Node

Type: **NOTE**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | TextAttr | TEXT |


## OGL-Controller Node

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


## Offset Node

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


## OpenGL-Cache-Lock Node

Type: **GLCacheLock**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | COMPOSITE_3D |


## Orbit Node

Type: **ParticleOrbit**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | EnumAttr | strategy |
| Main |  | DoubleAttr | magnitude |
| Main |  | DoubleAttr | v0x |
| Main |  | DoubleAttr | v0y |
| Main |  | DoubleAttr | v0z |
| Main |  | DoubleAttr | v1x |
| Main |  | DoubleAttr | v1y |
| Main |  | DoubleAttr | v1z |


## OrthoLock Node

Type: **ORTHOLOCK**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | ROTATION_AXIS |
| Main |  | DoubleAttr | MAX_ANGLE |


## Overlay-Layer Node

Type: **OVERLAY**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | FLATTEN |
| Main |  | BoolAttr | APPLY_TO_MATTE_PORTS |
| Main |  | EnumAttr | ANTIALIASING_QUALITY |
| Main |  | DoubleAttr | ANTIALIASING_EXPONENT |


## Particle-Baker Node

Type: **ParticleBaker**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | maxNumParticles |
| Main |  | EnumAttr | simulationQuality |
| Main |  | IntAttr | seed |
| Main |  | IntAttr | transientFrames |
| Main |  | BoolAttr | moveAge |
| Main |  | BoolAttr | movePosition |
| Main |  | BoolAttr | moveAngle |
| Main |  | BoolAttr | roundAge |


## Particle-Visualizer Node

Type: **ParticleVisualizer**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | forceDots |
| Main |  | EnumAttr | sortingStrategy |
| Main |  | BoolAttr | fixAlpha |
| Main |  | BoolAttr | useViewScaling |
| Main |  | DoubleAttr | globalSize |


## Peg Node

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


## Pixelate Node

Type: **PIXELATE**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | DoubleAttr | FACTOR |


## Planar-Region Node

Type: **ParticlePlanarRegion**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | shapeType |
| Main |  | DoubleAttr | sizeX |
| Main |  | DoubleAttr | sizeY |
| Main |  | DoubleAttr | x1 |
| Main |  | DoubleAttr | y1 |
| Main |  | DoubleAttr | x2 |
| Main |  | DoubleAttr | y2 |
| Main |  | DoubleAttr | x3 |
| Main |  | DoubleAttr | y3 |
| Main |  | DoubleAttr | minRadius |
| Main |  | DoubleAttr | maxRadius |
| Main |  | BoolAttr | mirrorNegativeFrames |


## Point-Kinematic-Output Node

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


## Pre-render-Cache Node

Type: **PRECOMP**

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
| Main |  | BoolAttr | PRERENDER_CURRENT_FRAME |
| Main |  | BoolAttr | PRERENDER_SELECTED_FRAMES |
| Main |  | IntAttr | PRERENDER_FRAMES_FROM |
| Main |  | IntAttr | PRERENDER_FRAMES_TO |
| Main |  | Attribute | RENDER_PRERENDER_CACHE |
| Main |  | Attribute | CLEAR_PRERENDER_CACHE |


## Quadmap Node

Type: **QUADMAP**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | Pos2DAttr | SRC_POINT_1 |
| Sub | SRC_POINT_1 | BoolAttr | SRC_POINT_1/SEPARATE |
| Sub | SRC_POINT_1 | DoubleAttr | SRC_POINT_1.X |
| Sub | SRC_POINT_1 | DoubleAttr | SRC_POINT_1.Y |
| Sub | SRC_POINT_1 | Attribute | SRC_POINT_1.2DPOINT |
| Main |  | Pos2DAttr | SRC_POINT_2 |
| Sub | SRC_POINT_2 | BoolAttr | SRC_POINT_2/SEPARATE |
| Sub | SRC_POINT_2 | DoubleAttr | SRC_POINT_2.X |
| Sub | SRC_POINT_2 | DoubleAttr | SRC_POINT_2.Y |
| Sub | SRC_POINT_2 | Attribute | SRC_POINT_2.2DPOINT |
| Main |  | Pos2DAttr | SRC_POINT_3 |
| Sub | SRC_POINT_3 | BoolAttr | SRC_POINT_3/SEPARATE |
| Sub | SRC_POINT_3 | DoubleAttr | SRC_POINT_3.X |
| Sub | SRC_POINT_3 | DoubleAttr | SRC_POINT_3.Y |
| Sub | SRC_POINT_3 | Attribute | SRC_POINT_3.2DPOINT |
| Main |  | Pos2DAttr | SRC_POINT_4 |
| Sub | SRC_POINT_4 | BoolAttr | SRC_POINT_4/SEPARATE |
| Sub | SRC_POINT_4 | DoubleAttr | SRC_POINT_4.X |
| Sub | SRC_POINT_4 | DoubleAttr | SRC_POINT_4.Y |
| Sub | SRC_POINT_4 | Attribute | SRC_POINT_4.2DPOINT |
| Main |  | Pos2DAttr | POINT_1 |
| Sub | POINT_1 | BoolAttr | POINT_1/SEPARATE |
| Sub | POINT_1 | DoubleAttr | POINT_1.X |
| Sub | POINT_1 | DoubleAttr | POINT_1.Y |
| Sub | POINT_1 | Attribute | POINT_1.2DPOINT |
| Main |  | Pos2DAttr | POINT_2 |
| Sub | POINT_2 | BoolAttr | POINT_2/SEPARATE |
| Sub | POINT_2 | DoubleAttr | POINT_2.X |
| Sub | POINT_2 | DoubleAttr | POINT_2.Y |
| Sub | POINT_2 | Attribute | POINT_2.2DPOINT |
| Main |  | Pos2DAttr | POINT_3 |
| Sub | POINT_3 | BoolAttr | POINT_3/SEPARATE |
| Sub | POINT_3 | DoubleAttr | POINT_3.X |
| Sub | POINT_3 | DoubleAttr | POINT_3.Y |
| Sub | POINT_3 | Attribute | POINT_3.2DPOINT |
| Main |  | Pos2DAttr | POINT_4 |
| Sub | POINT_4 | BoolAttr | POINT_4/SEPARATE |
| Sub | POINT_4 | DoubleAttr | POINT_4.X |
| Sub | POINT_4 | DoubleAttr | POINT_4.Y |
| Sub | POINT_4 | Attribute | POINT_4.2DPOINT |
| Main |  | Pos2DAttr | PIVOT |
| Sub | PIVOT | BoolAttr | PIVOT/SEPARATE |
| Sub | PIVOT | DoubleAttr | PIVOT.X |
| Sub | PIVOT | DoubleAttr | PIVOT.Y |


## Quake Node

Type: **Quake**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | Hold |
| Main |  | BoolAttr | Interpolate |
| Main |  | DoubleAttr | MoveAmplitude |
| Main |  | BoolAttr | ApplyX |
| Main |  | BoolAttr | ApplyY |
| Main |  | BoolAttr | ApplyZ |
| Main |  | DoubleAttr | RotationAmplitude |
| Main |  | IntAttr | Seed |


## RGB-Difference-Keyer Node

Type: **RGB_DIFFERENCE_KEYER**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | ColorAttr | COLOR |
| Sub | COLOR | IntAttr | COLOR.RED |
| Sub | COLOR | IntAttr | COLOR.GREEN |
| Sub | COLOR | IntAttr | COLOR.BLUE |
| Sub | COLOR | IntAttr | COLOR.ALPHA |
| Sub | COLOR | EnumAttr | COLOR.PREFERRED_UI |
| Main |  | BoolAttr | PRE_MULTIPLIED_ALPHA |
| Main |  | DoubleAttr | KEY_DIFFERENCE_WEIGHTING |
| Main |  | DoubleAttr | EDGE_KEY_THRESHOLD |
| Main |  | DoubleAttr | KEY_PRIMARY_SPILL_REDUCTION |
| Main |  | DoubleAttr | KEY_LOW_INTENSITY_SCALED_THRESH |
| Main |  | BoolAttr | BLEND_INPUT_ALPHA |
| Main |  | BoolAttr | DESPILL_MATTE |
| Main |  | ColorAttr | SPILL_COLOR |
| Sub | SPILL_COLOR | IntAttr | SPILL_COLOR.RED |
| Sub | SPILL_COLOR | IntAttr | SPILL_COLOR.GREEN |
| Sub | SPILL_COLOR | IntAttr | SPILL_COLOR.BLUE |
| Sub | SPILL_COLOR | IntAttr | SPILL_COLOR.ALPHA |
| Sub | SPILL_COLOR | EnumAttr | SPILL_COLOR.PREFERRED_UI |
| Main |  | DoubleAttr | MATTE_CLIP_BLACK |
| Main |  | DoubleAttr | MATTE_CLIP_WHITE |
| Main |  | BoolAttr | INVERT_MATTE |


## Random-Parameter Node

Type: **ParticleRandom**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | EnumAttr | parameterToRandomize |


## Refract Node

Type: **REFRACT**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | DoubleAttr | INTENSITY |
| Main |  | DoubleAttr | HEIGHT |


## Remove-Transparency Node

Type: **REMOVE_TRANSPARENCY**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | THRESHOLD |
| Main |  | BoolAttr | REMOVE_COLOR_TRANSPARENCY |
| Main |  | BoolAttr | REMOVE_ALPHA_TRANSPARENCY |


## RenderPreview Node

Type: **OpenGLPreview**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | refreshStrategy |
| Main |  | EnumAttr | scaling |
| Main |  | EnumAttr | renderStrategy |
| Main |  | Attribute | computeAllImages |


## Repulse Node

Type: **ParticleRepulse**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | DoubleAttr | magnitude |
| Main |  | DoubleAttr | lookAhead |
| Main |  | DoubleAttr | epsilon |


## Retime Node

Type: **Retime**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | RetimeMode |
| Main |  | DoubleAttr | Value |
| Main |  | BoolAttr | HoldFirstFrame |
| Main |  | BoolAttr | PreventSelection |
| Main |  | BoolAttr | HideTimeline |


## Retime-Transformation Node

Type: **RetimeTransformation**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | RetimeMode |
| Main |  | DoubleAttr | Value |
| Main |  | BoolAttr | PreventSelection |
| Main |  | BoolAttr | HideTimeline |


## Rigid-Point-Deform Node

Type: **RigidPointDeform**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | DoubleAttr | MINDIST |
| Main |  | DoubleAttr | MAXDIST |


## Rotation-Velocity Node

Type: **ParticleRotationVelocity**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | DoubleAttr | w0 |
| Main |  | DoubleAttr | w1 |
| Main |  | EnumAttr | axisStrategy |
| Main |  | DoubleAttr | v0x |
| Main |  | DoubleAttr | v0y |
| Main |  | DoubleAttr | v0z |
| Main |  | DoubleAttr | v1x |
| Main |  | DoubleAttr | v1y |
| Main |  | DoubleAttr | v1z |


## Scale-Output Node

Type: **SCALE**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | BY_VALUE |
| Main |  | TextAttr | RESOLUTION_NAME |
| Main |  | IntAttr | RES_X |
| Main |  | IntAttr | RES_Y |


## ScriptModule Node

Type: **SCRIPT_MODULE**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | TextAttr | SPECS_EDITOR |
| Main |  | Attribute | SCRIPT_EDITOR |
| Sub | SCRIPT_EDITOR | TextAttr | SCRIPT_EDITOR.FILENAME |
| Sub | SCRIPT_EDITOR | TextAttr | SCRIPT_EDITOR.EDITOR |
| Main |  | Attribute | INIT_SCRIPT |
| Sub | INIT_SCRIPT | TextAttr | INIT_SCRIPT.FILENAME |
| Sub | INIT_SCRIPT | TextAttr | INIT_SCRIPT.EDITOR |
| Main |  | Attribute | CLEANUP_SCRIPT |
| Sub | CLEANUP_SCRIPT | TextAttr | CLEANUP_SCRIPT.FILENAME |
| Sub | CLEANUP_SCRIPT | TextAttr | CLEANUP_SCRIPT.EDITOR |
| Main |  | Attribute | UI_SCRIPT |
| Sub | UI_SCRIPT | TextAttr | UI_SCRIPT.FILENAME |
| Sub | UI_SCRIPT | TextAttr | UI_SCRIPT.EDITOR |
| Main |  | TextAttr | UI_DATA |
| Main |  | TextAttr | FILES |


## Scripted-Action[Beta] Node

Type: **ParticleJavascript**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | Attribute | PARTICLE_ACTION_SCRIPT |
| Sub | PARTICLE_ACTION_SCRIPT | TextAttr | PARTICLE_ACTION_SCRIPT.FILENAME |
| Sub | PARTICLE_ACTION_SCRIPT | TextAttr | PARTICLE_ACTION_SCRIPT.EDITOR |
| Main |  | TextAttr | FILES |


## Shadow Node

Type: **SHADOW**

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


## Shake Node

Type: **Shake**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | Frequency |
| Main |  | IntAttr | Octaves |
| Main |  | DoubleAttr | Multiplier |
| Main |  | DoubleAttr | PositionX |
| Main |  | DoubleAttr | PositionY |
| Main |  | DoubleAttr | PositionZ |
| Main |  | DoubleAttr | RotationX |
| Main |  | DoubleAttr | RotationY |
| Main |  | DoubleAttr | RotationZ |
| Main |  | DoubleAttr | PivotX |
| Main |  | DoubleAttr | PivotY |
| Main |  | DoubleAttr | PivotZ |
| Main |  | IntAttr | Steps |
| Main |  | IntAttr | Seed |


## Shape-Aware-Deformation Node

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


## Shape-Curve Node

Type: **ShapeCurve**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | FlattenZ |
| Main |  | Pos3DAttr | Position1 |
| Sub | Position1 | BoolAttr | Position1/SEPARATE |
| Sub | Position1 | DoubleAttr | Position1.X |
| Sub | Position1 | DoubleAttr | Position1.Y |
| Sub | Position1 | DoubleAttr | Position1.Z |
| Sub | Position1 | Attribute | Position1.3DPATH |
| Main |  | Pos3DAttr | Position2 |
| Sub | Position2 | BoolAttr | Position2/SEPARATE |
| Sub | Position2 | DoubleAttr | Position2.X |
| Sub | Position2 | DoubleAttr | Position2.Y |
| Sub | Position2 | DoubleAttr | Position2.Z |
| Sub | Position2 | Attribute | Position2.3DPATH |
| Main |  | Pos3DAttr | Position3 |
| Sub | Position3 | BoolAttr | Position3/SEPARATE |
| Sub | Position3 | DoubleAttr | Position3.X |
| Sub | Position3 | DoubleAttr | Position3.Y |
| Sub | Position3 | DoubleAttr | Position3.Z |
| Sub | Position3 | Attribute | Position3.3DPATH |
| Main |  | BoolAttr | CloseShape |


## Shape-Line Node

Type: **ShapeLine**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | FlattenZ |
| Main |  | Pos3DAttr | Position1 |
| Sub | Position1 | BoolAttr | Position1/SEPARATE |
| Sub | Position1 | DoubleAttr | Position1.X |
| Sub | Position1 | DoubleAttr | Position1.Y |
| Sub | Position1 | DoubleAttr | Position1.Z |
| Sub | Position1 | Attribute | Position1.3DPATH |
| Main |  | BoolAttr | CloseShape |


## Shape-Render Node

Type: **ShapeRender**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | EdgeType |
| Main |  | DoubleAttr | Scale |
| Main |  | DoubleAttr | DISCRETIZATIONSCALE |
| Main |  | DoubleAttr | PreBlur |
| Main |  | DoubleAttr | PostBlur |


## Shine Node

Type: **BACKLIGHT**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | BLEND_MODE |
| Main |  | EnumAttr | CLAMPING_MODE |
| Main |  | EnumAttr | FLASH_BLEND_MODE |
| Main |  | BoolAttr | Highlights |
| Main |  | DoubleAttr | Highlight_Threshold |
| Main |  | Pos2DAttr | Focus |
| Sub | Focus | BoolAttr | Focus/SEPARATE |
| Sub | Focus | DoubleAttr | Focus.X |
| Sub | Focus | DoubleAttr | Focus.Y |
| Sub | Focus | Attribute | Focus.2DPOINT |
| Main |  | DoubleAttr | Blurriness |
| Main |  | DoubleAttr | Fall_Off |
| Main |  | DoubleAttr | Alpha_Gamma |
| Main |  | DoubleAttr | Alpha_Black_Out |
| Main |  | DoubleAttr | Alpha_White_Out |
| Main |  | BoolAttr | USE_MATTE_COLOR |
| Main |  | ColorAttr | COLOR |
| Sub | COLOR | IntAttr | COLOR.RED |
| Sub | COLOR | IntAttr | COLOR.GREEN |
| Sub | COLOR | IntAttr | COLOR.BLUE |
| Sub | COLOR | IntAttr | COLOR.ALPHA |
| Sub | COLOR | EnumAttr | COLOR.PREFERRED_UI |
| Main |  | DoubleAttr | COLOUR_GAIN |


## Sink Node

Type: **ParticleSink**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | BoolAttr | ifInside |


## Size Node

Type: **ParticleSize**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | EnumAttr | sizeStrategy |
| Main |  | DoubleAttr | particleSize |


## Sparkle Node

Type: **PLUGIN**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ANGLE |
| Main |  | DoubleAttr | SCALE |
| Main |  | DoubleAttr | FACTOR |
| Main |  | DoubleAttr | DENSITY |
| Main |  | IntAttr | N_POINTS |
| Main |  | DoubleAttr | PROB_APP |
| Main |  | DoubleAttr | POINT_NOISE |
| Main |  | DoubleAttr | CENTER_NOISE |
| Main |  | DoubleAttr | ANGLE_NOISE |
| Main |  | IntAttr | SEED |
| Main |  | BoolAttr | USE_DRAWING_COLOR |
| Main |  | BoolAttr | FLATTEN_SPARKLES_OF_SAME_COLOR |
| Main |  | ColorAttr | SPARKLE_COLOR |
| Sub | SPARKLE_COLOR | IntAttr | SPARKLE_COLOR.RED |
| Sub | SPARKLE_COLOR | IntAttr | SPARKLE_COLOR.GREEN |
| Sub | SPARKLE_COLOR | IntAttr | SPARKLE_COLOR.BLUE |
| Sub | SPARKLE_COLOR | IntAttr | SPARKLE_COLOR.ALPHA |
| Sub | SPARKLE_COLOR | EnumAttr | SPARKLE_COLOR.PREFERRED_UI |


## Sprite-Emitter Node

Type: **ParticleSprite**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | DoubleAttr | ageAtBirth |
| Main |  | DoubleAttr | ageAtBirthStd |
| Main |  | DoubleAttr | mass |
| Main |  | EnumAttr | typeChoosingStrategy |
| Main |  | IntAttr | particleType0 |
| Main |  | IntAttr | particleType1 |
| Main |  | DoubleAttr | particleSize |
| Main |  | BoolAttr | overrideVelocity |
| Main |  | EnumAttr | BLEND_MODE |
| Main |  | DoubleAttr | blendIntensity |
| Main |  | EnumAttr | colouringStrategy |
| Main |  | ColorAttr | particleColour |
| Sub | particleColour | IntAttr | particleColour.RED |
| Sub | particleColour | IntAttr | particleColour.GREEN |
| Sub | particleColour | IntAttr | particleColour.BLUE |
| Sub | particleColour | IntAttr | particleColour.ALPHA |
| Sub | particleColour | EnumAttr | particleColour.PREFERRED_UI |
| Main |  | BoolAttr | alignWithDirection |
| Main |  | BoolAttr | useRotation |
| Main |  | BoolAttr | directionalScale |
| Main |  | DoubleAttr | directionalScaleFactor |
| Main |  | BoolAttr | keepVolume |
| Main |  | EnumAttr | blur |
| Main |  | DoubleAttr | blurIntensity |
| Main |  | DoubleAttr | blurFallof |
| Main |  | BoolAttr | flipWithDirectionX |
| Main |  | BoolAttr | flipWithDirectionY |
| Main |  | EnumAttr | alignWithDirectionAxis |
| Main |  | EnumAttr | renderingStrategy |
| Main |  | EnumAttr | cycleType |
| Main |  | IntAttr | cycleSize |
| Main |  | IntAttr | numberOfParticles |
| Main |  | DoubleAttr | probabilityOfGeneratingParticles |
| Main |  | IntAttr | indexSelector |
| Main |  | DoubleAttr | multiSize |
| Main |  | BoolAttr | copyVelocity |
| Main |  | DoubleAttr | minInitialAngle |
| Main |  | DoubleAttr | maxInitialAngle |
| Main |  | BoolAttr | copyAge |
| Main |  | BoolAttr | applyProbabilityForEachParticle |
| Main |  | DoubleAttr | sourceTimeSpan |
| Main |  | DoubleAttr | sourceSamplesPerFrame |
| Main |  | IntAttr | seed |
| Main |  | DoubleAttr | streakSize |
| Main |  | DoubleAttr | sourceTimeOffset |
| Main |  | BoolAttr | setMaxLifespan |
| Main |  | DoubleAttr | maxLifespan |
| Main |  | DoubleAttr | maxLifespanSigma |


## Static-Transformation Node

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


## Stick Node

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


## Surface-Map Node

Type: **ComputeWorld**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | TextAttr | ObjectList |
| Main |  | DoubleAttr | BlurScale |
| Main |  | BoolAttr | ClipBlurredWithGeometry |
| Main |  | DoubleAttr | ElevationScale |
| Main |  | DoubleAttr | ElevationSmoothness |
| Main |  | BoolAttr | UseTruckFactor |
| Main |  | TextAttr | ColorInformation |


## Surface-Normal Node

Type: **SurfaceNormal**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | NormalQuality |


## Three-Points-Constraints Node

Type: **PointConstraint3**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | EnumAttr | FLATTENTYPE |
| Main |  | EnumAttr | TRANSFORMTYPE |
| Main |  | EnumAttr | PRIMARYPORT |


## Tone Node

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


## Tone-Shader Node

Type: **ToneShader**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | LightType |
| Main |  | DoubleAttr | FloodAngle |
| Main |  | DoubleAttr | FloodSharpness |
| Main |  | DoubleAttr | FloodRadius |
| Main |  | DoubleAttr | PointElevation |
| Main |  | DoubleAttr | AngleThreshold |
| Main |  | EnumAttr | ShadeType |
| Main |  | DoubleAttr | Bias |
| Main |  | DoubleAttr | Exponent |
| Main |  | ColorAttr | LightColor |
| Sub | LightColor | IntAttr | LightColor.RED |
| Sub | LightColor | IntAttr | LightColor.GREEN |
| Sub | LightColor | IntAttr | LightColor.BLUE |
| Sub | LightColor | IntAttr | LightColor.ALPHA |
| Sub | LightColor | EnumAttr | LightColor.PREFERRED_UI |
| Main |  | BoolAttr | Flatten |
| Main |  | BoolAttr | UseImageColor |
| Main |  | DoubleAttr | ImageColorWeight |
| Main |  | BoolAttr | AdjustLevel |
| Main |  | DoubleAttr | AdjustedLevel |
| Main |  | DoubleAttr | Scale |
| Main |  | BoolAttr | UseSurface |
| Main |  | DoubleAttr | SpecularTransparency |
| Main |  | DoubleAttr | Specularity |
| Main |  | DoubleAttr | DistanceFalloff |


## Transform-Loop Node

Type: **TransformLoop**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | AutoRange |
| Main |  | IntAttr | RangeStart |
| Main |  | IntAttr | RangeEnd |
| Main |  | EnumAttr | LoopType |


## Transformation-Gate Node

Type: **TransformGate**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | IntAttr | TARGET_GATE |
| Main |  | IntAttr | DEFAULT_GATE |


## Transformation-Limit Node

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


## Transformation-Switch Node

Type: **TransformationSwitch**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DrawingAttr | Drawing |
| Sub | Drawing | BoolAttr | Drawing/ELEMENT_MODE |
| Sub | Drawing | ElementAttr | Drawing/ELEMENT |
| Sub | Drawing | Attribute | Drawing.CUSTOM_NAME |
| Main |  | Attribute | TransformationNames |
| Sub | TransformationNames | IntAttr | TransformationNames.Size |


## Transparency Node

Type: **FADE**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | TRANSPARENCY |


## Turbulence Node

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


## TurbulentNoise Node

Type: **TurbulentNoise**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | DEPTH |
| Main |  | BoolAttr | INVERT_MATTE_PORT |
| Main |  | EnumAttr | Fractal_Type |
| Main |  | EnumAttr | Noise_Type |
| Main |  | Attribute | Frequency |
| Sub | Frequency | BoolAttr | Frequency/SEPARATE |
| Sub | Frequency | DoubleAttr | Frequency.xyFrequency |
| Sub | Frequency | DoubleAttr | Frequency.xFrequency |
| Sub | Frequency | DoubleAttr | Frequency.yFrequency |
| Main |  | Attribute | Offset |
| Sub | Offset | BoolAttr | Offset/SEPARATE |
| Sub | Offset | DoubleAttr | Offset.xyOffset |
| Sub | Offset | DoubleAttr | Offset.xOffset |
| Sub | Offset | DoubleAttr | Offset.yOffset |
| Main |  | DoubleAttr | Evolution |
| Main |  | DoubleAttr | Evolution_Frequency |
| Main |  | DoubleAttr | Gain |
| Main |  | DoubleAttr | Lacunarity |
| Main |  | DoubleAttr | Octaves |


## Two-Points-Constraint Node

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


## Underlay-Layer Node

Type: **UNDERLAY**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | FLATTEN |
| Main |  | BoolAttr | APPLY_TO_MATTE_PORTS |
| Main |  | EnumAttr | ANTIALIASING_QUALITY |
| Main |  | DoubleAttr | ANTIALIASING_EXPONENT |


## Unsharp-Mask Node

Type: **UnsharpMask**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | AMOUNT |
| Main |  | DoubleAttr | RADIUS |
| Main |  | DoubleAttr | THRESHOLD |
| Main |  | EnumAttr | QUALITY |
| Main |  | BoolAttr | TRUCK_FACTOR |
| Main |  | BoolAttr | INVERT_MATTE_PORT |


## Velocity Node

Type: **ParticleVelocity**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | EnumAttr | velocityType |
| Main |  | DoubleAttr | v0x |
| Main |  | DoubleAttr | v0y |
| Main |  | DoubleAttr | v0z |
| Main |  | DoubleAttr | minSpeed |
| Main |  | DoubleAttr | maxSpeed |
| Main |  | DoubleAttr | theta0 |
| Main |  | DoubleAttr | theta1 |
| Main |  | BoolAttr | bilateral |


## Visibility Node

Type: **VISIBILITY**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | BoolAttr | OGLRENDER |
| Main |  | BoolAttr | SOFTRENDER |


## Volume-Object Node

Type: **ObjectDefinition**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | ObjectID |
| Main |  | BoolAttr | CutVolumeCues |
| Main |  | BoolAttr | UseGeometry |
| Main |  | DoubleAttr | GeometryIntensity |
| Main |  | DoubleAttr | ElevationMin |
| Main |  | DoubleAttr | ElevationMax |
| Main |  | DoubleAttr | Smoothness |
| Main |  | BoolAttr | InvertMask |


## Vortex Node

Type: **ParticleVortex**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | DoubleAttr | vortexX |
| Main |  | DoubleAttr | vortexY |
| Main |  | DoubleAttr | vortexZ |
| Main |  | DoubleAttr | vortexRadius |
| Main |  | DoubleAttr | vortexExponent |
| Main |  | DoubleAttr | vortexUpSpeed |
| Main |  | DoubleAttr | vortexInSpeed |
| Main |  | DoubleAttr | vortexAroundSpeed |


## Weighted-Curve Node

Type: **WeightCurve**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | EnumAttr | CURVETYPE |
| Main |  | DoubleAttr | ACTIVE |
| Main |  | DoubleAttr | MINDIST |
| Main |  | DoubleAttr | MAXDIST |


## Weighted-Deform Node

Type: **WeightedDeform**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | BLEND |
| Main |  | DoubleAttr | POSTBLEND |
| Main |  | Attribute | DeformationQuality |
| Sub | DeformationQuality | EnumAttr | DeformationQuality.type |
| Sub | DeformationQuality | EnumAttr | DeformationQuality.level |


## Weighted-Drawing Node

Type: **WeightDrawing**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | DoubleAttr | MINDIST |
| Main |  | DoubleAttr | MAXDIST |


## Weighted-Line Node

Type: **WeightLine**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | DoubleAttr | MINDIST |
| Main |  | DoubleAttr | MAXDIST |


## Weighted-Point Node

Type: **WeightPoint**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | DoubleAttr | ACTIVE |
| Main |  | DoubleAttr | MINDIST |
| Main |  | DoubleAttr | MAXDIST |


## Wind-Friction Node

Type: **ParticleWindFriction**

| Level | Parent Keyword | Attribute Type | Attribute Keyword |
|---|---|---|---|
| Main |  | IntAttr | trigger |
| Main |  | DoubleAttr | windFrictionX |
| Main |  | DoubleAttr | windFrictionY |
| Main |  | DoubleAttr | windFrictionZ |
| Main |  | DoubleAttr | windFrictionMinSpeed |
| Main |  | DoubleAttr | windFrictionMaxSpeed |


## Write Node

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

