f=open('./data.txt',mode='w',encoding='utf8')

num=15000000000
for i in range(0,10):
    t = num + i*100
    f.write('%d, testuser%03d\n' % (t, i+1))

f.close()





