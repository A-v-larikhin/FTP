import psycopg2

def connect_to_db():
    con = psycopg2.connect(
        database='testdb',
        user='testuser',
        password='123456',
        host='192.168.10.61'
    )
    return con
# ID CHAR(50),
# PURCHASENUMBER CHAR(50),
# HREF TEXT,
# MAXPRICE

#con = connect_to_db()

def db_insert(con, not_id, not_purch_num, not_href, not_price):
    cur = con.cursor()
    insert_in = f"INSERT INTO TESTSCHEME01 (id, purchasenumber, href, maxprice) VALUES (%(a)s, %(b)s, %(c)s, %(d)s);"
    cur.execute(insert_in, {'a' : not_id, 'b' : not_purch_num, 'c' : str(not_href), 'd' : not_price})
    con.commit()