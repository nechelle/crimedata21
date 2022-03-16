import pandas as pd
import numpy as np

#load data from online csv file, remove unneccessary columns, index by incident number
crime_df = pd.read_csv('https://lky-open-data.s3.amazonaws.com/LMPD/CRIME_DATA_2021.csv', nrows=10)
to_drop = ['DATE_OCCURED','UOR_DESC', 'NIBRS_CODE', 'UCR_HIERARCHY', 'ATT_COMP', 'LMPD_BEAT', 'BLOCK_ADDRESS']
crime_df.drop(to_drop, inplace = True, axis = 1)
crime_df.set_index('INCIDENT_NUMBER', inplace = True)


#only populate sex crimes
a_crime = crime_df.loc[crime_df['CRIME_TYPE'] == 'ASSAULT']
print(a_crime)
#    += 1
#print column headers
print(a_crime.columns.tolist())

#print zip code counts
print(a_crime['ZIP_CODE'].value_counts())
print(a_crime['ZIP_CODE'].describe())


#list_type = ['VANDALISM', 'BURGLARY', 'ASSAULT', 'FRAUD', 'VEHICLE BREAK-IN/THEFT', 'OTHER', 'ROBBERY', 'THEFT/LARCENY', 'DRUGS/ALCOHOL VIOLATIONS', 'MOTOR VEHICLE THEFT', 'WEAPONS', 'HOMICIDE', 'ARSON', 'SEX CRIMES', 'DISTURBING THE PEACE']