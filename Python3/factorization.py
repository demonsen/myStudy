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

print(factorization(88))
