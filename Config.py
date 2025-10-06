import os
import json

CONFIG_DIR = "Config"
CONFIG_FILE = os.path.join(CONFIG_DIR, "Config.json")

def ensure_config_dir():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

def save_config(config_data):
    ensure_config_dir()
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config_data, f, indent=4)
    print(f"Configuration saved to {CONFIG_FILE}")

def load_config():
    if config_exists():
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def config_exists():
    return os.path.exists(CONFIG_FILE)