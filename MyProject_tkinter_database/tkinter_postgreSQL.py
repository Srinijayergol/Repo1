from tkinter import *
import psycopg2

window=Tk()

def create_table():
    conn = psycopg2.connect("dbname='Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor();
    cur.execute("CREATE TABLE IF NOT EXISTS book (Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
    conn.commit()
    conn.close()

def insert():
    conn = psycopg2.connect("dbname= 'Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor()
    book_title = e2_value.get()
    book_author = e6_value.get()
    book_year = e4_value.get()
    book_isbn = e8_value.get()
    cur.execute("INSERT INTO book VALUES ('%s','%s','%s','%s')" % (book_title, book_author, book_year, book_isbn))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.commit()
    t1.insert(END, rows)
    conn.close()
    #return rows

def delete():
    conn = psycopg2.connect("dbname= 'Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor()
    book_title = e2_value.get()
    cur.execute("DELETE FROM book WHERE Title='%s'" % (book_title,))
    conn.commit()
    conn.close()

def update(Author, Year,ISBN,Title):
    conn = psycopg2.connect("dbname= 'Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor()
    book_title = e2_value.get()
    book_author = e6_value.get()
    book_year = e4_value.get()
    book_isbn = e8_value.get()
    cur.execute("UPDATE book set Author='%s', Year=%s, ISBN=%s WHERE Title='%s'" % (book_author, book_year, book_isbn, book_title))
    conn.commit()
    conn.close()

#frame = Frame(width=5, height=2, bd=1, text="Book STore")
#frame.grid(row=2,column=2)

#create_table()
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
