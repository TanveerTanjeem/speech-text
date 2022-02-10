import pyttsx3

def tts(sentences:str, strong: bool = True):
    text_speech = pyttsx3.init()
    text_speech.say(sentences)
    text_speech.runAndWait()
    return sentences