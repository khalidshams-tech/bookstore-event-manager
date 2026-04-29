# Sofia's Bookstore Event Manager

A Python console application for managing bookstore events, event details, and attendee information.

## Project Description

Sofia's Bookstore Event Manager is a menu-driven Python program designed to replace manual event tracking with a simple digital system. It supports common event-management tasks such as adding events, viewing details, updating information, deleting records, and tracking attendees.

This project demonstrates Python fundamentals, CRUD logic, structured data, input validation, and clear command-line interaction.

## Technologies Used

- Python 3
- Lists and dictionaries
- Functions
- Loops and conditionals
- Exception handling
- Command-line interface

## Features

- Add new bookstore events
- View all events
- Search or review event details
- Update event name, type, date, time, or attendee information
- Delete events
- Add attendees to events
- Validate user input to reduce errors
- Store event records using dictionaries inside a list

## Event Data Structure

Each event is stored as a dictionary inside a list.

Example:

```text
ID: 101
Name: Author Signing
Type: Signing
Date: 2026-03-10
Time: 15:00
Attendees: Sofia, Alex, Jordan
```

## Project Structure

```text
Sofia-s-Bookstore-Event-Manager/
+-- event_manager.py
+-- README.md
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/khalidshams-tech/Sofia-s-Bookstore-Event-Manager.git
```

2. Open the project folder:

```bash
cd Sofia-s-Bookstore-Event-Manager
```

3. Run the program:

```bash
python event_manager.py
```

On macOS/Linux, you may need:

```bash
python3 event_manager.py
```

## Screenshots

Add screenshots here showing:

- Main menu
- Add event workflow
- View events output
- Update or delete event workflow

Example:

```markdown
![Bookstore Event Manager menu](screenshots/bookstore-menu.png)
```

## What I Learned

- How to design a menu-driven Python application
- How to use lists and dictionaries to store structured records
- How to write functions for separate tasks
- How to validate user input and handle errors
- How CRUD operations work in a simple application
- How to document a command-line project for GitHub

## Future Improvements

- Save events to a file so data remains after the program closes
- Add search by event ID, type, or date
- Add automated tests for event actions
- Add screenshots or a terminal demo
- Convert the console app into a Flask web app
- Rename the repository to a shorter name such as `bookstore-event-manager`

## Status

Active Python learning project. Good portfolio value after screenshots and persistent file storage are added.