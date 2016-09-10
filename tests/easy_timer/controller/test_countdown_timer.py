from __future__ import division, print_function, absolute_import, unicode_literals

from mog_commons.unittest import TestCase
from easy_timer.controller.countdown_timer import CountdownTimer
from easy_timer.view import Printer
from tests.easy_timer.view.mock_speaker import MockSpeaker


class TestCountdownTimer(TestCase):
    def test_loop(self):
        self.maxDiff = None

        with self.withAssertOutput('\r00:03 \r00:02 \r00:01 \r00:00 \n', '') as (out, err):
            printer = Printer(stdout=out, stderr=err)
            speaker = MockSpeaker(True)

            t = CountdownTimer(3, printer, speaker)
            t.loop()
            self.assertEqual(speaker.history, [
                ('speak_async', 'say "3"'),
                ('speak_async', 'say "2"'),
                ('speak_async', 'say "1"'),
                ('speak_async', 'say "time"')
            ])
