from flask import render_template, request
from app import app
from models.events_list import events, add_new_event
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
    new_event = Event(date, name, number_of_guests, room_location, description)
    add_new_event(new_event)
    return render_template('index.html', events=events)