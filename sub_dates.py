import pandas as pd
import random
import datetime
import matplotlib.pyplot as plt 
import raw_crime_data



mytest = []
#number to create random value from, use current time to get random number
#random.seed(datetime.datetime.now())
random.seed(27)

def random_day():
    ret_value = 0

    random_value = random.randint(0, 65000)
    if ((random_value % 5) != 0):
        ret_value = random_value % 42
    else:
        if ((random_value % 42) == 0):
            ret_value = random_value % 366
        else:
            ret_value = random_value % 42
    return(ret_value)
x_axis = []
y_axis = []
#print(raw_crime_data.a_crime)

for i in range(len(raw_crime_data.a_crime)):
    time_delta = random_day()
    my_time_date = datetime.datetime.strptime(raw_crime_data.a_crime['DATE_REPORTED'][i],'%Y-%m-%d %H:%M:%S')
    print(my_time_date)
    timestamp = datetime.datetime.timestamp(my_time_date) + (86400 * time_delta)
    print(timestamp)
    x_axis.append(i + 1)
    y_axis.append(time_delta)
    mytest.append({'INCIDENT_NUMBER': raw_crime_data.a_crime.index[i],
                   'DATE_REPORTED': raw_crime_data.a_crime['DATE_REPORTED'][i],
                   'DATE_SUBMITTED': timestamp,
                   'TIME_DELTA': time_delta})




plt.figure(1)
#plt.xticks(1)
plt.scatter(x_axis, y_axis)
#plt.plot([1,1])
plt.title('Sex Crimes Submissions')
plt.ylabel('Days until submission')
plt.xlabel('Cases')
plt.xticks(list(range(0, len(raw_crime_data.a_crime), 1)))
plt.show()