from tkinter import *
from tkinter import messagebox

wn = Tk()
wn.title("Calci")
num = StringVar()
n1 = ""

# create entry box to get input from user
entry = Entry(wn, textvariable = num, font = ("Times" , 18 , "bold"), width = 5, bd = 10, justify = "right").grid(sticky = "WE", column = 1, columnspan = 4)

def author():
    messagebox.showinfo("Author", "Muggalla Rahul")

def add(n):
    n1 = num.get()
    if n1 == "Error":
        num.set(n)
    else:
        num.set(n1+n)

def cal():
    try:
        num.set(eval(num.get()))
    except:
        num.set("Error")

def delete():
    num.set(num.get()[:-1])

def reset():
    num.set("")

# create buttons
clear = Button(wn, text = "C", command = reset, font = ("Times 18"), width = 5).grid(row = 1 ,column = 1)
delete = Button(wn, text = "del", command = delete, font = ("Times 18"), width = 5).grid(row = 1, column = 2)
div = Button(wn, text = "/", command = lambda:add("/"), font = ("Times 18"), width = 5).grid(row = 1, column = 3)
mult = Button(wn, text = "x", command = lambda:add("*"), font = ("Times 18"), width = 5).grid(row = 1, column = 4)
seven = Button(wn, text = "7", command = lambda:add("7"), font = ("Times 18"), width = 5).grid(row = 2, column = 1)
eight = Button(wn, text = "8", command = lambda:add("8"), font = ("Times 18"), width = 5).grid(row = 2, column = 2)
nine = Button(wn, text = "9", command = lambda:add("9"), font = ("Times 18"), width = 5).grid(row = 2, column = 3)
addition = Button(wn, text = "+", command = lambda:add("+"), font = ("Times 18"), width = 5).grid(row = 2, column = 4)
four = Button(wn, text = "4", command = lambda:add("4"), font = ("Times 18"), width = 5).grid(row = 3, column = 1)
five = Button(wn, text = "5", command = lambda:add("5"), font = ("Times 18"), width = 5).grid(row = 3, column = 2)
six = Button(wn, text = "6", command = lambda:add("6"), font = ("Times 18"), width = 5).grid(row = 3, column = 3)
sub = Button(wn, text = "-", command = lambda:add("-"), font = ("Times 18"), width = 5).grid(row = 3, column = 4)
one = Button(wn, text = "1", command = lambda:add("1"), font = ("Times 18"), width = 5).grid(row = 4, column = 1)
two = Button(wn, text = "2", command = lambda:add("2"), font = ("Times 18"), width = 5).grid(row = 4, column = 2)
three = Button(wn, text = "3", command = lambda:add("3"), font = ("Times 18"), width = 5).grid(row = 4, column = 3)
equal = Button(wn, text = "=", command = cal, font = ("Times 18"), width = 5).grid(sticky = "NS", row = 4, column = 4, rowspan = 2)
zero = Button(wn, text = "0", command = lambda:add("0"), font = ("Times 18"), width = 11).grid(row = 5, column = 1, columnspan = 2)
dot = Button(wn, text = ".", command = lambda:add("."), font = ("Times 18"), width = 5).grid(row = 5, column = 3)
author = Button(wn, text = "Author", command = author, font = ("Times 18"), width = 5).grid(row = 6, column = 1, columnspan = 4)

wn.mainloop()