import json

class MoistureSensor(object):
    def __init__(self):
        self.readings = []
        self.timestamps = []
        self.numReadings = 0
        self.id = 0



