from __future__ import division, print_function, absolute_import, unicode_literals

import sys
from mog_commons.case_class import CaseClass
from mog_commons.io import print_safe
from easy_timer.view.i18n import messages_en


class Printer(CaseClass):
    def __init__(self, i18n=messages_en, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
        CaseClass.__init__(
            self,
            ('i18n', i18n),
            ('stdin', stdin),
            ('stdout', stdout),
            ('stderr', stderr)
        )

    def print_time(self, remain_sec):
        print_safe('\r%02d:%02d ' % (remain_sec // 60, remain_sec % 60), output=self.stdout, newline='')

    def terminate(self):
        print_safe('', output=self.stdout)
