#!/usr/bin/python3
# coding: utf-8
# UE4_git.py
#
# script to setup git for Unreal Engine
# - sets up repo
# - adds all key files
# - generates list of all files, adds list to repo 
# - setup README.md
# - adds all UE4 assets less than 50M

import os 
import sys 
import aikif.lib.cls_filelist as fl 

pth = 'D:\\docs\\Unreal Projects\\sanct'
full_filelist = 'filelist.csv'
git_filelist = 'files_git.csv'
MAX_FILE_SIZE = 100000
my_folders = ['\\Content\\_DJM\\', 
              '\\Config\\', 
              '\\Content\\Maps\\'
            ]

def TEST():
    print('setting up git script for UE4 package for ' + pth)
    lst = get_list_of_UE4_files(pth)
    print(lst)

def get_list_of_UE4_files(pth):
    res = []
    lst1 = fl.FileList([pth], ['*.uasset'], [],  full_filelist)
    lst1.save_filelist(full_filelist, ["name", "path", "size", "date"])

    return get_list_of_files_for_git(lst1.get_list(), my_folders, MAX_FILE_SIZE)

def get_list_of_files_for_git(filelist, folders_to_keep, max_file_size):
    res = []
    file_details = []
    print('getting git list')
    for f in filelist:
        file_details = f.split(',')
        for valid in folders_to_keep:
            #print('valid = ', valid, ' file_details = ', file_details)
            if valid in file_details[0]:
                res.append(file_details)
                print(file_details)
                break



    return res


if __name__ == '__main__':  
    TEST()        