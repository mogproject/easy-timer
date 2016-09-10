from __future__ import division, print_function, absolute_import, unicode_literals

import sys
from easy_timer.setting.setting import Setting
from easy_timer.controller.countdown_timer import CountdownTimer


def main(stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    """
    Main function
    """

    setting = Setting(stdin=stdin, stdout=stdout, stderr=stderr).parse_args(sys.argv).verify_say_command()

    try:
        CountdownTimer(setting).loop()
    except KeyboardInterrupt:
        pass
