from MoistureSensors import MoistureSensor
import json, codecs
from bson import json_util
import operator
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
        Sensor.timestamps.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        Sensor.numReadings += 1

    def readingsToJson(self):
        sensorData = {}
        for key in self.sensorMap:
            sensorData[key] = self.sensorMap[key].__dict__
        #f = open('log.txt', 'w')
        a = sensorData
        #f.write(a)
        #f.close()
        return a


    def sendReadingsToServer(self):
        return 1

    def sendBrokenSensor(self):
        return 1

    def findMode(self, freqMap):
       return max(freqMap.iteritems(), key=operator.itemgetter(1))[0]

    def concatOutput(self, process):
        for line in process.stdout:
            if line[0] == 'o':
                line = line.translate(None, ':')
                # print (line)
                actual = line[32:-1]
                print(actual)
                actual = actual.decode("hex")
                output = output + actual
                # print(actual)

        output = output.translate(None, '\0')
        return output
