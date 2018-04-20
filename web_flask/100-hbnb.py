#!/usr/bin/python3
'''Start a flask web application
'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

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

# Get list of amenities
amenities = []
data = storage.all(Amenity)
for key, obj in data.items():
    amenities.append(obj)

# Get list of places
places = []
data = storage.all(Place)
for key, obj in data.items():
    places.append(obj)


@app.route('/hbnb')
def hbnb():
    '''Render a hbnb page with filter'''
    return render_template('100-hbnb.html', states=states, places=places,
                           cities=cities, amenities=amenities)


@app.teardown_appcontext
def close_db(error):
    '''Close db session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
