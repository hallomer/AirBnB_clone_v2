#!/usr/bin/python3
"""A simple Flask web application with multiple routes."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Route handler for the root URL."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
     """Route handler for the /hbnb URL."""
     return "HBNB"

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
