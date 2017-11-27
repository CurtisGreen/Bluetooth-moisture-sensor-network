from PiServerHelper import PiServerHelper
import random
import datetime

helper = PiServerHelper()
helper.Setup("Settings.txt", False)

##lines = [line.rstrip('\n\r') for line in open('Settings.txt')]
##addresses = []
##addressSet = set()
##names = []
##for line in lines[1:]:
##    info = line.split(',')
##    addressSet.add(info[0])
##    names.append(info[1])
##addresses = list(addressSet)
##
##helper.name = lines[0]
##payload = {"bluetooth_address":addresses, "name":names}
##payload["bluetooth_address"] = addresses
##payload["name"] = names
##print(payload)

#helper.initializeCluster(lines[0])
#helper.initializeAddresses(payload)


##time = datetime.datetime(2017, 11, 25, 11, 29 , 30, 79043)
##
###for i in range(0, 121):
##helper.insertReading(addresses[0], random.randint(1, 100), time + datetime.timedelta(minutes = 131*30+random.randint(0,3)))
    #helper.insertReading(addresses[1], random.randint(1, 100), time + datetime.timedelta(minutes = i*30+random.randint(0,3)))
    #helper.insertReading(addresses[2], random.randint(1, 100), time + datetime.timedelta(minutes = i*30+random.randint(0,3)))
    #helper.insertReading(addresses[3], random.randint(1, 100), time + datetime.timedelta(minutes = i*30+random.randint(0,3)))
    #helper.insertReading(addresses[4], random.randint(1, 100), time + datetime.timedelta(minutes = i*30+random.randint(0,3)))



#print helper.sendReading()
















# for i in range(0, 20):
#     helper.insertReading("50:65:83:8B:0A:92", random.randint(1, 100))
#     helper.insertReading("50:65:83:8C:12:22", random.randint(1, 100))
# values = {}
# values = helper.readingsToJson()
# print(values.keys())
# print(type(values))
#
# index = 0
# fname = "log"+str(index)+".txt"
# f = open('helloworld.txt', 'w')
# f.write(str(values))
# f.close()