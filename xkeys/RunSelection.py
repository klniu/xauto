#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Runs selection. Based on xdg-open tool. This tool must be installed.

Author Andrew Terekhine
Since 2011-11-25
"""

from xkeys import SystemUtil

if __name__ == "__main__":
        import sys, PythonCall
        PythonCall.PythonCall(sys.argv).execute()

def openSelection():
    SystemUtil.openSelection("xdg-open", "")

def runSelection():
    SystemUtil.runSelection()
