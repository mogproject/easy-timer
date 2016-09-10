from __future__ import division, print_function, absolute_import, unicode_literals

from mog_commons.unittest import TestCase
from easy_timer.view import Speaker
from easy_timer.setting.setting import DEFAULT_SAY_COUNTDOWN_SEC, DEFAULT_SAY_PERIODIC_MIN, DEFAULT_SAY_SPECIFIC_MIN
from tests.easy_timer.view.mock_speaker import MockSpeaker


class TestSpeaker(TestCase):
    def test_is_time_to_speak(self):
        s = Speaker(True, 'say', DEFAULT_SAY_COUNTDOWN_SEC, DEFAULT_SAY_PERIODIC_MIN, DEFAULT_SAY_SPECIFIC_MIN)

        self.assertTrue(s._is_time_to_speak(0))
        self.assertTrue(s._is_time_to_speak(1))
        self.assertTrue(s._is_time_to_speak(2))
        self.assertTrue(s._is_time_to_speak(3))
        self.assertTrue(s._is_time_to_speak(4))
        self.assertTrue(s._is_time_to_speak(5))
        self.assertTrue(s._is_time_to_speak(6))
        self.assertTrue(s._is_time_to_speak(7))
        self.assertTrue(s._is_time_to_speak(8))
        self.assertTrue(s._is_time_to_speak(9))
        self.assertTrue(s._is_time_to_speak(10))
        self.assertFalse(s._is_time_to_speak(11))
        self.assertFalse(s._is_time_to_speak(12))
        self.assertFalse(s._is_time_to_speak(59))
        self.assertTrue(s._is_time_to_speak(60))
        self.assertFalse(s._is_time_to_speak(61))
        self.assertFalse(s._is_time_to_speak(119))
        self.assertFalse(s._is_time_to_speak(120))
        self.assertFalse(s._is_time_to_speak(121))
        self.assertFalse(s._is_time_to_speak(299))
        self.assertTrue(s._is_time_to_speak(300))
        self.assertFalse(s._is_time_to_speak(301))
        self.assertFalse(s._is_time_to_speak(599))
        self.assertTrue(s._is_time_to_speak(600))
        self.assertFalse(s._is_time_to_speak(601))
        self.assertFalse(s._is_time_to_speak(1199))
        self.assertTrue(s._is_time_to_speak(1200))
        self.assertFalse(s._is_time_to_speak(1201))
        self.assertFalse(s._is_time_to_speak(1799))
        self.assertTrue(s._is_time_to_speak(1800))
        self.assertFalse(s._is_time_to_speak(1801))
        self.assertFalse(s._is_time_to_speak(1799))
        self.assertTrue(s._is_time_to_speak(1800))
        self.assertFalse(s._is_time_to_speak(1801))
        self.assertFalse(s._is_time_to_speak(599399))
        self.assertTrue(s._is_time_to_speak(599400))
        self.assertFalse(s._is_time_to_speak(599401))

        s2 = Speaker(False, 'say', DEFAULT_SAY_COUNTDOWN_SEC, DEFAULT_SAY_PERIODIC_MIN, DEFAULT_SAY_SPECIFIC_MIN)

        self.assertFalse(s2._is_time_to_speak(0))
        self.assertFalse(s2._is_time_to_speak(1))
        self.assertFalse(s2._is_time_to_speak(2))

    def test_get_speak_text(self):
        s = Speaker(True, 'say', DEFAULT_SAY_COUNTDOWN_SEC, DEFAULT_SAY_PERIODIC_MIN, DEFAULT_SAY_SPECIFIC_MIN)

        self.assertEqual(s._get_speak_text(0), 'time')
        self.assertEqual(s._get_speak_text(1), '1')
        self.assertEqual(s._get_speak_text(60), '1 minute')
        self.assertEqual(s._get_speak_text(300), '5 minutes')
        self.assertEqual(s._get_speak_text(9990 * 60), '9990 minutes')

    def test_verify(self):
        s1 = MockSpeaker(True)
        self.assertTrue(s1.verify())
        self.assertEqual(s1.history, [('speak', 'say "."')])

        s2 = MockSpeaker(False)
        self.assertTrue(s2.verify())
        self.assertEqual(s2.history, [])
