import MongoDB

class Transaction:
	
	RESTAURANTS = "REST"
	PARKING = "PARK"
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
		"Hapa Izakaya",
		"Akbars Own Dining",
		"Wildtale",
		"Nando's",
		"The Chopped Leaf",
		"Dominos",
		"Trees",
		"Bella Gelateria"
		]
		
		parkGroupList = ["Impark",
		"Easypark"
		]
		
		for restKeyword in restGroupList:
			if((restKeyword.upper() in self.description) and self.amount > 14 ):
				self.type = self.RESTAURANTS
				return self.RESTAURANTS
		
		for parkKeyword in parkGroupList:
			if((parkKeyword.upper() in self.description)):
				self.type = self.PARKING
				return self.PARKING
		
		
		return self.TYPE_NOT_DEFINED
		