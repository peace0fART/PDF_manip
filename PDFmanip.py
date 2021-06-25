from PyPDF2 import PdfFileReader, PdfFileWriter

# Output object
out = PdfFileWriter()

# Reading a PDF
file = PdfFileReader("C:/fakesnake/unrelatednote/git-cheat-sheet.pdf")
num = file.numPages

# Iterating thru the PDF
for pg in range(num):
    page = file.getPage(pg)
    # And adding them to the output object
    out.addPage(page)

# Creating a Password
pw = "pass123"
out.encrypt(pw)

with open("git_enc","wb") as f:
    out.write(f)
print("File Encrypted!")