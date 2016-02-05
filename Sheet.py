import xlsxwriter

class Sheet:
		
	filename = None
	
		
	def __init__(self, filename):
		self.filename = filename
		#should create formats here
		
	def recordTransactions(self, pdfString):

		workbook = xlsxwriter.Workbook(self.filename)
		worksheet = workbook.add_worksheet()
	
		#add Currency Format
		currencyFormat = workbook.add_format()
		currencyFormat.set_num_format('"$"#,##0.00')
		
		#add Header Format
		headerFormat = workbook.add_format({'bold':True,'font_size':12 ,'bg_color':'#9BC2E6'})
		grandTotalHeaderFormat = workbook.add_format({'bold':True,'font_size':16 ,'bg_color':'#9BC2E6'})
		
		self.createSheetTemplate(worksheet, headerFormat, grandTotalHeaderFormat)
		
		#start transactions here in sheet matrix, since template was written already
		row = 1
		col = 1

		for transaction in (pdfString.transactions):
			worksheet.write(row,col,transaction.description)
			worksheet.write(row,col+1,transaction.amount, currencyFormat)
			row+=1

		workbook.close()
		

	def createSheetTemplate(self, worksheet, headColumnFormat, grandTotalFormat):
	
		headers = ["Total",
					"Description",
					"Amount",
					"SR",
					"Expensed"]
		row = 0
		col = 0
	
		for header in headers:
			if (header == "Total"):
				worksheet.write(row,col,header,grandTotalFormat)
				col+=1
			else:
				worksheet.write(row,col,header,headColumnFormat)
				col+=1
			
		print "got here: createSheetTemplate"