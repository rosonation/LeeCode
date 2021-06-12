import PyPDF4

minutesFile = open('/Users/tony/Downloads/automate_online-materials/meetingminutes.pdf', 'rb')
pdfReader = PyPDF4.PdfFileReader(minutesFile)
# page = pdfReader.getPage(0)

pdfWriter = PyPDF4.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    # rotatedPage = pdfReader.getPage(pageNum).rotateClockwise(90)
    normalPage = pdfReader.getPage(pageNum)
    # pdfWriter.addPage(rotatedPage)
    pdfWriter.addPage(normalPage)
resultPdfFile = open('/Users/tony/Tony/PDF/rotatedPage.pdf', 'wb')
print("Write PDF to file:", '/Users/tony/Tony/PDF/rotatedPage.pdf')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()
