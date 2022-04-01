# LMPD Case submissions project

This project focuses on the criminal activity data that has been obtained and filed by the Louisville Metro Police Department for the year 2021. The data is sourced from: http://data.louisvilleky.gov. This site offers various data sets for the city of Louisville, KY. 

In 2016 the Kentucky General Assembly created a law mandating that any sexual assault kit reported to law enforcement be submitted to the State Forensic Laboratory for testing within 30 days of receipt. This law can be found in the Kentucky Revised Statutes (KRS 15.440(1)(i)(3)). This project looks at the data provided by LMPD, the biggest law enforcement agency in KY, to see if their cases are being submitted to the lab within the 30 day timeframe. The dataset used is from 2021.

Attempts were made to get accurate submission dates from the Crime Laboratory but to no avail. In this project, random dates are generated based on the day the offense was reported to LMPD and will look at all case types, not just sexual assaults. In reality,not all of these case types would contain probative evidence that would be submitted for testing. Ultimately, it would be advantageous to see actual submission dates to determine if there were areas that needed to be addressed to help the flow of the justice system. 

The question I want to answer: Is LMPD submitting their cases in accordance with the law?

### Setup virtual environment:
  #### On Windows:
  `py -m venv env`
  #### On Unix or MacOs:
  `python3 -m venv env`

### Activate virtual environment:
  #### On Windows:
  `env\Scripts\activate`
  #### On Linux or MacOs:
  `source env/bin/activate`

### Install required packages:
  `pip install -r requirements.txt`

### Execute program:
  `python3 sub_dates.py`


Packages used:
- pip 22.0.4
- Python 3.10.2

Modules that need to be installed:
- pandas
- matplotlib



## Features demonstrated:
#### Category 1:
- implement a "master loop" console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program.

- create and call at least 3 functions or methods, with at least one returning a value that is used somewhere else in your code

#### Category 2:
- read data from an external file such as text, JSON, CSV, etc, and use that data in your application

#### Category 3:
- visualize data in a graph, chart or other visual representation of data

#### Category 4:
- implement a log that records errors, invalid inputs, or other important events and writes them to a text file
- the program should utilize a virtual environment and document library dependencies in a requirements.txt file

