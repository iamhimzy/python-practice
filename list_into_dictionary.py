'''
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
    print('Animal name not available')'''



animal={
    "water_animal":["fish","shark","crocodile"],
    "land_animal":["dinasour","lion","elephant"],
    "sky_animal":["bird","peacock","crow"],
    "reptile" : {
        'land_animal' : ['lizard','monitor'],
        'water_animal' :  'anaconda' ,
    }
}
animal['reptile']['land_animal'][ 1]='dragon'
print(animal)
