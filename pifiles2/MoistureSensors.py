import json
import datetime

class MoistureSensor(object):
    def __init__(self):
        self.readings = []
        self.timestamps = []
        self.numReadings = 0
        self.id = 0
        self.lastTime = datetime.datetime.now()



