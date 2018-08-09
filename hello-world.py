from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    #os.system('flask-experiments/eseguimi.sh')
    return 'Hello, World!'