'''
Append in file
'''

user_email = input('Type your email--')
b = open('eamil_task.txt' , 'a')





if '@' in user_email and user_email.endswith('.com'):
    print(user_email)
    b.write(user_email + '\n' )
else:
    print('Try again')

b.close()
















'''keijser@yahoo.ca
mgreen@att.net
shubhansh@gmail.com
seasweb@att.net
data
hoangle@outlook.com
himzy@gmail.com
data
kludge@aol.com
sacraver@mac.com
data
something@gmail.com
sisyphus@sbcglobal.net
bolow@gmail.com
konst@hotmail.com
dexter@aol.com
adamk@mac.com
ianbuck@verizon.net
something
data
random
'''













'''file_open = open('email.txt' , 'r')

file_read = file_open.read().split()

#print(file_read)

write_file_open = open( 'eamil_task.txt' , 'w')

for x in file_read:
    if  x.endswith('.com') and x.startswith('s'):
        print(x)
        write_file_open.write(x + '\n')

write_file_open.close()

file_open.close()

#d = open ('email.txt' , 'w')'''
