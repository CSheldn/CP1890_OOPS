import sqlite3

conn = sqlite3.connect('class_example.sqlite')

c = conn.cursor()
query = """CREATE TABLE IF NOT EXISTS students 
            (id INTEGER PRIMARY KEY,
            Firstname TEXT,
            LastName TEXT,
            age INTEGER,
            marks INTEGER);"""
print(query)
c.execute(query)
print("Table has been created")

c.execute("""INSERT INTO students VALUES (1, 'Sheldon', 'Jacque', 22, 100)""")
conn.commit()
conn.close()

