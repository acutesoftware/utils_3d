#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_quest_gen.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )
pth = os.path.join(root_folder, 'file_tools_ue')
sys.path.append(pth)

import size_ue4 as mod_size_ue

class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)


    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_01_test_import(self):
        self.assertEqual( mod_size_ue.op_file, 'files_ue4.txt')

    def test_02_get_project_details(self):
        """
        collects Assets folder lists, looking for 'Content' folder
        """
        # check for no assets (in this test subfolder)
        self.assertEqual([], mod_size_ue.get_project_details('.','.', sum_only='N'))

        # check for assets in live (fast) drive
        live_files = mod_size_ue.get_project_details(mod_size_ue.pth, 'test_Landscape_UE', sum_only='N')
        self.assertEqual(live_files, ['Assets', 'Collections', 'Developers', 'Maps'])

        live_files = mod_size_ue.get_project_details(mod_size_ue.pth, 'BLAST', sum_only='Y')
        self.assertEqual(live_files, [])  # no list of assets returned if sum_only=Y

        # check for assets in backup NAS (works but slow, during backup)
        """
        nas_root = '\\\\FANGORN\\user\\duncan\\duncan_sapling\\_BACKUP_D_UNREAL'
        nas_files = mod_size_ue.get_project_details(nas_root, 'PVP_zone', sum_only='N')
        print(nas_files)
        self.assertTrue(len(nas_files) > 10)  # at least 10 asset folders in the PVP_zone backup
        """

    def test_03_get_all_files(self):
        """
        basic file scanning utils used by root functions
        """
        files, tot_files, tot_size = mod_size_ue.get_all_files(root_folder)  # full python project
        #print('files, tot_files, tot_size = ', len(files), tot_files, tot_size)
        self.assertTrue(len(files) == tot_files)
        self.assertTrue(tot_files > 20)
        self.assertTrue(tot_size > 2)
        
    def test_04_get_next_subfolders(self):
        """
        basic file scanning utils used by root functions
        """
        res = mod_size_ue.get_next_subfolders(root_folder)  # full python project
        print(res)
        self.assertEqual(res, ['.git', 'file_tools_ue', 'git_tools_ue', 'test'])
        


if __name__ == '__main__':
    unittest.main()