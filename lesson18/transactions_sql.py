# https://www.psycopg.org/docs/connection.html
import psycopg2

from lesson18.config import get_config

# Psycopg commits the transaction if no exception occurs within the with block,
# and otherwise it rolls back the transaction.

params = get_config()

conn: psycopg2._psycopg.connection = None

with psycopg2.connect(**params) as conn:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO transactions...")
        cur.execute("update table accounts set...")
        #...

    # conn.commit()
    # conn.rollback()


conn.close()




