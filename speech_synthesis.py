import re

import pyttsx3
import locale
import ctypes


class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.volume = self.engine.getProperty('volume')
        self.rate = self.engine.getProperty('rate')
        windll = ctypes.windll.kernel32
        self.language = locale.windows_locale[windll.GetUserDefaultUILanguage()]
        if self.language == "pl_PL":
            self.change_to_polish()

    def change_to_polish(self):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            x = re.search("Polish", voice.name)
            if x:
                self.engine.setProperty('voice', voice.id)

    def change_to_english(self):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            x = re.search("English", voice.name)
            if x:
                self.engine.setProperty('voice', voice.id)

    def speak(self, txt):
        self.engine.say(txt)
        self.engine.runAndWait()
