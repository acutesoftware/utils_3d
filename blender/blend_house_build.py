# blend_house_build.py

import bpy 
import math

CEILING_HEIGHT = 3.0
WALL_THICKNESS = 0.1
FLOOR_LOCATION = 0.0

def build_house(x=0,y=0):
    build_room('Bedroom', 0,0, 4,6)
    build_room('Hall', 3,4+WALL_THICKNESS/2, 2,7)
    make_window_EW('Bedroom Window', 0,2,0.5, 1.5, 1.5)
    make_window_NS('Bedroom Door', 4,4,0, 1, 2.5)

def build_room(room_name, x, y, width, length):
    make_wall_NS(room_name + ' - North wall', x, y,length)
    make_wall_NS(room_name + ' - South wall', x, y+width,length)

    make_wall_EW(room_name + ' - East wall', x, y,width)
    make_wall_EW(room_name + ' - West wall', x+length, y,width)

def make_wall_EW(nme, x,y, length):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(x,y, FLOOR_LOCATION))
    cube = bpy.context.selected_objects[0]
    cube.name = nme    
    bpy.context.object.scale[0] = WALL_THICKNESS
    bpy.context.object.scale[1] = length
    bpy.context.object.scale[2] = CEILING_HEIGHT
    bpy.context.object.location=(x,y+(length/2),FLOOR_LOCATION)


def make_wall_NS(nme, x, y,length):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(x,y, FLOOR_LOCATION))
    cube = bpy.context.selected_objects[0]
    cube.name = nme    
    bpy.context.object.scale[0] = length
    bpy.context.object.scale[1] = WALL_THICKNESS
    bpy.context.object.scale[2] = CEILING_HEIGHT
    bpy.context.object.location=(x+(length/2),y,FLOOR_LOCATION)
  

def make_window_EW(nme,  x, y, z, length, height):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(x,y, z))
    cube = bpy.context.selected_objects[0]
    cube.name = nme    
    bpy.context.object.scale[0] = WALL_THICKNESS * 2
    bpy.context.object.scale[1] = length
    bpy.context.object.scale[2] = height
    #bpy.context.object.location=(x+(length/2),y,FLOOR_LOCATION)

def make_window_NS(nme,  x, y, z, length, height):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(x,y, z))
    cube = bpy.context.selected_objects[0]
    cube.name = nme    
    bpy.context.object.scale[0] = length
    bpy.context.object.scale[1] = WALL_THICKNESS * 2.5
    bpy.context.object.scale[2] = height
    #bpy.context.object.location=(x+(length/2),y,FLOOR_LOCATION)



build_house(x=0,y=0)
