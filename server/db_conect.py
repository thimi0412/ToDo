import mysql.connector

def conect():
    '''
    MySQLに接続する
    @return conn, cur
    '''
    conn = mysql.connector.connect(user='root',
                                   password='',
                                  host='localhost',
                                  database='test')

    cur = conn.cursor(buffered=True)
    return conn, cur

def disconecrt(conn, cur):
    '''
    MySQLの接続を切断
    @param conn, cur
    '''
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
        VALUES('{user_name}', '{title}', '{details}', '{limit}', now(), '0', '0')
    '''.format(user_name=Task.user_name, title=Task.title, details=Task.details, limit=Task.limit)
    cur.execute(sql)
    conn.commit()

    disconecrt(conn, cur)
    return 'succcess'


def update_task(Task, index):
    conn, cur = conect()
    sql = '''
        UPDATE test.todo SET task_title = '{title}', task_details = '{details}', task_limit = Date('{limit}'), update_date = now()
        WHERE id = {id}
    '''.format(title=Task.title, details=Task.details, limit=Task.limit, id=index+1)
    cur.execute(sql)
    conn.commit()
    disconecrt(conn, cur)

    return 'succcess'


def main():
    pass



if __name__ == '__main__':
    main()