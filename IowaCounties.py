"""
Program: IowaCounties.py
Author: Lily Ellison
Last date modified: 04/06/2023

The purpose of this program is to create a class to hold county information in a list in CountyReader.py.

"""

class IACounty:

    def __init__(self, pci, mhi, mfi, pop, noh):
        self.per_capita_income = pci
        self.median_household_income = mhi
        self.median_family_income = mfi
        self.population = pop
        self.num_households = noh
