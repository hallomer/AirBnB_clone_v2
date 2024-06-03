#!/usr/bin/python3
"""A Flask web application that lists all State objects."""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Route handler for /cities_by_states URL."""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown of the app context."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
