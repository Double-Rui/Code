import datetime
import random

print('{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())+''.join([str(random.randint(1,10)) for i in range(5)]))