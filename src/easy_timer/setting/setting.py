from __future__ import division, print_function, absolute_import, unicode_literals

import os
import sys
import locale
import re
from mog_commons.case_class import CaseClass
from mog_commons.functional import oget
from mog_commons.types import *
from mog_commons import command

from easy_timer.setting import arg_parser


DEFAULT_SAY_COUNTDOWN_SEC = 10
DEFAULT_SAY_PERIODIC_MIN = 10
DEFAULT_SAY_SPECIFIC_MIN = [1, 5]


class Setting(CaseClass):
    """
    Manages all settings.
    """

    @types(timer_sec=Option(int))
    def __init__(self, timer_sec=None, say_enabled=None, say_cmd=None, say_countdown_sec=None, say_periodic_min=None,
                 say_specific_min=None, lang=None, i18n=None, stdin=None, stdout=None, stderr=None):
        lang_setting = oget(lang, self._find_lang())

        CaseClass.__init__(
            self,
            ('timer_sec', timer_sec),
            ('say_enabled', say_enabled),
            ('say_cmd', say_cmd),
            ('say_countdown_sec', oget(say_countdown_sec, DEFAULT_SAY_COUNTDOWN_SEC)),
            ('say_periodic_min', oget(say_periodic_min, DEFAULT_SAY_PERIODIC_MIN)),
            ('say_specific_min', oget(say_specific_min, DEFAULT_SAY_SPECIFIC_MIN)),
            ('lang', lang_setting),
            ('i18n', self._find_i18n(lang_setting)),
            ('stdin', oget(stdin, sys.stdin)),
            ('stdout', oget(stdout, sys.stdout)),
            ('stderr', oget(stderr, sys.stderr))
        )

    @staticmethod
    def _find_lang():
        # environment LANG is the first priority
        lang = os.environ.get('LANG')

        if not lang:
            lang = locale.getdefaultlocale()[0]
        return lang

    @staticmethod
    def _find_i18n(lang):
        from easy_timer import i18n

        if not lang:
            return i18n.messages_en
        elif lang.lower().startswith('ja'):
            return i18n.messages_ja
        else:
            return i18n.messages_en

    def parse_args(self, argv):
        option, args = arg_parser.parser.parse_args(argv[1:])
        timer_sec = None

        if len(args) == 1:
            time_spec = args[0]
            timer_sec = self._parse_time_spec(time_spec)

        if timer_sec is None:
            arg_parser.parser.print_help()
            arg_parser.parser.exit(2)

        return self.copy(say_enabled=option.say_enabled, say_cmd=option.say_cmd, timer_sec=timer_sec, lang=option.lang)

    def verify_say_command(self):
        """Test if "say" command works correctly."""

        if self.say_enabled:
            ret = command.execute_command(self.say_cmd + ' .',
                                          shell=True, stdin=self.stdin, stdout=self.stdout, stderr=self.stderr)
            if ret != 0:
                self.stdout.write('\nError: "say" command is not working correctly.\n')
                arg_parser.parser.exit(2)

        return self

    @staticmethod
    @types(Option(int), time_spec=str)
    def _parse_time_spec(time_spec):
        # MMMM
        if re.compile(r"""^[0-9]{1,4}$""").match(time_spec):
            return int(time_spec) * 60

        # MMMM:SS
        m = re.compile(r"""^([0-9]{1,4}):([0-5]?[0-9])$""").match(time_spec)
        if m:
            return int(m.group(1)) * 60 + int(m.group(2))

        return None
