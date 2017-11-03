from MoistureSensors import MoistureSensor
import json, codecs
from bson import json_util
import datetime

class PiServerHelper(object):
    def __init__(self):
        self.sensorMap = {}  # map to store the readings
        self.threshold = 100  # amount of readings to collect
        self.intervals = 30  # Intervals to Poll the sensors
        self.pollMode = False  # poll or interrupt mode
        self.numSensors = 5  # number of sensors
        self.outsideMode = False  # is the cluster outside
        self.temperature = 0

    def insertReading(self, id, moistureReading):
        if id not in self.sensorMap:
            self.sensorMap[id] = MoistureSensor()
            self.sensorMap[id].id = id;

        Sensor = self.sensorMap[id]
        Sensor.readings.append(moistureReading)
        Sensor.timestamps.append(int(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
        Sensor.numReadings += 1

    def readingsToJson(self):
        sensorData = {}
        for key in self.sensorMap:
            sensorData[key] = json.dumps(self.sensorMap[key].__dict__)
        f = open('log.txt', 'w')
        a = sensorData[0]
        f.write(a)
        print json.dumps(a)
        f.close()
        return a


    def sendReadingsToServer(self):
        return 1

    def sendBrokenSensor(self):
        return 1

