#!/usr/bin/python

import pymysql

con = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='admin',
    password='password',
    db='my_database'
)

def get_all(table_name):
    try:
        cursor_type = pymysql.cursors.DictCursor
        with con.cursor(cursor=cursor_type) as cur:
            cur.execute(f"SELECT name FROM {table_name}")
            rows = cur.fetchall()
            for row in rows:
                print(f'{row[0]}')
    finally:
        con.close()
