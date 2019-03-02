
from speech import Speech
from raport import Raport

class Jarvis():

    def __init__(self, Speech, Raport):
        self.s = Speech
        self.r = Raport

    def say_hello(self):
        self.s.text_to_speech("Dzień dobry. W czym mogę pomóc?")
        self.s.speech_to_text()

    def command(self):
        if "jaka jest pogoda".upper() in self.s.speech:
            self.r.weater("https://www.google.com/search?q=pogoda&oq=pogoda&aqs=chrome.0.69i59j0l5.3511j0j8&sourceid=chrome&ie=UTF-8")
            self.s.text_to_speech("Mamy " + self.r.temperature + " stopnie celcjusza, oraz jest " + self.r.atmospheric_conditions + ". Szansa opadów to " + self.r.precipitation)
            self.end()

        if "jaka pogoda będzie jutro".upper() in self.s.speech:
            self.r.weater("https://www.google.com/search?q=pogoda+na+jutro&oq=pogoda+na+&aqs=chrome.1.69i57j0l5.7399j1j8&sourceid=chrome&ie=UTF-8")
            self.s.text_to_speech("Będzie " + self.r.temperature + " stopni celcjusza, oraz będzie " + self.r.atmospheric_conditions + ". Szansa opadów to " + self.r.precipitation)
            self.end()

        if "opowiedz mi o".upper() in self.s.speech:
            phrase = self.s.speech[14:].lower().split()
            phrase = "+".join(phrase)
            try:
                self.s.text_to_speech(self.r.info_centre(phrase))
            except:
                self.s.text_to_speech(self.r.info_right(phrase))
            self.end()

        else:
            self.s.text_to_speech("Tego jeszcze nie umiem!")
            self.end()

    def end(self):
        self.s.text_to_speech("Czy mogę zrobić coś jeszcze?")
        self.s.speech_to_text()
        if self.s.speech != "nie dziękuję".upper():
            self.command()
        else:
            self.s.text_to_speech("Do usług!")

j = Jarvis(Speech(), Raport())
j.say_hello()
j.command()
j.end()