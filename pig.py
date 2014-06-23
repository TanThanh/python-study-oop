from pet import Pet
class Pig(Pet):
	def __init__(self, species, price):
		Pet.__init__(self, species)
		self.price = 4

	def say(self):
		return	"Fuck"