from PyPDF2 import PdfFileReader, PdfFileWriter

# Output object
out = PdfFileWriter()

# Reading a PDF
path = input("Enter file path_\t")
file = PdfFileReader(path)
num = file.numPages

# Iterating thru the PDF
for pg in range(num):
    page = file.getPage(pg)
    # And adding them to the output object
    out.addPage(page)

# Creating a Password
pw = input("Enter new password_\t")
out.encrypt(pw)

# Creating a new (encrypted) file and adding the output abject into it.
newfile = input("Enter a new name for the encrypted file_\t")
with open(newfile,"wb") as f:
    out.write(f)
print("File Encrypted!")