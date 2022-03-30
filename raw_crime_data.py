import pandas as pd

#load data from online csv file, remove unneccessary columns, index by incident number 
crime_df = pd.read_csv('https://lky-open-data.s3.amazonaws.com/LMPD/CRIME_DATA_2021.csv')
to_drop = ['DATE_OCCURED','UOR_DESC', 'NIBRS_CODE', 'UCR_HIERARCHY', 'ATT_COMP', 'LMPD_BEAT', 'BLOCK_ADDRESS']
crime_df.drop(to_drop, inplace = True, axis = 1)
crime_df.set_index('INCIDENT_NUMBER', inplace = True)

a_crime = []
crime_type = ""
#create menu for user to choose crime, populates all crimes committed in 2021
#asks for user input, outputs input
def crime_menu():
    print("*******************************************************")
    print("********** 2021 LMPD Crime Submissions Menu ***********")
    print("*******************************************************")
    print("**** Choose a crime, enter 'Q' to quit.            ****")
    print("*******************************************************")
    crime_list = crime_df.CRIME_TYPE.unique()
    for number, letter in enumerate(crime_list, start=1):
        print(number, letter) 
    
    offense = input("Which criminal offense are you interested in? ")
    
    return offense
#give number corresponding crime type from specified list
def set_crime_search(offense):
  global a_crime
  global crime_type
  ret_val = 0

  if offense == '1':
    crime_type = 'VANDALISM'
  elif offense == '2':
    crime_type = 'BURGLARY'
  elif offense == '3':
    crime_type = 'ASSAULT'
  elif offense == '4':
    crime_type = 'VEHICLE BREAK-IN/THEFT'
  elif offense == '5':
    crime_type = 'OTHER'
  elif offense == '6':
    crime_type = 'ROBBERY'
  elif offense == '7':
    crime_type = 'THEFT/LARCENY'
  elif offense == '8':
    crime_type = 'MOTOR VEHICLE THEFT'
  elif offense == '9':
    crime_type = 'DRUGS/ALCOHOL VIOLATIONS'
  elif offense == '10':
    crime_type = 'WEAPONS'
  elif offense == '11':
    crime_type = 'ARSON'
  elif offense == '12':
    crime_type = 'HOMICIDE'
  elif offense == '13':
    crime_type = 'FRAUD'
  elif offense == '14':
    crime_type = 'SEX CRIMES'
  elif offense == '15':
    crime_type = 'DISTURBING THE PEACE'
  elif offense == 'Q':
    ret_val = 2
  else:
    ret_val = -1
    print("Offense not found.\n")
#create variable for specified crime type retrieved from input
  if ret_val == 0:
    print("You chose to look at the offense: " + crime_type)
    a_crime = crime_df.loc[crime_df['CRIME_TYPE'] == crime_type]

  return ret_val