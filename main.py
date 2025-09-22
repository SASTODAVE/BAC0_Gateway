from bacnet import BacnetServer
from bacnet.config_loader import load_config


def main():
    # if len(sys.argv) < 3:
    #   print(f"Usage : {os.path.basename(__file__)} -ip 0.0.0.0")
    #   sys.exit()

    config = load_config()
    device_config = dict(config["Device"])
    server = BacnetServer(device_config["device_name"], device_config["device_identifier"])
    server.start()

if __name__ == "__main__":
    main()