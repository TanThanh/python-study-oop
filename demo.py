from pet import Pet 
from dog import Dog
from cat import Cat 
from cow import Cow 
from farm import Farm

pet1 = Dog(species = "Dog")
pet2 = Cow(species = "Cow")


pet_list = [pet1, pet2]
HappyFarm = Farm(pet_list)
HappyFarm.farm_show()

print pet1.show()
print pet2.show()
print pet1.say()