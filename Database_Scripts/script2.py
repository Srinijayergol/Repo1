import psycopg2

def create_table():
    conn = psycopg2.connect("dbname= 'Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_table(item, quantity, price):
    conn = psycopg2.connect("dbname= 'Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname= 'Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item='%s'" % (item,))
    conn.commit()
    conn.close()

def update_table(quantity, price,item):
    conn = psycopg2.connect("dbname= 'Database1' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store set quantity=%s, price=%s WHERE item='%s'" % (quantity, price, item))
    conn.commit()
    conn.close()

#print(view())
#create_table()
#insert_table("Coffee", 10, 15.99)
#delete("Coffee")
update_table(11, 22.99, "Coffee")
