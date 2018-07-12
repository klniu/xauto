from unittest import TestCase

from helpers.FileUtil import readLines


class TestReadLines(TestCase):
    def testReadLines(self):
        lines = readLines('./test_docs/readlines')
        self.assertListEqual(['test1', 'test2', 'test3', 'test4', 'test5'], lines)
        lines = readLines('./test_docs/readlines', 1)
        self.assertListEqual(['test2', 'test3', 'test4', 'test5'], lines)
        lines = readLines('./test_docs/readlines', 1, 1)
        self.assertListEqual(['test2', 'test4'], lines)


