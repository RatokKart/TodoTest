#!/bin/env python
# coding: utf-8

import os
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return u'テスト'

#初期表示
@app.route('/top/<name>')
def hello(name=''):
    return render_template('index.html', name=name)

#検索
@app.route('/search')
def search():
    dt = request.args.get('text', '')

    ddd = dt







#おまじない
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)