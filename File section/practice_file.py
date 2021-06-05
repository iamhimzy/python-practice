a = open ('new_file.txt' , 'r')
b = a.read().split()

y = open ('myk_new.txt' , 'w')

a.close()


for x in b:

    if len(x) > 8:
        print( x)
        y.write(x + '\n')
y.close()
