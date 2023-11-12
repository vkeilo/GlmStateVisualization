# 该模块解析 visual_config.json 中的内容，并提供对应的class
import json


class VisualConfig():
    def __init__(self, config_path = "./visual_config.json"):
        self.config = self.get_config(config_path)
        self.save_dir_path = self.config['config.json']
        self.tmp_dir_path = self.config["tmp_dir_path"]
        self.THUDM_dir_path = self.config["THUDM_dir_path"]
    def get_config(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config

