import bpy
import random

def create_Cube(positions,size):
    for idx, sub_array in enumerate(positions):
        loc = (sub_array[0], sub_array[1], sub_array[2])
        bpy.ops.mesh.primitive_cube_add(size=size, enter_editmode=False, align='WORLD', location=loc)
        cube = bpy.context.active_object
           # Create a new material and assign it to the cube
        material = bpy.data.materials.new("CubeMaterial")
        cube.data.materials.append(material)
        
        # random colour chosen from a red - green gradient.
        red = random.randint(255 * 0, 255 * 1)
        green = random.randint(255 * 0, 255 * 1)
        blue = 0
        cube.data.materials[0].diffuse_color = (red / 255, green / 255, blue / 255, 1)
        
         # Animate jittered rotation
        for frame in range(0, 101):
            cube.rotation_euler.x += random.uniform(0, 2 * 3.14159) # adding a random rotation around the X axis 
            cube.rotation_euler.y += random.uniform(0, 2 * 3.14159) # adding a random rotation around the Y axis 
            cube.rotation_euler.z += random.uniform(0, 2 * 3.14159) # adding a random rotation around the Z axis 
            cube.keyframe_insert(data_path="rotation_euler", frame=frame)
            
        # Set end frame for animation
        bpy.context.scene.frame_end = 100



# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()


initial_size = 1
positions = [
[4,6,3],
[6,6,3],
[3,3,3],
[3,2,3],
[7,3,3],
[7,2,3],
[4,1,3],
[5,1,3],
[6,1,3]
]

create_Cube(positions,initial_size)