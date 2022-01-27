from flask import render_template, request
from app import app
from models.events_list import events, add_new_event, delete_event_from_events
from models.events import Event

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/', methods=['POST'])
def add_event():
    date = request.form["date"]
    name = request.form["name"]
    number_of_guests = request.form["number_of_guests"]
    room_location = request.form["room_location"]
    description = request.form["description"]
    recurring = request.form["recurring"]
    new_event = Event(date, name, number_of_guests, room_location, description, recurring)
    add_new_event(new_event)
    return render_template('index.html', events=events)

@app.route('/<name>', methods=['POST'])
def delete_event(name):
    delete_event_from_events(name)
    return render_template('index.html', events=events)