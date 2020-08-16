from tkinter import *


window = Tk()

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l1 = Label(window, text="Author")
l1.grid(row=0, column=2)

l1 = Label(window, text="Year")
l1.grid(row=1, column=0)

l1 = Label(window, text="ISBN")
l1.grid(row=1, column=2)


title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e1 = Entry(window, textvariable=author_text)
e1.grid(row=0, column=3)

year_text = StringVar()
e1 = Entry(window, textvariable=year_text)
e1.grid(row=1, column=1)

ISBN_text = StringVar()
e1 = Entry(window, textvariable=ISBN_text)
e1.grid(row=1, column=3)

List1 = Listbox(window, height=6, width=35)
List1.grid(row=2, column=0)
window.mainloop()

