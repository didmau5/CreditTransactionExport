from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
#for input file selection dialog
from Tkinter import Tk
from tkFileDialog import askopenfilename

import Statement
import Transaction
import Sheet
import Database

import re

def getFilePath():

	Tk().withdraw()
	filename = askopenfilename()
	return filename

#creates transaction objects given a list of transaction details
#This should be a Transaction method
def createTransaction(transaction):
	resultTransaction= Transaction.Transaction(transaction[0].strip(" "), transaction[1] + " " + transaction[2], float(transaction[len(transaction)-1]),  "TestType")
	return resultTransaction
	
def main():

	path = getFilePath()
	
	#Description string has 25 chars max
	#location string has 13 chars max + 2 chars to denote the state/province
	transactionReg = re.compile("(\S.{24})(.{13})(..)( +)(\d+\.\d\d)")

	#Statement object
	statementDescription = path.split("/")
	pdfOutput = Statement.Statement(path, statementDescription[-1].strip(".pdf"))
	#print pdfOutput.pdfString

	#create transaction objects and append them to Statement Transactions
	for result in transactionReg.findall(pdfOutput.pdfString):
		pdfOutput.transactions.append(createTransaction(result))

	#set statement amount
	pdfOutput.calculateTotal()

	newSheet = Sheet.Sheet(statementDescription[-1].strip(".pdf") + '.xlsx')
	#sheet template created here too
	newSheet.recordTransactions(pdfOutput)
	
	#========================================
	#write to database
	db = Database.Database("localhost", 27017)
	db.connect()
	#test find
	testFindAllResults = db.findAll()
	
	print pdfOutput.convertToDBDoc()
	print db.insert(pdfOutput.convertToDBDoc())
	
	
	#========================================
	
if __name__ == "__main__":
    main()