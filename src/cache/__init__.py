class Cache:
    def __init__(self, name):
        self.name = name  # NOTE: "gp-led"

    def read(self):
        if not self.name:
            return

        ...  # TODO: load cached file

    def write(self):
        if not self.name:
            return

        ...  # TODO: write cached file
