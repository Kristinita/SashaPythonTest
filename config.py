"""Configuration.

Configuration for tests.

Variables:
    VERSION {str} -- version of module
    all_txt_in_eric_room_wihtout_subfolders {list(current_directory)} -- get all files in current directory
"""

import glob
import logbook
import sys

VERSION = "0.1"

# Get all .txt file in a directory
# https://stackoverflow.com/a/3964689/5951529
all_txt_in_eric_room_wihtout_subfolders = glob.glob('*.txt')


def version():
    """Show version.

    For details see:
    https://clize.readthedocs.io/en/stable/dispatching.html#alternate-actions
    """
    print(VERSION)


def v():
    """Alternative show version.

    For details see: https://github.com/epsy/clize/issues/34
    """
    print(VERSION)


def clize_log_level(*, logbook_level: 'll'="NOTICE"):
    """Change log levels via command line.

    User select, which logging messages to see. See about 6 log levels here:
    https://logbook.readthedocs.io/en/stable/quickstart.html

    :param logbook_level: user select logging level
    """
    if logbook_level == "DEBUG":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.DEBUG).push_application()
    elif logbook_level == "NOTICE":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.NOTICE).push_application()
    elif logbook_level == "ERROR":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.ERROR).push_application()
    else:
        logbook.StreamHandler(sys.stdout,
                              level=logbook.NOTICE).push_application()
