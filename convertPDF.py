from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

import Statement
import Transaction
import Sheet

import re

#path variables
#need better way to get path, user input? / browse to GUI?
WINDOWS_PATH = "C:\Users\dmow\Documents\CreditTransactionExport\Input\JAN16.pdf"
OSX_PATH = "/Users/DM/Downloads/creditStatementConversion/Input/NOV14.pdf"

path = WINDOWS_PATH

#Description string has 25 chars max
#location string has 13 chars max + 2 chars to denote the state/province
transactionReg = re.compile("(\S.{24})(.{13})(..)( +)(\d+\.\d\d)")

#creates transaction objects given a list of transaction details
#This should be a Transaction method, or a Statement method?
def createTransaction(transaction):
	resultTransaction= Transaction.Transaction(transaction[0].strip(" "), transaction[1] + " " + transaction[2], float(transaction[len(transaction)-1]),  "TestType")
	return resultTransaction

#Statement object
statementDescription = path.split("\\")
pdfOutput = Statement.Statement(path, statementDescription[-1].strip(".pdf"))
#print pdfOutput.pdfString

#create transaction objects and append them to Statement Transactions
for result in transactionReg.findall(pdfOutput.pdfString):
	pdfOutput.transactions.append(createTransaction(result))

#TESTPRINT
#for transaction in pdfOutput.transactions:
#	transaction.printTransaction()

#set statement amount
pdfOutput.calculateTotal()

#TESTPRINT
#pdfOutput.printTransactions()

#TESTPRINT
#print to console
#print pdfOutput.amount

newSheet = Sheet.Sheet(statementDescription[-1].strip(".pdf") + '.xlsx')
#sheet template created here too
newSheet.recordTransactions(pdfOutput)

