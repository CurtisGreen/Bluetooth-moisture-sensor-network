from __future__ import print_function

import sys
from PiServerHelper import PiServerHelper
from gattlib import GATTRequester, DiscoveryService
import subprocess 
import time

try:
    service = DiscoveryService("hci0")
    devices = service.discover(4)
    helper = PiServerHelper()
except:
    print("ERROR")
addr = ''
while addr == '':
    #time.sleep(1)
    for address, name in list(devices.items()):
        print("name: {}, address: {}".format(name, address))
        print(name),
        if name[:5] == "Bluno":
            addr = address
            print("got addr " + addr)
            
            

try:
    proc = subprocess.Popen(['python', 'write.py', addr],stdout=subprocess.PIPE)
except:
    print("HELLO")
output = ''

for line in proc.stdout:
    if line[0] == 'o':
        line = line.translate(None, ':')
        #print (line)
        actual = line[32:-1]
        print(actual)
        actual = actual.decode("hex")
        output = output + actual
        #print(actual)

output = output.translate(None, '\0')
print(output)

readings = []
mode = {}

for i in range(0,len(output)):
    if output[i] == 's':
        index = i+4
        size = int(output[i+1:index])
        reading = output[index:index+size]
        readings.append(reading)
        i = index+size
        if reading not in mode:
                mode[reading] = 0
        mode[reading] = mode[reading] + 1
        
print('mode'+helper.findMode(mode))
print(readings)