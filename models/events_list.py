from models.events import Event

event1 = Event('2022-01-15', 'CodeFest', "16", 'Conference Room B', 'Hackathon', "on")
event2 = Event('2022-01-16', 'CodeFest Afterparty', "20", 'Conference Room B', 'Party', "off")

events = [event1, event2]

def add_new_event(event):
    events.append(event)

def delete_event_from_events(name):
    for event in events:
        if event.name == name:
            events.remove(event)