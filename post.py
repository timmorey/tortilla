#! /usr/bin/python

##
# post.py - Created by Timothy Morey on 9/6/2013
#

import json
import sys

import cgitb
cgitb.enable()

storedir = '/srv/tortilla/'

body = sys.stdin.read()
content = json.loads(body)

filename = storedir + content['id'] + '.json'
file = open(filename, 'w')
file.write(body)

print 'Content-Type: text/html'
print

