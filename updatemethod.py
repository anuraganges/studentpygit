
import  datetime
from time import gmtime,strftime
import  time
from time import  time


time_stamp = str(datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))
print(time_stamp)


timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(timestamp)