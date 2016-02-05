from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

import Transaction

class Statement:
	
	#GIVEN PATH TO PDF, RETURNS STRING
	#http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
	def convert_pdf_to_txt(self,path):
		rsrcmgr = PDFResourceManager()
		retstr = StringIO()
		codec = 'ascii'
		laparams = LAParams()
		device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
		fp = file(path, 'rb')
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		password = ""
		maxpages = 0
		caching = True
		pagenos=set()
		for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
			interpreter.process_page(page)
		fp.close()
		device.close()
		str = retstr.getvalue()
		retstr.close()
		return str
		
	def __init__(self, path,description):
		self.description = description
		self.path = path
		self.pdfString = self.convert_pdf_to_txt(path)
		self.transactions = []
		self.amount = 0
		
	def populateTransactions(self):
		print "got here: populateTransactions()"
		
	def calculateTotal(self):
		for transaction in self.transactions:
			self.amount += transaction.amount
		
	def getNumTransactions(self):
		return len(self.transactions)
		
	def printTransactions(self):
		for transaction in self.transactions:
			transaction.printTransaction()
		
	def printStatement(self):
		print self.description
		print "========================="
		print "Total:                   " + str(self.amount)
		print "Number of Transactions:  " + str(self.getNumTransactions())
		#get user input: print all transactions?