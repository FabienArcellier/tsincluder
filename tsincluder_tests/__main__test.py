# coding=utf-8

from tsincluder import Processor
import unittest

class ProcessorTest(unittest.TestCase):


    def setUp(self):
        self.tested = Processor()

    def test_a_line_without_a_markup_is_return_as_is(self):
        # Assign
        
        # Acts
        text = self.tested.process('test')
        # Assert
        self.assertEqual('test', text)
