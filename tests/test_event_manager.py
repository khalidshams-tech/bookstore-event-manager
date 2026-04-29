import unittest

from event_manager import add_attendee, add_event, delete_event, find_event, update_event


class EventManagerTests(unittest.TestCase):
    def test_add_event_creates_event_record(self):
        events = []

        event = add_event(events, "101", "Author Signing", "Signing", "2026-03-10", "15:00")

        self.assertEqual(event["name"], "Author Signing")
        self.assertEqual(events[0]["id"], "101")

    def test_duplicate_event_id_is_rejected(self):
        events = []
        add_event(events, "101", "Author Signing", "Signing", "2026-03-10", "15:00")

        with self.assertRaises(ValueError):
            add_event(events, "101", "Book Club", "Club", "2026-03-11", "18:00")

    def test_update_and_add_attendee(self):
        events = []
        add_event(events, "101", "Author Signing", "Signing", "2026-03-10", "15:00")

        update_event(events, "101", name="Community Book Night")
        add_attendee(events, "101", "Sofia")

        event = find_event(events, "101")
        self.assertEqual(event["name"], "Community Book Night")
        self.assertEqual(event["attendees"], ["Sofia"])

    def test_delete_event_removes_record(self):
        events = []
        add_event(events, "101", "Author Signing", "Signing", "2026-03-10", "15:00")

        delete_event(events, "101")

        self.assertEqual(events, [])


if __name__ == "__main__":
    unittest.main()
