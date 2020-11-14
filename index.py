#! /bin/python
'''Renders bar graph to web page based on Fibonacci sequence.'''
from flask import Flask
from flask import render_template
import pygal

APP = Flask(__name__)  # Flask instance

@APP.route('/')
def render_bar_chart():
    '''Renders bar graph to web page based on Fibonacci sequence.'''
    bar_chart = pygal.Bar(height=300)  # instance of Bar class
    bar_chart.title = 'Fibonacci sequence'  # title of bar chart
    bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # add fibo data to chart
    chart = bar_chart.render_data_uri()  # render bar chart
    return render_template('index.htm', chart=chart)  # render Jinja2 template

if __name__ == '__main__':
    APP.run(host='localhost', port=3000)  # if standalone
