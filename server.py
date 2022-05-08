from flask import Flask
import numpy as np
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('arduinoData.csv')
print('Starting flask server')

@app.route('/')
def send():
    return df.to_html()

asdflkj;jadfs
