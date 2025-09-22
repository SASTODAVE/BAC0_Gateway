import os.path
import sys

from bacnet import BacnetServer

def main():
    # if len(sys.argv) < 3:
    #   print(f"Usage : {os.path.basename(__file__)} -ip 0.0.0.0")
    #   sys.exit()

    server = BacnetServer("MyDevice", 1000)
    server.start()

if __name__ == "__main__":
    main()