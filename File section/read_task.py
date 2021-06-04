f = open ( 'new_file.txt', 'r' )
d = f.read()

data_list = d.lower().split()
panda_list = []

for x in data_list:
    if x.startswith('panda'):
        panda_list.append(x)

print('Panda comes ',len(panda_list),' times.')

f.close()
