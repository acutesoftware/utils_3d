#!/usr/bin/python3
# coding: utf-8
# size_ue4.py

# shows project size of each Unreal Engine project and what Assets are used

import os 
import sys 
from shutil import copyfile
import aikif.lib.cls_filelist as fl 

pth = r'E:\UE4_proj'
op_file = 'files_ue4.txt'

just_summ = 'N'

def main():
    lst = get_next_subfolders(pth)
    #print('folders = ', lst)
    for folder in lst:
        get_project_details(pth, folder, just_summ)

def get_project_details(base_path, folder, sum_only='N'):
    top_level_folders = get_next_subfolders(os.path.join(base_path, folder))
    content_folder = '.'  

    if len(top_level_folders) > 1:
        content_folder = os.path.join(base_path, folder, 'Content')
    elif len(top_level_folders) == 1:
        try:
            content_folder = os.path.join(base_path, folder, top_level_folders[0], 'Content')
        except Exception as ex:
            print('no Content folder found')
    else:
        content_folder = os.path.join(base_path, folder)

    if sum_only == 'N':
        assetts_folders = get_next_subfolders(content_folder)
    else:
        assetts_folders = []

    files, tot_files, tot_size = get_all_files(content_folder)
    if sum_only != 'N':
        print(folder, str(tot_size) + ' MB (' + str(tot_files) + ' files)' )
    else:
        print(folder, str(tot_size) + ' MB (' + str(tot_files) + ' files). Assets = ',assetts_folders )
    return assetts_folders
    
def get_all_files(start_path):   
    """
    get complete list of all files and subfolders under path
    """
    fl_ue4 = fl.FileList([start_path], ['*.*'], [],  op_file)
    #fl_ue4.save_filelist(op_file, ["name", "path", "size", "date"])
    files = fl_ue4.get_metadata()
    
    tot_size = 0
    tot_files = 0
    for file_dict in files:
            tot_files += 1
            tot_size += int(file_dict["size"])
    return files, int(tot_files), int(tot_size/1000000)

def get_next_subfolders(start_path):
    """
    returns a singe list of subfolders under the folder start_path
    """
    dirs = []
    try:
        dirs = [ item for item in os.listdir(start_path) if os.path.isdir(os.path.join(start_path, item)) ]
    except:
        print('No subfolders found')
    return dirs

if __name__ == '__main__':  
    main()            