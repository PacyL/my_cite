import psycopg2

def bain():
    conn = psycopg2.connect(
        dbname="",
        user="postgres",
        password="",
        host="localhost",
        port=""
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bain")
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res

def into(id, name, login, password):
    conn = psycopg2.connect(
        dbname="",
        user="postgres",
        password="",
        host="localhost",
        port=""
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bain VALUES (%s, %s, %s, %s)", (id, name, login, password))
    conn.commit()
    cursor.close()
    conn.close()

def delete(id):
    conn = psycopg2.connect(
        dbname="",
        user="postgres",
        password="",
        host="localhost",
        port=""
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM bain WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
