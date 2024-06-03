#!/usr/bin/python3
"""A Flask web application that lists all State objects."""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Route handler for /hbnb_filters URL."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown of the app context."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
