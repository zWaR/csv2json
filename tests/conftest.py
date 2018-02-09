import pytest

from csv2json.csv2json import Csv2Json

@pytest.fixture
def csv2json():
    csv2json: Csv2Json = Csv2Json()

    yield csv2json
