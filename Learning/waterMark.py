import PyPDF4

minutesFile = open('/Users/tony/Downloads/automate_online-materials/meetingminutes.pdf', 'rb')
pdfReader = PyPDF4.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfFileWatermark = open('/Users/tony/Downloads/automate_online-materials/watermark.pdf', 'rb')
pdfWatermarkReader = PyPDF4.PdfFileReader(pdfFileWatermark)
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF4.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open('/Users/tony/Tony/PDF/watermarkCover.pdf', 'wb')
print("Write PDF to file:", '/Users/tony/Tony/PDF/watermarkCover.pdf')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()
