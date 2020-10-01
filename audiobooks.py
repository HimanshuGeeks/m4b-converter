import pyttsx3  # package text to speech
import PyPDF2   # package to read the pdf
from tkinter.filedialog import *

book = askopenfilename()  # opens the pop up to select the book pdf
pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.numPages
print(pages)            #to get number of pages of the given book


for num in range(1,pages):
    page = pdfReader.getPage(num) #to read from page_2 of the book
    text = page.extractText()
    speaker = pyttsx3.init()   # initialization#to get the text from pdf
    speaker.say(text)           # to speak out thr text
    speaker.runAndWait()
#made by himanshuGeeks
