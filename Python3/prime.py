def prime(N):
    yield 2
    for i in range(3,N+1,2):
        for j in range(3,int(i**0.5)+3,2):
            if(i%j==0):
                break
        else:
            yield i 

s = prime(200)
for i in s:
    print(i)
