from tkinter import *
import backEnd

window=Tk()

window.wm_title("BookStore")

e1=Label(window,text="Title")
e1.grid(row=0,column=0)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=1)

e3=Label(window,text="Year")
e3.grid(row=1,column=0)

e4_value=StringVar()
e4=Entry(window,textvariable=e4_value)
e4.grid(row=1,column=1)

e5=Label(window,text="Author")
e5.grid(row=0,column=10)

e6_value=StringVar()
e6=Entry(window,textvariable=e6_value)
e6.grid(row=0,column=11)

e7=Label(window,text="ISBN")
e7.grid(row=1,column=10)

e8_value=StringVar()
e8=Entry(window,textvariable=e8_value)
e8.grid(row=1,column=11)

b1=Button(window,text="View All", width=12, command=view)
b1.grid(row=2,column=12)

b2=Button(window,text="Add Entry", width=12, command=insert)
b2.grid(row=3,column=12)

b3=Button(window,text="Delete Selected", width=12, command=delete)
b3.grid(row=4,column=12)

b4=Button(window,text="Update Selected", width=12, command=delete)
b4.grid(row=5,column=12)

t1=Text(window,height=5,width=40)
t1.grid(row=2,column=0)

window.mainloop()
