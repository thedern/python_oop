class Dog:
	"""
	this is a general dog class
	"""
	# class attribute for all dogs
	species = 'mammal'

	def __init__(self, name: str, age: int):
		# instance attributes
		self.name = name
		self.age = age

	def description(self):
		print(self.name, self.age, self.species)

	def bite(self):
		return 'ouch!!!!'

	def birthday(self):
		self.age += 1
