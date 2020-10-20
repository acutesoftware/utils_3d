# blend_house_build.py

import bpy 
import math

CEILING_HEIGHT = 3.0
WALL_THICKNESS = 0.1
FLOOR_LOCATION = 0.0

def build_house(x=0,y=0):
    build_room('Bedroom', 0,0, 4,6)
    build_room('Hall', 4,0, 1,12)
    make_window_EW(0,2,1.5, 1.5)

def build_room(room_name, x, y, width, length):
    make_wall_NS(room_name + ' - North wall', x+(length/2), y,length)
    make_wall_NS(room_name + ' - South wall', x+(length/2), y+width,length)

    make_wall_EW(room_name + ' - East wall', x, y+(width/2),width)
    make_wall_EW(room_name + ' - West wall', x+length, y+(width/2),width)

def make_wall_EW(nme, x,y, length):
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(x,y, FLOOR_LOCATION))
    cube = bpy.context.selected_objects[0]
    cube.name = nme    
    bpy.context.object.scale[0] = WALL_THICKNESS
    bpy.context.object.scale[1] = length
    bpy.context.object.scale[2] = CEILING_HEIGHT


def make_wall_NS(nme, x, y,length):
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(x,y, FLOOR_LOCATION))
    cube = bpy.context.selected_objects[0]
    cube.name = nme    
    bpy.context.object.scale[0] = length
    bpy.context.object.scale[1] = WALL_THICKNESS
    bpy.context.object.scale[2] = CEILING_HEIGHT

def make_window_EW( x, y, width, length):
    print('pretending to make a window')

build_house(x=0,y=0)
