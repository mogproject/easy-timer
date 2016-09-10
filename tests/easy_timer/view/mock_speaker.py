from __future__ import division, print_function, absolute_import, unicode_literals

import sys
from mog_commons.types import *
from easy_timer.view.i18n import messages_en
from easy_timer.view.speaker import Speaker
from easy_timer.setting.setting import DEFAULT_SAY_COUNTDOWN_SEC, DEFAULT_SAY_PERIODIC_MIN, DEFAULT_SAY_SPECIFIC_MIN


class MockSpeaker(Speaker):
    def __init__(self,
                 enabled=False,
                 say_cmd='say',
                 say_countdown_sec=DEFAULT_SAY_COUNTDOWN_SEC,
                 say_periodic_min=DEFAULT_SAY_PERIODIC_MIN,
                 say_specific_min=DEFAULT_SAY_SPECIFIC_MIN,
                 i18n=messages_en,
                 stdin=sys.stdin,
                 stdout=sys.stdout,
                 stderr=sys.stderr):
        Speaker.__init__(self, enabled, say_cmd, say_countdown_sec, say_periodic_min, say_specific_min,
                         i18n=i18n, stdin=stdin, stdout=stdout, stderr=stderr)
        self.history = []

    @types(int, text=String)
    def speak(self, text):
        self.history.append(('speak', self._get_cmd_str(text)))
        return 0

    @types(text=String)
    def speak_async(self, text):
        self.history.append(('speak_async', self._get_cmd_str(text)))
