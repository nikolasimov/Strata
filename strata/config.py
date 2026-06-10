class Config:
    def __init__(self, path="strata.conf"):
        self.path = path
        self.data = {
            "server": {},
            "static": {},
            "proxy": {},
            "logging": {}
        }
        self.load()

    def load(self):
        current_section = None

        with open(self.path, "r") as f:
            for line in f:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if line.startswith("[") and line.endswith("]"):
                    current_section = line[1:-1]
                    continue

                if "=" in line and current_section:
                    key, value = line.split("=", 1)
                    self.data[current_section][key.strip()] = value.strip()

    def get(self, section, key, default=None):
        return self.data.get(section, {}).get(key, default)