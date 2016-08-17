import MongoDB

class Transaction:
	
	RESTAURANTS = "REST"
	PARKING = "PARK"
	GROCERY = "GROC"
	TYPE_NOT_DEFINED = ""
	
	def __init__(self, description, location, amount, type, db):
		self.description = description
		self.location = location
		self.amount = amount
		self.type = type
		
		#Return transaction detected
		if (self.type == 'CR'):
			self.amount = -self.amount
		self.findType(db)

	def printTransaction(self):
		print str(self.description) + ";   " + str(self.amount) + ";   " + str(self.location) + ";	" + self.type
		
	def findType(self, db):
		cursor = db.findTransactionGroups()
		
		for result in cursor:
			#better way to store this in the db?
			restGroupList = result["Restaurants"]
			parkGroupList = result["Parking"]

		for restKeyword in restGroupList:
			if((restKeyword.upper() in self.description) and self.amount > 14 ):
				self.type = self.RESTAURANTS
				return self.RESTAURANTS
		
		for parkKeyword in parkGroupList:
			if((parkKeyword.upper() in self.description)):
				self.type = self.PARKING
				return self.PARKING
		
		
		return self.TYPE_NOT_DEFINED
		