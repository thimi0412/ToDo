import mysql.connector

def conect():
    conn = mysql.connector.connect(user='root',
                                   password='',
                                  host='localhost',
                                  database='test')

    cur = conn.cursor(buffered=True)
    return conn, cur

def disconecrt(conn, cur):
    cur.close()
    conn.close()


def get_task():
    conn, cur = conect()

    sql = "select * from test.todo"

    cur.execute(sql)
    row = cur.fetchall()

    disconecrt(conn, cur)
    return row

def insert_task(Task):
    conn, cur = conect()
    sql = '''
        INSERT INTO test.todo(user_name, task_title, task_details, task_limit, insert_date, is_complete, del_flg)
        VALUES('{user_name}', '{title}', '{details}', Date('{limit}'), now(), '0', '0')
    '''.format(user_name=Task.user_name, title=Task.title, details=Task.details, limit=Task.limit)
    cur.execute(sql)
    conn.commit()

    disconecrt(conn, cur)
    return 'succcess'

def main():
    row = get_task()
    result = []
    for i in row:
        json = {
            'title' : i[2],
            'details': i[3],
            'limit': str(i[4]),
            'insert': str(i[5]),
        }
        result.append(json)
    res_json = {'result': result}
    print(res_json)



if __name__ == '__main__':
    main()