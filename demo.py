from pet import Pet
from dog import Dog
from cat import Cat
from cow import Cow
from farm import Farm


# Nhap danh sach Pet
pet1 = Dog("dog")
pet2 = Dog("dog")
pet3 = Dog("dog")

list_pets = [pet1, pet2, pet3]
farm = Farm(list_pets)

print farm
print "Total price: " + str(farm.total_price())



# Xuat tong san luong


# Cho tung pet noi

# pet1 = Dog(species = "Dog")
# pet2 = Cow(species = "Cow")
#
# pet_list = [pet1, pet2]
# HappyFarm = Farm(pet_list)
# HappyFarm.farm_show()
#
# print pet1.show()
# print pet2.show()
# print pet1.say()
