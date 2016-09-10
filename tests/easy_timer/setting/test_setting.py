from __future__ import division, print_function, absolute_import, unicode_literals

import os
from mog_commons.unittest import TestCase
from easy_timer.setting.setting import Setting


class TestSetting(TestCase):
    def test_init(self):
        s1 = Setting()
        self.assertEqual(s1.timer_sec, None)
        self.assertEqual(s1.say_enabled, None)
        self.assertEqual(s1.say_cmd, None)
        self.assertEqual(s1.say_countdown_sec, 10)
        self.assertEqual(s1.say_periodic_min, 10)
        self.assertEqual(s1.say_specific_min, [1, 5])

    def test_find_lang(self):
        s = Setting()
        old = os.environ.get('LANG')

        if old:
            del os.environ['LANG']
        s._find_lang()  # return value depends on the system

        os.environ['LANG'] = 'en_US'
        self.assertEqual(s._find_lang(), 'en_US')

        if old:
            os.environ['LANG'] = old

    def test_find_i18n(self):
        import easy_timer.view.i18n.messages_en
        import easy_timer.view.i18n.messages_ja

        s = Setting()
        self.assertEqual(s._find_i18n(None), easy_timer.view.i18n.messages_en)
        self.assertEqual(s._find_i18n('ja_JP.UTF-8'), easy_timer.view.i18n.messages_ja)
        self.assertEqual(s._find_i18n('C'), easy_timer.view.i18n.messages_en)

    def test_parse_args(self):
        self.maxDiff = None

        s = Setting(say_cmd='say', say_countdown_sec=10, say_periodic_min=10, say_specific_min=[1, 5])

        self.assertEqual(Setting().parse_args(['easy-timer', '0']), s.copy(timer_sec=0, say_enabled=False))
        self.assertEqual(Setting().parse_args(['easy-timer', '1']), s.copy(timer_sec=60, say_enabled=False))
        self.assertEqual(Setting().parse_args(['easy-timer', '2']), s.copy(timer_sec=120, say_enabled=False))
        self.assertEqual(Setting().parse_args(['easy-timer', '03']), s.copy(timer_sec=180, say_enabled=False))
        self.assertEqual(Setting().parse_args(['easy-timer', '003']), s.copy(timer_sec=180, say_enabled=False))
        self.assertEqual(Setting().parse_args(['easy-timer', '0003']), s.copy(timer_sec=180, say_enabled=False))
        self.assertEqual(Setting().parse_args(['easy-timer', '9999']), s.copy(timer_sec=9999 * 60, say_enabled=False))

        self.assertEqual(Setting().parse_args(['easy-timer', '0:0']), s.copy(timer_sec=0, say_enabled=False))
        self.assertEqual(Setting().parse_args(['easy-timer', '0:00']), s.copy(timer_sec=0, say_enabled=False))
        self.assertEqual(Setting().parse_args(['easy-timer', '0:01']), s.copy(timer_sec=1, say_enabled=False))
        self.assertEqual(Setting().parse_args(['easy-timer', '0:1']), s.copy(timer_sec=1, say_enabled=False))
        self.assertEqual(Setting().parse_args(['easy-timer', '1:00']), s.copy(timer_sec=60, say_enabled=False))
        self.assertEqual(Setting().parse_args(['easy-timer', '02:34']), s.copy(timer_sec=154, say_enabled=False))
        self.assertEqual(Setting().parse_args(['easy-timer', '002:34']), s.copy(timer_sec=154, say_enabled=False))
        self.assertEqual(Setting().parse_args(['easy-timer', '0002:34']), s.copy(timer_sec=154, say_enabled=False))
        self.assertEqual(
            Setting().parse_args(['easy-timer', '9999:59']), s.copy(timer_sec=9999 * 60 + 59, say_enabled=False))

        self.assertEqual(
            Setting().parse_args(['easy-timer', '-s', '12:34']),
            s.copy(timer_sec=12 * 60 + 34, say_enabled=True))
