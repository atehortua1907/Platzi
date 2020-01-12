import yaml
import os

script_dir = os.path.dirname(__file__)
rel_path = "config.yaml"
abs_file_path = os.path.join(script_dir, rel_path)

__config = None

def config():
    global __config
    if not __config:
        with open(abs_file_path, mode='r') as file:
            __config = yaml.load(file, Loader=yaml.FullLoader)
    
    return __config