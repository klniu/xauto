from unittest import TestCase

from xauto.helpers.FileUtil import readLines


class TestReadLines(TestCase):
    def testReadLines(self):
        lines = readLines('./test_docs/readlines')
        self.assertListEqual(
            ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9',
             'test10'], lines)
        lines = readLines('./test_docs/readlines', 1)
        self.assertListEqual(
            ['test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10'],
            lines)
        lines = readLines('./test_docs/readlines', 1, 1)
        self.assertListEqual(['test2', 'test4', 'test6', 'test8', 'test10'], lines)

        lines = readLines('./test_docs/readlines', 3, 2)
        self.assertListEqual(['test4', 'test7', 'test10'], lines)
