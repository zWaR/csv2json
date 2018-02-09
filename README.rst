csv2json
========

Tool for csv to json file conversion.

Support for python 3.6+

------------
Installation
------------

::

    pip install csv2json


-----
Usage
-----

::

    csv2json input.csv output.json --has_header --pretty_print

    usage: main.py [-h] [--has_header] [--pretty_print] csv json

    positional arguments:
    csv             CSV input file path
    json            JSON otput path

    optional arguments:
    -h, --help      show this help message and exit
    --has_header    Does the CSV file have a header
    --pretty_print  JSON should be pretty formated


Module can also be imported to your source code::

    import csv2json

    csv2json.run(
        csv_file_path: str, 
        json_file_path: str, 
        has_header: bool = False, 
        pretty_print: bool = False
    )