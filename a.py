#!/usr/local/bin/python

import cgi, cgitb
import subprocess
import pexpect
# import paramiko

# path = 'output/dir'
# data = 'second string\n'
# cmd = ['ssh', 'gcl', 'mkdir -p ' + path + '; cd ' + path + '; echo "' + data + '" >> file.dat']

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')
server = form.getvalue('server')
path = form.getvalue('path')
ip = form.getvalue('ip')
mac = form.getvalue('mac')
name = form.getvalue('name')
comments = form.getvalue('comments')

data = ip + " " + mac + " " + name + " " + comments
cmd = ['ssh', 'gcl', 'mkdir -p ' + path + '; cd ' + path + '; echo "' + data + '" >> file.dat']

p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
# p.stdin.write(data)

print "Content-type:text/html\n\n"
print '<html>'
print '<head>'
print '<title>Updaters</title>'
print '</head>'
print '<body>'
print '<h2>Hello Word! This is my first CGI program</h2>'
print data
print '</body>'
print '</html>'

# (IP, Mac Address, Name of the Machine, Some comments)
