# run_tests.py
import os
import time
import unittest as unittest

all_tests = unittest.TestLoader().discover('.', pattern='test*.py')
unittest.TextTestRunner().run(all_tests)    

def wipe_file(fname):
    if os.path.exists(fname):
        try:
            os.remove(fname)
            print('deleted ' + fname)
        except:
            pass
        
