from pet import Pet
class Chicken(Pet):
	def __init__(self, species, price):
		Pet.__init__(self, species)
		self.price = 2

	def say(self):
		return	"Cuc tac Cuc tac"