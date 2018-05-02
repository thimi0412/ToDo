# coding: UTF-8

from flask import Flask, make_response, request
import json
import db_conect
import Task

api = Flask(__name__)

def format_date(str_date):
    month_dict = {'jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6,
                    'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
    date = str_date.split()

    result = '{year}-{month}-{date} {time}'.format(
                year=date[3], month=month_dict[date[1]], date=date[2], time=date[4])

    return result


@api.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@api.route('/get', methods=['GET'])
def get_user():
    row = db_conect.get_task()

    result = []
    for i in row:
        res_json = {
            'title' : i[2],
            'details': i[3],
            'limit': str(i[4]),
            'insert': str(i[5]),
        }
        result.append(res_json)

    res_json = {'result': result}

    return make_response(json.dumps(res_json, ensure_ascii=False))

@api.route('/set', methods=['POST'])
def set_task():
    title = request.form['title']
    details = request.form['details']
    limit = format_date(request.form['limit'])
    insert = format_date(request.form['insert'])

    task = Task.Task(title, details, limit, insert)
    res = db_conect.insert_task(task)

    return make_response(json.dumps({'status': res}, ensure_ascii=False))


@api.route('/update', methods=['POST'])
def update_task():
    title = request.form['title']
    details = request.form['details']
    limit = format_date(request.form['limit'])
    insert = format_date(request.form['insert'])
    index = request.form['index']

    task = Task.Task(title, details, limit, insert)
    res = db_conect.update_task(task, index)

    return make_response(json.dumps({'status': res}, ensure_ascii=False))

if __name__ == '__main__':
    api.run(host='localhost', port=8080)
