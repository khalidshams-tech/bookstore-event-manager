"""Console event manager for a small bookstore.

The core functions are written separately from the menu so they can be tested
and reused later in a web version.
"""


def add_event(events, event_id, name, event_type, date, time):
    if find_event(events, event_id):
        raise ValueError("Event ID already exists.")

    event = {
        "id": str(event_id),
        "name": name.strip(),
        "type": event_type.strip(),
        "date": date.strip(),
        "time": time.strip(),
        "attendees": [],
    }

    if not all([event["id"], event["name"], event["type"], event["date"], event["time"]]):
        raise ValueError("All event fields are required.")

    events.append(event)
    return event


def find_event(events, event_id):
    event_id = str(event_id)
    for event in events:
        if event["id"] == event_id:
            return event
    return None


def update_event(events, event_id, **updates):
    event = find_event(events, event_id)
    if not event:
        raise ValueError("Event not found.")

    for key in ("name", "type", "date", "time"):
        if key in updates and updates[key]:
            event[key] = str(updates[key]).strip()

    return event


def delete_event(events, event_id):
    event = find_event(events, event_id)
    if not event:
        raise ValueError("Event not found.")

    events.remove(event)
    return event


def add_attendee(events, event_id, attendee_name):
    event = find_event(events, event_id)
    if not event:
        raise ValueError("Event not found.")

    attendee_name = attendee_name.strip()
    if not attendee_name:
        raise ValueError("Attendee name is required.")

    event["attendees"].append(attendee_name)
    return event


def display_event(event):
    attendees = ", ".join(event["attendees"]) if event["attendees"] else "No attendees yet"
    return (
        f"ID: {event['id']}\n"
        f"Name: {event['name']}\n"
        f"Type: {event['type']}\n"
        f"Date: {event['date']}\n"
        f"Time: {event['time']}\n"
        f"Attendees: {attendees}"
    )


def prompt_for_event():
    return {
        "event_id": input("Event ID: "),
        "name": input("Event name: "),
        "event_type": input("Event type: "),
        "date": input("Date: "),
        "time": input("Time: "),
    }


def main():
    events = []

    while True:
        print("\nSofia's Bookstore Event Manager")
        print("1. Add event")
        print("2. View events")
        print("3. Update event")
        print("4. Delete event")
        print("5. Add attendee")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                data = prompt_for_event()
                add_event(events, **data)
                print("Event added.")
            elif choice == "2":
                if not events:
                    print("No events found.")
                for event in events:
                    print("\n" + display_event(event))
            elif choice == "3":
                event_id = input("Event ID to update: ")
                update_event(
                    events,
                    event_id,
                    name=input("New name (blank to keep): "),
                    event_type=input("New type (blank to keep): "),
                    date=input("New date (blank to keep): "),
                    time=input("New time (blank to keep): "),
                )
                print("Event updated.")
            elif choice == "4":
                delete_event(events, input("Event ID to delete: "))
                print("Event deleted.")
            elif choice == "5":
                add_attendee(events, input("Event ID: "), input("Attendee name: "))
                print("Attendee added.")
            elif choice == "6":
                print("Goodbye.")
                break
            else:
                print("Invalid option.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
