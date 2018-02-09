
import argparse

from .csv2json import Csv2Json

def main():
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("csv", help="CSV input file path", type=str)
    parser.add_argument("json", help="JSON otput path", type=str)
    parser.add_argument(
        "--has_header", 
        help="Does the CSV file have a header",
        action="store_true"
    )
    parser.add_argument(
        "--pretty_print",
        help="JSON should be pretty formated",
        action="store_true"
    )
    args: argparse.Namespace = parser.parse_args()

    Csv2Json().run(args.csv, args.json, args.has_header, args.pretty_print)
