#!/usr/bin/env python3
# coding:utf-8


# 日志模块
import logging, logging.handlers
# 系统相关模块
import os, sys
import re

def log_dir(logdir):
    if os.path.exists(logdir):
        if os.path.isdir(logdir):
            return True
        else:
            print('！已存在路径文件 %s' % logdir)
            return False
    else:
        os.mkdir(logdir)
        return True

def log(logname='log', lvl='info'):
    
    # 获取路径信息
    rundir = os.getcwd()
    filepath = os.path.abspath(sys.argv[0])
    if sys.argv[0]:
        filedir = os.path.dirname(filepath)
    else:
        filedir = filepath
    filename = os.path.basename(filepath)
    logfilename = 'log.log'
    logdir = os.path.join(filedir, 'log')

    # 日志目录设定
    if log_dir(logdir):
        logpath = os.path.join(logdir, logfilename)
    else:
        logpath = os.path.join(filedir, logfilename)

    print(rundir, filepath, filedir, filename)
    print(logdir)
    
    if lvl == 'debug':
        loglvl = logging.DEBUG 
    elif lvl == 'info':
        loglvl = logging.INFO
    elif lvl == 'warn':
        loglvl = logging.WARN
    elif lvl == 'error':
        loglvl = logging.ERROR
    elif lvl == 'critical':
        loglvl = logging.CRITICAL
    else:
        loglvl = logging.INFO

    logger = logging.getLogger(logname)
    logger.setLevel(loglvl)
    handler = logging.handlers.TimedRotatingFileHandler(logpath, when='midnight', interval=1, backupCount=30)
    # 设置日志文件名格式
    handler.suffix="%Y%m%d-%H%M.log"
    handler.extMatch=r"^\d{8}-\d{4}.log$"
    handler.extMatch = re.compile(handler.extMatch)
    # 设置日志格式
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')  
    handler.setFormatter(formatter)  
    if not logger.handlers:
        logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    print(logpath)
    # use
    # import log
    # a=log.log(name)
    # a.info('msg')


