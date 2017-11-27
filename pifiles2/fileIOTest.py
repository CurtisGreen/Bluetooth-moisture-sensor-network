from PiServerHelper import PiServerHelper
import random
helper = PiServerHelper()
# helper.initializeCluster("ORIGINAL_PI")
for i in range(0, 20):
    helper.insertReading("50:65:83:8B:0A:92", random.randint(1, 100))
    helper.insertReading("50:65:83:8C:12:22", random.randint(1, 100))
values = {}
values = helper.readingsToJson()
print(values.keys())
print(type(values))

f = open('helloworld.txt', 'w')
f.write(str(values))
f.close()