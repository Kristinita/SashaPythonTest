"""Check files for body.

Check, contains files of current directory <body> or no.
"""

import logbook

from sashatest.config import all_txt_in_eric_room_wihtout_subfolders

log = logbook.Logger("eric_body logbook")

body_test = True


def eric_body_function():
    """Check, contains body in a file, or no."""
    for filename in all_txt_in_eric_room_wihtout_subfolders:

        if "<body>" in open(filename, encoding='windows-1251').read():
            log.debug(filename + " contains <body>")
        else:
            log.error(
                "File " +
                filename +
                " not contain <body>.")
            global body_test
            body_test = False


def eric_body_summary():
    """Report, contains <body> in all files or no.

    Use flags, see https://stackoverflow.com/a/48052480/5951529
    """
    eric_body_function()
    if body_test is True:
        log.notice("All files contains <body>")
    else:
        log.error("Not all files contains <body>. Please, correct your files.")
