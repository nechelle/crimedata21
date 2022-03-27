import pandas as pd
import random
import datetime
import matplotlib.pyplot as plt 
import raw_crime_data



num_30_and_below = 0
num_above_30 = 0
mytest = []
pie_chart_data = []

#number to create random value from, use current time to get random number
random.seed(datetime.datetime.now().timestamp())
#random.seed(27)


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

def process_delta_for_graph(delta):
    global num_above_30
    global num_30_and_below

    if delta > 30:
        num_above_30 += 1
    else:
        num_30_and_below += 1

def draw_graph():
    pie_chart_data.append(num_30_and_below)
    pie_chart_data.append(num_above_30)
    pie_chart_labels = ['<= 30', '> 30']
    plt.pie(pie_chart_data, labels = pie_chart_labels, autopct='%1.2f%%')
    plt.title('Sex Crimes Submissions')
    plt.show()


for i in range(len(raw_crime_data.a_crime)):
    time_delta = random_day()
    my_time_date = datetime.datetime.strptime(raw_crime_data.a_crime['DATE_REPORTED'][i],'%Y-%m-%d %H:%M:%S')
    #print(my_time_date)
    timestamp = datetime.datetime.timestamp(my_time_date) + (86400 * time_delta)
    #print(timestamp)
    mytest.append({'INCIDENT_NUMBER': raw_crime_data.a_crime.index[i],
                   'DATE_REPORTED': raw_crime_data.a_crime['DATE_REPORTED'][i],
                   'DATE_SUBMITTED': timestamp,
                   'TIME_DELTA': time_delta})
    process_delta_for_graph(time_delta)

print(">30:", num_above_30)
print("<30:", num_30_and_below)

draw_graph()  
