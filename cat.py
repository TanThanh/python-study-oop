from pet import Pet
class Cat(Pet):
	def __init__(self, species):
		Pet.__init__(self, species)
		

	def say(self):
		return	"Meo Meo"