import PyPDF2

reader = PyPDF2.PdfReader('Atomic Habits.pdf') #read the pdf file
page = reader.pages[3] # reading page by giving a specific page number
print(page.extractText()) # used to extract text from the page

#print(reader.getNumPages()) #get total number of pages 
#print(reader.getPage(3).extract_text()) # another way to extract a particular page

# Retrieve 10 pages text from a pdf .

# Option 1 : get 10 pages and store in a text file
import logging
logging.basicConfig(filename='Reader.txt',level=logging.INFO , encoding= 'utf-8')

str = ''
for i in range(1,11):
        str = str + '\n' + reader.getPage(i).extract_text()

logging.info(str)

# Option 2 : whole pdf to store in text file

k = ''
for i in range(reader.getNumPages()):
        k = k+ '\n' + reader.getPage(i).extract_text()

with open('Text.txt','w',encoding='utf-8') as l:
        l.write(k)
