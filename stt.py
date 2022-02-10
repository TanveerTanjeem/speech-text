
import speech_recognition as sr


def workaround():
    r1=sr.Recognizer()
    r2= sr.Recognizer()
    with sr.Microphone() as source:
        print('speak now')
        audio= r1.listen(source)
    return r2.recognize_google(audio)
#print(workaround())
