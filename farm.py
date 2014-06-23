class Farm():
	def __init__(self, pet_list):
		self.pet_product = []

		for i in pet_list:
			self.pet_product.append(i)

		

	def farm_show(self):
		print "Danh sach nong trai: " + str(self.pet_product)




