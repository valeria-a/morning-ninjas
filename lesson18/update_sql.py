#!/usr/bin/python

import psycopg2

from lesson18.config import get_config


def insert_customer(passport_num, name, address):
    """ update vendor name based on the vendor id """
    sql = """ INSERT INTO customers
                (passport_num, name, address)
                VALUES
                (%s, %s, %s)"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = get_config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (passport_num, name, address))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    # Insert customer
    insert_customer(12121212, 'Stieven Spielberg', 'California')