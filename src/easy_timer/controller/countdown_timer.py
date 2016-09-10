from __future__ import division, print_function, absolute_import, unicode_literals

import time
import subprocess
from mog_commons.types import *


class CountdownTimer:
    def __init__(self, setting):
        self.setting = setting

    def loop(self):
        start_time = time.time()
        current_time = start_time
        last_printed_sec = -1

        while True:
            elapsed = current_time - start_time
            elapsed_sec = int(elapsed)

            if elapsed_sec != last_printed_sec:
                remain_sec = max(0, self.setting.timer_sec - elapsed_sec)

                self._print_time(remain_sec)
                if self._is_time_to_say(remain_sec):
                    self._say_time(remain_sec)

                if remain_sec <= 0:
                    self.setting.stdout.write('\n')
                    break

                last_printed_sec = elapsed_sec

            time.sleep(0.01)
            current_time = time.time()

    def _print_time(self, remain_sec):
        self.setting.stdout.write('\r%02d:%02d ' % (remain_sec // 60, remain_sec % 60))
        self.setting.stdout.flush()

    @types(bool, remain_sec=int)
    def _is_time_to_say(self, remain_sec):
        if not self.setting.say_enabled:
            return False

        if remain_sec <= self.setting.say_countdown_sec:
            return True

        if remain_sec % 60 != 0:
            return False

        remain_min = remain_sec // 60
        if remain_min % self.setting.say_periodic_min == 0:
            return True

        if remain_min in self.setting.say_specific_min:
            return True

        return False

    def _say_time(self, remain_sec):
        if remain_sec >= 60:
            remain_min = remain_sec // 60
            min_str = self.setting.i18n.MSG_MINUTE if remain_min == 1 else self.setting.i18n.MSG_MINUTES
            s = '%d %s' % (remain_min, min_str)
        elif remain_sec > 0:
            s = '%d' % remain_sec
        else:
            s = self.setting.i18n.MSG_TIME

        subprocess.Popen(self.setting.say_cmd + ' "%s"' % s, shell=True)
