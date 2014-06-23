class Farm():

	def __init__(self, pet_list):
		# tao danh sach pet
		self.pets = []
		for i in pet_list:
			self.pets.append(i)

		self.total = 0;

	def total_price(self):
		total_price = 0
		for pet in self.pets:
			total_price = total_price + pet.price

		self.total = total_price
		return self.total

	def __str__(self):
		result = ""
		for index in range(0, len(self.pets)):
			result = result + str(index) + ". " + self.pets[index].species + "\n"

		return result
