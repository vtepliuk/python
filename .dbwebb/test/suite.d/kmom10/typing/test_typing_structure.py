#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import unittest
import os
import sys
from unittest import TextTestRunner
from examiner import ExamTestCase, ExamTestResult, tags
from examiner import import_module, find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)


class TestStructure(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.
    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    link_to_assignment = "https://dbwebb.se/uppgift/analysera-text-och-ord-v3"

    @classmethod
    def setUpClass(cls):
        """
        To find all relative files that are read or written to.
        """
        os.chdir(REPO_PATH)


    @tags("struct")
    def test_file_main_py_exist(self):
        """
        Testerna hittar inte filen 'main.py'.
        """
        self.assertModule("main", REPO_PATH)



if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
