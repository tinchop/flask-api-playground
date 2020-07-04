import json

class Place:

    def __init__(self, name):
        self.name = name

    def to_JSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))