#!/usr/bin/env python
# -*- coding: utf-8 -*-


def readLines(filename: str, start: int = 0, skip: int = 0) -> list:
    """
    Read lines from file and return as a list.
    :param filename: the path of the file
    :param start: the number of lines to be skiped at the header
    :param skip: skip lines between two line.
    """
    result = []
    with open(filename, 'rt') as f:
        lines = f.readlines()[start:]
        for i, line in enumerate(lines):
            no = i
            if no % (skip + 1) == 0:
                result.append(str.strip(line))
    return result
