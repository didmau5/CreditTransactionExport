from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

import Statement
import Transaction

import re

#path variables
WINDOWS_PATH = "C:\Users\dmow\Documents\CreditTransactionExport\Input\NOV14.pdf"
OSX_PATH = "/Users/DM/Downloads/creditStatementConversion/Input/NOV14.pdf"

##TEST PRINT LIST
def printRawTransactions(transactions):
	for i in transactions:
		print i
	
#creates transaction objects given a list of transaction details
def createTransaction(transaction):
	resultTransaction= Transaction.Transaction(transaction[0].strip(" "), transaction[1] + " " + transaction[2], transaction[len(transaction)-1],  "TestType")
	
	resultTransaction.printTransaction()
	#print transaction
	
	#NEED TO ADD DATA STRUCTURE TransactionType, for now, using TestType string

#Statement object
pdfOutput = Statement.Statement(WINDOWS_PATH)
print pdfOutput.pdfString
#test print transactions
#printRawTransactions(pdfOutput.pdfString)


#testReg = re.compile("\d\d")
transactionReg = re.compile("(\S.{24})(.{13})(..)( +)(\d+\.\d\d)")
#transactionRegSearchResult = 
for result in transactionReg.findall(pdfOutput.pdfString):
	createTransaction(result)
#print testReg.search("12")
