#!/usr/bin/env python3
# coding:utf-8

import sys  


def prime(N):
    yield 2
    for i in range(3,N+1,2):
        for j in range(3,int(i**0.5)+2,2):
            if(i%j==0):
                break
        else:
            yield i 
            
            
def factorization(N):
    S = prime(N)
    M = next(S)
    R = []
    T = N
    while True:
        if T == M :
            R.append(M)
            R = str(N) + '=' + '*'.join(str(i) for i in R)
            return R
        elif T % M == 0:
            R.append(M)
            T = T // M
        else:
            M = next(S)


if __name__ == '__main__':
    if(len(sys.argv)>1):
        #print(sys.argv)
        if(len(sys.argv)==2):
            try:
                num = int(sys.argv[1])
            except:
                print("# 请输入一个整数")
            else:
                print(factorization(num))
    else:
        print("--- 示例: \n\t", sys.argv[0] , "88\n\t", factorization(88))

