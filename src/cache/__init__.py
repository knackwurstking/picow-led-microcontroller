class Cache:
    def __init__(self, name):
        self.name = name  # NOTE: "gp-led"

    def read(self):
        if not self.name:
            return None

        ...  # TODO: load cached file

    def write(self):
        if not self.name:
            return None

        ...  # TODO: write cached file