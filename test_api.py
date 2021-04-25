import pandas as pd
from api.service_api import getAll,getCountry
import unittest

class apiTest(unittest.TestCase):
    def test_country_empty(self):
        json_all = getAll()
        df = pd.read_json(json_all)
        df = df.groupby("region").sum()
        regiones = df.index.values.tolist()
        print(f"regiones:{regiones}")
        for i in regiones:
            print(f"i:{i}")
            assert(i!="")
    def test_country_none(self):
        json_all = getAll()
        df = pd.read_json(json_all)
        df = df.groupby("region").sum()
        regiones = df.index.values.tolist()
        print(f"regiones:{regiones}")
        for i in regiones:
            self.assertIsNone(getCountry(i))

if __name__ == "__main__":
    unittest.main()
