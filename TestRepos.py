# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from repos import getRepos

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestRepos(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testA(self): 
        self.assertEqual(getRepos(Andre-asn))

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

