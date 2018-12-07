import pickle
import flask
from flask import Flask, request, redirect, render_template

app = flask.Flask(__name__)

#getting our trained model from a file we created earlier
model = pickle.load(open("model.pkl","r"))

@app.route('/result', methods=['GET'])
def result():
    #grabbing a set of wine features from the request's body
    foo = request.args.getlist('foo')
    
    #our model rates the wine based on the input array
    prediction = model.predict([foo])
    
    #sending our response object back as json
    return render_template('result.html', prediction=prediction)

@app.route('/')
def index():
		return render_template('index.html')

@app.route('/panel')
def panel():
		return render_template('manage-resumes.html')

@app.route('/insert')
def insert():
		return render_template('insert.html')