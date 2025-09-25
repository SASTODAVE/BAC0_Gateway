import unittest

from bacnet.config_loader import load_config


class ReadConfig(unittest.TestCase):
    def test_device_config(self):
        config = load_config("config.yaml")
        self.assertIn("device", config)

        device = config.get('device')
        self.assertIn("name", device)
        self.assertIn("identifier", device)
        self.assertIn("vendor_id", device)

    def test_apis_config(self):
        config = load_config("config.yaml")
        self.assertIn("apis", config)

        apis = config.get('apis')
        for api in apis:
            self.assertIn("name", api)
            self.assertIn("source", api)
            self.assertIn("path", api)

if __name__ == '__main__':
    unittest.main()