from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

import Statement
import Transaction

#path variables
WINDOWS_PATH = "C:\Users\dmow\Desktop\creditStatementConversion\Input\NOV14.pdf"
OSX_PATH = "/Users/DM/Downloads/creditStatementConversion/Input/NOV14.pdf"

##TEST PRINT LIST
def printRawTransactions(transactions):
	for i in transactions:
		print i
	
#checks next line for string 'US DOLLAR'
#returns true if found, meaning there are more transactions
#return false if not found, meaning there are no more transactions
def checkNextLine(transaction):
	print "check: " + str(transaction)
	
	#if("US DOLLAR" in transaction):
		#print transaction
	#	return True
	#else:
	#	return False
	
#given an index in the transactionIndex list, prints transactions up to end of group
#detects the next newline, signalling the end of the transaction group
#NEED TO FIND A WAY TO LOOK ANOTHER LINE AHEAD FOR 'US DOLLAR' MEANING THE TRANSACTION GROUP HAS MORE ENTRIES
def getTransactions(index, transactions):
	for transaction in transactions[index:]:
		if (len(transaction) == 0):
			#if(not checkNextLine(transactions[ind+1:ind+2])):
			return
		else:
			print str(index) + transaction

#given raw transaction list, returns indices of the first transaction in a group
def getTransactionIndices(transactions):
	amountFlagIndices = []
	#find 'Amount' in this string, what follows are transactions
	for ind, val in enumerate(transactions):
		if (val=='Amount'):
			amountFlagIndices.append(ind)
	return [x+2 for x in amountFlagIndices]

#return string of pdf conversion
pdfOutput = Statement.Statement(WINDOWS_PATH)

#test print transactions
#printRawTransactions(pdfOutput.pdfString)

#holds indices of first transaction per group of transactions
transactionIndices = getTransactionIndices(pdfOutput.pdfString)

#print transactionIndices

#get transactions
for i in transactionIndices:
	getTransactions(i, pdfOutput.pdfString)


	
####

# TRANSACTION
# >amount
# >description
# >type

###

# STATEMENT
# >pdf path
# >return string
# >total

###
