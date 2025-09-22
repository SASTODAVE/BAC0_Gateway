import argparse

from bacnet import BacnetServer
from bacnet.config_loader import load_config
from utils.helpers import check_ip


def main():
    #Parser for ip
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--ip", dest="IP Address", type=check_ip, required=True, help="Invalid ip address.")

    args = parser.parse_args()

    #Load config
    config = load_config()
    device_config = dict(config["Device"])

    #Start server
    server = BacnetServer(device_config["device_name"], device_config["device_identifier"], ip=args.ip)
    server.start()

if __name__ == "__main__":
    main()