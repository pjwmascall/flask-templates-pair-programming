from flask import render_template, request
from app import app
from models.events_list import events
from models.events import Event

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/', methods=['POST'])
def add_event():
    date = form.request[date]
    name = form.request[name]
    number_of_guests = form.requests[number_of_guests]
    room_location = form.requests[room_location]
    description = form.requests[description]
    new_event = Event(date, name, number_of_guests, room_location, description)
    add_new_event(new_event)
    return render_template('index.html', events=events)