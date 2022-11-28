#app.py file for Flask app
from flask import Flask
from flask import render_template

# Create the app
app = Flask(__name__)

# Create a homepage for the app
@app.route("/")

# When we go to our.URL.com/
    # Then flask will run this function below
def helloWorld():
    return render_template('hello.html')
    #"<h1>This is our Flask app!</h1>"

@app.route("/hi/<name>")
def showUser(name):
    information = {'name': 'kimmy', 'job': 'student'}
    return render_template('hello.html', myVar=name)
    

@app.route("/test/<name>")
def test(name):
    return render_template('test.html', result=name)
    #"<h1>This is a test!</h1> <p>This is some text.</p>" 
