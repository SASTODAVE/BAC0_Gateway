import time
import threading

class ObjectUpdater:
    def __init__(self, bacnet_objects, interval_readings, update_interval=2):
        self.thread = None
        self.objects = bacnet_objects
        self.readings = interval_readings
        self.update_interval = update_interval
        self.running = False

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._loop, daemon=True)
        self.thread.start()

    def _loop(self):
        i = 0
        while self.running and i < len(self.readings):
            reading = self.readings[i]
            value = float(reading.get("value", 0))
            timestamp = reading.get("date", "unknown")

            for obj in self.objects:
                obj.presentValue = value
                print(f"[{timestamp}] {obj.objectName} = {value} {obj.units}")

            i += 1
            time.sleep(self.update_interval)

    def stop(self):
        self.running = False
        if hasattr(self, "thread") and self.thread.is_alive():
            self.thread.join()
