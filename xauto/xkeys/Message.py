# Author Andrew Terekhine
# Since 2011-02-01 test

import subprocess

def hint(text):
    subprocess.call(('notify-send', "-t", "1000", text))
