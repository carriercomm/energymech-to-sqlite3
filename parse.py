#!env/bin/python
import re
import os
from os import listdir
from os.path import isfile, join

normalline = re.compile('^\[[^\]]*(\d{2}):\d+:\d+\] <([^>]+)> (.*)$')
actionline = re.compile('^\[[^\]]*(\d{2}):\d+:\d+\] \* (\S+) (.*)$')
serverline = re.compile('^\[[^\]]*(\d{2}):(\d+):\d+\] \*{3} (.+)$')

basedir = os.path.abspath(os.path.dirname(__file__))
logfolder = os.path.join(basedir, 'log')


def get_files(logfolder):
    files = [f for f in listdir(logfolder) if isfile(join(logfolder, f))]
    return files


def main():
    get_files(logfolder)

if __name__ == '__main__':
    main()
