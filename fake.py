animal = {
    'lion' : [ 'Carnivores','Big Claws' ],
    'elephant' : [ 'Hervibores','No Claws' ],
    'crow' : [ 'Herbivores' , 'Medium Claws'],
}

'''
li = [ 1,2,3]
li.append(46)
print(li)
'''

animal_name = input('Name of animal-')
animal_pro  = input('Animal property-')

animal[animal_name].append(animal_pro)

print(animal[animal_name])
