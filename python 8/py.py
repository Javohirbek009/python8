import sqlite3
connect = sqlite3.connect('mydatabase.db')

# cursor method

cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS shopping(
    name TEXT,
    last_name TEXT,
    age INTEGER
)
               
""")

cursor.execute("""
INSERT INTO shopping VALUES
('Javohir', 'Nematov', 15),
('Mashhurbek', 'Ergashev', 15)
               
""")

cursor.execute("SELECT * FROM shopping")
print(cursor.fetchall())