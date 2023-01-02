import tkinter as tk
import customtkinter as ctk
import speech_synthesis as ss
from PIL import Image


class Settings(ctk.CTkToplevel):
    def __init__(self, keyboard):
        super().__init__()
        self.kb = keyboard
        self.title("Settings")
        self.configure(padx=25, pady=10)
        self.geometry("%dx%d+%d+%d" % (
        self.winfo_screenwidth() / 2, self.winfo_screenheight() / 2, self.winfo_screenwidth() / 4,
        self.winfo_screenheight() / 4))
        self.minsize(300, 350)
        self.resizable(True, True)

        # volume
        self.volume_label = ctk.CTkLabel(master=self, text="Volume", font=('Segoe UI Historic', 25, 'bold'))
        self.volume_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.volume = ctk.CTkLabel(master=self, text=round(self.kb.tts.volume, 1),
                                   font=('Segoe UI Historic', 25, 'bold'))
        self.volume.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.plus = ctk.CTkImage(light_image=Image.open("img/add.png"), size=(40, 40))
        self.minus = ctk.CTkImage(light_image=Image.open("img/remove.png"), size=(40, 40))

        self.down = ctk.CTkButton(self, image=self.minus, text="", height=80, width=120, text_color='white',
                                  fg_color='black',
                                  hover_color="#ff8c00", font=('Segoe UI Historic', 19, 'bold'),
                                  command=lambda x="DOWN": update_volume(x))
        self.up = ctk.CTkButton(self, image=self.plus, text="", height=80, width=120, text_color='white',
                                fg_color='black',
                                hover_color="#ff8c00", font=('Segoe UI Historic', 19, 'bold'),
                                command=lambda x="UP": update_volume(x))

        self.down.place(relx=0.3, rely=0.3, anchor=tk.CENTER)
        self.up.place(relx=0.7, rely=0.3, anchor=tk.CENTER)

        # rate

        self.rate_label = ctk.CTkLabel(master=self, text="Rate", font=('Segoe UI Historic', 25, 'bold'))
        self.rate_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        self.rate = ctk.CTkLabel(master=self, text=keyboard.tts.rate,
                                 font=('Segoe UI Historic', 25, 'bold'))
        self.rate.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        self.slower = ctk.CTkButton(self, image=self.minus, text="", height=80, width=120, text_color='white',
                                    fg_color='black',
                                    hover_color="#ff8c00", font=('Segoe UI Historic', 19, 'bold'),
                                    command=lambda x="SLOW": update_rate(x))
        self.faster = ctk.CTkButton(self, image=self.plus, text="", height=80, width=120, text_color='white',
                                    fg_color='black',
                                    hover_color="#ff8c00", font=('Segoe UI Historic', 19, 'bold'),
                                    command=lambda x="FAST": update_rate(x))

        self.slower.place(relx=0.3, rely=0.55, anchor=tk.CENTER)
        self.faster.place(relx=0.7, rely=0.55, anchor=tk.CENTER)

        # language
        self.language_label = ctk.CTkLabel(master=self, text="Language",
                                           font=('Segoe UI Historic', 25, 'bold'))
        self.language_label.place(relx=0.5, rely=0.70, anchor=tk.CENTER)

        self.PL = ctk.CTkImage(light_image=Image.open("img/polish_flag.png"), size=(120, 80))
        self.UK = ctk.CTkImage(light_image=Image.open("img/UK_flag.png"), size=(120, 80))

        self.polish = ctk.CTkButton(self, image=self.PL, text='',
                                    fg_color='black',
                                    hover_color="#ff8c00", font=('Segoe UI Historic', 19, 'bold'),
                                    command=lambda x="POLISH": self.change_language(x))
        self.english = ctk.CTkButton(self, image=self.UK, text='',
                                     fg_color='black',
                                     hover_color="#ff8c00", font=('Segoe UI Historic', 19, 'bold'),
                                     command=lambda x="ENGLISH": self.change_language(x))
        self.polish.place(relx=0.4, rely=0.80, anchor=tk.CENTER)
        self.english.place(relx=0.6, rely=0.80, anchor=tk.CENTER)

        if self.kb.tts.language == "pl_PL":
            self.change_language('POLISH')
        else:
            self.english.configure(fg_color="#ff8c00")

        def update_volume(key):
            if key == "DOWN":
                if self.kb.tts.volume > 0.01:
                    self.kb.tts.volume -= 0.1
            else:
                if self.kb.tts.volume != 1.0:
                    self.kb.tts.volume += 0.1
            self.volume.configure(text=round(self.kb.tts.volume, 1))
            self.kb.tts.engine.setProperty('volume', self.kb.tts.volume)

        def update_rate(key):
            if key == "SLOW":
                if self.kb.tts.rate > 70:
                    self.kb.tts.rate -= 2
            else:
                if self.kb.tts.rate < 330:
                    self.kb.tts.rate += 2
            self.rate.configure(text=self.kb.tts.rate)
            self.kb.tts.engine.setProperty('rate', self.kb.tts.rate)

    def change_language(self, key):
        if key == "POLISH":
            if self.kb.tts.language != "pl_PL":
                self.kb.tts.change_to_polish()
                self.kb.tts.language = 'pl_PL'
            self.kb.buttons['READ'].configure(text='CZYTAJ')
            self.kb.buttons['CLEAR'].configure(text='WYCZYŚĆ')
            self.volume_label.configure(text='Głośność')
            self.rate_label.configure(text='Prędkość')
            self.language_label.configure(text='Język')
            self.kb.buttons['ALT'].configure(state='enabled')
            self.polish.configure(fg_color='#ff8c00')
            self.english.configure(fg_color='black')

        if key == "ENGLISH":
            if self.kb.tts.language == "pl_PL":
                self.kb.tts.change_to_english()
                self.kb.tts.language = 'en_GB'
            self.kb.buttons['READ'].configure(text='READ')
            self.kb.buttons['CLEAR'].configure(text='CLEAR')
            self.volume_label.configure(text='Volume')
            self.rate_label.configure(text='Rate')
            self.language_label.configure(text='Language')
            self.kb.buttons['ALT'].configure(state='disabled')
            self.english.configure(fg_color='#ff8c00')
            self.polish.configure(fg_color='black')
