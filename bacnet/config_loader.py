import yaml

def load_config(path="config.yaml"):
    """
    Loads configuration from YAML file.
    :param path: path to configuration file
    :return: config
    """
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config
