import argparse
import os

UI_CONVERTER_BINARY_CMD = 'pyuic5'
PROGRAM_NAME = "ui-converter"
DESCRIPTION = "Script to automatically convert qt design '.ui' files to python '.py' generated files"


def main():
    parser = initialize_argument_parser()
    args = parser.parse_args()

    binary = args.ui2pyc
    input_file = args.input
    output_file = args.output

    os.system(f"{binary} {input_file} -o {output_file}")


def initialize_argument_parser():
    """ Parse all the input arguments to the script

        :return: Parser object for parsing command line strings into Python objects.
    """

    parser = argparse.ArgumentParser(
        prog=PROGRAM_NAME,
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter)

    ### General arguments ###
    script_options = parser.add_argument_group("Script Options")

    # Path to pyuic5 utility
    script_options.add_argument("--ui2pyc", default="pyuic5", type=str, nargs="?",
                                help='Path to pyuic5 binary (Default: %(default)s)')

    # Input UI file
    script_options.add_argument("--input", default="MBTA_window_qtdesign.ui", type=str, nargs="?",
                                help="Path to input '.ui' file (Default: %(default)s)")

    # Output python file
    script_options.add_argument("--output", default="ui_main_window.py", type=str, nargs="?",
                                help="Output file '.py' file (Default: %(default)s)")

    return parser


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
