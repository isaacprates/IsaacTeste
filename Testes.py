from datetime import datetime as dt
from datetime import timedelta as td
UsrInput = '00:00'
fmtString = '%H:%M'
myTime = dt.strptime(UsrInput, fmtString)
increment = td(0,1)
for count in range(10):
    myTime += increment
    print (dt.strftime(myTime, fmtString))