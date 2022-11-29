#app.py file for Flask app
from flask import Flask
from flask import render_template

# Create the app
app = Flask(__name__)

# Create a homepage for the app
@app.route("/")

# When we go to our.URL.com/
    # Then flask will run this function below
def homepage():
    return render_template('base.html')
    
