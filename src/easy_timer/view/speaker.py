from __future__ import division, print_function, absolute_import, unicode_literals

import sys
import subprocess
from mog_commons.case_class import CaseClass
from mog_commons.types import *
from mog_commons.command import execute_command
from easy_timer.view.i18n import messages_en


class Speaker(CaseClass):
    @types(enabled=bool, say_cmd=String, say_countdown_sec=int, say_periodic_min=int, say_specific_min=ListOf(int))
    def __init__(self, enabled, say_cmd, say_countdown_sec, say_periodic_min, say_specific_min,
                 i18n=messages_en, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
        CaseClass.__init__(
            self,
            ('enabled', enabled),
            ('say_cmd', say_cmd),
            ('say_countdown_sec', say_countdown_sec),
            ('say_periodic_min', say_periodic_min),
            ('say_specific_min', say_specific_min),
            ('i18n', i18n),
            ('stdin', stdin),
            ('stdout', stdout),
            ('stderr', stderr)
        )

    @types(bool)
    def verify(self):
        """Test if "say" command works correctly."""
        return not self.enabled or self.speak('.') == 0

    @types(int, text=String)
    def speak(self, text):
        """Speak a text synchronously."""
        ret = execute_command(self._get_cmd_str(text),
                              shell=True, stdin=self.stdin, stdout=self.stdout, stderr=self.stderr)
        return ret

    @types(text=String)
    def speak_async(self, text):
        """Speak a text asynchronously."""
        subprocess.Popen(self._get_cmd_str(text),
                         shell=True, stdin=self.stdin, stdout=self.stdout, stderr=self.stderr)

    @types(remain_sec=int)
    def speak_time(self, remain_sec):
        if self._is_time_to_speak(remain_sec):
            self.speak_async(self._get_speak_text(remain_sec))

    @types(String, text=String)
    def _get_cmd_str(self, text):
        return self.say_cmd + ' "%s"' % text

    @types(remain_sec=int)
    def _get_speak_text(self, remain_sec):
        if remain_sec >= 60:
            remain_min = remain_sec // 60
            min_str = self.i18n.MSG_MINUTE if remain_min == 1 else self.i18n.MSG_MINUTES
            return '%d %s' % (remain_min, min_str)
        elif remain_sec > 0:
            return '%d' % remain_sec
        else:
            return self.i18n.MSG_TIME

    @types(bool, remain_sec=int)
    def _is_time_to_speak(self, remain_sec):
        if not self.enabled:
            return False

        if remain_sec <= self.say_countdown_sec:
            return True

        if remain_sec % 60 != 0:
            return False

        remain_min = remain_sec // 60
        if remain_min % self.say_periodic_min == 0:
            return True

        if remain_min in self.say_specific_min:
            return True

        return False
