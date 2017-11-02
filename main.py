#!/usr/local/bin/python

# import subprocess
import os

# cmd = ['ssh', 'gcl', 'python < ' + os.getcwd() + '/helper.py - ip mac name comments path']

# p = subprocess.Popen(cmd)

os.system("ssh gcl python < helper.py - ip mac name comments a.txt")