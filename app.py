#!/bin/env python
# coding: utf-8
import os, psycopg2
from flask import Flask, render_template, request
from psycopg2.extras import DictCursor

app = Flask(__name__)
app.debug = True

#*************************************
# ルート
#*************************************
@app.route('/')
def top():
    return u'テスト'

#*************************************
# 初期表示
#*************************************
@app.route('/top/<name>')
def index(name=''):
    return render_template('index.html', name=name)

#*************************************
# 一覧検索
#*************************************
@app.route('/tododata', methods=['GET'])
def search_tododata_all():

    sql = "SELECT * FROM public.tododata"
    resultData = selectData(sql)

    return render_template('index.html', resultData=resultData)

#*************************************
# 未完了検索
#*************************************
@app.route('/tododata/incomp', methods=['GET'])
def search_tododata_incomp():

    sql = """SELECT * FROM public.tododata WHERE "Status" = '0'"""
    resultData = selectData(sql)

    return render_template('index.html', resultData=resultData)

#*************************************
# 登録
#*************************************
@app.route('/tododata', methods=['POST'])
def regist_tododata():

    content = request.form.getlist('content')
    priority = request.form.getlist('priority')

    resultData = ""
    if len(content) > 0 and len(priority) > 0:
        sql = ""
        resultData = registData(sql)

    return render_template('index.html', resultData=resultData)

#******************************
# データ取得
#******************************
def selectData(sql):

    db = psycopg2.connect(setDbCfg())

    #実行結果を辞書形式で取得する
    cur = db.cursor(cursor_factory=DictCursor)
    cur.execute(sql)

    resultData = cur.fetchall()

    cur.close()
    db.close()

    return resultData

#******************************
# データ登録
#******************************
def registData(sql):

    #TODO 登録処理検討中

    db = psycopg2.connect(setDbCfg())

    #実行結果を辞書形式で取得する
    cur = db.cursor(cursor_factory=DictCursor)
    cur.execute(sql)

    resultData = cur.fetchall()

    cur.close()
    db.close()

    return resultData

#**************************************************
# DB接続設定
#**************************************************
def setDbCfg():

    #ローカル用
    return setDbCfgLocal()

    #Heroku用
    #return setDbCfgHeroku()

#**********************
# DB接続設定(ローカル)
#**********************
def setDbCfgLocal():

    dbnameStr = 'postgres'
    hostStr = 'localhost'
    userStr = 'postgres'
    passwordStr = 'hiropost'

    dbStr = 'dbname={0} host={1} user={2} password={3}'.format(dbnameStr, hostStr, userStr, passwordStr)
    return dbStr

#**********************
# DB接続設定(Heroku)
#**********************
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
