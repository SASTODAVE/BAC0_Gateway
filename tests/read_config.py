import unittest

from bacnet.config_loader import load_config


class ReadConfig(unittest.TestCase):
    def test_device_config(self):
        config = load_config("config.ini")
        device_config = dict(config["Device"])

        self.assertIn("device_name", device_config)
        self.assertIn("device_identifier", device_config)
        self.assertIn("vendor_identifier", device_config)


if __name__ == '__main__':
    unittest.main()
