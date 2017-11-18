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
    proc = subprocess.Popen(['python', 'write.py', addr], stdout=subprocess.PIPE)
except:
    print("HELLO")

output = helper.concatOutput(proc)
print(output)
mode = helper.findMode(output)
print(mode)
