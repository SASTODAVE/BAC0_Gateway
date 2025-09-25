import configparser

def load_config(path="config.ini"):
    config = configparser.ConfigParser()
    config.read(path)
    return config

def load_client_config():
    config = load_config()
    return dict(config["Client"])
