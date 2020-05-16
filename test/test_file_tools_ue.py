#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_quest_gen.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )
pth = root_folder #+ os.sep + 'worldbuild'
sys.path.append(pth)



class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)


    def tearDown(self):
        unittest.TestCase.tearDown(self)



if __name__ == '__main__':
    unittest.main()