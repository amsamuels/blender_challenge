import bpy
import random
import string
import math as m

n=200
r=8
z=0

# generate random names 
def generate_random_name():
    random_letters = random.choices(string.ascii_lowercase, k=5)
    random_numbers = random.randint(100, 999)
    return ''.join(random_letters) + ':' + str(random_numbers)

# draw the double helix shape
def create_double_helix(r,z,n):
    for i in range(1,n+1):
        angle = ((i-1)*8*m.pi)/n
        x = r*m.cos(angle)
        y = r*m.sin(angle)
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(x, y, z))
        bpy.context.object.rotation_euler[2]=angle
        z+=0.4
        cube = bpy.context.active_object
        cube.name = generate_random_name()


# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()


create_double_helix(r,z,n)

# Print statistics
total_objects = len(bpy.data.objects)


print("Total Objects:", total_objects)

