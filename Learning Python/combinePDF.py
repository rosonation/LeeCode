import PyPDF4
import os

# Get all PDF filenames.

pdfFiles = []
for filename in os.listdir('/Users/tony/Downloads/automate_online-materials'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

print("All PDF filenames is:", pdfFiles)
pdfFiles.sort(key=str.lower)
print("All PDF filenames is:", pdfFiles)

pdfWriter = PyPDF4.PdfFileWriter()
# Loop through all the PDF files.
for filename in pdfFiles:
    os.chdir('/Users/tony/Downloads/automate_online-materials')
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
    # print("Currently path is:",os.path.abspath(os.curdir))
    if pdfReader.isEncrypted is True:
        print('current decrypt filename is:', filename)
        if pdfReader.decrypt('swordfish'):
            print("decrypt compelete.")
        else:
            print("Wrong password!.")
    # Loop through all the pages (except for the first page) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutputFile = open('/Users/tony/Tony/PDF/allminutes.pdf', 'wb')
print("Save PDF to file:", '/Users/tony/Tony/PDF/allminutes.pdf')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
