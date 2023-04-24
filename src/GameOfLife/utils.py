import argparse
def setting_arguments_parser() -> argparse.Namespace:
    """Adds and configures the argument parser to enable the debug (logging) flag."""
    parser = argparse.ArgumentParser(
        prog="The entry point to the game of Live",
        description="Logging mode is available, to enable it, make sure that all \
        the dependencies specified in README.md, then set the --debug flag"
    )
    parser.add_argument('-D', '--debug', action='store_true', help="Enables game logging")
    args = parser.parse_args()
    return args