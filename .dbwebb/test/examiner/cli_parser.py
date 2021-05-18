"""
Parses all custom options and arguments
"""
import argparse

def parse():
    """
    Handles the arguments and options.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        "-w", "--what", dest="what",
        help="REQUIRED - The absolute path to the folder containing the tests"
    )

    parser.add_argument(
        "-t", "--tags", dest="tags", default=[],
        help="Collects tags to run specific tests\n" + \
            "USAGE: -t=tag1 || -t=tag1,tag2"
    )

    parser.add_argument(
        "-e", "--extra", dest="extra_assignments", default=False,
        action="store_true", help="Includes tests for extra assignments"
    )

    parser.add_argument(
        "--trace", dest="trace_assertion_error", default=False,
        action="store_true", help="Adds a traceback option for assertion errors"
    )

    args, _empty = parser.parse_known_args()

    if args.tags:
        args.tags = args.tags.split(",")

    return args