"""Run tests.

Main file for running tests.
"""

import body_check
import logbook

from clize import run
from config import clize_log_level
from config import v
from config import version

log = logbook.Logger("run_tests logbook")


def main():
    if __name__ == '__main__':
        run(clize_log_level, alt=[version, v], exit=False)
        body_check.eric_body_summary()


    if body_check.body_test is True:
        log.notice("Success!")
    else:
        log.error("Failure!")
