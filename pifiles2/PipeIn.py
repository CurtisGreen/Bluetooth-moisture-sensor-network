from __future__ import print_function
from PiServerHelper import PiServerHelper
from gattlib import GATTRequester, DiscoveryService
from random import randint
import sys, os
import urllib
import urllib2

import sys, subprocess, time, signal



def destroy():
    print('destroying')



#####################   SETUP   #####################
try:
    service = DiscoveryService("hci0")
    devices = service.discover(4)
    helper = PiServerHelper()
    url = 'http://192.168.0.101:5000/product/add'  # Set destination URL here
    LogIndex = 0
except:
    print("Device Discovery ERROR")


while True:
    addresses = []
    for address, name in list(devices.items()):
        if name[:5] == "Bluno":
            addresses.append(address)
        #print(addresses)
    if addresses:
        try:
            addr = addresses[randint(0, len(addresses)-1)]
            if helper.timeToRead(addr): 
                proc = subprocess.Popen(['python', 'write.py', addr], stdout=subprocess.PIPE)
                output = helper.concatOutput(proc)
                parsed = helper.parseOutput(output)
                if parsed != -1:
                    helper.insertReading(addr, parsed)
                    print(addr)
                    print(parsed)



            if helper.numReadings == 10000:
                values = helper.readingsToJson()
                print(values);
                print("______")
                data = urllib.urlencode(values)
                req = urllib2.Request(url, data)
                response = urllib2.urlopen(req)
                the_page = response.read()
                print(the_page)

        except KeyboardInterrupt:
            print("stopping cause of keyboard")
            print(helper.readingsToJson())
            time.sleep(1)
            destroy()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)



