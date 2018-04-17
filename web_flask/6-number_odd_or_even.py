#!/usr/bin/python3
'''Start a flask web application
'''
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/')
def hello_hbnb():
    '''hello hbnb'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''hbnb'''
    return 'HBNB'


@app.route('/c/<text>')
def c_is(text):
    '''c is...'''
    text = text.replace('_', ' ')
    return 'C %s' % text


@app.route('/python')
@app.route('/python/<text>')
def python(text=''):
    '''python is...'''
    if text:
        text = text.replace('_', ' ')
    else:
        text = 'is cool'
    return 'Python %s' % text


@app.route('/number/<int:n>')
def number(n):
    '''Display number'''
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def number_template(n):
    '''Display number template page'''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_even(n):
    '''Display odd/even number template page'''
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
