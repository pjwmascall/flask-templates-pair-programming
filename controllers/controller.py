from flask import render_template, request
from app import app
from models.events_list import events
from models.events import Event

@app.route('/')
def index():
    return render_template('index.html')