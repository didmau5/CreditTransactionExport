import xlsxwriter
import json
import MongoDB

class Sheet:
	#Globals
	filename = None
	workbook = None
	
	#formats
	currencyFormat = None
	headerFormat = None
	grandTotalHeaderFormat = None
	grandTotalFormat = None
	subTotalsHeaderFormat = None
	topSubTotalHeaderFormat = None
	
	#calculated fields formulae
		
	def __init__(self, filename):
		
		global workbook
		global currencyFormat
		global headerFormat
		global grandTotalHeaderFormat
		global grandTotalFormat
		global subTotalsHeaderFormat
		global topSubTotalHeaderFormat
		
		self.filename = filename
		
		#create workbook
		workbook = xlsxwriter.Workbook(self.filename)
		
		#SET FORMATS
		#add Currency Format
		currencyFormat = workbook.add_format()
		currencyFormat.set_num_format('"$"#,##0.00')
		#add Header Format
		headerFormat = workbook.add_format({'bold':True,
											'align':'center',
											'font_size':12 ,
											'bg_color':'#9BC2E6'})
		grandTotalHeaderFormat = workbook.add_format({'bold':True,
														'align':'center',
														'font_size':16 ,
														'bg_color':'#9BC2E6'})
		#add grand total format
		grandTotalFormat = workbook.add_format({'align':'center','font_size':16})
		grandTotalFormat.set_num_format('"$"#,##0.00')
		
		#add calculated total format
		topSubTotalHeaderFormat = workbook.add_format({'bold':True,
														'align':'center',
														'font_size':16})
		subTotalsHeaderFormat = workbook.add_format({'bold':True,
														'italic':True})
		
	#def setFormats(self)	
		
	def recordTransactions(self, pdfString, db):

		global currencyFormat
		
		worksheet = workbook.add_worksheet()
		self.createSheetTemplate(worksheet, db)

		#start transactions here in sheet matrix, since template was written already
		row = 1
		col = 1
		for transaction in (pdfString.transactions):
			worksheet.write(row,col,transaction.description)
			worksheet.write(row,col+1,transaction.amount, currencyFormat)
			worksheet.write(row,col+2,transaction.type)
			row+=1

		workbook.close()

	def createSheetTemplate(self, worksheet,db):
	
		self.writeHeader(worksheet)
		self.writeCalculatedFieldHeaders(worksheet)
		self.writeCalculatedFields(worksheet,db)
		
	def writeHeader(self,worksheet):
		headers = ["Total",
					"Description",
					"Amount",
					"Type",
					"Expensed"]

		row = 0
		col = 0
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
	
	def writeCalculatedFieldHeaders(self, worksheet):
		#pull these from DB
		calculatedFieldHeaders=["Grocery Total", 
								"Gas Total",
								"Restaurant Total",
								"BC Ferries Total",
								"Parking Total",
								"Shared Total",
								"Nester's Total", 
								"Choices Total", 
								"Whole Foods Total", 
								"Save On Foods Total",
								"Urban Fair Total", 
								"London Drugs Total",
								"Expense Spent",
								]
								
		topSubTotalHeaders = calculatedFieldHeaders[0:6]
								
		#starting point in sheet of calculated totals
		row = 5
		col = 0
		#spacing between headers
		calculatedRowHeaderSpacing = 4
		
		for header in calculatedFieldHeaders:
			if (header in topSubTotalHeaders):
				worksheet.write(row,col,header, topSubTotalHeaderFormat)
				row = row + calculatedRowHeaderSpacing
			else:
				worksheet.write(row,col,header, subTotalsHeaderFormat)
				row = row + calculatedRowHeaderSpacing
	
	
	def writeCalculatedFields(self,worksheet, db):
		#write to database
		#should check for successful connection before doing any of this
		
		key = 'CalculatedFieldFormulas'
		
		#test find
		cursor = db.findConfigObject(key)
		
		row = 1;
		col = 0;
		
		for result in cursor:
			#do i need to be concerned about the order of the results here?
			#if so use displayOrder to sort
			sortedResults = sorted(result[key], key=lambda k:k['displayOrder'])
			for field in sortedResults:
				#print 'Writing: ' + field['formula'] + ' to excel sheet.'
				worksheet.write(row,col,field['formula'],grandTotalFormat)
				if(row == 1):
					row +=5
				else:
					row += 4