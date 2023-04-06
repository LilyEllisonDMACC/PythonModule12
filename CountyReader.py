"""
Program: CountyReader.py
Author: Lily Ellison
Last date modified: 04/06/2023

The purpose of this program is to read a csv file and process information via a class with a list of objects.

"""

import csv
from IowaCounties import IACounty
'''
practice:
with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are{",".join(row)}')
            line_count += 1
        elif row[0] == '':
            continue
        else:
            print(row)
            line_count += 1
    print(f'processed {line_count} rows')
'''


#Method to remove the commas and return the number strings as ints:
def remove_comma(num_as_str: str) -> int:
    #remove commas using split function, which creates a list:
    num_as_list = num_as_str.split(',')
    #concatenate the number strings back together with no commas:
    num_as_num = num_as_list[0] + num_as_list[1]
    return int(num_as_num)


#method to calculate population per household:
def pop_per_house(county_list, co: str) -> str:
    #Remove the commas and get ints:
    num_pop = remove_comma(county_list[co].population)
    num_household = remove_comma(county_list[co].num_households)
    #Divide the numbers and return a string:
    return str(num_pop/num_household)


#open the csv file and get info as a list of objects:
with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    county = {}
    for row in csv_reader:
        #first row is titles only:
        if line_count == 0:
            line_count += 1
            continue
        #skips over the Iowa state info and the United States info by ignoring entries with blank rank:
        elif row[0] == '':
            continue
        #All other counties get entered by county name as an IACounty object into the county list
        county[str(row[1])] = IACounty(row[2], row[3], row[4], row[5], row[6])
    #print(county)

#Information requested:
    print("Population of Dallas county: " + county['Dallas'].population)

    print("Number of households in Dallas county: " + county['Dallas'].num_households)

    print("Average number of people per household in Dallas county: " + pop_per_house(county, 'Dallas'))


#method to calculate Iowa's total population:
    def pop_of_iowa(pop_stats) -> int:
        pop_ia = 0
        for entry in pop_stats:
            county_pop = remove_comma(pop_stats[entry].population)
            pop_ia += county_pop
        return pop_ia

    print("Population of Iowa: {:,}".format(pop_of_iowa(county)))
