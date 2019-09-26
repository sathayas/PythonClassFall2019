# writing to a file
f = open('IDs.txt','w')
for i in range(10,26):
    f.write('%05d' % i + '\n')

f.close()


# appending to an existing file
f = open('IDs.txt','a')
for i in range(110,126):
    f.write('%05d' % i + '\n')

f.close()
