import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor();
    cur.execute("CREATE TABLE IF NOT EXISTS book (Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
    conn.commit()
    conn.close()

def insert(book_title, book_author, book_year, book_isbn):
    conn = psycopg2.connect("dbname= 'Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES ('%s','%s','%s','%s')" % (book_title, book_author, book_year, book_isbn))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(book_title):
    conn = psycopg2.connect("dbname= 'Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE Title='%s'" % (book_title,))
    conn.commit()
    conn.close()

def update(Author, Year,ISBN,Title):
    conn = psycopg2.connect("dbname= 'Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE book set Author='%s', Year=%s, ISBN=%s WHERE Title='%s'" % (Author, Year, ISBN, Title))
    conn.commit()
    conn.close()

#create_table()
