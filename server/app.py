#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing Views</h1>'

@app.route('/print/<string: name>')
def print_string(name):
    return f'<h1>Your named is {name}</h1>'

@app.route('count/<integer: number>')
def count(number):
    x = range(number)
    for i in x:
        return i
    
@app.route('/math/<integer: num1, string: operation, integer: num2>')
def math(num1, operation, num2):
    sum = f'The sum is {num1} {operation} {num2}'
    return sum

if __name__ == '__main__':
    app.run(port=5555, debug=True)