from flask import Flask
import numpy as np
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('dummy.csv')
print('Starting flask server')
print(df.iloc[:,2]) #for all rows, the second column

@app.route('/')
def hello_world():
    print('Sending Hello World')
    return 'Hello World!'

@app.route('/<name>')
def hello_name(name):
    print('Sending Hello', name)
    return 'Hello {}!'.format(name)

@app.route('/light')
def sensSend():
    print('Sending special message')
    out = (df.iloc[:,2].values)
    print(out)
    return out

# @app.route('/temp')
# def sensSend():
#     print

#@app.route('/')

# print('Hello World')


