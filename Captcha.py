from tkinter import *
from tkinter import messagebox
import random

text = 'abcdefghijklmnopqrstuvwxyz0123456789'
root = Tk()
root.title("Captcha verification App")
root.geometry("300x150")
captcha = StringVar()
input = StringVar()

def create_captcha():
    c = random.choices(text, k = 5)
    captcha.set(''.join(c))

def check():
    if captcha.get() == input.get():
        messagebox.showinfo('Captcha Verification', 'Captcha verified Succesfully..')
    else:
        messagebox.showerror('Captcha Verification', 'Incorrect Captcha')
    input.set('')

    create_captcha()

Label(root, textvariable=captcha, font="ariel 16 bold").pack(padx=5, pady=5)
Entry(root, textvariable=input, bg='white', font="ariel 12 bold").pack(padx=5, pady=5)
Button(root, text="Check", font="ariel 15 bold", bg='gold', command=check).pack(padx=5, pady=5)

create_captcha()

root.mainloop()