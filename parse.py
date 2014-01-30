#!env/bin/python
import re
import os
from os import listdir
from os.path import isfile, join
from multiprocessing.dummy import Pool as ThreadPool
# import timing

chatline = re.compile('^\[[^\]]*(\d{2}:\d{2}:\d{2})\] <([^>]+)> (.*)$')
actionline = re.compile('^\[[^\]]*(\d{2}:\d{2}:\d{2})\] \* (\S+) (.*)$')
serverline = re.compile('^\[[^\]]*(\d{2}:\d{2}:\d{2})\] \*{3} (.+)$')

basedir = os.path.abspath(os.path.dirname(__file__))
logfolder = os.path.join(basedir, 'log')


def get_files(logfolder):
    files = [f for f in listdir(logfolder) if isfile(join(logfolder, f))]
    return files


def get_chatline(log):
    file = open(log)
    date = str(log)[-12:-4]
    results = []
    for line in file:
        if chatline.match(line):
            timestmp = chatline.search(line).group(1)
            nick = chatline.search(line).group(2)
            text = chatline.search(line).group(3)
            say = {'date': date, 'timestamp': timestmp,
                   'nick': nick, 'text': text}
            results.append(say)
    print "\n\nresults are " + str(results)
    return results


def parse_logs(files):
    """ form the date, timestamp, nick, text dictionary list
    in an async fashion """
    pool = ThreadPool(8)
    chatdict = pool.map(get_chatline, files)
    pool.close()
    pool.join()
    return chatdict


def main():
    filesrel = get_files(logfolder)
    # regular method
    # for file in filesrel:
    #     files = get_chatline(os.path.join(logfolder, file))
    # for a in files:
    #     print str(a)

    # threaded method
    files = []
    for file in filesrel:
        files.append(os.path.join(logfolder, file))
    values = parse_logs(files)
    for value in values:
        print "\n\nDEBUGLIST " + str(value)

if __name__ == '__main__':
    main()
