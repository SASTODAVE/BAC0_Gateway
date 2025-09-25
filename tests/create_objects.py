import unittest
from bacnet.objects import create_objects_from_json

class CreateObjects(unittest.TestCase):
    def test_create_objects_from_json(self):
        data = {
            "meter_reading": {
                "reading_type": {"unit": "W"},
                "interval_reading": [{"value": "100", "date": "2025-09-14"}]
            }
        }
        objs = create_objects_from_json(data)
        assert len(objs) == 1
        assert objs[0].presentValue == 100.0

if __name__ == '__main__':
    unittest.main()
