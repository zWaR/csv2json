
import csv
import json

from typing import List
from typing import Dict
from typing import Iterable

class Csv2Json(object):

    def run(self, 
        csv_path: str, 
        json_path: str, 
        has_header: bool = False,
        pretty_print: bool = False
    ) -> None:
        """Execute csv 2 json conversion.
        Args:
            csv_path (str): Path to the CSV input file.
            json_path (str): Path to the JSON output file.
            has_header (bool): Does the CSV file have a header.
            pretty_print (bool): Pretty JSON formatting enabled.
        """

        csv_array: List = []
        with open(
            csv_path, newline="", encoding="utf-8", errors="ignore"
        ) as csv_file:
            csv_content: Iterable = csv.reader(csv_file, delimiter=",")
            for row in csv_content:
                csv_array.append(row)

        header: List[str] = []
        json_struct: List = []
        if has_header:
            header = csv_array.pop(0)
            for row in csv_array:
                temp_struct: Dict = {}
                for index, element in enumerate(header):
                    temp_struct[element] = row[index]
                json_struct.append(temp_struct)

        if not has_header:
            for row in csv_array:
                json_struct.append(row)

        with open(json_path, "w") as json_file:
            if pretty_print:
                json.dump(json_struct, json_file, indent=2)
            else:
                json.dump(json_struct, json_file)
