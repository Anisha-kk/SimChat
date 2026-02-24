from .config_read import read_config
import json

'''
def load_rules():
    rule_base_dict = read_config()
    with open(rule_base_dict["rule_base"]) as f:
        return json.load(f)
'''
import json, os
from time import time


_rules_cache = {}
_last_modified = 0

def get_rules():
    global _rules_cache, _last_modified
    rule_base_dict = read_config()
    file_path = rule_base_dict["rule_base"]
    modified = os.path.getmtime(file_path)

    if modified > _last_modified:  # file changed
        with open(file_path) as f:
            _rules_cache = json.load(f)
        _last_modified = modified

    return _rules_cache