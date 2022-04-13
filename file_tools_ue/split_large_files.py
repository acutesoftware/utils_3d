#!/usr/bin/python3
# coding: utf-8
# split_large_files.py
# written by Duncan Murray 2022

# takes all large text files in a folder and splits them to smaller
# sizes of X lines each


import os 
import sys 
import aikif.lib.cls_filelist as fl 

max_line_size = 50000
folder = r'D:\dev\src\utils_3d\test\test_data'
orig_filelist = 'files_to_split.csv'

def main():
    print('splitting files in ' + folder)
    fl_to_split = fl.FileList([folder], ['*.*'], [],  orig_filelist).get_list()
    for file in fl_to_split:
        if '.SPLIT_' in file:
            print('ignoring file already split - ' + file)
        else:
            split_file(str(file))

def split_file(fname):
    print(' splitting - ' + fname)
    cur_op_file = get_next_filename(fname + '.SPLIT_0')
    num_op_files = 1
    tot_lines_read = 0
    cur_line_limit = max_line_size
    with open(fname, 'r') as fip:
        cur_lines = []
        for line_num, line in enumerate(fip):
            cur_lines.append(line)
            tot_lines_read += 1
            if line_num > cur_line_limit: 
                write_cur_lines(cur_lines, cur_op_file)
                cur_op_file = get_next_filename(cur_op_file)
                num_op_files += 1
                cur_line_limit += max_line_size
                cur_lines = []
        write_cur_lines(cur_lines, cur_op_file)
        print('lines in input = ' + str(tot_lines_read))

def write_cur_lines(lines, cur_op_file):
    print('saving ' + str(len(lines)) + ' to ' + cur_op_file)
    with open(cur_op_file, 'w') as fop:
        fop.writelines(lines)

def get_next_filename(cur_filename):
    
    num = int(cur_filename[-1])
    return cur_filename[:-1] + str(num + 1)

main()