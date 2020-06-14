#!/usr/bin/python

import os, errno

HOME = os.getenv("HOME")
CWD = os.getcwd()
confpath = HOME + "/.config/"

def symlink_force(target, link):
    try:
        os.symlink(target, link)
    except OSError as e:
        if e.errno == errno.EEXIST:
            os.remove(link)
            os.symlink(target, link)

if not os.path.exists(confpath):
    os.makedirs(confpath)

lns = []



for dir1 in os.listdir():
    if os.path.isdir(dir1):
        if not os.path.exists(confpath+dir1):
            os.makedirs(confpath+dir1)
        for dir2 in os.listdir(dir1):
            confdir=dir1+'/'+dir2
            lns.append(confdir)
    else:
        lns.append(dir1)

for ln in lns:
    src = CWD + '/' + ln
    dest = HOME + '/' + ln
    if ln[0]=='.':
        print(src + " ln - " + src )
        symlink_force(src, dest)
    else:
        print(src + " ln - " + confpath +ln)
        symlink_force(src, confpath +ln)
print('done')


#os.symlink('src', 'dest')symlinks = p
