import pyttsx3                      # Text to Speach
import PyPDF2                       # PDF Reader
text = "I am alive"
 
engine = pyttsx3.init()
rate = 100
engine.setProperty("rate", rate)
engine.say(text)
engine.runAndWait()

read_file = input("FILENAME: ")
book = open(read_file + '.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

starting_page = input("Start from page: ")

for num in range(int(starting_page), pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()