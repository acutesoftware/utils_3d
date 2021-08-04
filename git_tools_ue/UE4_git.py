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
from shutil import copyfile
import aikif.lib.cls_filelist as fl 

# project specific details
pth = 'E:\\UE4_proj\\sanct'
proj_name = 'sanct'

# choose folders in your Content folder to check
# (idea is to ignore all the add on packs like Megascans)
my_folders = ['\\Content\\_DJM\\', 
              '\\Config\\', 
              '\\Saved\\Screenshot\\'
             ]

# git specific variables
git_remote_url_base = 'https://github.com'
git_username = 'acutesoftware'
git_project_name = 'UE4_sanct'   # normally, same as proj_name
MAX_FILE_SIZE = 40000000
            
# file names
full_filelist = proj_name + '_all_files.csv'
git_filelist = proj_name + '_git_files.csv'
missed_files_CSV = proj_name + '_missed_files.csv'
git_add_BAT = 'git_add.bat'
git_init_BAT = 'init_git_UE4.bat'



def TEST():
    print('setting up git script for UE4 package for ' + pth)
    lst_git, missed_files = get_list_of_files_for_git(full_filelist, my_folders, MAX_FILE_SIZE)
    create_git_init(git_init_BAT)
    create_git_add_list(git_add_BAT, lst_git)
    append_list_to_file(missed_files_CSV, missed_files)
    append_list_to_file(git_filelist, lst_git)
    
    print('WARNING = ' + str(len(missed_files)) + ' are too big for git, save separately')
    deploy_scripts_to_UE4_folder()

def deploy_scripts_to_UE4_folder():
    copyfile(git_add_BAT, os.path.join(pth, git_add_BAT))
    copyfile(git_init_BAT, os.path.join(pth, git_init_BAT))

    copyfile(full_filelist, os.path.join(pth, full_filelist))
    copyfile(git_filelist, os.path.join(pth, git_filelist))
    copyfile(missed_files_CSV, os.path.join(pth, missed_files_CSV))


def save_full_filelist_of_UE4_files(pth):
    res = []
    lst1 = fl.FileList([pth], ['*.uasset'], [],  full_filelist)
    lst1.save_filelist(full_filelist, ["name", "path", "size", "date"])

def get_list_of_files_for_git(filelist, folders_to_keep, MAX_FILE_SIZE):
    res = []
    file_details = []
    missed_files = []
    save_full_filelist_of_UE4_files(pth)  # saves to CSV file 
    filelist = read_file_to_csv(full_filelist)


    print('getting git list')

    with open (missed_files_CSV,'w') as f:
        f.write('List of files in ' + git_project_name + ' not saved to git\n')

    with open (git_filelist,'w') as f:
        f.write('List of Saved files in ' + git_project_name + '\n')



    for f in filelist:
        file_details = f.split(',')
        for valid in folders_to_keep:
            #print('valid = ', valid, ' file_details = ', file_details)
            if valid in file_details[0]:
                if int(file_details[3].strip('"')) < MAX_FILE_SIZE:
                    res.append(file_details)
                    #print(file_details)
                    break
                else:
                    #print('warning = file too big for git ', file_details)
                    missed_files.append(file_details)



    return res, missed_files

def read_file_to_csv(fname):
    res = []
    with open(fname, 'r') as f:
        for line in f:
            res.append(line)
    return res

def append_list_to_file(git_filename, lst):
    with open (git_filename,'a') as f:
        for line in lst:
            f.write('git add ' + line[0] + '\n')

def create_git_add_list(git_filename, lst):
    with open (git_filename,'w') as f:
        f.write('ECHO Git add file generated by UE4_git.py\n')
        f.write('cd ' + pth + '\n')
        f.write('git add *.*\n')
    append_list_to_file(git_filename, lst)    


def create_git_init(git_filename):
    with open (git_filename,'w') as f:
        f.write('ECHO Git init file generated by UE4_git.py\n')
        f.write('git init\n')

        f.write('git add ' + git_add_BAT + '\n')
        f.write('git add ' + git_init_BAT + '\n')
        f.write('git add ' + full_filelist + '\n')
        f.write('git add ' + git_filelist + '\n')
        f.write('git add ' + missed_files_CSV + '\n')
        f.write('git commit -m "initial setup of ' + proj_name + '"\n')
        f.write('git remote add origin ' + git_remote_url_base + '/' + git_username + '/' + git_project_name + '\n\n')
        f.write('ECHO you may want the following commands as well:\n')
        f.write('ECHO    git pull origin master\n')
        f.write('ECHO    git push --set-upstream origin master\n\n')
 



if __name__ == '__main__':  
    TEST()        