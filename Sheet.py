import xlsxwriter

class Sheet:
		
	filename = None
	workbook = None
		
	def __init__(self, filename):
		
		global workbook
		self.filename = filename
		
		#create workbook
		workbook = xlsxwriter.Workbook(self.filename)

	def recordTransactions(self, pdfString):

		worksheet = workbook.add_worksheet()
		
		self.createSheetTemplate(worksheet)
		
		#add Currency Format
		currencyFormat = workbook.add_format()
		currencyFormat.set_num_format('"$"#,##0.00')
		
		#start transactions here in sheet matrix, since template was written already
		row = 1
		col = 1

		for transaction in (pdfString.transactions):
			worksheet.write(row,col,transaction.description)
			worksheet.write(row,col+1,transaction.amount, currencyFormat)
			row+=1

		workbook.close()
		

	def createSheetTemplate(self, worksheet):
	
		headers = ["Total",
					"Description",
					"Amount",
					"SR",
					"Expensed"]

		row = 0
		col = 0
				
		#add Header Format
		headerFormat = workbook.add_format({'bold':True,'font_size':12 ,'bg_color':'#9BC2E6'})
		grandTotalHeaderFormat = workbook.add_format({'bold':True,'font_size':16 ,'bg_color':'#9BC2E6'})
		
		for header in headers:
			if (header == "Total"):
				worksheet.write(row,col,header,grandTotalHeaderFormat)
				col+=1
			else:
				worksheet.write(row,col,header,headerFormat)
				col+=1
		
		#set column widths
		worksheet.set_column('A:A', 20)
		worksheet.set_column('B:B', 26)
		worksheet.set_column('D:E', 9)
		
		print "got here: createSheetTemplate"