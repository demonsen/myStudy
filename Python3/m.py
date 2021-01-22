#!/usr/bin/env python3
# coding:utf-8

import sys  
# import math

def t(num):
    try:
        num = int(num)
    except:
        print("# 请输入一个奇数")
    else:
        if num % 2 == 0:
            print('# 请输入一个奇数！')
            return
        elif num % 5 == 0:
            print('# 请勿输入5及5的倍数！')
            return
        i = len(str(num))            # 数字小 没什么太大差别，这个可能快一些
        #i = int(math.log10(num)+1)  # 数字大这个快 60位以上，数字越大越明显
        s = (10**i-1)
        #print(s ,i )
        while True:
            if s % num == 0:
                break
            else:
                i += 1
                s = (s*10+9)
                s = (10**i-1)
                #s += 9 * (10 ** i) 
        print(' - %d个9: %d 可以被%d整除 | %d / %d = %d ' % (i, s, num, s, num, s/num))
        
if __name__ == '__main__':
    if(len(sys.argv)>1):
        # print(sys.argv)
        t(sys.argv[1])
    else:
        print("--- 示例: \n\t",sys.argv[0] , "11\n\t", t(11))


