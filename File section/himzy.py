'''text = 'i am here for inform you his information'
print(text.replace('for ','TO'))
print(text)
'''


a = open ('himzy.txt' , 'r')
d = open('himzy_new.txt' , 'w')
b = a.read()


z = b.replace(' for ', ' TO ')
d.write(z)


d.close()
a.close()
