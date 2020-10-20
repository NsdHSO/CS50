
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/<string:name>')
def name(name):
    
    return render_template('name.html' , sami = name)
