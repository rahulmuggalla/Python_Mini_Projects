from tkinter import *
import calendar

root = Tk()
root.title("Calendar")
root.geometry("270x340")

def search():
    months = month.get()
    years = year.get()
    month_int = int(months)
    year_int = int(years)
    cal = calendar.month(year_int , month_int)
    textfield.delete(0.0 , END)
    textfield.insert(INSERT , cal)

#create labels to display informatioin for user
lbl = Label(root , text = "Select Mont :",font=("times",15,"bold"))
lbl.place(x=10,y=10)
lbl2 = Label(root , text = "Select Year :",font=("times",15,"bold"))
lbl2.place(x=10,y=50)

#create spinbox to select month and year
month = Spinbox(root , from_ = 1  , to = 12 , width = 5,font=("times",15,"bold"))
month.place(x=160,y=10)
year = Spinbox(root ,  from_ = 1990 , to = 2022 ,width=6,font=("times",15,"bold"))
year.place(x=160,y=50)

#create button to search selected month details
searchbtn = Button(root , text = "Search" ,relief=GROOVE , width = 10,font=("times",15,"bold"),command = search)
searchbtn.place(x=70,y=100)

#create text field to display searched month details
textfield = Text(root , height = 10 ,bd=5, width = 25,relief=GROOVE,fg='red')
textfield.place(x=17,y=150)

root.mainloop()