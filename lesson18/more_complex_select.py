import psycopg2

from lesson18.config import get_config


def demo_query():
    # read connection parameters
    params = get_config()

    with psycopg2.connect(**params) as conn:

        # create a cursor
        cur = conn.cursor()

        query = """
        select
            c.name as customer_name,
            a.id as account_id,
            a.balance
        from 
            accounts a
        join account_owners ao on
            a.id = ao.account_id
        join customers c on
            c.id = ao.customer_id;
        """

        # execute a statement
        cur.execute(query)
        result = cur.fetchall()
        return result


if __name__ == '__main__':
    res = demo_query()
    print(res)