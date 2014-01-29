#!env/bin/python
import re
import os

normalline = re.compile('^\[[^\]]*(\d{2}):\d+:\d+\] <([^>]+)> (.*)$')
actionline = re.compile('^\[[^\]]*(\d{2}):\d+:\d+\] \* (\S+) (.*)$')
serverline = re.compile('^\[[^\]]*(\d{2}):(\d+):\d+\] \*{3} (.+)$')

basedir = os.path.abspath(os.path.dirname(__file__))
logfolder = os.path.join(basedir, 'log')
