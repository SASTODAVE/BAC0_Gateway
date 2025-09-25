import argparse

from bacnet import BacnetServer, load_config
from utils.helpers import check_ip
from bacnet.api_client import fetch_objects
from bacnet.objects import create_objects_from_json

def main():
    #Parser for ip
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--ip", type=check_ip, required=True, help="Invalid ip address.")

    args = parser.parse_args()

    #Load config
    config = load_config()
    device_config = dict(config["Device"])

    data = fetch_objects()
    create_objects_from_json(data)

    #Start server
    server = BacnetServer(device_name=device_config["device_name"], device_id=device_config["device_identifier"], ip=args.ip)
    server.start()

if __name__ == "__main__":
    main()