import json

from typing import Dict
from typing import List

from src.csv2json import Csv2Json
from pyfakefs.fake_filesystem import FakeFilesystem


class TestCsv2Json(object):

    def test_run_header(self, csv2json: Csv2Json, fs: FakeFilesystem) -> None:
        mock_csv: str = "a,b,c,d\n1,2,3,4\n5,6,7,8"
        mock_csv_file_path: str = "/tmp/file.csv"
        mock_json_file_path: str = "/tmp/result.json"
        has_header: bool = True

        with open(mock_csv_file_path, "w") as file:
            file.write(mock_csv)

        csv2json.run(mock_csv_file_path, mock_json_file_path, has_header)

        expected_result: List[Dict[str, str]] = [
            {
                "a": "1",
                "b": "2",
                "c": "3",
                "d": "4"
            },
            {
                "a": "5",
                "b": "6",
                "c": "7",
                "d": "8"
            }

        ]

        with open(mock_json_file_path, "r") as file:
            result_content = json.load(file)

        assert expected_result == result_content

    def test_run_no_header(self, csv2json: Csv2Json, fs: FakeFilesystem) -> None:
        mock_csv: str = "1,2,3,4\n5,6,7,8"
        mock_csv_file_path: str = "/tmp/file.csv"
        mock_json_file_path: str = "/tmp/result.json"
        has_header: bool = False

        with open(mock_csv_file_path, "w") as file:
            file.write(mock_csv)

        csv2json.run(mock_csv_file_path, mock_json_file_path, has_header)

        expected_result: List[List[str]] = [
            [ "1", "2", "3", "4" ],
            [ "5", "6", "7", "8" ]
        ]

        with open(mock_json_file_path, "r") as file:
            result_content = json.load(file)

        assert expected_result == result_content
