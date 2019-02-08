#!/bin/env python
# coding: utf-8
import os, psycopg2
from flask import Flask, render_template, request
from psycopg2.extras import DictCursor

app = Flask(__name__)
app.debug = True

#*************************************
#ルート
#*************************************
@app.route('/')
def top():
    return u'テスト'

#*************************************
#初期表示
#*************************************
@app.route('/top/<name>')
def index(name=''):
    return render_template('index.html', name=name)

#*************************************
#検索
#*************************************
@app.route('/search', methods=['GET','POST'])
#@app.route('/search')
def search():

    #GET、POST判定
    if request.method == 'GET':
        res = request.args.get('get_value')
    elif request.method == 'POST':
        res = request.form['post_value']

    resultData = ""

    if len(res) > 0:
        #データ取得
        resultData = selectData(res)

    return render_template('index.html', resultData=resultData)

#******************************
#データ取得
#******************************
def selectData(res):

    db = psycopg2.connect(setDbCfg())

    #実行結果を辞書形式で取得する
    cur = db.cursor(cursor_factory=DictCursor)

    sql = 'SELECT * FROM public.sample'
    #sql = 'SELECT * FROM world.country WHERE world.country.Name LIKE %s'
    para = ('%' + res + '%',)

    cur.execute(sql, para)

    resultData = cur.fetchall()

    cur.close()
    db.close()

    return resultData

#**************************************************
#DB接続設定(TODO コンフィグで切替するまでの仮対応)
#**************************************************
def setDbCfg():

    #ローカル用
    #return setDbCfgLocal()

    #Heroku用
    return setDbCfgHeroku()


def setDbCfgLocal():

    dbnameStr = 'postgres'
    hostStr = 'localhost'
    userStr = 'postgres'
    passwordStr = 'hiropost'

    dbStr = 'dbname={0} host={1} user={2} password={3}'.format(dbnameStr, hostStr, userStr, passwordStr)
    return dbStr


def setDbCfgHeroku():

    dbnameStr = 'dbrt0fsq9u00rg'
    hostStr = 'ec2-184-72-239-186.compute-1.amazonaws.com'
    userStr = 'gsrcnbjllcvskz'
    passwordStr = '9c3d8452aef3e916739e506f90c46b51e2e79a9a2728b04b81bd0f6aef4d15fa'

    dbStr = 'dbname={0} host={1} user={2} password={3}'.format(dbnameStr, hostStr, userStr, passwordStr)
    return dbStr

#********************************
#おまじない（最下部に書くこと）
#********************************
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
