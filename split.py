data = [1,3,None,4,5,None,7,8,None,10,11,None]

new_list = []

for x in data:
    if x != None and x >= 5 and x%2==0:
        new_list.append(x)

print(new_list)
