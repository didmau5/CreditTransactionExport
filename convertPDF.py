from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

import Statement
import Transaction
import Sheet

import xlsxwriter

import re

#path variables
WINDOWS_PATH = "C:\Users\dmow\Documents\CreditTransactionExport\Input\OCT15.pdf"
OSX_PATH = "/Users/DM/Downloads/creditStatementConversion/Input/NOV14.pdf"

path = WINDOWS_PATH

#creates transaction objects given a list of transaction details
def createTransaction(transaction):
	resultTransaction= Transaction.Transaction(transaction[0].strip(" "), transaction[1] + " " + transaction[2], float(transaction[len(transaction)-1]),  "TestType")
	return resultTransaction

#Statement object
statementDescription = path.split("\\")
pdfOutput = Statement.Statement(WINDOWS_PATH, statementDescription[-1].strip(".pdf"))
#print pdfOutput.pdfString

#Description string has 25 chars max
#location string has 13 chars max + 2 chars to denote the state/province
transactionReg = re.compile("(\S.{24})(.{13})(..)( +)(\d+\.\d\d)")

#create transaction objects and append them to Statement Transactions
for result in transactionReg.findall(pdfOutput.pdfString):
	pdfOutput.transactions.append(createTransaction(result))

#for transaction in pdfOutput.transactions:
#	transaction.printTransaction()

#set statement amount
pdfOutput.calculateTotal()
pdfOutput.printTransactions()

#print to console
print pdfOutput.amount

#===================================
#BREAK THIS INTO METHOD
#1.	setup sheet template (formulae and headers)
#2. populate with transactions
#==================================
#Excel Write Test
workbook = xlsxwriter.Workbook(statementDescription[-1].strip(".pdf") + '.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for transaction in (pdfOutput.transactions):
	worksheet.write(row,col,transaction.description)
	worksheet.write(row,col+1,transaction.amount)
	row+=1

workbook.close()