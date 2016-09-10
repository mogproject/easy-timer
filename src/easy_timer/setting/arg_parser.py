from __future__ import division, print_function, absolute_import, unicode_literals

from optparse import OptionParser

VERSION = 'easy-timer %s' % __import__('easy_timer').__version__

USAGE = """%prog [options...] <MM> | <MM:SS>"""


def __get_parser():
    p = OptionParser(version=VERSION, usage=USAGE)

    p.add_option(
        '-s', '--say', dest='say_enabled', action='store_true', default=False,
        help='enable spoken countdown (default: False)'
    )

    p.add_option(
        '--say-cmd', dest='say_cmd', default='say', type='string', metavar='SAY_CMD',
        help='set "say" command to SAY_CMD (default: say)'
    )

    p.add_option(
        '--lang', dest='lang', default=None, type='string', metavar='LANG',
        help='set language to LANG (in RFC 1766 format)'
    )
    return p


parser = __get_parser()
