
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk


class StartWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.overrideredirect(True)
        height = self.winfo_screenheight()
        width=self.winfo_screenwidth()
        self.geometry("%dx%d+%d+%d" % (width,height , 0, 0))
        self.start_label = ctk.CTkLabel(self, text="HELLO", padx=10, pady=10,
                                   text_color="#fdd890", font=('Segoe UI Historic', 40, 'bold'))


        self.start_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        image1 = Image.open("img/icon.png")
        self.test = ImageTk.PhotoImage(image1)
        self.label = tk.Label(self, image = self.test, bg='white', height=height, width=width,  font=('Segoe UI Historic', 50, 'bold'),
                              fg="#fdd890")
        self.label.pack()
        self.lift()
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-disabled", True)
        self.wm_attributes("-transparentcolor", "white")
        self.label.pack()

