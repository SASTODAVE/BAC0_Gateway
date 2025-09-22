import signal

from bacpypes.app import BIPSimpleApplication
from bacpypes.core import run, stop
from bacpypes.local.device import LocalDeviceObject

class BacnetServer:
    def __init__(self, device_name, device_id, vendor_id=9999, ip="0.0.0.0"):
        self.device = LocalDeviceObject(
            objectIdentifier=int(device_id),
            objectName=device_name,
            segmentationSupported="noSegmentation",
            vendorIdentifier=int(vendor_id)
        )

        self.app = BIPSimpleApplication(self.device, ip)

    @staticmethod
    def start():
        def handle_stop(signum, frame):
            print("🛑 Stopping server...")
            stop()

        signal.signal(signal.SIGINT, handle_stop)

        print("🚀 Launch server...")
        run()
