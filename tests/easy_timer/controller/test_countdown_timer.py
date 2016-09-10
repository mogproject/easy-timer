from __future__ import division, print_function, absolute_import, unicode_literals

from mog_commons.unittest import TestCase
from easy_timer.setting.setting import Setting
from easy_timer.controller.countdown_timer import CountdownTimer


class TestCountdownTimer(TestCase):
    def test_is_time_to_say(self):
        s = Setting(say_enabled=True)
        t = CountdownTimer(s)

        self.assertTrue(t._is_time_to_say(0))
        self.assertTrue(t._is_time_to_say(1))
        self.assertTrue(t._is_time_to_say(2))
        self.assertTrue(t._is_time_to_say(3))
        self.assertTrue(t._is_time_to_say(4))
        self.assertTrue(t._is_time_to_say(5))
        self.assertTrue(t._is_time_to_say(6))
        self.assertTrue(t._is_time_to_say(7))
        self.assertTrue(t._is_time_to_say(8))
        self.assertTrue(t._is_time_to_say(9))
        self.assertTrue(t._is_time_to_say(10))
        self.assertFalse(t._is_time_to_say(11))
        self.assertFalse(t._is_time_to_say(12))
        self.assertFalse(t._is_time_to_say(59))
        self.assertTrue(t._is_time_to_say(60))
        self.assertFalse(t._is_time_to_say(61))
        self.assertFalse(t._is_time_to_say(119))
        self.assertFalse(t._is_time_to_say(120))
        self.assertFalse(t._is_time_to_say(121))
        self.assertFalse(t._is_time_to_say(299))
        self.assertTrue(t._is_time_to_say(300))
        self.assertFalse(t._is_time_to_say(301))
        self.assertFalse(t._is_time_to_say(599))
        self.assertTrue(t._is_time_to_say(600))
        self.assertFalse(t._is_time_to_say(601))
        self.assertFalse(t._is_time_to_say(1199))
        self.assertTrue(t._is_time_to_say(1200))
        self.assertFalse(t._is_time_to_say(1201))
        self.assertFalse(t._is_time_to_say(1799))
        self.assertTrue(t._is_time_to_say(1800))
        self.assertFalse(t._is_time_to_say(1801))
        self.assertFalse(t._is_time_to_say(1799))
        self.assertTrue(t._is_time_to_say(1800))
        self.assertFalse(t._is_time_to_say(1801))
        self.assertFalse(t._is_time_to_say(599399))
        self.assertTrue(t._is_time_to_say(599400))
        self.assertFalse(t._is_time_to_say(599401))

        s2 = Setting()  # say_enabled=False
        t2 = CountdownTimer(s2)
        self.assertFalse(t2._is_time_to_say(0))
        self.assertFalse(t2._is_time_to_say(1))
        self.assertFalse(t2._is_time_to_say(2))
