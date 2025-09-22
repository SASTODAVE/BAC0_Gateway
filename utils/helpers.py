import ipaddress
import argparse
def check_ip(value):
    try:
        return ipaddress.ip_address(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} n'est pas une adresse IP valide")