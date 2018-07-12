import os
import subprocess
import string

from xauto.xkeys import Message


def getPid(processName):
    pid = os.popen("pidof " + processName).read().rstrip()
    return pid


def openProcess(processName, title, message, argument):
    if getPid(processName) == "":
        subprocess.Popen(processName)
        if Message != "":
            Message.hint(message)
    else:
        os.popen("wmctrl -R '" + title + "'")


def openProcessWithTitleCheck(processName, title, message, args):
    if isWindowExist(title):
        os.popen("wmctrl -R '" + title + "'")
    else:
        if Message != "":
            Message.hint(message)
        subprocess.Popen([processName, args])


def isAtiveTitle(title):
    windowName = os.popen("xdotool getactivewindow getwindowname").read().rstrip()
    index = string.find(windowName, title)
    return index != -1


def isWindowExist(title):
    windowName = os.popen("wmctrl -l | grep '" + title + "'").read().rstrip()
    index = string.find(windowName, title)
    return index != -1
