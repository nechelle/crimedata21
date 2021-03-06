import pandas as pd
import random
import datetime
import matplotlib.pyplot as plt 
import raw_crime_data
import logging

logger=logging.getLogger('matplotlib.font_manager').disabled=True
logging.basicConfig(filename='error.log', filemode='w', level=logging.DEBUG)

num_30_and_below = 0
num_above_30 = 0
boundary_time = 50

#number to create random value from, use current time to get random number
random.seed(datetime.datetime.now().timestamp())

def random_day():
    global boundary_time
    ret_value = random.randint(0, boundary_time)
    boundary_time = random.randint(28, 65)
    
    return(ret_value)

#generate totals from time data
def process_delta_for_graph(delta):
    global num_above_30
    global num_30_and_below

    if delta > 30:
        num_above_30 += 1
    else:
        num_30_and_below += 1

#create pie chart percentages from time delta totals
def draw_graph(equal_and_below, above):
    pie_chart_data = []
    pie_chart_labels = []
    pie_chart_data.append(equal_and_below)
    pie_chart_data.append(above)
    pie_chart_labels.append('<=30 days')
    pie_chart_labels.append('>30 days')
    plt.pie(pie_chart_data, labels = pie_chart_labels, autopct='%1.2f%%')
    plt.title(raw_crime_data.crime_type + ' Submissions')
    plt.show()
    logging.info("Display pie chart.")
#create while loop for asking user input
crime_option = 0

while crime_option != 'Q':
    num_30_and_below = 0
    num_above_30 = 0

    crime_option = raw_crime_data.crime_menu()
    
    if crime_option.isalpha():
        crime_option = crime_option.upper()

    result = raw_crime_data.set_crime_search(crime_option)

    if result == 2:
        logging.warning("Quitting the application.")
        continue
    elif result == -1:
        logging.error("Entered invalid option.")
    elif result == 0:
        logging.info("Valid option entered.")
        print('This offense occurred', len(raw_crime_data.a_crime), 'times in 2021.')
#create TIME DELTA column and generate time_delta based on info in DATE REPORTED column
        mylist = []
        for i in range(len(raw_crime_data.a_crime)):
            time_delta = random_day()
            my_time_date = datetime.datetime.strptime(raw_crime_data.a_crime['DATE_REPORTED'][i],'%Y-%m-%d %H:%M:%S')
            #print(my_time_date)
            timestamp = datetime.datetime.timestamp(my_time_date) + (86400 * time_delta)
            #print(timestamp)
            mylist.append({'INCIDENT_NUMBER': raw_crime_data.a_crime.index[i],
                        'DATE_REPORTED': raw_crime_data.a_crime['DATE_REPORTED'][i],
                        'DATE_SUBMITTED': timestamp,
                        'TIME_DELTA': time_delta})
        
            process_delta_for_graph(time_delta)
    #print totals generated from new time data
        print("Cases submitted >30 days:", num_above_30)
        print("Cases submitted <30 days:", num_30_and_below, "\n")

        draw_graph(num_30_and_below, num_above_30)  
print('Thanks for your inquiry.')