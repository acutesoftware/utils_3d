#!/usr/bin/python3
# coding: utf-8
# create_ue4_filelist.py

# builds a full filelist of all revelant UE files
# This gets the content folder and ignore saves and cooked files

import os 
import sys 
from shutil import copyfile
import aikif.lib.cls_filelist as fl 

pth = r'E:\UE4_proj'
#pth = r'E:\UE4_proj\sanct'

op_file = 'files_ue4.txt'


def main():
    ignore_folders = [
        'Binaries', 
        'Build', 
        'Intermediate',
        'Crashes',
        'MaterialStats',
        'MaterialStatsDebug',
        'StagedBuilds',
        'Autosaves',
        'Cooked',
        'Temp',
        'DerivedDataCache'
    ]

    clean_ignore = []
    for i in ignore_folders:
        clean_string = os.sep + i + os.sep
        print(clean_string)
        clean_ignore.append(clean_string)


    fl_ue4 = fl.FileList([pth], ['*.*'], clean_ignore,  op_file)
    fl_ue4.save_filelist(op_file, ["name", "path", "size", "date"])


if __name__ == '__main__':  
    main()            