import tkinter as tk
import customtkinter as ctk

app = ctk.CTk()
app.title("Keyboard")
app.configure(padx=25, pady=10, background="black")
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry("%dx%d" % (width, height))
app.minsize(300, 350)
app.resizable(True, True)

ctk.set_appearance_mode("dark")


class Keyboard:
    def __init__(self):
        self.text_box = ctk.CTkTextbox(app, padx=25, pady=25, height=5, font=("arial", 20, "bold"), wrap=tk.WORD)

        for i in range(13):
            app.grid_columnconfigure(i, weight=1)
            if i <= 8:
                app.grid_rowconfigure(i, weight=1)

        self.text_box.grid(row=0, column=0, columnspan=13, rowspan=3, sticky="nsew")
        self.text_box.configure(state="disabled", corner_radius=50, fg_color="#c9c9c9")
        keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '#', 'Backspace',
                'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                'A', 'S', 'Enter', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '?', '!', '%', '+', '@', '*', '=', '$', '€', '£',
                'CLEAR', 'SPACE', 'READ']

        row = 4
        column = 0
        for key in keys:

            if row != 8:
                ctk.CTkButton(app, text=key, height=6, text_color='white', fg_color='black', corner_radius=20,
                              hover_color="#ff8c00",
                              command=lambda x=key: self.select(x)).grid(row=row, column=column, sticky="nsew")
            elif row == 8 and column == 0:
                ctk.CTkButton(app, text=key, text_color='white', fg_color='black', corner_radius=20,
                              hover_color="#ff8c00",
                              command=lambda x=key: self.select(x)).grid(columnspan=3, row=row, column=column,
                                                                         sticky="nsew")
            elif row == 8 and column == 1:
                ctk.CTkButton(app, text=key, text_color='white', fg_color='black', corner_radius=20,
                              hover_color="#ff8c00",
                              command=lambda x=key: self.select(x)).grid(columnspan=7, row=row, column=column + 2,
                                                                         sticky="nsew")
            else:
                ctk.CTkButton(app, text=key, text_color='white', fg_color='black', corner_radius=20,
                              hover_color="#ff8c00",
                              command=lambda x=key: self.select(x)).grid(columnspan=3, row=row, column=column + 8,
                                                                         sticky="nsew")

            column += 1
            if column > 12:
                column = 0
                row += 1

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
            self.text_box.insert(tk.INSERT, '\n Reading not implemented yet')
        else:
            self.text_box.insert(tk.INSERT, key)

        self.text_box.configure(state="disabled")


if __name__ == '__main__':
    k = Keyboard()
    app.mainloop()
