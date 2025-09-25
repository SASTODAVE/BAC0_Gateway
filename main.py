from bacnet import BacnetServer, load_config
from utils.helpers import check_ip
from bacnet.api_client import fetch_objects
from bacnet.objects import create_objects_from_json

def main():
    #Parser for ip
    #parser = argparse.ArgumentParser()
    #parser.add_argument("-ip", "--ip", type=check_ip, required=True, help="Invalid ip address.")

    #args = parser.parse_args()

    #Load config
    config = load_config()
    device_cfg = config.get("device", {})

    data = fetch_objects()
    create_objects_from_json(data)
    check_ip(device_cfg["ip"])

    #Start server
    server = BacnetServer(device_name=device_cfg.get("name"), device_id=device_cfg.get("identifier"), ip=device_cfg.get("ip"))
    server.start()

if __name__ == "__main__":
    main()