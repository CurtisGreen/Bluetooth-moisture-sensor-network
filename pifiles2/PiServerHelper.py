from MoistureSensors import MoistureSensor
import json, codecs
from bson import json_util
import operator
import datetime
import time

class PiServerHelper(object):
    def __init__(self):
        self.sensorMap = {}  # map to store the readings
        self.threshold = 100  # amount of readings to collect
        self.intervals = 30  # Intervals to Poll the sensors
        self.pollMode = False  # poll or interrupt mode
        self.numSensors = 5  # number of sensors
        self.outsideMode = False  # is the cluster outside
        self.temperature = 0
        self.numReadings = 0
        self.timeToWait = 8

    def insertReading(self, id, moistureReading):
        if id not in self.sensorMap:
            self.sensorMap[id] = MoistureSensor()
            self.sensorMap[id].id = id;

        Sensor = self.sensorMap[id]
        Sensor.readings.append(moistureReading)
        now = datetime.datetime.now()
        Sensor.lastTime = now;
        Sensor.timestamps.append(now.strftime("%Y-%m-%d %H:%M:%S"))
        Sensor.numReadings += 1
        self.numReadings += 1

    def clearReadings(self):
        self.sensorMap.clear
        self.numReadings = 0

    def readingsToJson(self):
        sensorData = {}
        for key in self.sensorMap:
            sensorData[key] = self.sensorMap[key].__dict__
        return sensorData
    
    def timeToRead(self, address):
        now = time.mktime(datetime.datetime.now().timetuple())
        if address not in self.sensorMap:
            return True;        
        last = time.mktime(self.sensorMap[address].lastTime.timetuple())
        diff = now-last
        return diff > self.timeToWait

    def sendReadingsToServer(self):
        return 1

    def sendBrokenSensor(self):
        return 1

    def findMode(self, freqMap):
        try:
           return max(freqMap.iteritems(), key=operator.itemgetter(1))[0]
        except:
            return -1

    def concatOutput(self, process):
        output = ''
        for line in process.stdout:
            if line[0] == 'o':
                line = line.translate(None, ':')
                actual = line[32:-1]
                actual = actual.decode("hex")
                output = output + actual

        output = output.translate(None, '\0')
        return output

    def parseOutput(self, toParse):
        readings = []
        mode = {}
        for i in range(0, len(toParse)):
            if toParse[i] == 's':
                index = i + 4
                size = int(toParse[i + 1:index])
                reading = toParse[index:index + size]
                readings.append(reading)
                i = index + size
                if reading not in mode:
                    mode[reading] = 0
                    mode[reading] = mode[reading] + 1

        return self.findMode(mode)
