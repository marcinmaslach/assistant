from gtts import gTTS
import os
import speech_recognition as sr

"""This is class to change text to speech and vice versa"""

class Speech():

    def __init__(self):

        self.speech = " "

    def text_to_speech(self, text):
        obj = gTTS(text, "pl")
        obj.save("/home/marcin/Pulpit/assistant/myvoice.mp3")
        os.system("mplayer myvoice.mp3 -af scaletempo -speed 1.2")

    def speech_to_text(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            self.speech = r.recognize_google(audio, language="pl-PL").upper()
        except:
            self.speech = "Przepraszam, nie zrozumiałem tego co powiedziałeś. Mógłbyś powtórzyć?".upper()

    def end(self):
        if self.speech == "dziękuję".upper():
            pass
        else:
            self.speech_to_text()


