def prime(N):
    yield 2
    for i in range(3,N+1,2):
        for j in range(3,int(i**0.5)+3,2):
            if(i%j==0):
                break
        else:
            yield i 

i=prime(1234567)
while True:
    next(i)
