"""Run tests.

Main file for running tests.
"""

import sashatest.body_check
import logbook

from clize import run
from sashatest.config import clize_log_level
from sashatest.config import v
from sashatest.config import version

log = logbook.Logger("run_tests logbook")


def main():
    run(clize_log_level, alt=[version, v], exit=False)
    sashatest.body_check.eric_body_summary()

    if sashatest.body_check.body_test is True:
        log.notice("Success!")
    else:
        log.error("Failure!")


if __name__ == '__main__':
    main()
