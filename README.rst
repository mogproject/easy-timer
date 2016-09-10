==========
Easy Timer
==========

Super Simple Command-line Countdown Timer

.. image:: https://badge.fury.io/py/easy-timer.svg
   :target: http://badge.fury.io/py/easy-timer
   :alt: PyPI version

.. image:: https://travis-ci.org/mogproject/easy-timer.svg?branch=master
   :target: https://travis-ci.org/mogproject/easy-timer
   :alt: Build Status

.. image:: https://coveralls.io/repos/mogproject/easy-timer/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/mogproject/easy-timer?branch=master
   :alt: Coverage Status

.. image:: https://img.shields.io/badge/license-Apache%202.0-blue.svg
   :target: http://choosealicense.com/licenses/apache-2.0/
   :alt: License

.. image:: https://badge.waffle.io/mogproject/easy-timer.svg?label=ready&title=Ready
   :target: https://waffle.io/mogproject/easy-timer
   :alt: 'Stories in Ready'

--------
Features
--------

*Are you sick of fancy timer applications?*

Easy Timer provides you a minimalist countdown timer inside your command-line terminal.

When you turn on the spoken countdown, the remaining time is periodically notified by voice.
This is useful for studying or working in time without watching a computer screen.

------------
Dependencies
------------

* ``say`` command or its alternatives (for spoken countdown)
* Python: 2.6 / 2.7 / 3.2 / 3.3 / 3.4 / 3.5
* six
* `mog-commons <https://github.com/mogproject/mog-commons-python>`_

----------
Quickstart
----------

You can now try Easy Timer by typing two command lines.

::

    pip install easy-timer
    easy-timer -s 0:10

------------
Installation
------------

* ``pip`` command may need ``sudo``

+-------------------------+---------------------------------------+
| Operation               | Command                               |
+=========================+=======================================+
| Install                 |``pip install easy-timer``             |
+-------------------------+---------------------------------------+
| Upgrade                 |``pip install --upgrade easy-timer``   |
+-------------------------+---------------------------------------+
| Uninstall               |``pip uninstall easy-timer``           |
+-------------------------+---------------------------------------+
| Check installed version |``easy-timer --version``               |
+-------------------------+---------------------------------------+
| Help                    |``easy-timer -h``                      |
+-------------------------+---------------------------------------+

--------
Examples
--------

Set a 10-minute timer.

::

    easy-timer 10

Set an 80-minute (= 1 hour 20 minutes) timer.

::

    easy-timer 80

Set a 90-second (= 1 minute 30 seconds) timer.

::

    easy-timer 1:30
    
Enable the spoken countdown.

::

    easy-timer -s 10
    easy-timer --say 10

Specify ``say`` options.

::

    easy-timer -s --say-cmd='say -v Karen' 1
    easy-timer -s --say-cmd='say -v "Pipe Organ"' 0:10

Set the language to Japanese.

::

    easy-timer -s --say-cmd='say -v Kyoko' --lang=ja 1
    LANG=ja_JP.UTF-8 easy-timer -s --say-cmd='say -v Kyoko' 1
    
Run a timer with ``caffeinate`` command to prevent the system from sleeping.

::

    caffeinate -d easy-timer -s 80

--------------------------
When does the timer speak?
--------------------------

By default, the timer speaks on the following timings.

* Every 10 minutes
* Last 5 minites and 1 minite
* Each of final 10 seconds (countdown)

