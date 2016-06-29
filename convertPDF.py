from cStringIO import StringIO
import os
#for input file selection dialog
from Tkinter import Tk
from tkFileDialog import askopenfilename

import Statement
import Transaction
import Sheet
import MongoDB

import re

def getFilePath():

	Tk().withdraw()
	filename = askopenfilename()
	return filename
	
#should be a DB method
def dbWriteStatement(statementData):

	#write to database
	#should check for successful connection before doing any of this
	db = MongoDB.MongoDB()
	db.connect()
	#test find
	testFindAllResults = db.findAllTransactions()
	
	#print statementData.convertToDBDoc()
	print db.insert(statementData.convertToDBDoc())

def main():

	#path = getFilePath()
	
	path = '/Users/DM/CreditTransactionExport/INPUT/StephCreditCard.pdf'
	
	db = MongoDB.MongoDB()
	db.connect()
	
	#Description string has 25 chars max
	#location string has 13 chars max + 2 chars to denote the state/province
	#CR indicates a credit return
	transactionReg = re.compile("(\S.{24})(.{13})(..)( +)(\d+\.\d\d)(?!%)(CR)?")

	#Statement object
	statementDescription = path.split("/")
	pdfOutput = Statement.Statement(path, os.path.splitext(statementDescription[-1])[0])
	#print pdfOutput.pdfString

	#create transaction objects and append them to Statement Transactions
	for transaction in transactionReg.findall(pdfOutput.pdfString):
		pdfOutput.transactions.append(Transaction.Transaction(transaction[0].strip(" "), transaction[1] + " " + transaction[2], float(transaction[len(transaction)-2]),  transaction[-1], db))

	#set statement amount
	pdfOutput.calculateTotal()
	newSheet = Sheet.Sheet(os.path.splitext(statementDescription[-1])[0] + '.xlsx')
	#sheet template created here too
	

	newSheet.recordTransactions(pdfOutput, db)
	
	##================
	#print pdfOutput.pdfString
	
	
	#dbWriteStatement(pdfOutput)
	
if __name__ == "__main__":
    main()