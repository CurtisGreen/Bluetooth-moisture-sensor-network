from __future__ import print_function

import sys
from gattlib import GATTRequester, DiscoveryService

service = DiscoveryService("hci0")
devices = service.discover(4)

#result = None
#while result is None:
    #try:

    #except:
    #    pass
    #print("collecting")
addr = ''

for address, name in list(devices.items()):
    #print("name: {}, address: {}".format(name, address))
    #print(name),
    if name[:5] == "Bluno":
        addr = address
print(addr)
import subprocess
proc = subprocess.Popen(['python', 'write.py', addr],stdout=subprocess.PIPE)

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
        print(output[i+1:index])
        size = int(output[i+1:index])
        print(size)
        readings.append(output[index:index+size])
        print(output[index:index+size])
        i = index+size
        
        
print(readings)