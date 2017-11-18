from PiServerHelper import PiServerHelper
import urllib
import urllib2
import random

helper = PiServerHelper()
url = 'http://192.168.0.104:5000/product/add' # Set destination URL here
post_fields = {'foo': 'bar'}     # Set POST fields here


mode = {}
for i in range(0, 34):
        helper.insertReading(i % 5, random.randint(1, 10))
        rand = random.randint(1, 10)
        if rand not in mode:
                mode[rand] = 0
        mode[rand] = mode[rand] + 1

print(mode)
print(helper.findMode(mode))

#for key in helper.sensorMap:
#    print "key: %s , value: %s" % (key, helper.sensorMap[key].readings)


values = helper.readingsToJson()
print(values);
print("______")
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print(the_page)