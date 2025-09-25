import signal
import time

from bacpypes.app import BIPSimpleApplication
from bacpypes.core import run, stop
from bacpypes.local.device import LocalDeviceObject
from .objects import create_objects_from_json
from .updater import ObjectUpdater
from .api_client import fetch_objects
from .config_loader import load_config

class BacnetServer:
    def __init__(self, device_name, device_id, vendor_id=9999, ip="0.0.0.0"):
        self.ip = str(ip)
        self.device = LocalDeviceObject(
            objectIdentifier=int(device_id),
            objectName=device_name,
            segmentationSupported="noSegmentation",
            vendorIdentifier=int(vendor_id)
        )

        self.app = BIPSimpleApplication(self.device, self.ip)
        self.updaters = []

        config = load_config()
        for api_cfg in config.get("apis", []):
            data = fetch_objects(
                from_type=api_cfg.get("source", "file"),
                path=api_cfg.get("path", None),
            )

            objects = create_objects_from_json(data)

            for obj in objects:
                self.app.add_object(obj)

            interval_readings = data.get("meter_reading", {}).get("interval_reading", [])
            updater = ObjectUpdater(objects, interval_readings)
            self.updaters.append(updater)

    def start(self):
        def handle_stop(signum, frame):
            print("🛑 Stopping server...")
            for upd in self.updaters:
                upd.stop()
            stop()

        signal.signal(signal.SIGINT, handle_stop)
        print(f"🚀 Launch server on {self.ip}:47808...")
        time.sleep(2)
        for updater in self.updaters:
            updater.start()
        run()
