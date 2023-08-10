import bpy
import math

def create_snowflake(center, size, recursion_level):
    if recursion_level == 0:
        return
    
    # Create the main branch
    bpy.ops.mesh.primitive_cube_add(size=size, location=center)
    cube = bpy.context.active_object
    
    # Rotate and scale the cube to form a branch
    bpy.context.view_layer.objects.active = cube
    bpy.ops.transform.rotate(value=math.radians(45), orient_axis='Z')

    
    # Recursively create sub-branches
    for i in range(6):
        angle = i * math.pi / 3
        offset = size * 2
        new_center = (
            center[0] + offset * math.cos(angle),
            center[1] + offset * math.sin(angle),
            center[2]
        )
        create_snowflake(new_center, size / 3, recursion_level - 1)

# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Create the initial snowflake shape
initial_size = 2.0
initial_center = (0, 0, 0)
initial_recursion_level = 3
create_snowflake(initial_center, initial_size, initial_recursion_level)
