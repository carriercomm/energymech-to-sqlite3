#!env/bin/python
import re
import os
from os import listdir
from os.path import isfile, join
# from multiprocessing.dummy import Pool as ThreadPool

normalline = re.compile('^\[[^\]]*(\d{2}:\d{2}:\d{2})\] <([^>]+)> (.*)$')
actionline = re.compile('^\[[^\]]*(\d{2}:\d{2}:\d{2})\] \* (\S+) (.*)$')
serverline = re.compile('^\[[^\]]*(\d{2}:\d{2}:\d{2})\] \*{3} (.+)$')

basedir = os.path.abspath(os.path.dirname(__file__))
logfolder = os.path.join(basedir, 'log')


def get_files(logfolder):
    files = [f for f in listdir(logfolder) if isfile(join(logfolder, f))]
    return files


def get_normalline(log):
    file = open(log)
    date = str(log)[-10:-4]
    results = []
    for line in file:
        if normalline.match(line):
            timestmp = normalline.search(line).group(1)
            nick = normalline.search(line).group(2)
            text = normalline.search(line).group(3)
            say = {'date': date, 'timestamp': timestmp,
                   'nick': nick, 'text': text}
            results.append(say)
    return results


# def parse_logs(files):
#     """ try and get the files in a threaded fashion"""
#     pool = ThreadPool(8)
#     stuff = pool.map(get_normalline(files), files)


def main():
    files = get_files(logfolder)
    print files
    for file in files:
        normallines = get_normalline(os.path.join(logfolder, file))
    # for i, timestamp in enumerated(d['timestamp'] for d in normallines):
    #    print i, timestamp
    for a in normallines:
        print str(a)
    # parse_logs(files)

if __name__ == '__main__':
    main()
