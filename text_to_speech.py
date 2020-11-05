import PyPDF2
import pyttsx3

def is_file_found(file_name):
	try:
		file_object = open(file_name)
	except FileNotFoundError:
		print("ERROR IN OPENING THE FILE OR FILE NOT FOUND")
		exit()

print("Do you want to read a text file or PDF :\n1. Text file\n2. PDF\n")
choice = int(input("Enter your choice: "))
if choice == 1:
	file_name = input("Provide text file to read: ")
	is_file_found(file_name)
	with open(file_name) as file_object:
		text = file_object.read()
	file_object.close()
elif choice == 2:
	PDF_file_name = input("Provide a PDF file name present in your currect woring directory: ")
	is_file_found(PDF_file_name)
	PDF_file_object = open(PDF_file_name, 'rb') 
	pdfReader = PyPDF2.PdfFileReader(PDF_file_object) 
	print("Number of pages in PDF: " + str(pdfReader.numPages))
	page_number = int(input("Specify a page number in PDF: "))
	page_object = pdfReader.getPage(page_number - 1) 
	text = page_object.extractText()
	PDF_file_object.close()
else:
	print("INVALID CHOICE")
try:
	speaker = pyttsx3.init()
	speaker.say(text)
	speaker.runAndWait()
except Exception:
	print("EXIT")
