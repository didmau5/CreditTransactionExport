class Transaction:
		
	def __init__(self, description, location, amount, type):
		self.description = description
		self.location = location
		self.amount = amount
		self.type = type
		
	def printTransaction(self):
		print str(self.description) + ";   " + str(self.amount) + ";   " + str(self.location)