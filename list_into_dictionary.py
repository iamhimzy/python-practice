print("hello world")
animal={
    "lion": ["Carnivores","danger"],
    "cow": ["Herbivores","innocent"],
 }

a=input("Animal name - ")
b=input("name property -")

#print( a in animal.keys() )

if a in animal.keys():
    animal[a].append(b)
    print(animal[a])
else:
    print('Animal name not available')
