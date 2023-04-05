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
            self.winfo_screenwidth() / 2, self.winfo_screenheight() / 2, (self.winfo_screenwidth()-1100)/ 2,
            (self.winfo_screenheight()-600) / 2))
        self.minsize(1100, 600)
        self.resizable(True, True)
        self.wm_attributes("-topmost",1)
        # volume
        self.volume_label = ctk.CTkLabel(master=self, text="Volume", font=('Segoe UI Historic', 30, 'bold'))
        self.volume_label.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        self.progressbar = ctk.CTkProgressBar(master=self, progress_color='#ff8c00', width=400, height=45)
        self.progressbar.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
        self.progressbar.set(round(self.kb.tts.volume, 1))

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

        self.down.place(relx=0.25, rely=0.25, anchor=tk.CENTER)
        self.up.place(relx=0.75, rely=0.25, anchor=tk.CENTER)

        # rate

        self.rate_label = ctk.CTkLabel(master=self, text="Rate", font=('Segoe UI Historic', 30, 'bold'))
        self.rate_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.rate = ctk.CTkLabel(master=self, text=keyboard.tts.rate,
                                 font=('Segoe UI Historic', 34, 'bold'), fg_color='black', width=220, height=80,
                                 corner_radius = 10, text_color = "#fffbf7" )

        self.rate.place(relx=0.5, rely=0.52, anchor=tk.CENTER)

        self.slower = ctk.CTkButton(self, image=self.minus, text="", height=80, width=120, text_color='white',
                                    fg_color='black',
                                    hover_color="#ff8c00", font=('Segoe UI Historic', 19, 'bold'),
                                    command=lambda x="SLOW": update_rate(x))
        self.faster = ctk.CTkButton(self, image=self.plus, text="", height=80, width=120, text_color='white',
                                    fg_color='black',
                                    hover_color="#ff8c00", font=('Segoe UI Historic', 19, 'bold'),
                                    command=lambda x="FAST": update_rate(x))

        self.slower.place(relx=0.25, rely=0.52, anchor=tk.CENTER)
        self.faster.place(relx=0.75, rely=0.52, anchor=tk.CENTER)

        # language
        self.language_label = ctk.CTkLabel(master=self, text="Language",
                                           font=('Segoe UI Historic', 30, 'bold'))
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
        self.polish.place(relx=0.42, rely=0.85, anchor=tk.CENTER)
        self.english.place(relx=0.57, rely=0.85, anchor=tk.CENTER)

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
            # self.volume.configure(text=round(self.kb.tts.volume, 1))
            self.progressbar.set(round(self.kb.tts.volume, 1))
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
            self.kb.buttons['CORRECT'].configure(text='POPRAW')
            self.kb.buttons['SPACE'].configure(text='SPACJA')
            self.volume_label.configure(text='GŁOŚNOŚĆ')
            self.rate_label.configure(text='PRĘDKOŚĆ')
            self.language_label.configure(text='JĘZYK')
            self.kb.buttons['ALT'].configure(state='normal')
            self.polish.configure(fg_color='#ff8c00')
            self.english.configure(fg_color='black')

        if key == "ENGLISH":
            if self.kb.tts.language == "pl_PL":
                self.kb.tts.change_to_english()
                self.kb.tts.language = 'en_GB'
            self.kb.buttons['READ'].configure(text='READ')
            self.kb.buttons['CLEAR'].configure(text='CLEAR')
            self.kb.buttons['CORRECT'].configure(text='CORRECT')
            self.kb.buttons['SPACE'].configure(text='SPACE')
            self.volume_label.configure(text='VOLUME')
            self.rate_label.configure(text='RATE')
            self.language_label.configure(text='LANGUAGE')
            self.kb.buttons['ALT'].configure(state='disabled')
            self.english.configure(fg_color='#ff8c00')
            self.polish.configure(fg_color='black')
