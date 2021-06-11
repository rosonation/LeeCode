import PyPDF2

pdfFileObj = open('/Users/tony/Downloads/automate_online-materials/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print("Number of pages :", pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
