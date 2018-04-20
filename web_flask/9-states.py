#!/usr/bin/python3
'''Start a flask web application
'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/states_list')
def states_list():
    '''Render states list'''
    # Get list of states
    states = []
    data = storage.all(State)
    for key, obj in data.items():
        states.append(obj)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_state():
    '''Render cities by state list'''
    # Get list of states
    states = []
    data = storage.all(State)
    for key, obj in data.items():
        states.append(obj)

    # Get list of cities
    cities = []
    data = storage.all(City)
    for key, obj in data.items():
        cities.append(obj)

    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)


@app.route('/states')
@app.route('/states/<id>')
def filter_state(id=''):
    '''Render a filtered cities by state list'''
    # Get list of states
    states = []
    data1 = storage.all(State)
    for key, obj in data1.items():
        states.append(obj)
    if id:
        key = 'State.' + id
        if key not in data1:
            states = ''

    # Get list of cities
    cities = []
    data2 = storage.all(City)
    for key, obj in data2.items():
        cities.append(obj)

    return render_template('9-states.html', id=id, states=states,
                           cities=cities)


@app.teardown_appcontext
def close_db(error):
    '''Close db session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
