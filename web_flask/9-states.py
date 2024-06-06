#!/usr/bin/python3
"""A Flask web application that lists all State objects."""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Route handler for /states URL."""
    states = storage.all("State").values()
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Route handler for /states/<id> URL."""
    state = None
    states = storage.all("State").values()
    for s in states:
        if s.id == id:
            state = s
            break
    if state is None:
        return render_template("9-states.html", state=None)
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown of the app context."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
