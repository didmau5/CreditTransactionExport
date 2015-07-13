class Transaction:
		
	def __init__(self, description, location, amount, type):
		self.description = description
		self.location = location
		self.amount = amount
		self.type = type
		
	def printTransaction(self):
		print self.description + "; " + self.amount + "; " + self.location