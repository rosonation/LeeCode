import PyPDF2

pdf1File = open('/Users/tony/Downloads/automate_online-materials/meetingminutes.pdf', 'rb')
pdf2File = open('/Users/tony/Downloads/automate_online-materials/meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('/Users/tony/Tony/combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
print("Write to file:", '/Users/tony/Tony/combinedminutes.pdf')
pdf1File.close()
pdf2File.close()
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
