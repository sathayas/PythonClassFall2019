f = open('IDs.txt','w')
for i in range(10,26):
    f.write('%05d' % i + '\n')
    
f.close()

