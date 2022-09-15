# from googletrans import Translator

from gtts import gTTS
import playsound
# trans = Translator()
# str1=input("Enter a string: ")
# language=input("Enter the language: ")
# out = trans.translate(str1, dest=language)
# print(out)
# print(out.text)

#it speeks!!!
def speak1():

    myobj=gTTS(text="Welcome",lang='en')
    myobj.save("welcome2.mp3")
    playsound.playsound("welcome2.mp3")