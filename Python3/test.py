#!/usr/bin/env python3
# coding:utf-8

import os

import sys

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b =b,a+b
        print(a)
        
fibonacci(10)

print(os.path.abspath(''))

print(os.getcwd())
print(sys.argv)

print(os.path.abspath(sys.argv[0]))


import os, sys
rundir = os.getcwd()
filepath = os.path.abspath(sys.argv[0])
filedir = os.path.dirname(filepath)
filename = os.path.basename(filepath)
logfile = 'log.log'
logpath = os.path.join(filedir, logfile)

print(rundir, filepath, filedir, filename,logpath)
