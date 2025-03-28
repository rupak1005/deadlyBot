import unittest
from unittest.mock import patch
import main

class TestDeadlyRBot(unittest.TestCase):

    @patch("main.bot.send_message")
    def test_send_message(self, mock_send):
        mock_send.return_value = True
        result = main.send_reminder(123456, {"subject": "Math", "time": "10:00 AM", "location": "Room 101"})
        self.assertIsNone(result)  # Function should return None after sending message

    def test_load_timetable(self):
        timetable = main.load_timetable()
        self.assertIsInstance(timetable, dict)  # Should return a dictionary

if __name__ == "__main__":
    unittest.main()
