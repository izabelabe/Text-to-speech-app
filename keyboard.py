import tkinter as tk
import customtkinter as ctk
import speech_synthesis as ss
from PIL import Image
import settings as st
from autocorrect import Speller
import multiprocessing

class Keyboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Keyboard")
        self.configure(padx=25, pady=10)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight() - 70
        self.geometry("%dx%d+%d+%d" % (self.width, self.height, -8, -1))
        self.minsize(300, 350)
        self.resizable(True, True)

        ctk.set_appearance_mode("dark")
        self.buttons = {}
        self.text_box = ctk.CTkTextbox(self, padx=25, pady=25, height=5, font=('Segoe UI Historic', 30, "bold"),
                                       text_color="black", wrap=tk.WORD)
        self.alt_state = False
        for i in range(13):
            self.grid_columnconfigure(i, weight=1)
            if i <= 8:
                self.grid_rowconfigure(i, weight=1)

        self.text_box.grid(row=0, column=0, columnspan=13, rowspan=3, sticky="nsew")
        self.text_box.configure(state="disabled", corner_radius=50, fg_color="#c9c9c9")

        self.keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '#', 'Backspace',
                     'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                     '*', '=', 'Enter', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '+', '@', '$', 'CORRECT',
                     'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '?', '!', '%', '£',
                     'ALT', 'CLEAR', 'SPACE', 'READ', 'settings']

        row = 4
        column = 0
        for key in self.keys:

            if row != 8:
                self.buttons[key] = ctk.CTkButton(self, text=key, height=6, text_color='white', fg_color='black',
                                                  hover_color="#ff8c00", font=('Segoe UI Historic', 19, 'bold'),
                                                  command=lambda x=key: self.select(x))
                self.buttons[key].grid(row=row, column=column, sticky="nsew")

            else:
                if column == 0:
                    self.buttons[key] = ctk.CTkButton(self, text=key, text_color='white', fg_color='black',
                                                      corner_radius=20,
                                                      hover_color="#ff8c00", font=('Segoe UI Historic', 19, 'bold'),
                                                      command=lambda x=key: self.select(x))

                    self.buttons[key].grid(columnspan=1, row=row, column=column, sticky="nsew")

                elif column == 1:
                    self.buttons[key] = ctk.CTkButton(self, text=key, text_color='white', fg_color='black',
                                                      corner_radius=20,
                                                      hover_color="#ff8c00", font=('Segoe UI Historic', 19, 'bold'),
                                                      command=lambda x=key: self.select(x))
                    self.buttons[key].grid(columnspan=2, row=row, column=column, sticky="nsew")

                elif column == 2:
                    self.buttons[key] = ctk.CTkButton(self, text=key, text_color='white', fg_color='black',
                                                      corner_radius=20,
                                                      hover_color="#ff8c00", font=('Segoe UI Historic', 19, 'bold'),
                                                      command=lambda x=key: self.select(x))
                    self.buttons[key].grid(columnspan=7, row=row, column=column + 1, sticky="nsew")

                elif column == 3:
                    self.buttons[key] = ctk.CTkButton(self, text=key, text_color='white', fg_color='black',
                                                      corner_radius=20,
                                                      hover_color="#ff8c00", font=('Segoe UI Historic', 19, 'bold'),
                                                      command=lambda x=key: self.select(x))
                    self.buttons[key].grid(columnspan=2, row=row, column=column + 7, sticky="nsew")


                else:
                    img = ctk.CTkImage(light_image=Image.open("img/gear.png"), size=(35, 35))
                    self.buttons[key] = ctk.CTkButton(self, image=img, corner_radius=20, fg_color='black', text="",
                                                      hover_color="#ff8c00",
                                                      command=lambda x=key: self.select(x))
                    self.buttons[key].grid(columnspan=1, row=row, column=column + 8, sticky="nsew")

            # image: Flaticon.com

            column += 1
            if column > 12:
                column = 0
                row += 1

        self.tts = ss.TTS()
        if self.tts.language != "pl_PL":
            self.buttons['ALT'].configure(state='disabled')
        else:
            self.buttons['READ'].configure(text='CZYTAJ')
            self.buttons['CLEAR'].configure(text='WYCZYŚĆ')
            self.buttons['CORRECT'].configure(text='POPRAW')

    def correct(self):
        txt = self.text_box.get(1.0, tk.END)
        txt = txt.lower()
        if self.tts.language != "pl_PL":
            spell = Speller()
        else:
            spell = Speller('pl')
        corrected = spell(txt)
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.INSERT, corrected.upper())

    def select(self, key):
        self.text_box.configure(state="normal")
        if key == "SPACE":
            self.text_box.insert(tk.INSERT, ' ')
        elif key == "Backspace":
            temp_text = self.text_box.get(1.0, tk.END)
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.INSERT, temp_text[:-2])
        elif key == 'Enter':
            self.text_box.insert(tk.INSERT, '\n')
        elif key == 'CLEAR':
            self.text_box.delete(1.0, tk.END)
        elif key == 'READ':
            txt = self.text_box.get(1.0, tk.END)
            self.tts.speak(txt)
        elif key == 'ALT':
            if not self.alt_state:
                self.alt_state = True
            else:
                self.alt_state = False
            self.alt()
        elif key == 'settings':
            st.Settings(self)
        elif key == 'CORRECT':
            self.correct()
        else:
            self.text_box.insert(tk.INSERT, self.buttons[key].cget("text"))

        self.text_box.configure(state="disabled")

    def alt(self):
        before = ['A', 'Z', 'X', 'C', 'N', 'L', 'S', 'E', 'O', 'U']
        after = ['Ą', 'Ż', 'Ź', 'Ć', 'Ń', 'Ł', 'Ś', 'Ę', 'Ó', '€']
        exceptions = ['ALT', 'CLEAR', 'SPACE', 'READ', 'settings', 'Backspace', 'Enter', 'CORRECT']
        i = 0
        if self.alt_state:
            for char in before:
                self.buttons[char].configure(text=after[i])
                i += 1
            for key in self.keys:
                if key not in before and key not in exceptions:
                    self.buttons[key].configure(text="")
        else:
            for key in self.keys:
                if key not in exceptions:
                    self.buttons[key].configure(text=key)



