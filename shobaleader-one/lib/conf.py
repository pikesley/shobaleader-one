from ruamel.yaml import YAML


def config(path="config/config.yaml"):
    """Read the config."""
    yaml = YAML()
    return yaml.load(open(path))
