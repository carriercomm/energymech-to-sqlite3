#!env/bin/python
import re
import os
from os import listdir
from os.path import isfile, join
# from multiprocessing.dummy import Pool as ThreadPool

# only matches the hour, not the full time. Need to find fix
normalline = re.compile('^\[[^\]]*(\d{2}):\d+:\d+\] <([^>]+)> (.*)$')
actionline = re.compile('^\[[^\]]*(\d{2}):\d+:\d+\] \* (\S+) (.*)$')
serverline = re.compile('^\[[^\]]*(\d{2}):(\d+):\d+\] \*{3} (.+)$')

basedir = os.path.abspath(os.path.dirname(__file__))
logfolder = os.path.join(basedir, 'log')


def get_files(logfolder):
    files = [f for f in listdir(logfolder) if isfile(join(logfolder, f))]
    return files


def get_line(log):
    file = open(log)
    results = []
    for line in file:
        if normalline.match(line):
            print normalline.search(line).groups()
        else:
            print 'not chat line'
    return results


# def parse_logs(files):
#     """ try and get the files in a threaded fashion"""
#     pool = ThreadPool(8)
#     stuff = pool.map(get_line(files), files)


def main():
    files = get_files(logfolder)
    print files
    for file in files:
        get_line(os.path.join(logfolder, file))
    # parse_logs(files)

if __name__ == '__main__':
    main()
