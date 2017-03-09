# -*- coding:utf-8 -*-
# hello.py
import commands
import os
import time

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print '-------vincio---------------shutDown-------start---------'
    shutDown()
    print '-------vincio---------------shutDown-------end---------'
    time.sleep(10)
    print '-------vincio---------------startUp-------start---------'
    startUp()
    print '-------vincio---------------startUp-------end---------'
    return '<h1>REBOOT SUCCESS, Please Wait for a Moment!!</h1>'


def shutDown():
    command = '/opt/app/tomcat-vincio-deploy/bin/./shutdown.sh'
    print os.system(command)
    # print os.popen(command)
    # return commands.getstatusoutput(command)

def startUp():
    command = '/opt/app/tomcat-vincio-deploy/bin/./startup.sh'
    print os.system(command)
    # print os.popen(command)
    # return commands.getstatusoutput(command)