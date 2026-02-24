import json

def read_config():
    with open("core/config.json",'r') as f:
        config_data = json.load(f)
    return config_data
