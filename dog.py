from pet import Pet
class Dog(Pet):
	def __init__(self, species):
		Pet.__init__(self, species)



	def say(self):
		return	"Gau Gau"