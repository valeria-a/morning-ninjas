import psycopg2

l = []
for i in range(200):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="bank",
        user="postgres",
        password="postgres")
    print(conn)
    l.append(conn)
# conn.close()
# print(conn)