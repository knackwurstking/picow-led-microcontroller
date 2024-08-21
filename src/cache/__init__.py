import json


class Cache:
    def __init__(self, name):
        self.name = name  # NOTE: "gp-led"

    def read(self):
        if not self.name:
            return None

        try:
            file_name = self.get_file_name()
            with open(file_name) as file:
                return json.load(file)
        except Exception:
            return None

    def write(self, data):
        if not self.name:
            return None

        try:
            file_name = self.get_file_name()
            with open(file_name) as file:
                json.dump(data, file)
        except Exception:
            pass

        return None

    def get_file_name(self):
        return f"cache-{self.name}.json"
