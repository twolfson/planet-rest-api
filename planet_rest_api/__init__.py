# Load in our dependencies
from flask import Flask

# Define our application
app = Flask(__name__)

# Bind our routes
@app.route('/')
def root():
    return 'OK'
