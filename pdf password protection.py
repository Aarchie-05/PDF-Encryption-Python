from PyPDF2 import PdfFileReader , PdfFileWriter
# Open the current pdf
file_pdf = PdfFileReader('Test.pdf')
# Object for pdf writer
out_pdf = PdfFileWriter()

for i in range(file_pdf.numPages):
    page_details = file_pdf.getPage(i)
    # Add to the output page
    out_pdf.addPage(page_details)
password = "Aarchie@123"
out_pdf.encrypt(password)
with open("encryptedTest.pdf","wb") as filename:
    out_pdf.write(filename)