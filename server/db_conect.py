import mysql.connector

def conect():
    conn = mysql.connector.connect(user='root',
                                   password='',
                                  host='localhost',
                                  database='test')

    cur = conn.cursor()
    return conn, cur

def disconecrt(conn, cur):
    cur.close()
    conn.close()


def get_task():

    conn, cur = conect()

    sql="select * from test.todo where id = 1"

    cur.execute(sql)
    row = cur.fetchone()

    disconecrt(conn, cur)

    

    return row

def main():
    row = get_task()
    res_json = {
        'title' : row[2],
        'details': row[3],
        'limit': row[4],
        'insert': row[5]
    }
    print(res_json)


if __name__ == '__main__':
    main()