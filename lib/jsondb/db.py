import os
import json

class JsonDB:
    def __init__(self, name: str):
        if not os.path.exists(name):
            with open(name, "w+") as f:
                f.write('{}')

        self._name = name

    def read_all(self):
        with open(self._name, 'r') as f:
            return json.loads(f.read())

    def read_key(self, key: str):
        data = self.read_all()

        if key in data:
            return data[key]

        return None

    def add_key(self, key: str, data: dict):
        db = self.read_all()
        db[key] = data

        with open(self._name, 'w') as f:
            f.write(json.dumps(db, indent=1))
