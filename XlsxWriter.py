import xlsxwriter

class XlsxWriter:

	workbook = None
	worksheet = None

	def __init__(self, filename):
		global workbook
		
		workbook = xlsxwriter.Workbook(filename)
		
		#add formats

		
	def open(self):
		global workbook
		global worksheet
		
		worksheet = workbook.add_worksheet()
		
		
	def close(self):
		workbook.close()
		
	
	def write(self,row,col,data,format):
		worksheet.write(row,col,data)


###CASE WHEN IN WRITE FUNCTION
#write_string()
#write_number()
#write_blank()
#write_formula()
#write_datetime()
#write_boolean()
#write_url()