#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template, request, teardown_appcontext
from models import storage
from models.state import State
from models.city import City
import uuid

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    """List all states"""
    states = sorted(list(storage.all(State).values()), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def list_cities_by_state(id):
    """List all cities by state"""
    state = storage.get(State, id)
    if not state:
        return render_template('9-states.html', not_found=True)
    cities = sorted(state.cities, key=lambda c: c.name)
    return render_template('9-states.html', state=state, cities=cities)


@app.teardown_appcontext
def teardown_db(error):
    """Closes the storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

