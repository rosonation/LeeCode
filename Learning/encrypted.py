import PyPDF4

pdfReader = PyPDF4.PdfFileReader(open('/Users/tony/Downloads/automate_online-materials/meetingminutes.pdf', 'rb'))
print('is encrypted or not :', pdfReader.isEncrypted)
print(pdfReader.getPage(0))
# pdfReader.decrypt('rosebud')
print("contents :", pdfReader.getPage(0))
