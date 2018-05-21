# coding: UTF-8

from flask import Flask, make_response, request, render_template
import json
import db_connect
import Task

api = Flask(__name__)

month_dict = {'jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
            'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}


def format_date(str_date):
    '''
    jsの日付をmysqlに入れる用の形式にする

    @param　str_date :js日付文字列

    @return result : mysqlに入れるようの文字列
    '''
    date = str_date.split()

    result = '''
        {year}-{month}-{date} {time}
        '''.format(
            year=date[3],
            month=month_dict[date[1]],
            date=date[2],
            time=date[4])

    return result


def format_date_T(str_date):
    '''
    jsの日付をmysqlに入れる用の形式にする(T付き)

    @param　str_date :js日付文字列

    @return result : mysqlに入れるようの文字列
    '''
    date = str_date.split('T')

    return date[0] + ' ' + date[1]


@api.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                        'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                        'GET,PUT,POST,DELETE,OPTIONS')

    return response


@api.route('/')
def index():
    return render_template('index.html')


@api.route('/get', methods=['GET'])
def get_user():
    '''
    タスク全取得
    '''
    row = db_connect.get_task()
    print('xxxxxxxxxxxxxxxxxxxxxxxxx')
    result = []
    for i in row:
        res_json = {
            'id': int(i[0]),
            'title': i[2],
            'details': i[3],
            'limit': str(i[4]),
            'insert': str(i[5]),
        }
        result.append(res_json)

    res_json = {'result': result}

    return make_response(json.dumps(res_json, ensure_ascii=False))


@api.route('/filter', methods=['POST'])
def get_filter_task():
    span = request.form['span']
    '''
    フィルターをかけたタスクを表示
    '''
    row = db_connect.get_task_btw(span)

    result = []
    for i in row:
        res_json = {
            'id': int(i[0]),
            'title': i[2],
            'details': i[3],
            'limit': str(i[4]),
            'insert': str(i[5]),
        }
        result.append(res_json)

    res_json = {'result': result}

    return make_response(json.dumps(res_json, ensure_ascii=False))


@api.route('/order', methods=['POST'])
def get_task_order():
    '''
    並び替えたをかけたタスクを表示
    '''
    item = request.form['item']
    order = request.form['order']

    row = db_connect.get_task_order(order, item)

    result = []
    for i in row:
        res_json = {
            'id': int(i[0]),
            'title': i[2],
            'details': i[3],
            'limit': str(i[4]),
            'insert': str(i[5]),
        }
        result.append(res_json)

    res_json = {'result': result}

    return make_response(json.dumps(res_json, ensure_ascii=False))


@api.route('/set', methods=['POST'])
def set_task():
    '''
    入力処理
    '''
    title = request.form['title']
    details = request.form['details']
    limit = format_date(request.form['limit'])
    insert = format_date(request.form['insert'])

    task = Task.Task(title, details, limit, insert)
    res = db_connect.insert_task(task)

    return make_response(json.dumps({'status': res}, ensure_ascii=False))


@api.route('/update', methods=['POST'])
def update_task():
    '''
    更新処理
    '''
    title = request.form['title']
    details = request.form['details']
    limit = format_date_T(request.form['limit'])
    insert = format_date(request.form['insert'])
    index = int(request.form['index'])

    task = Task.Task(title, details, limit, insert)
    res = db_connect.update_task(task, index)

    return make_response(json.dumps({'status': res}, ensure_ascii=False))


@api.route('/delete', methods=['POST'])
def delete_task():
    '''
    削除処理
    '''
    index = int(request.form['index'])
    res = db_connect.delete_task(index)

    return make_response(json.dumps({'status': res}, ensure_ascii=False))


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8080)
