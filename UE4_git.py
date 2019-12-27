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

pth = 'D:\\docs\\Unreal Projects\\sanct'

def TEST():
    print('setting up git script for UE4 package for ' + pth)
    lst = get_list_of_UE4_files(pth)

def get_list_of_UE4_files(pth):
    res = []


    return res 


if __name__ == '__main__':  
    TEST()        