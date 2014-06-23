from pet import Pet
class Cow(Pet):
	def __init__(self, species):
		Pet.__init__(self, species)
		self.price = 5

	def say(self):
		return	"Um bo"