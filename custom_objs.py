import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes

custom_marker_types = []
custom_container_types = []
custom_cube_types = []

async def declare_objects(robot):

    """
    await robot.world.define_custom_box(
        CustomObjectTypes.CustomType00,
        CustomObjectMarkers.Hexagons4,     # front
        CustomObjectMarkers.Triangles5,    # back
        CustomObjectMarkers.Circles2,      # top
        CustomObjectMarkers.Diamonds3,     # bottom
        CustomObjectMarkers.Circles4,      # left
        CustomObjectMarkers.Diamonds5,     # right
        50, 20, 1,   # depth, width, height
        40, 40,      # marker width and height
        True)        # is_unique
    return
    """

    global custom_marker_types, custom_cube_types
    
    decl_marker = robot.world.define_custom_wall
    custom_marker_types = []

# Markers for containers
    custom_container_types = []



# Markers for cubes

    decl_cube = robot.world.define_custom_cube

    custom_cube_types = [
        CustomObjectTypes.CustomType07,
        CustomObjectTypes.CustomType08,
        CustomObjectTypes.CustomType09,
        CustomObjectTypes.CustomType10,
        CustomObjectTypes.CustomType11,
        CustomObjectTypes.CustomType12,
        CustomObjectTypes.CustomType13,
        CustomObjectTypes.CustomType14,
        CustomObjectTypes.CustomType15,
        CustomObjectTypes.CustomType16,
        CustomObjectTypes.CustomType17,
        CustomObjectTypes.CustomType18,
        CustomObjectTypes.CustomType19,
        ]

    await decl_cube(CustomObjectTypes.CustomType06,
                    CustomObjectMarkers.Triangles3,
                    50, 40, 40, True)

    await decl_cube(CustomObjectTypes.CustomType07,
                    CustomObjectMarkers.Hexagons5,
                    50, 40, 40, True)
    await decl_cube(CustomObjectTypes.CustomType08,
                    CustomObjectMarkers.Circles5,
                    50, 40, 40, True)
    await decl_cube(CustomObjectTypes.CustomType09,
                    CustomObjectMarkers.Triangles5,
                    50, 40, 40, True)

    await decl_cube(CustomObjectTypes.CustomType10,
                    CustomObjectMarkers.Circles2,
                    50, 40, 40, True)
    await decl_cube(CustomObjectTypes.CustomType11,
                    CustomObjectMarkers.Diamonds2,
                    50, 40, 40, True)
    await decl_cube(CustomObjectTypes.CustomType12,
                    CustomObjectMarkers.Hexagons3,
                    50, 40, 40, True)
    await decl_cube(CustomObjectTypes.CustomType13,
                    CustomObjectMarkers.Triangles4,
                    50, 40, 40, True)
    await decl_cube(CustomObjectTypes.CustomType14,
                    CustomObjectMarkers.Hexagons2,
                    50, 40, 40, True)
    await decl_cube(CustomObjectTypes.CustomType15,
                    CustomObjectMarkers.Diamonds3,
                    50, 40, 40, True)
    await decl_cube(CustomObjectTypes.CustomType16,
                    CustomObjectMarkers.Hexagons4,
                    50, 40, 40, True)
    await decl_cube(CustomObjectTypes.CustomType17,
                    CustomObjectMarkers.Circles4,
                    50, 40, 40, True)
    await decl_cube(CustomObjectTypes.CustomType18,
                    CustomObjectMarkers.Diamonds5,
                    50, 40, 40, True)
    await decl_cube(CustomObjectTypes.CustomType19,
                    CustomObjectMarkers.Diamonds4,
                    50, 40, 40, True)
