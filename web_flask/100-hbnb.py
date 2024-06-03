#!/usr/bin/python3
"""A Flask web application that lists all State objects."""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route handler for /hbnb URL."""
    states = sorted(storage.all('State').values(), key=lambda x: x.name)
    amenities = sorted(storage.all('Amenity').values(), key=lambda x: x.name)
    places = sorted(storage.all('Place').values(), key=lambda x: x.name)
    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown of the app context."""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
