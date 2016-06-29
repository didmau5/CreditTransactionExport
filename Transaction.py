import MongoDB

class Transaction:
	
	RESTAURANTS = "REST"
	TYPE_NOT_DEFINED = ""
	
	def __init__(self, description, location, amount, type, db):
		self.description = description
		self.location = location
		self.amount = amount
		self.type = type
		
		if (self.type == 'CR'):
			self.amount = -self.amount
		self.findType(db)

	def printTransaction(self):
		print str(self.description) + ";   " + str(self.amount) + ";   " + str(self.location) + ";	" + self.type
		
	def findType(self, db):
	#get this from DB - hardcoded for testing purposes
		restGroupList = ["The Greek By Anatoli",
		"Salathai",
		"Twisted Fork",
		"Jam",
		"Yaletown Distilling Co",
		"Five Guys",
		"Parlour",
		"Hubbub",
		"Bellaggio",
		"Caliburger",
		"Biercraft",
		"Per Se Social Corner",
		"Shizen Ya",
		"Ramen Zinya",
		"Pastis",
		"Hapa Izakaya"
		]
		
		for keyword in restGroupList:
			if((keyword.upper() in self.description) and self.amount > 15 ):
				self.type = self.RESTAURANTS
				return self.RESTAURANTS
		
		return self.TYPE_NOT_DEFINED
		