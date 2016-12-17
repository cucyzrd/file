#!/bin/env python
#coding:utf8

'''
创建文件
'''
import os
ls = os.linesep

# 获取文件名
while True:
    if os.path.exists(fname):
        print 'error, %s already exits' % fname
    else:
        break

# get file content(text) line
all  = []
print "\nEnter lines ('.' by itself to quit).\n"

while True:
    entry = raw_input('> ')
    if entry =='.':
        break
    else:
        all.append(entry)

# wirte lines to file with prope line-ending
fobj = open(fname,w)
fobj.writelines(['%s%S' % (x, ls) for x in all])
fobj.close()
print 'Done'