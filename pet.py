class Pet(object):
	def __init__(self, species):
		self.species = species
		self.price = 0

	def show (self):
		return "%s cho nang suat: %s" %(self.species, self.price) + " $/ con"
