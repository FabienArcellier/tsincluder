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

    def test_a_line_that_begins_with_a_markup_invoke_a_subprocess(self):
        # Assign

        # Acts
        text = self.tested.process('@tsincluder echo "hello world"')
        # Assert
        self.assertEqual('hello world\n', text)

