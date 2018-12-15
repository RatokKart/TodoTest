#!/bin/env python
# coding: utf-8
import os, pymysql
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True


@app.route('/')
def top():
    return u'テスト'

#初期表示
@app.route('/top/<name>')
def index(name=''):
    return render_template('index.html', name=name)

#検索
@app.route('/search', methods=['GET','POST'])
#@app.route('/search')
def search():

    #GET、POST判定
    if request.method == 'GET':
        res = request.args.get('get_value')
    elif request.method == 'POST':
        res = request.form['post_value']

    #データ取得
    resultData = selectData(res)

    return render_template('index.html', resultData=resultData)

#******************************
#データ取得
#******************************
def selectData(res):

    db = pymysql.connect(
            host='localhost',
            user='root',
            password='password',
            db='world',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    cur = db.cursor()

    sql = 'SELECT * FROM world.country WHERE world.country.Name LIKE %s'
    para = ('%' + res + '%',)

    cur.execute(sql, para)

    resultData = cur.fetchall()

    cur.close()
    db.close()

    return resultData

#********************************
#おまじない（最下部に書くこと）
#********************************
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
