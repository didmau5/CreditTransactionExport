import xlsxwriter

class XlsxWriter:

	workbook = None
	worksheet = None

	def __init__(self, filename):
		global workbook
		
		workbook = xlsxwriter.Workbook(filename)
		
		#add formats
		
		
		
		
	#def open():
	
	#def close():
	
	#def write(row,column,data,format):
	
	