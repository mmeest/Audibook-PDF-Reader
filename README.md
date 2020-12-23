# Audibook-PDF-Reader
Let computer to read your PDF's. Written in Python

## Libraries needed
1. Text to Speech (TTS) library: https://pypi.org/project/pyttsx3/ \
install: **pip install pyttsx3** 

2. Python PDF library: https://pypi.org/project/PyPDF2/ \
install: **pip install PyPDF2**

## To check available voice options
```
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
```

# HAPPY CODING !!!
