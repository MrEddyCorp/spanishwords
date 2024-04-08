import sqlite3 as sq

conn =  sq.connect('words.db')
cursor = conn.cursor()



def SaveWord(w):
    try:
        size = str(len(w))
        table_name = "words_"+size
        sql = f'create table if not exists {table_name} (word VARCHAR({size}) NOT NULL)'
        cursor.execute(sql)
        conn.commit()

        sql_in = f"INSERT INTO {table_name}(word) VALUES ('{w.lower()}')"
        cursor.execute(sql_in)
        conn.commit()
    except ValueError:
        print("error")

def getwords(w):
    words = []
    size = str(len(w))
    table_name = "words_"+str(size)
    sql = f'select * from {table_name}'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
        words.append(record[0])
    return words
    