import pandas as pd
import numpy as np

#load data from online csv file, remove unneccessary columns, index by incident number 
crime_df = pd.read_csv('https://lky-open-data.s3.amazonaws.com/LMPD/CRIME_DATA_2021.csv')
to_drop = ['DATE_OCCURED','UOR_DESC', 'NIBRS_CODE', 'UCR_HIERARCHY', 'ATT_COMP', 'LMPD_BEAT', 'BLOCK_ADDRESS']
crime_df.drop(to_drop, inplace = True, axis = 1)
crime_df.set_index('INCIDENT_NUMBER', inplace = True)

#only populate sex crimes (make function:retrieved from input)
a_crime = crime_df.loc[crime_df['CRIME_TYPE'] == 'SEX CRIMES']

#print column headers
print(a_crime.columns.tolist())

#print crime count
print(len(a_crime))


#list_type = ['VANDALISM', 'BURGLARY', 'ASSAULT', 'FRAUD', 'VEHICLE BREAK-IN/THEFT', 'OTHER', 'ROBBERY', 'THEFT/LARCENY', 'DRUGS/ALCOHOL VIOLATIONS', 'MOTOR VEHICLE THEFT', 'WEAPONS', 'HOMICIDE', 'ARSON', 'SEX CRIMES', 'DISTURBING THE PEACE']