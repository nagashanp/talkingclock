from clockinfo import translate
from datetime import datetime
import unittest


class TestOutput(unittest.TestCase):

    def test_one_oclock1(self):
        self.assertEqual(translate("01:00"), "one  o'clock")

    def test_one_oclock2(self):
        self.assertEqual(translate("13:00"), "one  o'clock")

    def test_minute_past(self):
        self.assertEqual(translate("13:05"), "five past  one")

    def test_half_past(self):
        self.assertEqual(translate("13:30"), "half past one")

    def test_minute_to(self):
        self.assertEqual(translate("13:35"), "twenty five to  two")

    def test_now(self):
        now = datetime.now()
        translate(now.strftime("%H:%M"))

if __name__ == '__main__':
    unittest.main()
