from __future__ import division, print_function, absolute_import, unicode_literals

import time
from mog_commons.types import *

from easy_timer.view import Printer, Speaker


class CountdownTimer(object):
    @types(timer_sec=int, printer=Printer, speaker=Speaker)
    def __init__(self, timer_sec, printer, speaker):
        self.timer_sec = timer_sec
        self.printer = printer
        self.speaker = speaker

    def loop(self):
        start_time = time.time()
        current_time = start_time
        last_printed_sec = -1

        while True:
            elapsed = current_time - start_time
            elapsed_sec = int(elapsed)

            if elapsed_sec != last_printed_sec:
                remain_sec = max(0, self.timer_sec - elapsed_sec)

                self.printer.print_time(remain_sec)
                self.speaker.speak_time(remain_sec)

                if remain_sec <= 0:
                    self.printer.terminate()
                    break

                last_printed_sec = elapsed_sec

            time.sleep(0.01)
            current_time = time.time()
