#! /usr/bin/python

##
# post.py - Created by Timothy Morey on 9/6/2013
#

import os
import urlparse

import cgitb
cgitb.enable()

storedir = '/srv/tortilla/'

args = urlparse.parse_qs(os.environ['QUERY_STRING'])
filename = storedir + args['id'][0] + '.json'

if os.path.exists(filename):
    os.remove(filename)

    print 'Content-Type: text/html'
    print

else:

    print "Status: 404 Not Found"
    print "Content-Type: text/html"
    print
    print "<h1>404 File not found!</h1>"

