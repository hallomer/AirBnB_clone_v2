#!/usr/bin/python3
"""A Flask web application that lists all State objects."""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Route handler for /states_list URL."""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown of the app context."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
