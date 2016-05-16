from pymongo import MongoClient

class Database:
	
	def __init__(self, ipAddress, port):
		self.ipAddress = ipAddress
		self.port = port
		
		self.client = None
		self. db = None

	def connect(self):
		self.client = MongoClient()
		self.db = self.client.creditcard
	
	#Inserts object into transactions collection and returns the result code
	def insert(self, insertValue):
		result = self.db.transactions.insert_one(insertValue)
		return result
	
	#Enable filter search with parameters
	def findAll(self):
		cursor = self.db.transactions.find()
		return cursor
	
	#def find(self):
	
	#def update(self):
	
	#def close(self):