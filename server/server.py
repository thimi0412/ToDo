# coding: UTF-8

from flask import Flask, make_response
import json
import db_conect

api = Flask(__name__)

@api.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@api.route('/', methods=['GET'])
def get_user():
    row = db_conect.get_task()
    res_json = {
        'title' : row[2],
        'details': row[3],
        'limit': str(row[4]),
        'insert': str(row[5]),
    }
    return make_response(json.dumps(res_json, ensure_ascii=False))



if __name__ == '__main__':
    api.run(host='localhost', port=8080)
