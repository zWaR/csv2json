
from csv2json import main
from unittest.mock import patch
from unittest.mock import MagicMock

class TestMain(object):

    @patch("csv2json.main.argparse")
    @patch("csv2json.main.Csv2Json")
    def test_main(self, csv2json: MagicMock, argparse: MagicMock):
        main.main()

        assert argparse.ArgumentParser.called
        assert csv2json.called
