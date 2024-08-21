import os
import json


class Cache:
    def __init__(self, name):
        self.name = name  # NOTE: "gp-led"

    def read(self):
        if not self.name:
            return None

        file_name = self.get_file_name()
        with open(file_name) as file:
            return json.load(file)

    def write(self, data):
        if not self.name:
            return None

        file_name = self.get_file_name()
        with open(file_name) as file:
            json.dump(data, file)

        return None

    def get_file_name(self):
        return os.path.join("cache", self.name, ".json")
