#!/bin/env python
# coding: utf-8

import os
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

    if request.method == 'GET':
        res = request.args.get('get_value')
    elif request.method == 'POST':
        res = request.form['post_value']

    dd = res



    return render_template('index.html')


#おまじない（最下部に書くこと）
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
