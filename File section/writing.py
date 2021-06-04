name = input('Type your name - ')

if len(name) > 4:
    f = open('input.txt','w')
    for x in range(100):
        f.write( str(x) + '.) ' )
        f.write(name)
        f.write('\n')
    f.close()
else:
    print('Please type atleast 5 characters')
