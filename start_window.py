import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk


class StartWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.overrideredirect(True)
        height = self.winfo_screenheight()
        width = self.winfo_screenwidth()
        self.geometry("%dx%d+%d+%d" % (width,height, 0, 0))

        image1 = Image.open("img/icon.png")
        self.icon = ImageTk.PhotoImage(image1)
        self.label = tk.Label(self, image = self.icon, bg='white')

        self.wm_attributes("-disabled", True)
        self.wm_attributes("-transparentcolor", "white")
        self.label.pack(fill="both", expand=True)


