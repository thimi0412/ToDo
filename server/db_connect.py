import mysql.connector


def connect():
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


def fix_auto_increment_del(conn, cur):
    '''
    連番振り直し(削除)
    '''
    sql = '''
        alter table test.todo drop column id;
        '''
    cur.execute(sql)
    conn.commit()

    disconecrt(conn, cur)


def fix_auto_increment_add(conn, cur):
    '''
    連番振り直し(追加)
    '''
    sql = '''
    alter table test.todo add id int(11) primary key not null auto_increment first;
    '''
    cur.execute(sql)
    conn.commit()

    disconecrt(conn, cur)


def get_task():
    conn, cur = connect()

    sql = '''
        SELECT * FROM test.todo
    '''

    cur.execute(sql)
    row = cur.fetchall()

    disconecrt(conn, cur)
    return row


def get_task_btw(span):
    conn, cur = connect()
    if span == 'today':
        span = 'DAY'
    elif span == 'week':
        span = 'WEEK'
    elif span == 'month':
        span = 'MONTH'

    sql = '''
        SELECT * FROM test.todo
        WHERE task_limit between CURRENT_TIMESTAMP and CURRENT_TIMESTAMP + interval 1 {between};
    '''.format(between=span)
    cur.execute(sql)
    row = cur.fetchall()

    disconecrt(conn, cur)
    return row


def get_task_order(order, item):
    conn, cur = connect()

    sql = '''
        SELECT * FROM test.todo ORDER BY {item} {order}
    '''.format(item=item, order=order)
    cur.execute(sql)
    row = cur.fetchall()

    disconecrt(conn, cur)
    return row


def insert_task(Task):
    conn, cur = connect()
    sql = '''
        INSERT INTO test.todo(user_name, task_title, task_details, task_limit, insert_date, is_complete, del_flg)
        VALUES('{user_name}', '{title}', '{details}', '{limit}', now(), '0', '0')
    '''.format(user_name=Task.user_name, title=Task.title, details=Task.details, limit=Task.limit)
    cur.execute(sql)
    conn.commit()

    disconecrt(conn, cur)
    return 'succcess'


def update_task(Task, index):
    conn, cur = connect()
    sql = '''
        UPDATE test.todo SET task_title = '{title}', task_details = '{details}', task_limit = '{limit}', update_date = now()
        WHERE id = {id}
    '''.format(title=Task.title, details=Task.details, limit=Task.limit, id=index+1)
    cur.execute(sql)
    conn.commit()
    disconecrt(conn, cur)

    return 'succcess'


def delete_task(index):
    conn, cur = connect()
    sql = '''
        DELETE FROM test.todo WHERE id = {id}
    '''.format(id=index+1)
    cur.execute(sql)
    conn.commit()

    disconecrt(conn, cur)

    conn, cur = connect()
    fix_auto_increment_del(conn, cur)
    conn, cur = connect()
    fix_auto_increment_add(conn, cur)

    return 'succcess'


def main():
    pass


if __name__ == '__main__':
    main()
