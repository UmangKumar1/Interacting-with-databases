import psycopg2
#this creates the table and makes the database file (only applicable in sqllite)
def createTable():
    #connects to the db file
    conn = psycopg2.connect("dbname=databasename user=mehakkumar password=Kumars host=localhost port= 5432")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
#this sections allows you to enter more items into your data base
def enterValues(item, quantity, price):
    conn = psycopg2.connect("dbname=databasename user=mehakkumar password=Kumars host=localhost port= 5432")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item, quantity, price))
    conn.commit()
    conn.close()
#this shows you the current db file in a python list
def view():
    conn = psycopg2.connect("dbname=databasename user=mehakkumar password=Kumars host=localhost port= 5432")
    cur = conn.cursor()
    cur.execute("SELECT * from store")
    rows = cur.fetchall()
    conn.close()
    return rows
#allows you to enter the item you want to delete
def delete(item):
    conn = psycopg2.connect("dbname=databasename user=mehakkumar password=Kumars host=localhost port= 5432")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (item,))
    conn.commit()
    conn.close()

def update(quantity,price, item):
    conn = psycopg2.connect("dbname=databasename user=mehakkumar password=Kumars host=localhost port= 5432")
    cur = conn.cursor()
    cur.execute("UPDATE store Set quantity = %s,price = %s WHERE item = %s", (quantity,price, item))
    conn.commit()
    conn.close()

update(20, 10, "orange")
print(view())
