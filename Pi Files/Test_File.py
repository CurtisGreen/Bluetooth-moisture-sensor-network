from PiServerHelper import PiServerHelper
import urllib
import urllib2

helper = PiServerHelper()
url = 'http://127.0.0.1:5000/product/add' # Set destination URL here
post_fields = {'foo': 'bar'}     # Set POST fields here



for i in range(0, 10):
    for j in range(0,5):
        helper.insertReading(i,j)

#for key in helper.sensorMap:
#    print "key: %s , value: %s" % (key, helper.sensorMap[key].readings)
a = helper.readingsToJson()

values = a;

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()