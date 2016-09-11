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
        from easy_timer.view import i18n

        s = Setting()
        self.assertEqual(s._find_i18n(None), i18n.messages_en)
        self.assertEqual(s._find_i18n('ja_JP.UTF-8'), i18n.messages_ja)
        self.assertEqual(s._find_i18n('C'), i18n.messages_en)

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

    def test_parse_args_error(self):
        self.maxDiff = None
        expect_stdout = '\n'.join([
            'Usage: setup.py [options...] <MM> | <MM:SS>',
            '',
            'Options:',
            "  --version          show program's version number and exit",
            '  -h, --help         show this help message and exit',
            '  -s, --say          enable spoken countdown (default: False)',
            '  --say-cmd=SAY_CMD  set "say" command to SAY_CMD (default: say)',
            '  --lang=LANG        set language to LANG (in RFC 1766 format)',
            '',
        ])

        with self.withAssertOutput(expect_stdout, '') as (out, err):
            self.assertSystemExit(2, Setting(stdout=out, stderr=err).parse_args, ['easy-timer'])

    def test_parse_time_spec(self):
        s = Setting()
        self.assertEqual(s._parse_time_spec('a'), None)
        self.assertEqual(s._parse_time_spec(''), None)
        self.assertEqual(s._parse_time_spec('10000'), None)
        self.assertEqual(s._parse_time_spec('0:60'), None)
        self.assertEqual(s._parse_time_spec('0:99'), None)
