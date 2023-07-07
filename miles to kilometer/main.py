from tkinter import *
window = Tk()
window.title("miles to kilometer")
window.minsize(height=300, width=500)


def calculate():
    var = float(voroodi.get())
    meghadr = var * 1.6
    adad.config(text=meghadr)

meghadr = ''
voroodi = Entry()
voroodi.grid(column=1, row=0)
miles = Label(text="Miles")
miles.grid(column=2, row=0)
equal = Label(text="is equal to")
equal.grid(column=0, row=1)
adad = Label(text=meghadr)
adad.grid(column=1, row=1)
km = Label(text="KM")
km.grid(column=2, row=1)
button = Button(text="calculate", command=calculate)
button.grid(column=1, row=2)
window.mainloop()
