import os, sys
import log
def chk_log(logdir):
    if os.path.exists(logdir):
        if os.path.isdir(logdir):
            return True
        else:
            print('! 已存在 %s, 非目录' % logdir)
            return False
    else:
        print('# 建立目录 %s' % logdir)
        os.mkdir(logdir)
        return True

rundir = os.getcwd()
filepath = os.path.abspath(sys.argv[0])
filedir = os.path.dirname(filepath)
filename = os.path.basename(filepath)
logfile = 'log.log'
logpath = os.path.join(filedir, logfile)
print( '''
 执行时所在目录\t%s\r\n
 运行程序路径\t%s\r\n
 运行程序所在目录\t%s\r\n
 运行程序文件名\t%s''' % (rundir, filepath, filedir, filename))

#print('----',log.logpath)

import log
a=log.log('test')
a.info('9999')
