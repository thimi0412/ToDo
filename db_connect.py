import mysql.connector


def connect():
    '''
    MySQLに接続する
    @return conn, cur
    '''
    conn = mysql.connector.connect(user='root',
                                    password='Skou_0412',
                                    host='127.0.0.1',
                                    database='todo')

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
        alter table todo.task drop column id;
        '''
    cur.execute(sql)
    conn.commit()

    disconecrt(conn, cur)


def fix_auto_increment_add(conn, cur):
    '''
    連番振り直し(追加)
    '''
    sql = '''
    alter table todo.task add id int(11) primary key not null auto_increment first;
    '''
    cur.execute(sql)
    conn.commit()

    disconecrt(conn, cur)


def get_task():
    '''
    タスクを全て取得
    '''
    conn, cur = connect()

    sql = '''
        SELECT * FROM todo.task
    '''

    cur.execute(sql)
    row = cur.fetchall()

    disconecrt(conn, cur)
    return row


def get_task_btw(span):
    '''
    指定期間内のタスクを表示
    '''
    conn, cur = connect()
    if span == 'today':
        span = 'DAY'
    elif span == 'week':
        span = 'WEEK'
    elif span == 'month':
        span = 'MONTH'

    sql = '''
        SELECT * FROM todo.task
        WHERE task_limit between CURRENT_TIMESTAMP and CURRENT_TIMESTAMP + interval 1 {between};
    '''.format(between=span)
    cur.execute(sql)
    row = cur.fetchall()

    disconecrt(conn, cur)
    return row


def get_task_order(order, item):
    '''
    タスクの並び替え
    '''
    conn, cur = connect()

    sql = '''
        SELECT * FROM todo.task ORDER BY {item} {order}
    '''.format(item=item, order=order)
    cur.execute(sql)
    row = cur.fetchall()

    disconecrt(conn, cur)
    return row


def insert_task(Task):
    '''
    入力処理
    '''
    conn, cur = connect()
    sql = '''
        INSERT INTO todo.task(user_name, task_title, task_details, task_limit, insert_date)
        VALUES('{user_name}', '{title}', '{details}', '{limit}', now())
    '''.format(user_name=Task.user_name, title=Task.title, details=Task.details, limit=Task.limit)
    cur.execute(sql)
    conn.commit()

    disconecrt(conn, cur)
    return 'succcess'


def update_task(Task, index):
    '''
    更新処理
    '''
    conn, cur = connect()
    sql = '''
        UPDATE todo.task SET task_title = '{title}', task_details = '{details}', task_limit = '{limit}', update_date = now()
        WHERE id = {id}
    '''.format(title=Task.title, details=Task.details, limit=Task.limit, id=index)
    cur.execute(sql)
    conn.commit()
    disconecrt(conn, cur)

    return 'succcess'


def delete_task(index):
    '''
    削除処理
    '''
    conn, cur = connect()
    sql = '''
        DELETE FROM todo.task WHERE id = {id}
    '''.format(id=index)
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
