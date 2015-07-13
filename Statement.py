from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO


class Statement:
	
	#GIVEN PATH TO PDF, RETURNS STRING
	#http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
	def convert_pdf_to_txt(self,path):
		rsrcmgr = PDFResourceManager()
		retstr = StringIO()
		codec = 'utf-8'
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
		
	def __init__(self, path):
		self.path = path
		self.pdfString = self.convert_pdf_to_txt(path)
		#would be equal to the sum of all transaction amounts
		#self.amount = 0
		
		
	#def printStatement(self):