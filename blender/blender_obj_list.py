# blender_obj_list.py
# Run this in Blender 2.8 or above via

import bpy 


def main():
    res = get_obj_list()
    save_report(res)

def get_obj_list():
    """
    loop through all the obects in a blender file
    and collect info on them
    """
    res = []
    for obj in bpy.data.objects:
        res.append([obj.name, obj.location, obj.dimensions, obj.scale])
    return res

def save_report(res):
    fname = get_blend_filename()
    with open(fname + '_report.csv', 'w') as f:
        f.write("#Blender report,,,,,,,,,,\n")
        f.write("#Folder = " + bpy.path.abspath("//") + ',,,,,,,,,,\n')
        f.write("#Filename = " + fname + ',,,,,,,,,,\n')
        f.write("#Date = DATE,,,,,,,,,,\n")
        f.write("#Columns, Location,,, Dimensions,,, Scale,,,\n")
        f.write("Name, loc_x, loc_y, loc_z, dim_x, dim_y, dim_z, sc_x,sc_y,sc_z,\n")
        
        for line in res:
            f.write(line[0] + ',')
            f.write(str(line[1][0]) + ',')
            f.write(str(line[1][1]) + ',')
            f.write(str(line[1][2]) + ',')
            f.write(str(line[2][0]) + ',')
            f.write(str(line[2][1]) + ',')
            f.write(str(line[2][2]) + ',')
            f.write(str(line[3][0]) + ',')
            f.write(str(line[3][1]) + ',')
            f.write(str(line[3][2]) + ',')
            f.write('\n')


def get_blend_filename():
    """
    returns the current open and active blender file
    or 'Unsaved_blend'
    """
    res = bpy.data.filepath
    if res == '':
        res = 'Unsaved_blend'
    return res


if __name__ == '__main__':
    main()        