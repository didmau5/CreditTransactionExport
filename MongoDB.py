from pymongo import MongoClient
from bson.objectid import ObjectId
import json

class MongoDB:
	
	def __init__(self):
		self.client = None
		self. db = None

	def connect(self):
		self.client = MongoClient()
		self.db = self.client.creditcard
	
	#Inserts object into transactions collection and returns the result code
	def insert(self, insertValue):
		result = self.db.transactions.insert_one(json.loads(insertValue))
		return result
	
	#find all transactions
	#Enable filter search with parameters
	def findAllTransactions(self):
		cursor = self.db.transactions.find()
		return cursor
	
	#return specified config object
	def findConfigObject(self, configObjectKey):
		#currently uses config object of calculatedFieldFormulas
		#DO NOT LEAVE THIS HARDCODED
		cursor = self.db.configuration.find({'_id':1})
		return cursor
		
	#return specified transaction group
	def findTransactionGroups(self):
		#currently uses config object of Transaction Groups
		#DO NOT LEAVE THIS HARDCODED
		cursor = self.db.configuration.find({"_id" : 2})
		return cursor
		
	#def update(self):
	
	def close(self):
		self.client.close()