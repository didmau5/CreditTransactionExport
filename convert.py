import sys
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure

#http://stackoverflow.com/questions/25248140/how-does-one-obtain-the-location-of-text-in-a-pdf-with-pdfminer
def parse_layout(layout):
    for lt_obj in layout:
        if isinstance(lt_obj, LTTextBox): #or isinstance(lt_obj, LTTextLine):
            print(lt_obj.get_text())

def process_page(pdfFile):
	
	parser = PDFParser(pdfFile)
	doc = PDFDocument(parser)
	rsrcmgr = PDFResourceManager()
	laparams = LAParams()
	device = PDFPageAggregator(rsrcmgr, laparams=laparams)
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	
	for page in PDFPage.create_pages(doc):
		interpreter.process_page(page)
		layout = device.get_result()
		parse_layout(layout)
	
def main():

	#check the number of CL arguments
	if (len(sys.argv) == 2):
		print "Exporting",str(sys.argv[1]),"to Excel Sheet..."
		fp = open('NOV14.pdf', 'rb')
		process_page(fp)
	
	else:
		print "Wrong number of arguments, please supply filename."
	
if __name__ == "__main__":
    main()
	

#TODO:
#executable
#