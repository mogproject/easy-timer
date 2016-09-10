from __future__ import division, print_function, absolute_import, unicode_literals

import sys
from mog_commons.io import print_safe
from easy_timer.setting.setting import Setting
from easy_timer.controller.countdown_timer import CountdownTimer
from easy_timer.view import Printer, Speaker


def main(stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    """
    Main function
    """

    setting = Setting(stdin=stdin, stdout=stdout, stderr=stderr).parse_args(sys.argv)
    printer = Printer(setting.i18n, setting.stdin, setting.stdout, setting.stderr)
    speaker = Speaker(setting.say_enabled,
                      setting.say_cmd, setting.say_countdown_sec, setting.say_periodic_min, setting.say_specific_min,
                      i18n=setting.i18n, stdin=setting.stdin, stdout=setting.stdout, stderr=setting.stderr)

    if not speaker.verify():
        print_safe('\nError: "say" command is not working correctly.', output=stdout)
        sys.exit(2)

    try:
        CountdownTimer(setting.timer_sec, printer, speaker).loop()
    except KeyboardInterrupt:
        pass
