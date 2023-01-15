# https://www.psycopg.org/docs/connection.html



# Psycopg commits the transaction if no exception occurs within the with block,
# and otherwise it rolls back the transaction.
# with psycopg2.connect(dsn) as conn:
#     with conn.cursor() as cur:
#         cur.execute(sql)


